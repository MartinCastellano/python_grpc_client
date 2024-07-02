<https://jwt.io/>
# MANUAL EVANS TRY

evans --host vacancies.cyrextech.net --path ./proto --proto "auth_service.proto,rpc_signup_user.proto,user_service.proto,rpc_create_vacancy.proto,rpc_update_vacancy.proto,vacancy.proto,rpc_signin_user.proto,user.proto,vacancy_service.proto" --port 7823

init Evans"""
  ______
 |  ____|
 | |__    __   __   __ _   _ __    ___
 |  __|   \ \ / /  / _. | | '_ \  / __|
 | |____   \ V /  | (_| | | | | | \__ \
 |______|   \_/    \__,_| |_| |_| |___/

 more expressive universal gRPC client

"""
commands:

evans --host vacancies.cyrextech.net --port 7823  --reflection cli list


show package
+---------+
| PACKAGE |
+---------+
| pb      |
+---------+

show service
+----------------+---------------+----------------------+-----------------------+
|    SERVICE     |      RPC      |     REQUEST TYPE     |     RESPONSE TYPE     |
+----------------+---------------+----------------------+-----------------------+
| AuthService    | SignUpUser    | SignUpUserInput      | GenericResponse       |
| AuthService    | SignInUser    | SignInUserInput      | SignInUserResponse    |
| AuthService    | VerifyEmail   | VerifyEmailRequest   | GenericResponse       |
| UserService    | GetMe         | GetMeRequest         | UserResponse          |
| VacancyService | CreateVacancy | CreateVacancyRequest | VacancyResponse       |
| VacancyService | GetVacancy    | VacancyRequest       | VacancyResponse       |
| VacancyService | GetVacancies  | GetVacanciesRequest  | Vacancy               |
| VacancyService | UpdateVacancy | UpdateVacancyRequest | VacancyResponse       |
| VacancyService | DeleteVacancy | VacancyRequest       | DeleteVacancyResponse |
+----------------+---------------+----------------------+-----------------------+

show message
+-----------------------+
|        MESSAGE        |
+-----------------------+
| CreateVacancyRequest  |
| DeleteVacancyResponse |
| GenericResponse       |
| GetMeRequest          |
| GetVacanciesRequest   |
| SignInUserInput       |
| SignInUserResponse    |
| SignUpUserInput       |
| UpdateVacancyRequest  |
| UserResponse          |
| Vacancy               |
| VacancyRequest        |
| VacancyResponse       |
| VerifyEmailRequest    |
+-----------------------+

show header
+-------------+-------+
|     KEY     |  VAL  |
+-------------+-------+
| grpc-client | evans |
+-------------+-------+

show RPC
+---------------+---------------------------------+-------------------------+--------------------------+
|     NAME      |      FULLY-QUALIFIED NAME       |      REQUEST TYPE       |      RESPONSE TYPE       |
+---------------+---------------------------------+-------------------------+--------------------------+
| CreateVacancy | pb.VacancyService.CreateVacancy | pb.CreateVacancyRequest | pb.VacancyResponse       |
| DeleteVacancy | pb.VacancyService.DeleteVacancy | pb.VacancyRequest       | pb.DeleteVacancyResponse |
| GetVacancies  | pb.VacancyService.GetVacancies  | pb.GetVacanciesRequest  | pb.Vacancy               |
| GetVacancy    | pb.VacancyService.GetVacancy    | pb.VacancyRequest       | pb.VacancyResponse       |
| UpdateVacancy | pb.VacancyService.UpdateVacancy | pb.UpdateVacancyRequest | pb.VacancyResponse       |
+---------------+---------------------------------+-------------------------+--------------------------+

 evans --host vacancies.cyrextech.net --path ./proto --proto "auth_service.proto,rpc_signup_user.proto,user_service.proto,rpc_create_vacancy.proto,rpc_update_vacancy.proto,vacancy.proto,rpc_signin_user.proto,user.proto,vacancy_service.proto" --port 7823 -r cli desc  pb.VacancyService
pb.VacancyService:
service VacancyService {
  rpc CreateVacancy ( .pb.CreateVacancyRequest ) returns ( .pb.VacancyResponse );
  rpc DeleteVacancy ( .pb.VacancyRequest ) returns ( .pb.DeleteVacancyResponse );
  rpc GetVacancies ( .pb.GetVacanciesRequest ) returns ( stream .pb.Vacancy );
  rpc GetVacancy ( .pb.VacancyRequest ) returns ( .pb.VacancyResponse );
  rpc UpdateVacancy ( .pb.UpdateVacancyRequest ) returns ( .pb.VacancyResponse );
}

