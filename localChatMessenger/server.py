import socket
import os

try:
    # UNIXソケットをストリームモードで作成します
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    # このサーバが接続を待つUNIXソケットのパスを設定します
    server_address = '/tmp/socket_file'

    # 以前の接続が残っていた場合に備えて、サーバアドレスをアンリンク（削除）します
    try:
        os.unlink(server_address)
    except FileNotFoundError:
        pass

    print('Starting up on {}'.format(server_address))

    # サーバアドレスにソケットをバインド（接続）します
    sock.bind(server_address)

    # ソケットが接続要求を待機するようにします
    sock.listen(1)

    while True:
        # クライアントからの接続を受け入れます
        connection, client_address = sock.accept()
        try:
            print('connection established')

            while True:
                data = connection.recv(16)
                if data:
                    print('Received data:', data.decode('utf-8'))
                    response = 'Processing ' + data.decode('utf-8')
                    connection.sendall(response.encode('utf-8'))
                else:
                    print('no more data from client')
                    break
        finally:
            print("Closing current connection")
            connection.close()
except KeyboardInterrupt:
    print('KeyboardInterrupt, closing socket')
    sock.close()
