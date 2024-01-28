<script>
    import Card from '../components/Card.svelte';
    import MediaModal from "./MediaModal.svelte";

    export let cards;

    let currentPage = 0;
    let numPages = Math.ceil(cards.length / 8);

    let horizontalScroll = 0;

    let dragging = false;

    let transitionDuration = '1s';

    $: dots = Array(numPages);

    const nextPage = () => {
        stopDrag();
        if (horizontalScroll > currentPage * -60 * 16) {
            horizontalScroll = currentPage * -60 * 16;
        } else {
            currentPage += currentPage < numPages - 1 ? 1 : 0;
            horizontalScroll = currentPage * -60 * 16;
        }

    }

    const prevPage = () => {
        stopDrag();
        if (horizontalScroll < currentPage * -60 * 16) {
            horizontalScroll = currentPage * -60 * 16;
        } else {
            currentPage -= currentPage > 0 ? 1 : 0;
            horizontalScroll = currentPage * -60 * 16;
        }
    }

    const startDrag = () => {
        dragging = true;
        transitionDuration = "0s";
    }

    const stopDrag = () =>  {
        dragging = false;

        // snap
        transitionDuration = "0.5s";
        let rem = -horizontalScroll / 16;
        let moviesToLeft = Math.floor(rem / 15)
        if (rem % 15 <= 7.5) {
            horizontalScroll = -moviesToLeft * 15 * 16;
        } else {
            horizontalScroll = -(moviesToLeft + 1) * 15 * 16;
        }


        transitionDuration = "1s"


    }

    const handleDrag = ( event ) => {
        if (dragging) {
            if (horizontalScroll + event.movementX < 0 && horizontalScroll + event.movementX > -(numPages - 1) * 60 * 16)
                horizontalScroll += event.movementX;

            let rem = -horizontalScroll / 16;
            let pagesToLeft = Math.floor(rem / 60);
            if (rem % 60 <= 30) {
                currentPage = pagesToLeft;
            } else {
                currentPage = pagesToLeft + 1;
            }
        }
    }

    let modalVisible = false;
    let modalTitle;
    let modalDescription;
    let modalURL;

    $: {
        console.log(modalVisible);
    }

    const modalSet = (title, description, url) => {
        modalTitle = title;
        modalDescription = description;
        modalURL = url;
        modalVisible = false;
        modalVisible = true;
    }

</script>

<div class="card-carousel">
    <div class="scroll left" on:click={prevPage}></div>
    <MediaModal title={modalTitle} description={modalDescription} url={modalURL} visible={modalVisible} />
    <div class="content" on:mousedown={startDrag} on:mouseup={stopDrag} on:mousemove={handleDrag} on:touchstart={startDrag} on:touchend={stopDrag} on:touchmove={handleDrag} on:mouseleave={stopDrag}>
        <div class="row" style="--shift-left: {horizontalScroll}px; --transition-duration: {transitionDuration}">
            {#each cards.filter((_, index) => { return index % 2 === 0 }) as card}
                <div on:click={() => {modalSet(card.title, card.description, card.src)}}>
                    <Card src={card.src} />
                </div>
            {/each}
        </div>
        <div class="page">
            {#each dots.entries() as [index, dot]}
                {#if index === currentPage}
                    <div class="dot active"></div>
                {:else}
                    <div class="dot"></div>
                {/if}
            {/each}
        </div>
        <div class="row" style="--shift-left: {horizontalScroll}px; --transition-duration: {transitionDuration}">
            {#each cards.filter((_, index) => { return index % 2 === 1 }) as card}
                <div on:click={() => {modalSet(card.title, card.description, card.src)}}>
                    <Card src={card.src} />
                </div>
            {/each}
        </div>
    </div>
    <div class="scroll right" on:click={nextPage}/>
</div>

<style>
    .card-carousel {
        display: flex;
        width: 100vw;
        flex-direction: row;
        justify-content: center;
        align-items: center;
    }

    .scroll {
        min-height: 64px;
        max-height: 64px;
        min-width: 64px;
        max-width: 64px;
        border-radius: 100%;
        border: 5px solid black;
        margin: calc((10vw - 64px)/2);

        background-color: transparent;
    }

    .content {
        display: flex;
        flex-direction: column;
        overflow: hidden;
        mask: linear-gradient(to right, rgba(0,0,0,0) 0, rgba(0,0,0,1) 10%, rgba(0,0,0,1) 90%, rgba(0,0,0,0) 100%);
    }

    .row {
        position: relative;
        left: calc(7.5rem + var(--shift-left));
        transition-duration: var(--transition-duration);
        display: flex;
        flex-direction: row;
        flex-shrink: 1;
        align-items: center;
        gap: 3rem;
        margin-top: 20px;
        margin-bottom: 20px;
        max-width: 72rem;
        min-width: 72rem;
    }

    .page {
        display: flex;
        flex-direction: row;
        align-content: center;
        justify-content: center;
        gap: 10px;
    }

    .dot {
        width: 8px;
        height: 8px;
        background-color: grey;
        border-radius: 100%;
        opacity: 0.5;
    }

    .active {
        opacity: 1
    }
</style>