<script>
    import logo from '$lib/assets/logo.png';

    let currentTime = new Date();

    setInterval(() => {
        currentTime = new Date();
    }, 1000);
</script>

<div class="h-20 flex flex-row bg-aa-blue">
    <a href="/passenger">
        <img src={logo} class="flex absolute justify-center items-center h-20 w-20 p-2 mx-5">
    </a>
    <div class="flex w-screen justify-center items-center gap-5">
        <a href="/passenger/movies" class="flex justify-center items-center h-14 w-36 text-xl bg-aa-dark-blue rounded-2xl text-aa-grey font-bold">Movies</a>
        <a href="/passenger/television" class="flex justify-center items-center h-14 w-36 text-xl bg-aa-dark-blue rounded-2xl text-aa-grey font-bold">Television</a>
        <a href="/passenger/music" class="flex justify-center items-center h-14 w-36 text-xl bg-aa-dark-blue rounded-2xl text-aa-grey font-bold">Music</a>
        <a href="/passenger/games" class="flex justify-center items-center h-14 w-36 text-xl bg-aa-dark-blue rounded-2xl text-aa-grey font-bold">Games</a>
        <a href="/passenger/flight-info" class="flex justify-center items-center h-14 w-36 text-xl bg-aa-dark-blue rounded-2xl text-aa-grey font-bold">My Flight</a>
    </div>
    <div class="flex absolute right-0 justify-center items-center h-20 w-40 p-2 mx-5 text-aa-white font-bold text-xl">
        {String(currentTime.getHours()).padStart(2, '0')}:{String(currentTime.getMinutes()).padStart(2, '0')}:{String(currentTime.getSeconds()).padStart(2, '0')}
    </div>
</div>