import socket
import sys
import os

# プロトコルヘッダを作成する関数。ファイル名の長さ、JSONデータの長さ、データの長さをバイナリ形式で結合します。
def protocol_header(filename_length, json_length, data_length):
    # 各長さを指定されたバイト数でバイナリに変換し、結合します。
    return filename_length.to_bytes(1, "big") + json_length.to_bytes(3, "big") + data_length.to_bytes(4, "big")

# ソケットオブジェクトの作成。AF_INET はIPv4を意味し、SOCK_STREAM はTCPを意味します。
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # サーバのアドレス入力を求める。
    server_address = input("Type in the server's address to connect to: ")
    server_port = 9001  # 接続するポート番号。
    print('connecting to {} port {}'.format(server_address, server_port))
    # 指定されたアドレスとポートに接続を試みます。
    sock.connect((server_address, server_port))
except socket.error as err:
    # ソケット関連のエラーが発生した場合、エラーメッセージを表示して終了します。
    print(err)
    sys.exit(1)
except KeyboardInterrupt:
    # ユーザーがCtrl+Cを押して中断した場合、メッセージを表示して終了します。
    print('\nOperation cancelled by user.')
    sys.exit(1)

try:
    # アップロードするファイルのパスを入力させる。
    filepath = input('Type in a file to upload: ')
    with open(filepath, 'rb') as f:
        # ファイルサイズを取得するため、ファイルの末尾に移動します。
        f.seek(0, os.SEEK_END)
        filesize = f.tell()  # ファイルサイズを取得。
        f.seek(0, 0)  # ファイルの先頭に戻ります。

        if filesize > pow(2, 32):
            # ファイルサイズが2GBを超える場合は、例外を発生させます。
            raise Exception('File must be below 2GB.')

        filename = os.path.basename(filepath)  # ファイル名を取得。
        filename_bits = filename.encode('utf-8')  # ファイル名をUTF-8でエンコード。
        # プロトコルヘッダを作成してサーバに送信。
        header = protocol_header(len(filename_bits), 0, filesize)
        sock.send(header)  # ヘッダを送信。
        sock.send(filename_bits)  # ファイル名を送信。

        # ファイルデータを4096バイト単位で読み込み、送信します。
        data = f.read(4096)
        while data:
            sock.send(data)
            data = f.read(4096)
except KeyboardInterrupt:
    # ユーザーが途中でCtrl+Cを押して中断した場合、メッセージを表示します。
    print('\nUpload cancelled by user.')
finally:
    # 最終的に、ソケットを閉じてリソースを解放します。
    print('Closing socket.')
    sock.close()
