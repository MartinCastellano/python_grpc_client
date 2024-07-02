import utils.auth_service_pb2_grpc
import utils.rpc_create_vacancy_pb2
import utils.rpc_signin_user_pb2
import utils.rpc_update_vacancy_pb2
import utils.vacancy_pb2
import utils.vacancy_service_pb2_grpc
import utils.vacancy_service_pb2

from dotenv import load_dotenv

from locust.exception import LocustError
from locust import  TaskSet, between, task, constant, events, User, runners, constant_pacing
from locust.user.task import (
    LOCUST_STATE_RUNNING,
    LOCUST_STATE_STOPPING,
    LOCUST_STATE_WAITING,
    DefaultTaskSet,
    TaskSet,
    get_tasks_from_base_classes,
)

import typing 
import random
import string
import logging

import gevent
import time


import grpc
from grpc import _channel
# patch grpc so that it uses gevent instead of asyncio
import grpc.experimental.gevent as grpc_gevent

from grpc_interceptor import ClientInterceptor

grpc_gevent.init_gevent()
from concurrent import futures

# import asyncio
import os
import time

from typing import Any, Callable

load_dotenv()

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)


user_1_email = os.getenv("USER_1_EMAIL")
user_1_password = os.getenv("USER_1_PASSWORD")

user_2_email = os.getenv("USER_2_EMAIL")
user_2_password = os.getenv("USER_2_PASSWORD")

user_3_email = os.getenv("USER_3_EMAIL")
user_3_password = os.getenv("USER_3_PASSWORD")

USER_CREDENTIALS = [
    (user_1_email, user_1_password),
    (user_2_email, user_2_password),
    (user_3_email, user_3_password),   
]

def sign_in_user(stub,email,password) -> rpc_signin_user_pb2.SignInUserResponse:   
    request =  rpc_signin_user_pb2.SignInUserInput(email=email, password=password)       
    try:
        response = stub.SignInUser(request)        
             
        return response        
    except grpc.RpcError as rpc_error:
        _LOGGER.error("Error on Sign in user: %s (Request: %s)", rpc_error)
        return rpc_error
    else:
        _LOGGER.info("Signing in successfully. Response: %s", response)
        return response 
    

def create_vacancy(stub) -> vacancy_pb2.VacancyResponse:
    country_options = ["ARG", "USA", "BRAZIL", "MEXICO"] 
    division_options = ["DEVELOPMENT", "SECURITY", "SALES", "OTHER"]    
    random_code = ''.join(random.choice(string.ascii_letters) for _ in range(10))
    request = rpc_create_vacancy_pb2.CreateVacancyRequest(Title=f"random Title {random_code}", Description=f"random description {random_code}", Division=random.choice(division_options), Country=random.choice(country_options))
         
    try:         
        response = stub.CreateVacancy(request)
            
        return response        
    except grpc.RpcError as rpc_error:
        _LOGGER.error("Error creating vacancy: %s (Request: %s)", rpc_error)
        return rpc_error
    else:
        _LOGGER.info("Vacancy created successfully. Response: %s", response)
        return response 

def update_vacancy(stub,id)-> vacancy_pb2.VacancyResponse:
    country_options = ["ARG", "USA", "BRAZIL", "MEXICO"] 
    division_options = ["DEVELOPMENT", "SECURITY", "SALES", "OTHER"]    
    random_code = ''.join(random.choice(string.ascii_letters) for _ in range(10))
        
    request = rpc_update_vacancy_pb2.UpdateVacancyRequest(Id=id, Title=f"other random Title {random_code}", Description=f"other random description {random_code}", Views=1, Division=random.choice(division_options), Country=random.choice(country_options))
    
    try: 
        response = stub.UpdateVacancy(request) 
                    
        return response        
    except grpc.RpcError as rpc_error:
        _LOGGER.error("Error updating vacancy: %s (Request: %s)", rpc_error)
        return rpc_error
    else:
        _LOGGER.info("Vacancy updated successfully. Response: %s", response)
        return response
    
    

def read_vacancy(stub,id)-> vacancy_pb2.VacancyResponse:
    
    request = vacancy_service_pb2.VacancyRequest(Id=id)
    try:        
        response = stub.GetVacancy(request)
                    
        return response        
    except grpc.RpcError as rpc_error:
        _LOGGER.error("Error obtaining vacancy: %s (Request: %s)", rpc_error)
        return rpc_error
    else:
        _LOGGER.info("Vacancy obtained successfully. Response: %s", response)
        return response
    
    

