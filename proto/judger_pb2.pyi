from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JudgerCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RE: _ClassVar[JudgerCode]
    NA: _ClassVar[JudgerCode]
    WA: _ClassVar[JudgerCode]
    CE: _ClassVar[JudgerCode]
    AC: _ClassVar[JudgerCode]
    RF: _ClassVar[JudgerCode]
    TLE: _ClassVar[JudgerCode]
    MLE: _ClassVar[JudgerCode]
    OLE: _ClassVar[JudgerCode]

class JudgeMatchRule(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ExactSame: _ClassVar[JudgeMatchRule]
    IgnoreSNL: _ClassVar[JudgeMatchRule]
    SkipSNL: _ClassVar[JudgeMatchRule]
RE: JudgerCode
NA: JudgerCode
WA: JudgerCode
CE: JudgerCode
AC: JudgerCode
RF: JudgerCode
TLE: JudgerCode
MLE: JudgerCode
OLE: JudgerCode
ExactSame: JudgeMatchRule
IgnoreSNL: JudgeMatchRule
SkipSNL: JudgeMatchRule

class JudgeRequest(_message.Message):
    __slots__ = ("lang_uid", "code", "memory", "time", "rule", "tests")
    LANG_UID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    TESTS_FIELD_NUMBER: _ClassVar[int]
    lang_uid: str
    code: bytes
    memory: int
    time: int
    rule: JudgeMatchRule
    tests: _containers.RepeatedCompositeFieldContainer[TestIO]
    def __init__(self, lang_uid: _Optional[str] = ..., code: _Optional[bytes] = ..., memory: _Optional[int] = ..., time: _Optional[int] = ..., rule: _Optional[_Union[JudgeMatchRule, str]] = ..., tests: _Optional[_Iterable[_Union[TestIO, _Mapping]]] = ...) -> None: ...

class ExecRequest(_message.Message):
    __slots__ = ("lang_uid", "code", "memory", "time", "input")
    LANG_UID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    lang_uid: str
    code: bytes
    memory: int
    time: int
    input: bytes
    def __init__(self, lang_uid: _Optional[str] = ..., code: _Optional[bytes] = ..., memory: _Optional[int] = ..., time: _Optional[int] = ..., input: _Optional[bytes] = ...) -> None: ...

class Log(_message.Message):
    __slots__ = ("level", "msg")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    level: int
    msg: str
    def __init__(self, level: _Optional[int] = ..., msg: _Optional[str] = ...) -> None: ...

class ExecResult(_message.Message):
    __slots__ = ("output", "log")
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    output: bytes
    log: Log
    def __init__(self, output: _Optional[bytes] = ..., log: _Optional[_Union[Log, _Mapping]] = ...) -> None: ...

class TestIO(_message.Message):
    __slots__ = ("input", "output")
    INPUT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    input: bytes
    output: bytes
    def __init__(self, input: _Optional[bytes] = ..., output: _Optional[bytes] = ...) -> None: ...

class JudgeResponse(_message.Message):
    __slots__ = ("case", "result")
    CASE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    case: int
    result: JudgeResult
    def __init__(self, case: _Optional[int] = ..., result: _Optional[_Union[JudgeResult, _Mapping]] = ...) -> None: ...

class JudgeResult(_message.Message):
    __slots__ = ("status", "time", "memory", "accuracy")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    ACCURACY_FIELD_NUMBER: _ClassVar[int]
    status: JudgerCode
    time: int
    memory: int
    accuracy: int
    def __init__(self, status: _Optional[_Union[JudgerCode, str]] = ..., time: _Optional[int] = ..., memory: _Optional[int] = ..., accuracy: _Optional[int] = ...) -> None: ...

class Langs(_message.Message):
    __slots__ = ("list",)
    LIST_FIELD_NUMBER: _ClassVar[int]
    list: _containers.RepeatedCompositeFieldContainer[LangInfo]
    def __init__(self, list: _Optional[_Iterable[_Union[LangInfo, _Mapping]]] = ...) -> None: ...

class LangInfo(_message.Message):
    __slots__ = ("lang_uid", "lang_name", "info", "lang_ext")
    LANG_UID_FIELD_NUMBER: _ClassVar[int]
    LANG_NAME_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    LANG_EXT_FIELD_NUMBER: _ClassVar[int]
    lang_uid: str
    lang_name: str
    info: str
    lang_ext: str
    def __init__(self, lang_uid: _Optional[str] = ..., lang_name: _Optional[str] = ..., info: _Optional[str] = ..., lang_ext: _Optional[str] = ...) -> None: ...

class JudgeInfo(_message.Message):
    __slots__ = ("memory", "accuracy", "langs", "cpu_factor")
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    ACCURACY_FIELD_NUMBER: _ClassVar[int]
    LANGS_FIELD_NUMBER: _ClassVar[int]
    CPU_FACTOR_FIELD_NUMBER: _ClassVar[int]
    memory: int
    accuracy: int
    langs: Langs
    cpu_factor: float
    def __init__(self, memory: _Optional[int] = ..., accuracy: _Optional[int] = ..., langs: _Optional[_Union[Langs, _Mapping]] = ..., cpu_factor: _Optional[float] = ...) -> None: ...
