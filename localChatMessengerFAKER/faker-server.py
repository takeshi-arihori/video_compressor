import socket
import os
import json # json モジュールをインポート
from faker import Faker # faker ライブラリをインポート

# UNIXドメインソケットの設定
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server_address = '/tmp/udp_socket_file' # サーバのアドレス(ソケットファイルのパス)

# 既存のソケットファイルの削除
try:
    os.unlink(server_address) # ソケットファイルが存在する場合は削除
except FileNotFoundError:
    pass # ファイルが存在しない場合は何もしない

print(f'starting up on {server_address}')
sock.bind(server_address) # ソケットをアドレスにバインド

# Fakerのインスタンスを作成
fake = Faker()

# フェイクのユーザープロファイルを生成する関数
def generate_fake_profile():
    """フェイクのユーザープロファイルを生成する"""
    profile = {
        "name": fake.name(),  # フルネーム
        "address": fake.address(),  # 住所
        "email": fake.email(),  # メールアドレス
        "job": fake.job(),  # 職業
        "birthdate": fake.date_of_birth(minimum_age=18, maximum_age=90).isoformat()  # 生年月日
    }
    return profile

try:
    while True: # 無限ループでクライアントからのメッセージを待ち受ける
        print('\nwaiting to receive message')
        data, address = sock.recvfrom(4096) # クライアントからのデータを受信

        print(f'received {len(data)} bytes from {address}')
        print(data)

        if data:
            # Fakerを使用して偽のデータを生成
            fake_profile = generate_fake_profile()  # フェイクプロファイルの生成
            fake_data = json.dumps(fake_profile).encode('utf-8')  # テキストをバイト列にエンコード
            sent = sock.sendto(fake_data, address) # エンコードしたデータをクライアントに送信
            print(f'sent {sent} bytes back to {address}')
except KeyboardInterrupt:
    print('\nServer is shutting down.') # Ctrl+Cでサーバを終了
finally:
    sock.close()  # ソケットをクローズしてリソースを解放
    print('Socket closed.')
