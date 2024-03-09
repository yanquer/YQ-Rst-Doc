# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import rpc_cat_pb2 as rpc__cat__pb2


class RpcCatStub(object):
    """import 'google/protobuf/any.proto';

    定义服务
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_name = channel.unary_unary(
                '/rpc_cat.RpcCat/get_name',
                request_serializer=rpc__cat__pb2.EmptyMessage.SerializeToString,
                response_deserializer=rpc__cat__pb2.StringMessage.FromString,
                )
        self.get_age = channel.unary_unary(
                '/rpc_cat.RpcCat/get_age',
                request_serializer=rpc__cat__pb2.EmptyMessage.SerializeToString,
                response_deserializer=rpc__cat__pb2.IntMessage.FromString,
                )
        self.get_love = channel.unary_unary(
                '/rpc_cat.RpcCat/get_love',
                request_serializer=rpc__cat__pb2.EmptyMessage.SerializeToString,
                response_deserializer=rpc__cat__pb2.TupleMessage.FromString,
                )
        self.get_food_once = channel.unary_unary(
                '/rpc_cat.RpcCat/get_food_once',
                request_serializer=rpc__cat__pb2.EmptyMessage.SerializeToString,
                response_deserializer=rpc__cat__pb2.FoodMessage.FromString,
                )
        self.get_attr_by_name = channel.unary_unary(
                '/rpc_cat.RpcCat/get_attr_by_name',
                request_serializer=rpc__cat__pb2.StringMessage.SerializeToString,
                response_deserializer=rpc__cat__pb2.StringMessage.FromString,
                )
        self.get_attr_by_name_with_stream = channel.stream_stream(
                '/rpc_cat.RpcCat/get_attr_by_name_with_stream',
                request_serializer=rpc__cat__pb2.StringMessage.SerializeToString,
                response_deserializer=rpc__cat__pb2.StringMessage.FromString,
                )
        self.get_all = channel.unary_unary(
                '/rpc_cat.RpcCat/get_all',
                request_serializer=rpc__cat__pb2.EmptyMessage.SerializeToString,
                response_deserializer=rpc__cat__pb2.AllMessage.FromString,
                )


class RpcCatServicer(object):
    """import 'google/protobuf/any.proto';

    定义服务
    """

    def get_name(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_age(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_love(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_food_once(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_attr_by_name(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_attr_by_name_with_stream(self, request_iterator, context):
        """请求体使用流式传输, python 实现时使用迭代器即可
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_all(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RpcCatServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_name': grpc.unary_unary_rpc_method_handler(
                    servicer.get_name,
                    request_deserializer=rpc__cat__pb2.EmptyMessage.FromString,
                    response_serializer=rpc__cat__pb2.StringMessage.SerializeToString,
            ),
            'get_age': grpc.unary_unary_rpc_method_handler(
                    servicer.get_age,
                    request_deserializer=rpc__cat__pb2.EmptyMessage.FromString,
                    response_serializer=rpc__cat__pb2.IntMessage.SerializeToString,
            ),
            'get_love': grpc.unary_unary_rpc_method_handler(
                    servicer.get_love,
                    request_deserializer=rpc__cat__pb2.EmptyMessage.FromString,
                    response_serializer=rpc__cat__pb2.TupleMessage.SerializeToString,
            ),
            'get_food_once': grpc.unary_unary_rpc_method_handler(
                    servicer.get_food_once,
                    request_deserializer=rpc__cat__pb2.EmptyMessage.FromString,
                    response_serializer=rpc__cat__pb2.FoodMessage.SerializeToString,
            ),
            'get_attr_by_name': grpc.unary_unary_rpc_method_handler(
                    servicer.get_attr_by_name,
                    request_deserializer=rpc__cat__pb2.StringMessage.FromString,
                    response_serializer=rpc__cat__pb2.StringMessage.SerializeToString,
            ),
            'get_attr_by_name_with_stream': grpc.stream_stream_rpc_method_handler(
                    servicer.get_attr_by_name_with_stream,
                    request_deserializer=rpc__cat__pb2.StringMessage.FromString,
                    response_serializer=rpc__cat__pb2.StringMessage.SerializeToString,
            ),
            'get_all': grpc.unary_unary_rpc_method_handler(
                    servicer.get_all,
                    request_deserializer=rpc__cat__pb2.EmptyMessage.FromString,
                    response_serializer=rpc__cat__pb2.AllMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'rpc_cat.RpcCat', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RpcCat(object):
    """import 'google/protobuf/any.proto';

    定义服务
    """

    @staticmethod
    def get_name(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rpc_cat.RpcCat/get_name',
            rpc__cat__pb2.EmptyMessage.SerializeToString,
            rpc__cat__pb2.StringMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_age(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rpc_cat.RpcCat/get_age',
            rpc__cat__pb2.EmptyMessage.SerializeToString,
            rpc__cat__pb2.IntMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_love(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rpc_cat.RpcCat/get_love',
            rpc__cat__pb2.EmptyMessage.SerializeToString,
            rpc__cat__pb2.TupleMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_food_once(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rpc_cat.RpcCat/get_food_once',
            rpc__cat__pb2.EmptyMessage.SerializeToString,
            rpc__cat__pb2.FoodMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_attr_by_name(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rpc_cat.RpcCat/get_attr_by_name',
            rpc__cat__pb2.StringMessage.SerializeToString,
            rpc__cat__pb2.StringMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_attr_by_name_with_stream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/rpc_cat.RpcCat/get_attr_by_name_with_stream',
            rpc__cat__pb2.StringMessage.SerializeToString,
            rpc__cat__pb2.StringMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_all(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rpc_cat.RpcCat/get_all',
            rpc__cat__pb2.EmptyMessage.SerializeToString,
            rpc__cat__pb2.AllMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)