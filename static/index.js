// const ws = new WebSocket("ws://localhost:8080");
//
// ws.addEventListener('open', () => {
//     console.log('Connected to server!');
// })
//
// ws.addEventListener('upload', () => {
//     console.log('New image uploaded!');
//     location.reload();
// })

const socket = io('http://127.0.0.1:5000');

socket.on('connect', () => {
    console.log('Connected to server!');
    socket.emit('event1', 'hello');
});

socket.on('event1', x => {
    console.log('Server: ' +x);
})

socket.on('upload',() => {
    console.log('New image uploaded!');
    location.reload();
})