def delete_vacancy(stub,id)-> vacancy_service_pb2.DeleteVacancyResponse:
    
    request = vacancy_service_pb2.VacancyRequest(Id=id)
    try:  
        response = stub.DeleteVacancy(request)                 
        return response        
    except grpc.RpcError as rpc_error:
        _LOGGER.error("Error removing vacancy: %s (Request: %s)", rpc_error)
        return rpc_error
    else:
        _LOGGER.info("Vacancy removed successfully. Response: %s", response)
        return response
    
    

def get_all_vacancies(stub) -> typing.List[grpc._channel._MultiThreadedRendezvous]:
     
    # vacancy_list = []
    # for p in range(0, 43):        
    #     request = vacancy_service_pb2.GetVacanciesRequest(page=p, limit=200) 
    #     try:                
    #         response = stub.GetVacancies(request, timeout=5)
    #         for vacancy in response:
    #             vacancy_list.append(vacancy) 
              
    #         return vacancy_list       
    #     except grpc.RpcError as rpc_error:
    #         _LOGGER.error("Error obtaining all vacancies: %s (Request: %s)", rpc_error)
    #         return rpc_error
    #     else:
    #         _LOGGER.info("Vacancy obtained all vacancies successfully. Response: %s", response)
    #         return response  
    
    try:    
        vacancy_list = [        
        vacancy for page in range(0, 43)
            for vacancy in stub.GetVacancies(
                vacancy_service_pb2.GetVacanciesRequest(
                    page=page, 
                    limit=200
                    ),
                    timeout=5
                )
        ]      
        return vacancy_list       
    except grpc.RpcError as rpc_error:
        _LOGGER.error("Error obtaining all vacancies: %s (Request: %s)", rpc_error)
        return rpc_error
    else:
        _LOGGER.info("Vacancy obtained all vacancies successfully. Response: %s", response)
        return response 



class GrpcClient:
    def __init__(self, stub):
        self._stub_class = stub.__class__
        self._stub = stub

    def __getattr__(self, name):
        func = self._stub_class.__getattribute__(self._stub, name)

        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            request_meta = {
                "request_type": "grpc",
                "name": name,
                "response_length": 0,
                "exception": None,
                "context": None,
                "response": None,
            }
            try:
                request_meta["response"] = func(*args, **kwargs)
                request_meta["response_length"] = len(request_meta["response"].message)
            except grpc.RpcError as e:
                request_meta["exception"] = e
            request_meta["response_time"] = (time.perf_counter() - start_time) * 1000
            events.request.fire(**request_meta)
            return request_meta["response"]

        return wrapper
    
