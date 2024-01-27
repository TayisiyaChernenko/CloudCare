import { writable } from "svelte/store";
import io from "socket.io-client";

const createSocket = () => {
  const { subscribe, set, update } = writable([]);

  const socket = io("http://localhost:3000");

  socket.on("syncData", (data) => {
    update((messages) => [...messages, data]);
  });

  const sendMessage = (message) => {
    socket.emit("syncData", message);
  };

  return {
    subscribe,
    sendMessage,
  };
};

export const socket = createSocket();
