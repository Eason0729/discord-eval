run:
    export $(cat test.env | xargs) && python main.py

prepare:
    source bin/activate

install:
    pip install -r requirements.txt

codegen:
    python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=proto proto/judger.proto

