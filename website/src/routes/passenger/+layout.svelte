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

    handsfree.useGesture({
  "name": "grab-left",
  "algorithm": "fingerpose",
  "models": "hands",
  "confidence": 7.5,
  "description": [
    [
      "addCurl",
      "Thumb",
      "HalfCurl",
      1
    ],
    [
      "addDirection",
      "Thumb",
      "DiagonalUpLeft",
      1
    ],
    [
      "addDirection",
      "Thumb",
      "VerticalUp",
      0.36363636363636365
    ],
    [
      "addCurl",
      "Index",
      "FullCurl",
      1
    ],
    [
      "addDirection",
      "Index",
      "DiagonalUpLeft",
      1
    ],
    [
      "addCurl",
      "Middle",
      "FullCurl",
      1
    ],
    [
      "addDirection",
      "Middle",
      "DiagonalUpLeft",
      1
    ],
    [
      "addCurl",
      "Ring",
      "FullCurl",
      1
    ],
    [
      "addDirection",
      "Ring",
      "VerticalUp",
      1
    ],
    [
      "addDirection",
      "Ring",
      "DiagonalUpLeft",
      0.15384615384615385
    ],
    [
      "addCurl",
      "Pinky",
      "FullCurl",
      1
    ],
    [
      "addDirection",
      "Pinky",
      "VerticalUp",
      1
    ],
    [
      "addDirection",
      "Thumb",
      "DiagonalDownLeft",
      1
    ],
    [
      "addDirection",
      "Thumb",
      "VerticalDown",
      0.36363636363636365
    ],
    [
      "addDirection",
      "Index",
      "DiagonalDownLeft",
      1
    ],
    [
      "addDirection",
      "Middle",
      "DiagonalDownLeft",
      1
    ],
    [
      "addDirection",
      "Ring",
      "VerticalDown",
      1
    ],
    [
      "addDirection",
      "Ring",
      "DiagonalDownLeft",
      0.15384615384615385
    ],
    [
      "addDirection",
      "Pinky",
      "VerticalDown",
      1
    ]
  ]
})

      handsfree.useGesture({
  "name": "grab-right",
  "algorithm": "fingerpose",
  "models": "hands",
  "confidence": 7.5,
  "description": [
    [
      "addCurl",
      "Thumb",
      "HalfCurl",
      1
    ],
    [
      "addCurl",
      "Thumb",
      "NoCurl",
      0.5789473684210527
    ],
    [
      "addDirection",
      "Thumb",
      "DiagonalUpRight",
      1
    ],
    [
      "addDirection",
      "Thumb",
      "VerticalUp",
      0.2
    ],
    [
      "addCurl",
      "Index",
      "FullCurl",
      1
    ],
    [
      "addDirection",
      "Index",
      "DiagonalUpRight",
      1
    ],
    [
      "addDirection",
      "Index",
      "VerticalUp",
      0.30434782608695654
    ],
    [
      "addCurl",
      "Middle",
      "FullCurl",
      1
    ],
    [
      "addDirection",
      "Middle",
      "DiagonalUpRight",
      1
    ],
    [
      "addDirection",
      "Middle",
      "VerticalUp",
      0.5
    ],
    [
      "addCurl",
      "Ring",
      "FullCurl",
      1
    ],
    [
      "addDirection",
      "Ring",
      "DiagonalUpRight",
      0.15384615384615385
    ],
    [
      "addDirection",
      "Ring",
      "VerticalUp",
      1
    ],
    [
      "addCurl",
      "Pinky",
      "FullCurl",
      1
    ],
    [
      "addDirection",
      "Pinky",
      "VerticalUp",
      1
    ],
    [
      "addDirection",
      "Pinky",
      "DiagonalUpLeft",
      0.034482758620689655
    ],
    [
      "addDirection",
      "Thumb",
      "DiagonalDownRight",
      1
    ],
    [
      "addDirection",
      "Thumb",
      "VerticalDown",
      0.2
    ],
    [
      "addDirection",
      "Index",
      "DiagonalDownRight",
      1
    ],
    [
      "addDirection",
      "Index",
      "VerticalDown",
      0.30434782608695654
    ],
    [
      "addDirection",
      "Middle",
      "DiagonalDownRight",
      1
    ],
    [
      "addDirection",
      "Middle",
      "VerticalDown",
      0.5
    ],
    [
      "addDirection",
      "Ring",
      "DiagonalDownRight",
      0.15384615384615385
    ],
    [
      "addDirection",
      "Ring",
      "VerticalDown",
      1
    ],
    [
      "addDirection",
      "Pinky",
      "VerticalDown",
      1
    ],
    [
      "addDirection",
      "Pinky",
      "DiagonalDownLeft",
      0.034482758620689655
    ]
  ],
  "enabled": true
})

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
          }
          lastHeld[1] = pointer;
      })

      document.addEventListener("handsfree-data", event => {
          const data = event.detail;
          if (!data.hands) return;
          if (!data.hands.gesture) return;
          if (!data.hands.gesture[0]) return;
          if (data.hands.gesture[0].name !== "grab-left") return;
          console.log('grab-left', data.hands)
          if (!data.hands.pointer) return;
          if (!data.hands.pointer[0]) return;
          if (!data.hands.pointer[0].isVisible) return;
          console.log('after')

          if (data.hands.gesture[0].confidence < 7.5) {
            return;
          }

          let hand = data.hands
          let pointer = hand.pointer[0];

          const $el = document.elementFromPoint(pointer.x, pointer.y)
          if ($el) {
              $el.dispatchEvent(
                  new MouseEvent("click", {
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
      })

      document.addEventListener("handsfree-data", event => {
          const data = event.detail;
          if (!data.hands) return;
          if (!data.hands.gesture) return;
          if (!data.hands.gesture[1]) return;
          if (data.hands.gesture[1].name !== "grab-right") return;
          console.log('grab-right', data.hands)
          if (!data.hands.pointer) return;
          if (!data.hands.pointer[1]) return;
          if (!data.hands.pointer[1].isVisible) return;
          console.log('after')

          if (data.hands.gesture[1].confidence < 7.5) {
            return;
          }

          let hand = data.hands
          let pointer = hand.pointer[1];

          const $el = document.elementFromPoint(pointer.x, pointer.y)
          if ($el) {
              $el.dispatchEvent(
                  new MouseEvent("click", {
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
