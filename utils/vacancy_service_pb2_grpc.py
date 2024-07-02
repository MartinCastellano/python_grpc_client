# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import utils.rpc_create_vacancy_pb2 as rpc__create__vacancy__pb2
import utils.rpc_update_vacancy_pb2 as rpc__update__vacancy__pb2
import utils.vacancy_pb2 as vacancy__pb2
import utils.vacancy_service_pb2 as vacancy__service__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in vacancy_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class VacancyServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateVacancy = channel.unary_unary(
                '/pb.VacancyService/CreateVacancy',
                request_serializer=rpc__create__vacancy__pb2.CreateVacancyRequest.SerializeToString,
                response_deserializer=vacancy__pb2.VacancyResponse.FromString,
                _registered_method=True)
        self.GetVacancy = channel.unary_unary(
                '/pb.VacancyService/GetVacancy',
                request_serializer=vacancy__service__pb2.VacancyRequest.SerializeToString,
                response_deserializer=vacancy__pb2.VacancyResponse.FromString,
                _registered_method=True)
        self.GetVacancies = channel.unary_stream(
                '/pb.VacancyService/GetVacancies',
                request_serializer=vacancy__service__pb2.GetVacanciesRequest.SerializeToString,
                response_deserializer=vacancy__pb2.Vacancy.FromString,
                _registered_method=True)
        self.UpdateVacancy = channel.unary_unary(
                '/pb.VacancyService/UpdateVacancy',
                request_serializer=rpc__update__vacancy__pb2.UpdateVacancyRequest.SerializeToString,
                response_deserializer=vacancy__pb2.VacancyResponse.FromString,
                _registered_method=True)
        self.DeleteVacancy = channel.unary_unary(
                '/pb.VacancyService/DeleteVacancy',
                request_serializer=vacancy__service__pb2.VacancyRequest.SerializeToString,
                response_deserializer=vacancy__service__pb2.DeleteVacancyResponse.FromString,
                _registered_method=True)


class VacancyServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateVacancy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVacancy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVacancies(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateVacancy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteVacancy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VacancyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateVacancy': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateVacancy,
                    request_deserializer=rpc__create__vacancy__pb2.CreateVacancyRequest.FromString,
                    response_serializer=vacancy__pb2.VacancyResponse.SerializeToString,
            ),
            'GetVacancy': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVacancy,
                    request_deserializer=vacancy__service__pb2.VacancyRequest.FromString,
                    response_serializer=vacancy__pb2.VacancyResponse.SerializeToString,
            ),
            'GetVacancies': grpc.unary_stream_rpc_method_handler(
                    servicer.GetVacancies,
                    request_deserializer=vacancy__service__pb2.GetVacanciesRequest.FromString,
                    response_serializer=vacancy__pb2.Vacancy.SerializeToString,
            ),
            'UpdateVacancy': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateVacancy,
                    request_deserializer=rpc__update__vacancy__pb2.UpdateVacancyRequest.FromString,
                    response_serializer=vacancy__pb2.VacancyResponse.SerializeToString,
            ),
            'DeleteVacancy': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteVacancy,
                    request_deserializer=vacancy__service__pb2.VacancyRequest.FromString,
                    response_serializer=vacancy__service__pb2.DeleteVacancyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pb.VacancyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('pb.VacancyService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class VacancyService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateVacancy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/pb.VacancyService/CreateVacancy',
            rpc__create__vacancy__pb2.CreateVacancyRequest.SerializeToString,
            vacancy__pb2.VacancyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetVacancy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/pb.VacancyService/GetVacancy',
            vacancy__service__pb2.VacancyRequest.SerializeToString,
            vacancy__pb2.VacancyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetVacancies(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/pb.VacancyService/GetVacancies',
            vacancy__service__pb2.GetVacanciesRequest.SerializeToString,
            vacancy__pb2.Vacancy.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateVacancy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/pb.VacancyService/UpdateVacancy',
            rpc__update__vacancy__pb2.UpdateVacancyRequest.SerializeToString,
            vacancy__pb2.VacancyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteVacancy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/pb.VacancyService/DeleteVacancy',
            vacancy__service__pb2.VacancyRequest.SerializeToString,
            vacancy__service__pb2.DeleteVacancyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
