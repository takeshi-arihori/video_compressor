const net = require('net');
const client = new net.Socket();
const port = 12345;
const host = '127.0.0.1';

client.connect(port, host, function () {
    console.log('Connected');

    // subtract
    const request = {
        method: "subtract",
        params: [42, 23],
        param_types: ["int", "int"],
        id: 1
    };

    // sort
    // const request = {
    //     method: "sort",
    //     params: [["c", "a", "b"]],
    //     param_types: ["strArr"],
    //     id: 1
    // };

    // reverse
    // const request = {
    //     method: "reverse",
    //     params: ["hello"],
    //     param_types: ["str"],
    //     id: 1
    // };

    client.write(JSON.stringify(request));
});

client.on('data', (data) => {
    console.log('Received:', data.toString());
    client.destroy(); // 接続を閉じる
});

client.on('close', () => {
    console.log('Connection closed');
});