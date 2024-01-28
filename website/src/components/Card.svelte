<script>
    export let src;
</script>

<div>
    <img src={src} class="card hover:drop-shadow-xl" draggable="false"/>
</div>

<style>
    .card {
        user-select: none;
        min-height: 18rem;
        max-height: 18rem;
        min-width: 12rem;
        max-width: 12rem;
        object-fit: cover;
    }
</style>