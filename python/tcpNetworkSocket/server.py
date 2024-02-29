import socket
import os
from pathlib import Path

# ソケットオブジェクトの作成。IPv4とTCPプロトコルを指定。
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = '0.0.0.0'  # 任意のIPアドレスからの接続を受け入れる。
server_port = 9001  # 使用するポート番号。

# 「temp」フォルダがない場合は作成。受信したファイルを格納するためのフォルダです。
dpath = 'tcpNetworkSocket/temp'
if not os.path.exists(dpath):
    os.makedirs(dpath)

print('Starting up on {} port {}'.format(server_address, server_port))

# サーバのアドレスとポートにソケットをバインド。
sock.bind((server_address, server_port))

# ソケットをリスニング状態に設定。1つの接続を待ち受ける。
sock.listen(1)

while True:
    try:
        # 接続を受け入れ、クライアントのアドレス情報を取得。
        connection, client_address = sock.accept()
        print('connection from', client_address)

        # ヘッダ情報を受信。
        header = connection.recv(8)

        # ヘッダからファイル名の長さ、JSONデータの長さ、データの長さを抽出。
        filename_length = int.from_bytes(header[:1], "big")
        json_length = int.from_bytes(header[1:4], "big")
        data_length = int.from_bytes(header[4:8], "big")

        # ファイル名を受信してデコード。
        filename = connection.recv(filename_length).decode('utf-8')
        print('Filename: {}'.format(filename))

        if json_length != 0:
            # JSONデータはサポートされていないため、例外を発生させます。
            raise Exception('JSON data is not currently supported.')
        if data_length == 0:
            # データがない場合は例外を発生させます。
            raise Exception('No data to read from client.')

        # 「temp」フォルダに新しいファイルを作成し、受信したデータを書き込みます。
        with open(os.path.join(dpath, filename), 'wb') as f:
            while data_length > 0:
                # データを受信し、ファイルに書き込みます。
                data = connection.recv(min(data_length, 4096))
                f.write(data)
                data_length -= len(data)

        print('Finished downloading the file from client.')
    except KeyboardInterrupt:
        # ユーザーがCtrl+Cでサーバを中断しようとした場合、安全に終了します。
        print('\nServer shutdown on user request.')
        break
    except Exception as e:
        # その他のエラーが発生した場合、エラーメッセージを表示します。
        print('Error: ' + str(e))
    finally:
        # 現在の接続を閉じて、次の接続を待ち受けます。
        connection.close()
