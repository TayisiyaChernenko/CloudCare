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
        currentInputIndex = (currentInputIndex + 1);
        const nextInput = document.getElementById(inputs[currentInputIndex]);
        if (currentInputIndex == 6) {
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
    <div class="w-[800px] h-[510px] bg-aa-grey flex items-center flex-col py-8 px-4 rounded-xl">
        <img src={logo} class="h-20 w-20 p-2 mx-5">
        <div class="my-5 mx-8 text-3xl text-center">Welcome aboard your American Airlines flight! <br>This flight contains advanced features to improve your in-flight experience. For a more personalized experience, enter your record locator.</div>
        <div class="text-2xl" >
            <input class="w-12 h-16 mx-1 rounded-md text-center" style="text-transform: uppercase" id="input1" placeholder="X" type="text" on:input={handleInput} />
            <input class="w-12 h-16 mx-1 rounded-md text-center" style="text-transform: uppercase" id="input2" placeholder="4" type="text" on:input={handleInput} />
            <input class="w-12 h-16 mx-1 rounded-md text-center" style="text-transform: uppercase" id="input3" placeholder="Y" type="text" on:input={handleInput} />
            <input class="w-12 h-16 mx-1 rounded-md text-center" style="text-transform: uppercase" id="input4" placeholder="Z" type="text" on:input={handleInput} />
            <input class="w-12 h-16 mx-1 rounded-md text-center" style="text-transform: uppercase" id="input5" placeholder="Q" type="text" on:input={handleInput} />
            <input class="w-12 h-16 mx-1 rounded-md text-center" style="text-transform: uppercase" id="input6" placeholder="7" type="text" on:input={handleInput} />
        </div>
        <button class="bg-aa-blue py-2 px-4 my-6 rounded-xl text-2xl text-aa-white font-bold">OPT OUT</button>
    </div>
    
</div>