class LocustInterceptor(ClientInterceptor):
    def __init__(self, environment, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.env = environment

    def intercept(
        self,
        method: Callable,
        request_or_iterator: Any,
        call_details: grpc.ClientCallDetails,
    ):
        response = None
        exception = None
        start_perf_counter = time.perf_counter()
        response_length = 0
        try:
            response = method(request_or_iterator, call_details)
            response_length = response.result().ByteSize()
        except grpc.RpcError as e:
            exception = e

        self.env.events.request.fire(
            request_type="grpc",
            name=call_details.method,
            response_time=(time.perf_counter() - start_perf_counter) * 1000,
            response_length=response_length,
            response=response,
            context=None,
            exception=exception,
        )
        return response

class GrpcUser(User):
    abstract = True

    stub_class = None

    def __init__(self, environment):
        super().__init__(environment)
        for attr_value, attr_name in ((self.host, "host"), (self.stub_class, "stub_class")):
            if attr_value is None:
                raise LocustError(f"You must specify the {attr_name}.")
        self._channel = grpc.insecure_channel(self.host)
        self._channel_closed = False
        stub = self.stub_class(self._channel)
        self.client = GrpcClient(stub)
        
        self.request_fail_stats = [list()]
        self.request_success_stats = [list()]
        
    # @events.init_command_line_parser.add_listener
    # def init_parser(parser):
    #     parser.add_argument("--customarg", type=str, env_var="LOCUST_MY_ARGUMENT", default="1234", help="It's working")

    # @events.init.add_listener
    # def _(environment, **kw):
    #     print("Custom argument supplied: %s" % environment.parsed_options.customarg)
    
    # @events.request.add_listener
    # def hook_request_fail(self,request_type, name, response_time, exception,**kwargs):
    #     if exception:
    #         print(f"{exception}")
    #     else:
    #         self.request_fail_stats.append([name, request_type, response_time, exception])
    
    @events.request.add_listener
    def save_success_stats(self,**kwargs):
        import csv
        with open('success_req_stats.csv', 'wb') as csv_file:
            writer = csv.writer(csv_file)
            for value in self.request_success_stats:
                writer.writerow(value)
                    
    @events.quitting.add_listener
    def hook_locust_quit(self,**kwargs):
        self.save_success_stats()
                         
    # @events.request.add_listener
    # def hook_request_success(self,request_type, name, response_time, response_length,**kwargs):
        
    #     self.request_success_stats.append([name, request_type, response_time, response_length])
        
    def stop(self, force=False):
        self._channel_closed = True
        time.sleep(1)
        self._channel.close()
        super().stop(force=True)


class TaskGrpcUser(GrpcUser):
    host = "vacancies.cyrextech.net:7823"
    stub_class = auth_service_pb2_grpc.AuthServiceStub
    wait_time = constant_pacing(30)
    
    def on_start(self):
        
        if len(USER_CREDENTIALS) > 0:            
            user, passw = USER_CREDENTIALS.pop()
            print(user,passw)
            with grpc.insecure_channel("vacancies.cyrextech.net:7823") as self.channel:
                # sign in
                self.stub = auth_service_pb2_grpc.AuthServiceStub(self.channel)                       
                sign_in_user(self.stub,email=user,password=passw)
            
            
    def _on_background(self,timeout):
        iteration = 0                    
        while self.environment.runner.state != LOCUST_STATE_STOPPING:
            if iteration % timeout == 0:
                channel = grpc.insecure_channel("vacancies.cyrextech.net:7823")
                self.stub = vacancy_service_pb2_grpc.VacancyServiceStub(channel)
                start =  time.time() 
                response = get_all_vacancies(self.stub) 
                print("all vacancies")
                # self.environment.events.request.fire(request_type="grpc", name="list all vacancies", response_time=time.time()-start, response_length=0)    
              
            gevent.sleep(1)  
            iteration += 1
    
    def _on_task(self,timeout):
        iteration = 0                    
        while self.environment.runner.state != LOCUST_STATE_STOPPING:
            if iteration % timeout == 0:
                self.channel = grpc.insecure_channel("vacancies.cyrextech.net:7823")
                self.stub = vacancy_service_pb2_grpc.VacancyServiceStub(self.channel)              
                
                #create
                start = time.time()
                response = create_vacancy(self.stub)
                print("create")               
                # locust.event.EventHook.measure
                # self.environment.events.request.fire(**request_meta)
                # self.environment.events.request.fire(request_type="grpc", name="create", response_time=time.time()-start, response_length=0)    
                vacancy_id = response.vacancy.Id        
                
                #update
                start = time.time()
                response = update_vacancy(self.stub,id=vacancy_id)                
                # self.environment.events.request.fire(request_type="grpc", name="update", response_time=time.time()-start, response_length=0)    
                print("update")   
                #read 
                start = time.time()
                response = read_vacancy(self.stub,id=vacancy_id)                
                # self.environment.events.request.fire(request_type="grpc", name="read", response_time=time.time()-start, response_length=0)    
                print("read") 
                #delete
                start = time.time()
                response = delete_vacancy(self.stub,id=vacancy_id)
                # self.environment.events.request.fire(request_type="grpc", name="delete", response_time=time.time()-start, response_length=0)    
                print("delete") 
            
            gevent.sleep(1)  
            iteration += 1
    
    @task
    def locust_tasks(self):
        if not self._channel_closed:
            gevent.spawn(self._on_task(timeout=30))        
        gevent.spawn(self._on_background(timeout=45)) 
    
    # @task
    # def sayHello(self):
    #     if not self._channel_closed:
    #         self.client.SayHello(hello_pb2.HelloRequest(name="Test"))
    #     time.sleep(1)