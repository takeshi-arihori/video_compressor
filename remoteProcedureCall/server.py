import socket
import json

# 関数の定義
def floor(x):
    return int(x)

def nroot(n, x):
    return x ** (1/n)

def reverse(s):
    return s[::-1]

def validAnagram(str1, str2):
    return sorted(str1) == sorted(str2)

def sort(strArr):
    return sorted(strArr)

def subtract(x, y):
    return x - y


# メソッド名と関数のマッピング
methods = {
    "floor": floor,
    "nroot": nroot,
    "reverse": reverse,
    "validAnagram": validAnagram,
    "sort": sort,
    "subtract": subtract
}

# パラメータの型検証
def validate_params(params, param_types):
    for value, expected_type in zip(params, param_types):
        if not isinstance(value, expected_type):
            return False
    return True

# メソッドの実行とレスポンスの生成
def execute_method(request):
    method_name = request["method"]
    params = request["params"]
    param_types = request["param_types"]
    # 型検証
    if not validate_params(params, [int if t == 'int' else str for t in param_types]):
        return {"error": "Invalid parameter types", "id": request["id"]}

    if method_name in methods:
        result = methods[method_name](*params)
        return {"results": str(result), "result_type": type(result).__name__, "id": request["id"]}
    else:
        return {"error": "Method not found", "id": request["id"]}

# クライアントからのリクエストの処理
def process_request(connection):
    while True:
        request_text = connection.recv(1024).decode('utf-8')
        if not request_text:
            break
        request = json.loads(request_text)
        response = execute_method(request)
        connection.sendall(json.dumps(response).encode('utf-8'))

# サーバの起動
def start_server(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', port))
        s.listen()
        while True:
            conn, _ = s.accept()
            with conn:
                process_request(conn)

if __name__ == '__main__':
    start_server(12345)
