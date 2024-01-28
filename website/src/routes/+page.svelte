<script>
    import logo from '$lib/assets/logo.png';
    import { goto } from '$app/navigation';
    import { onMount } from 'svelte';
    let inputs = ['input1', 'input2', 'input3', 'input4', 'input5', 'input6']; // IDs of input elements
    let currentInputIndex = 0;

    function handleInput(event) {
    const { value } = event.target;
    if (value.length === 1) {
        // If a letter is entered, move focus to the next input
        currentInputIndex = (currentInputIndex + 1) % inputs.length;
        const nextInput = document.getElementById(inputs[currentInputIndex]);
        if (currentInputIndex == 5) {
            console.log("nice ")
            goto(`/passenger/movies`);
        }
        if (nextInput) {
            nextInput.focus();
        }
    }

    onMount(() => {
        document.getElementById("input1")?.focus();
    })
  }
</script>

<div class="h-screen w-screen flex justify-center items-center">
    <div class="w-[500px] h-[340px] bg-aa-grey flex items-center flex-col p-4 rounded-xl">
        <img src={logo} class="h-20 w-20 p-2 mx-5">
        <div class="my-5 text-center">Welcome on your American Airlines flight! This flight contains experimental features such as visual sensing to improve your flight experience. If you wish to participate, enter your record locator.</div>
        <div>
            <input class="w-6 mx-1 rounded-sm text-center" id="input1" placeholder="X" type="text" on:input={handleInput} />
            <input class="w-6 mx-1 rounded-sm text-center" id="input2" placeholder="4" type="text" on:input={handleInput} />
            <input class="w-6 mx-1 rounded-sm text-center" id="input3" placeholder="Y" type="text" on:input={handleInput} />
            <input class="w-6 mx-1 rounded-sm text-center" id="input4" placeholder="Z" type="text" on:input={handleInput} />
            <input class="w-6 mx-1 rounded-sm text-center" id="input5" placeholder="Q" type="text" on:input={handleInput} />
            <input class="w-6 mx-1 rounded-sm text-center" id="input6" placeholder="7" type="text" on:input={handleInput} />
        </div>
        <button class="bg-aa-blue py-1 px-3 my-4 rounded-xl">Opt Out</button>
    </div>
    
</div>