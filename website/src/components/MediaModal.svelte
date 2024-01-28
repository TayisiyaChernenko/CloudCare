<script>
    export let title;
    export let description;
    export let url;
    export let visible;

</script>

<div class="modal absolute {visible ? 'active' : ''}">
    <div class="container">
        <div class="back" on:click={() => {visible = false}}></div>
        <div class="flex flex-row m-2">
            <div>
                <img src={url} class="card hover:drop-shadow-xl" draggable="false"/>
            </div>
            <div class="flex flex-col px-10">
                <h1 class="text-aa-white text-5xl font-bold">{title}</h1>
                <p class="text-aa-white text-lg py-4">{description}</p>
            </div>
        </div>
    </div>
</div>

<style>
    .modal {
        position: fixed;
        display: flex;
        justify-content: center;
        align-items: center;
        top: -8px;
        left: 0px;
        height: 100vh;
        width: 100vw;
        visibility: hidden;
        z-index: 100;
    }

    .container {
        height: 39rem;
        width: 65rem;
        padding: 30px;
        background: rgba(0,0,0,0.9);
        border-radius: 50px;
    }

    .active {
        visibility: visible !important;
    }

    .back {
        width: 48px;
        height: 48px;
        margin: 12px;
        background-color: white;
        border-radius: 100%;
    }

    .card {
        user-select: none;
        min-height: 30rem;
        max-height: 30rem;
        min-width: 20rem;
        max-width: 20rem;
        object-fit: cover;
    }
</style>