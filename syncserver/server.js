const express = require("express");
const http = require("http");
const socketIo = require("socket.io");

const app = express();
const server = http.createServer(app);
const io = socketIo(server, {
  cors: {
    origin: 'http://localhost:5173',
  }
});

io.on("connection", (socket) => {
  console.log("A user connected");

  // Handle a simple custom message from clients
  socket.on("syncData", (data) => {
    console.log("Data received: ", data);
    // Emit data to all connected clients
    io.emit("syncData", data);
  });

  socket.on("disconnect", () => {
    console.log("User disconnected");
  });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
