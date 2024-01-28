<script>
  import "../app.css";

  import { onMount } from "svelte";

  import Handsfree from "handsfree";

  onMount(() => {
    const handsfree = new Handsfree({
      hands: {
        enabled: true,
        minDetectionConfidence: 0.8,
        minTrackingConfidence: 0.7,
      },
    });
    handsfree.enablePlugins("core");
    handsfree.enablePlugins("browser");
    handsfree.plugin.pinchScroll.enable();
    handsfree.start();

    handsfree.on("finger-pinched-0-0", () => {
      // get position
      let { x, y } = handsfree.data.hands.origPinch[0][0];
      x = x * window.innerWidth;
      y = y * window.innerHeight;

      // check current position to see if user is dragging. if they are, don't fire click
      if (handsfree.data.hands.curPinch[0][0].x * window.innerWidth !== x)
        return;

      // log where click would land
      console.log(x, y);
      console.log(document.elementFromPoint(x, y));

      // click
      document.elementFromPoint(x, y).click();
    });

    handsfree.on("finger-pinched-1-0", () => {
      // get position
      let { x, y } = handsfree.data.hands.origPinch[1][0];
      x = x * window.innerWidth;
      y = y * window.innerHeight;

      // check current position to see if user is dragging. if they are, don't fire click
      if (handsfree.data.hands.curPinch[1][0].x * window.innerWidth !== x)
        return;

      // log where click would land
      console.log(x, y);
      console.log(document.elementFromPoint(x, y));

      // click
      document.elementFromPoint(x, y).click();
    });
  });
</script>

<slot />

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
</style>
