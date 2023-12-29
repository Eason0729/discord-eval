import asyncio
import logging
import time

import grpc
from proto.judger_pb2 import *
from proto.proto.judger_pb2_grpc import *


class ExecRes:
    log: str
    stdout: str

    def __init__(self, log, stdout):
        self.log = log
        self.stdout = stdout


async def collect_stream(stream) -> ExecRes:
    log = ""
    stdout = ""
    res: ExecResult
    async for res in stream:
        if res.WhichOneof("result") == "output":
            stdout += getattr(res, res.WhichOneof('result')).decode()
        if res.WhichOneof("result") == "log":
            raw:Log=getattr(res, res.WhichOneof('result'))
            log+=raw.msg
    await asyncio.sleep(3)
    return ExecRes(log, stdout)

async def run(code: str, uuid: str) -> ExecRes:
    channel = grpc.aio.insecure_channel("localhost:8080")
    stub = JudgerStub(channel)
    stream = stub.Exec(ExecRequest(
        lang_uid=uuid, code=code.encode(), memory=1024*1024, time=1000*1000*1000, input=b""))
    response = await collect_stream(stream)
    await channel.close()
    return response

if __name__ == "__main__":
    logging.basicConfig()
    asyncio.run(run("print(\"hi\")", "1c41598f-e253-4f81-9ef5-d50bf1e4e74f"))
    # There should be something to prevent main from returning
    # such as using main thread as worker thread(in Rust, we do that)?
