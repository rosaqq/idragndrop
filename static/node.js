const WebSocket = require("ws");

const wss = new WebSocket.Server({port:8080})

wss.on("connection", ws =>{
    console.log("New client connection");

    ws.on("close", ws => {
        console.log("Client disconnected!");
    });
});
