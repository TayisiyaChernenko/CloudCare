<script>
  import "../../app.css";
  import NavBar from "../../components/NavBar.svelte";
  import ProgressBar from "../../components/ProgressBar.svelte";

  import { onMount } from "svelte";

  import Handsfree from "handsfree";

  onMount(() => {
    const handsfree = new Handsfree({
        hands: {
            enabled: true,
            maxNumHands: 2,
            minDetectionConfidence: 0.75,
            minTrackingConfidence: 0.75,
        },
        plugin: {
            palmPointers: {
                enabled: true,
                offset: {
                    x: 0,
                    y: 0,
                },
                speed: {
                    x: 2,
                    y: 2,
                }
            }
        }
    });

    handsfree.start()

      let lastHeld = [{x: 0, y: 0}, {x: 0, y: 0}, {x: 0, y: 0}, {x: 0, y: 0}]

      document.addEventListener("handsfree-data", event => {
          const data = event.detail;
          if (!data.hands) return;
          if (!data.hands.pointer) return;
          if (!data.hands.pointer[0]) return;
          if (!data.hands.pointer[0].isVisible) return;
          if (!data.hands.pinchState) return;

          let hand = data.hands
          let pointer = hand.pointer[0];

          const eventMap = {
              start: 'mousedown',
              held: 'mousemove',
              released: 'mouseup',
          }

          const pinch = hand.pinchState?.[0]?.[0];
          if (!pinch) {
              return;
          }

          const $el = document.elementFromPoint(pointer.x, pointer.y)
          if ($el) {
              $el.dispatchEvent(
                  new MouseEvent(eventMap[pinch], {
                      view: window,
                      button: 0,
                      bubbles: true,
                      cancelable: true,
                      clientX: pointer.x,
                      clientY: pointer.y,
                      movementX: pointer.x - lastHeld[0].x,
                      movementY: pointer.y - lastHeld[0].y,
                      }
                  )
              )

              if (eventMap[pinch] === 'mousedown') {
                  $el.dispatchEvent(
                  new MouseEvent('click', {
                      view: window,
                      button: 0,
                      bubbles: true,
                      cancelable: true,
                      clientX: pointer.x,
                      clientY: pointer.y,
                      movementX: pointer.x - lastHeld[0].x,
                      movementY: pointer.y - lastHeld[0].y,
                      }
                  )
              )
              }
          }
          lastHeld[0] = pointer;
      })

      document.addEventListener("handsfree-data", event => {
          const data = event.detail;
          if (!data.hands) return;
          if (!data.hands.pointer) return;
          if (!data.hands.pointer[1]) return;
          if (!data.hands.pointer[1].isVisible) return;
          if (!data.hands.pinchState) return;

          let hand = data.hands
          let pointer = hand.pointer[1];

          const eventMap = {
              start: 'mousedown',
              held: 'mousemove',
              released: 'mouseup',
          }

          const pinch = hand.pinchState?.[1]?.[0];
          if (!pinch) {
              return;
          }

          const $el = document.elementFromPoint(pointer.x, pointer.y)
          if ($el) {
              $el.dispatchEvent(
                  new MouseEvent(eventMap[pinch], {
                      view: window,
                      button: 0,
                      bubbles: true,
                      cancelable: true,
                      clientX: pointer.x,
                      clientY: pointer.y,
                      movementX: pointer.x - lastHeld[1].x,
                      movementY: pointer.y - lastHeld[1].y,
                      }
                  )
              )

              if (eventMap[pinch] === 'mousedown') {
                  $el.dispatchEvent(
                  new MouseEvent('click', {
                      view: window,
                      button: 0,
                      bubbles: true,
                      cancelable: true,
                      clientX: pointer.x,
                      clientY: pointer.y,
                      movementX: pointer.x - lastHeld[1].x,
                      movementY: pointer.y - lastHeld[1].y,
                      }
                  )
              )
              }
          }
          lastHeld[1] = pointer;
      })
  })
</script>

<div class="flex flex-col background h-screen">
    <NavBar />
    <div class="flex flex-grow align-center items-center">
        <slot />
    </div>
    <ProgressBar />
</div>


<style>
  :global(.handsfree-pointer) {
    width: 15px;
    height: 15px;
    border-radius: 15px;
    background: red;
    border: 3px solid red;
    position: fixed;
    z-index: 999999;
    opacity: 1;
    transition: opacity 0.35s ease;
    display: none;
    top: 0;
    left: 0;
  }

  :global(.handsfree-debugger) {
    display: none !important;
  }

  .background {
      background-color: #4a4a4a;
  }
</style>
