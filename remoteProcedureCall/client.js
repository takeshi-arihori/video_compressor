const net = require('net');
const client = new net.Socket();
const port = 12345;
const host = '127.0.0.1';

client.connect(port, host, function () {
    console.log('Connected');
    // const request = {
    //     method: "reverse",
    //     params: ["hello"],
    //     id: 1
    // };
    const request = {
        method: "subtract",
        params: [42, 23],
        param_types: ["int", "int"],
        id: 1
    };
    client.write(JSON.stringify(request));
});

client.on('data', (data) => {
    console.log('Received:', data.toString());
    client.destroy(); // 接続を閉じる
});

client.on('close', () => {
    console.log('Connection closed');
});