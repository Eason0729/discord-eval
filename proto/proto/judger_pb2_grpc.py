# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from proto import judger_pb2 as proto_dot_judger__pb2


class JudgerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Judge = channel.unary_stream(
                '/oj.judger.Judger/Judge',
                request_serializer=proto_dot_judger__pb2.JudgeRequest.SerializeToString,
                response_deserializer=proto_dot_judger__pb2.JudgeResponse.FromString,
                )
        self.JudgerInfo = channel.unary_unary(
                '/oj.judger.Judger/JudgerInfo',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=proto_dot_judger__pb2.JudgeInfo.FromString,
                )
        self.Exec = channel.unary_stream(
                '/oj.judger.Judger/Exec',
                request_serializer=proto_dot_judger__pb2.ExecRequest.SerializeToString,
                response_deserializer=proto_dot_judger__pb2.ExecResult.FromString,
                )


class JudgerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Judge(self, request, context):
        """Send Code for judge
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def JudgerInfo(self, request, context):
        """Get judger info, useful for getting supported language and load balancing
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Exec(self, request, context):
        """Execute the sandbox once, OLE also apply
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_JudgerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Judge': grpc.unary_stream_rpc_method_handler(
                    servicer.Judge,
                    request_deserializer=proto_dot_judger__pb2.JudgeRequest.FromString,
                    response_serializer=proto_dot_judger__pb2.JudgeResponse.SerializeToString,
            ),
            'JudgerInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.JudgerInfo,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=proto_dot_judger__pb2.JudgeInfo.SerializeToString,
            ),
            'Exec': grpc.unary_stream_rpc_method_handler(
                    servicer.Exec,
                    request_deserializer=proto_dot_judger__pb2.ExecRequest.FromString,
                    response_serializer=proto_dot_judger__pb2.ExecResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'oj.judger.Judger', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Judger(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Judge(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/oj.judger.Judger/Judge',
            proto_dot_judger__pb2.JudgeRequest.SerializeToString,
            proto_dot_judger__pb2.JudgeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def JudgerInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/oj.judger.Judger/JudgerInfo',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            proto_dot_judger__pb2.JudgeInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Exec(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/oj.judger.Judger/Exec',
            proto_dot_judger__pb2.ExecRequest.SerializeToString,
            proto_dot_judger__pb2.ExecResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
