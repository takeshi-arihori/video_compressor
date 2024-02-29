import os
import json

# 'config.json'という名前のJSONファイルを開いてロードします。
config = json.load(open('config.json'))

# 既に同じ名前のパイプが存在する場合はそれを削除します。
if os.path.exists(config['filepath']):
    os.remove(config['filepath'])

# 'os.mkfifo'は、指定したパスに名前付きパイプを作成します。
os.mkfifo(config['filepath'], 0o600)

print("FIFO named '%s' is created successfully." % config['filepath'])
print("Type in what you would like to send to clients.")

# ユーザーからの入力を取得し、それを名前付きパイプに書き込みます。
flag = True
while flag:
    inputstr = input()
    if inputstr == 'exit':
        flag = False
    else:
        with open(config['filepath'], 'w') as f:
            f.write(inputstr)

# プログラムの終了時に名前付きパイプを削除します。
os.remove(config['filepath'])
