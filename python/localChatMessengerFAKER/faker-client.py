import socket
import os

# UNIXドメインソケットの設定
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server_address = '/tmp/udp_socket_file' # サーバのアドレス
client_address = '/tmp/udp_client_socket_file' # クライアントのアドレス(ソケットファイルのパス)

# 既存のソケットファイルの削除
try:
    os.unlink(client_address) # ソケットファイルが存在する場合は削除
except FileNotFoundError:
    pass # ファイルが存在しない場合は何もしない

sock.bind(client_address) # ソケットをアドレスにバインド

try:
    message = b'Hello, server!' # サーバに送信するメッセージ
    print(f'sending {message!r}')
    sent = sock.sendto(message, server_address) # メッセージをサーバに送信

    print('waiting to receive')
    data, server = sock.recvfrom(4096) # サーバからの応答を受信
    print(f'received {data!r}') # 受信したデータを表示

finally:
    print('closing socket')
    sock.close() # ソケットをクローズしてリソースを解放