try a CALL :
evans --host vacancies.cyrextech.net --path ./proto --proto "auth_service.proto,rpc_signup_user.proto,user_service.proto,rpc_create_vacancy.proto,rpc_update_vacancy.proto,vacancy.proto,rpc_signin_user.proto,user.proto,vacancy_service.proto" --port 7823 -r cli call  --file request.json pb.UserService.GetMe
{
  "user": {
    "createdAt": "2024-06-30T22:29:26.622Z",
    "email": "<martin.castellano89+1@gmail.com>",
    "id": "6681dc46cf1eb847f0f7166a",
    "name": "martin2",
    "role": "user",
    "updatedAt": "2024-06-30T22:31:08.321Z"
  }
}

CALL getvacancies with a json file

 evans --host vacancies.cyrextech.net --path ./proto --proto "auth_service.proto,rpc_signup_user.proto,user_service.proto,rpc_create_vacancy.proto,rpc_update_vacancy.proto,vacancy.proto,rpc_signin_user.proto,user.proto,vacancy_service.proto" --port 7823 -r cli call --file getVacancies.json pb.VacancyService.GetVacancies

{
  "Country": "Faroe Islands",
  "Description": "tmihvtdcrn",
  "Id": "667fc393cf1eb847f0f715da",
  "Title": "evjigysqts",
  "createdAt": "2024-06-29T08:19:31.117Z",
  "updatedAt": "2024-06-29T08:19:31.117Z"
}

verify email with code on file 

evans --host vacancies.cyrextech.net --path ./proto --proto "auth_service.proto,rpc_signup_user.proto,user_service.proto,rpc_create_vacancy.proto,rpc_update_vacancy.proto,vacancy.proto,rpc_signin_user.proto,user.proto,vacancy_service.proto" --port 7823 -r cli call --file verifyEmail.json pb.AuthService.VerifyEmail
{
  "message": "Email verified successfully",
  "status": "success"
}

evans --host vacancies.cyrextech.net  --port 7823 -r cli call --file getVacancies.json pb.VacancyService.GetVacancies  

{
  "Country": "Faroe Islands",
  "Description": "tmihvtdcrn",
  "Id": "667fc393cf1eb847f0f715da",
  "Title": "evjigysqts",
  "createdAt": "2024-06-29T08:19:31.117Z",
  "updatedAt": "2024-06-29T08:19:31.117Z"
}

evans --host vacancies.cyrextech.net --path ./proto --proto "auth_service.proto,rpc_signup_user.proto,user_service.proto,rpc_create_vacancy.proto,rpc_update_vacancy.proto,vacancy.proto,rpc_signin_user.proto,user.proto,vacancy_service.proto" --port 7823 -r cli --file signin.json call pb.AuthService.SignInUser
{
  "accessToken": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTk4MTAxMTksImlhdCI6MTcxOTgwOTIxOSwibmJmIjoxNzE5ODA5MjE5LCJzdWIiOiI2NjgxYzkxZWNmMWViODQ3ZjBmNzE2NjcifQ.TPuEP91blxIfae-FoQ4a6p2TLNdpL5oMuEfxdIwwpOJXfAd8HoJhjpeMF7DxnWbPp6LAJkPDwow21xysIi34hQ",
  "refreshToken": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTk4MTI4MTksImlhdCI6MTcxOTgwOTIxOSwibmJmIjoxNzE5ODA5MjE5LCJzdWIiOiI2NjgxYzkxZWNmMWViODQ3ZjBmNzE2NjcifQ.GiCGHBVFauzfw4rRx0EyMpi2NinPT0hsc2TFaYtgmAwej7WPUKIy3SB5BDN4vKt-F_SxNZzeW_sQzvtyUEbWRw",
  "status": "success"
}


I create grpc.py and pb2.py files with 

python -m grpc_tools.protoc -I./proto --python_out=. --pyi_out=. --grpc_python_out=. ./proto/*.proto  

after made the locustfile_client

locust -f locustfile_client.py --master-host vacancies.cyrextech.net --master-port 7823 --headless


locust -f locustfile.py --master-host vacancies.cyrextech.net --master-port 7823 --users 3 --spawn-rate 30 --run-time 5m


--autostart
