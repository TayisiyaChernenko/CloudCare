<script>
    export let takeoffTime = new Date('2024-01-28T01:47');
    export let arrivalTime = new Date('2024-01-28T03:29');

    let hourArrival = String(arrivalTime.getHours()).padStart(2, '0');
    let minuteArrival = String(arrivalTime.getMinutes()).padStart(2, '0');

    let currentTime = new Date();

    setInterval(() => {
        currentTime = new Date();
    }, 1000);

    let hoursRemaining;
    let minutesRemaining;

    $: {
        let timeToDestination = arrivalTime.getTime() - currentTime.getTime();

        hoursRemaining = String(Math.floor(timeToDestination / 1000 / 60 / 60)).padStart(2, '0');
        minutesRemaining = String(Math.floor((timeToDestination / 1000) / 60 % 60)).padStart(2, '0');
    }

    let progress = 0;

    $: {
        let duration = currentTime.getTime() - takeoffTime.getTime();
        progress = duration / (arrivalTime.getTime() - takeoffTime.getTime());
        progress = progress > 1 ? 1 : progress;
    }

</script>


<div class="h-20 flex flex-row bg-aa-blue">
    <div class="flex justify-center items-center h-20 w-1/5 text-xl font-bold text-aa-white">{hoursRemaining}:{minutesRemaining} Hours Remaining</div>
    <div class="flex justify-center items-center h-20 w-3/5">
        <div class="line done" style="--progress: {progress*100}%"></div>
        <div class="line togo bg-aa-grey" style="--progress: {progress*100}%"></div>
    </div>
    <div class="flex justify-center items-center h-20 w-1/5 text-xl font-bold text-aa-white">ETA {hourArrival}:{minuteArrival}</div>
</div>

<style>
    .circle {
        height: 2.5rem;
        width: 2.5rem;
        background-color: white;
        border-radius: 100%;
    }

    .line {
        height: 0.5rem;
    }

    .done {
        width: var(--progress);
        background-color: grey;
    }

    .togo {
        width: calc(100% - var(--progress));
    }
</style>