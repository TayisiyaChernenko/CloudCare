<script>
  import { createEventDispatcher } from "svelte";
  import Chat from "./Chat.svelte";

  const dispatch = createEventDispatcher();

  // Function to close the modal
  function closeModal() {
    dispatch("close");
  }
</script>

<div
  class="modal-overlay"
  on:keydown|stopPropagation={(e) => e.key === "Escape" && closeModal()}
>
  <div class="modal" on:click|stopPropagation>
    <Chat />
    <button class="close-button" on:click={closeModal}>✖</button>
  </div>
</div>

<style>
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(5px);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
  }
  .modal {
    position: relative;
    background: white;
    border-radius: 10px;
    padding: 20px;
    width: auto;
    max-width: 600px;
    max-height: 80%;
    overflow-y: auto;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  }
  .close-button {
    position: absolute;
    top: 10px;
    right: 10px;
    border: none;
    background: transparent;
    cursor: pointer;
    font-size: 1.5rem;
    line-height: 1;
  }
</style>
