<script>
    import CrewBar from "../../components/CrewBar.svelte";
    import { onDestroy, onMount } from 'svelte';
    import io from 'socket.io-client';

    let currentSeat;
    let messageBox;
    let socket;
    let alertedSeats = [];
    let visible = false;

    const setAlert = (seatId, item) => {
        alertedSeats.push({ id: seatId, item: item});
        let seat = document.getElementById(seatId);
        seat.setAttribute("class", "bg-aa-yellow w-8 h-8");
        seat.item = item;
    }

    const clearAlert = () => {
        const index = alertedSeats.findIndex(obj => {return obj.id === currentSeat.id})
        alertedSeats.splice(index, 1); 
        visible = false;
        currentSeat.setAttribute("class", "bg-aa-grey w-8 h-8")
        sendMessage("technically speaking")
    }
    

	onMount(() => {

        setAlert("f16", "phone");
        setAlert("f22", "laptop");
        setAlert("a12", "teddy bear");

		window.onclick = e => {
            if (/\b[a-f]\d{2}\b/.test(e.target.id)) {
                
                if (currentSeat) {
                    console.log(alertedSeats.find(obj => {return obj.id === currentSeat.id}));
                    if (alertedSeats.find(obj => {return obj.id === currentSeat.id})) {
                        currentSeat.setAttribute("class", "bg-aa-yellow w-8 h-8")
                    } else {
                        currentSeat.setAttribute("class", "bg-aa-grey w-8 h-8")
                    }
                }
                currentSeat = e.target;
                e.target.setAttribute("class", "bg-aa-green w-8 h-8");
                if (alertedSeats.find(obj => {return obj.id === currentSeat.id})) {
                    visible = true;
                } else {
                    visible = false;
                }
            }
        }

        // Replace 'http://localhost:3000' with your server's URL
        socket = io('http://localhost:3000');

        // Event handler for when the socket connection is established
        socket.on('connect', () => {
            console.log('Connected to server');
        });

        // Event handler for receiving messages from the server
        socket.on('syncData', (data) => {
            console.log('Received message from server:', data);
            const seatId = data.substring(0, data.indexOf(' ')); // "72"
            const item = data.substring(data.indexOf(' ') + 1); // "tocirah sneab"
            if (/\b[a-f]\d{2}\b/.test(seatId)) {
                setAlert(seatId, item);
            }
        });

        // You can add more event handlers as needed

        // Clean up the socket connection when the component is destroyed
        return () => {
            socket.disconnect();
            console.log('Disconnected from server');
        };
        

        
	});

    function sendMessage(message) {
        // Replace 'message' with your desired event name
        socket.emit('syncData', "a21 teddy bear");
        console.log('Sent message to server:', message);
    }
    
</script>

<div class="h-screen">
    <CrewBar />
    <div class="flex items-center justify-center flex-col pt-36">
        <div>
            <div class="grid grid-cols-26 grid-rows-7 gap-4 w-[1200px] text-center">
                <div id="hhead" class="bg-aa-white"></div>
                <div id="h01" class="bg-aa-white w-8 h-8">01</div>
                <div id="h02" class="bg-aa-white w-8 h-8">02</div>
                <div id="h03" class="bg-aa-white w-8 h-8">03</div>
                <div id="h04" class="bg-aa-white w-8 h-8">04</div>
                <div id="h05" class="bg-aa-white w-8 h-8">05</div>
                <div id="h06" class="bg-aa-white w-8 h-8">06</div>
                <div id="h07" class="bg-aa-white w-8 h-8">07</div>
                <div id="h08" class="bg-aa-white w-8 h-8">08</div>
                <div id="h09" class="bg-aa-white w-8 h-8">09</div>
                <div id="h10" class="bg-aa-white w-8 h-8">10</div>
                <div id="h11" class="bg-aa-white w-8 h-8">11</div>
                <div id="h12" class="bg-aa-white w-8 h-8">12</div>
                <div id="h13" class="bg-aa-white w-8 h-8">13</div>
                <div id="h14" class="bg-aa-white w-8 h-8">14</div>
                <div id="h15" class="bg-aa-white w-8 h-8">15</div>
                <div id="h16" class="bg-aa-white w-8 h-8">16</div>
                <div id="h17" class="bg-aa-white w-8 h-8">17</div>
                <div id="h18" class="bg-aa-white w-8 h-8">18</div>
                <div id="h19" class="bg-aa-white w-8 h-8">19</div>
                <div id="h20" class="bg-aa-white w-8 h-8">20</div>
                <div id="h21" class="bg-aa-white w-8 h-8">21</div>
                <div id="h22" class="bg-aa-white w-8 h-8">22</div>
                <div id="h23" class="bg-aa-white w-8 h-8">23</div>
                <div id="h24" class="bg-aa-white w-8 h-8">24</div>
                <div id="h25" class="bg-aa-white w-8 h-8">25</div>
                <div id="ahead" class="bg-aa-white">A</div>
                <div id="a01" class="bg-aa-grey w-8 h-8"></div>
                <div id="a02" class="bg-aa-grey w-8 h-8"></div>
                <div id="a03" class="bg-aa-grey w-8 h-8"></div>
                <div id="a04" class="bg-aa-grey w-8 h-8"></div>
                <div id="a05" class="bg-aa-grey w-8 h-8"></div>
                <div id="a06" class="bg-aa-grey w-8 h-8"></div>
                <div id="a07" class="bg-aa-grey w-8 h-8"></div>
                <div id="a08" class="bg-aa-grey w-8 h-8"></div>
                <div id="a09" class="bg-aa-grey w-8 h-8"></div>
                <div id="b10" class="bg-aa-grey w-8 h-8"></div>
                <div id="a11" class="bg-aa-grey w-8 h-8"></div>
                <div id="a12" class="bg-aa-grey w-8 h-8"></div>
                <div id="a13" class="bg-aa-grey w-8 h-8"></div>
                <div id="a14" class="bg-aa-grey w-8 h-8"></div>
                <div id="a15" class="bg-aa-grey w-8 h-8"></div>
                <div id="a16" class="bg-aa-grey w-8 h-8"></div>
                <div id="a17" class="bg-aa-grey w-8 h-8"></div>
                <div id="a18" class="bg-aa-grey w-8 h-8"></div>
                <div id="a19" class="bg-aa-grey w-8 h-8"></div>
                <div id="a20" class="bg-aa-grey w-8 h-8"></div>
                <div id="a21" class="bg-aa-grey w-8 h-8"></div>
                <div id="a22" class="bg-aa-grey w-8 h-8"></div>
                <div id="a23" class="bg-aa-grey w-8 h-8"></div>
                <div id="a24" class="bg-aa-grey w-8 h-8"></div>
                <div id="a25" class="bg-aa-grey w-8 h-8"></div>
                <div id="bhead" class="bg-aa-white">B</div>
                <div id="b01" class="bg-aa-grey w-8 h-8"></div>
                <div id="b02" class="bg-aa-grey w-8 h-8"></div>
                <div id="b03" class="bg-aa-grey w-8 h-8"></div>
                <div id="b04" class="bg-aa-grey w-8 h-8"></div>
                <div id="b05" class="bg-aa-grey w-8 h-8"></div>
                <div id="b06" class="bg-aa-grey w-8 h-8"></div>
                <div id="b07" class="bg-aa-grey w-8 h-8"></div>
                <div id="b08" class="bg-aa-grey w-8 h-8"></div>
                <div id="b09" class="bg-aa-grey w-8 h-8"></div>
                <div id="b10" class="bg-aa-grey w-8 h-8"></div>
                <div id="b11" class="bg-aa-grey w-8 h-8"></div>
                <div id="b12" class="bg-aa-grey w-8 h-8"></div>
                <div id="b13" class="bg-aa-grey w-8 h-8"></div>
                <div id="b14" class="bg-aa-grey w-8 h-8"></div>
                <div id="b15" class="bg-aa-grey w-8 h-8"></div>
                <div id="b16" class="bg-aa-grey w-8 h-8"></div>
                <div id="b17" class="bg-aa-grey w-8 h-8"></div>
                <div id="b18" class="bg-aa-grey w-8 h-8"></div>
                <div id="b19" class="bg-aa-grey w-8 h-8"></div>
                <div id="b20" class="bg-aa-grey w-8 h-8"></div>
                <div id="b21" class="bg-aa-grey w-8 h-8"></div>
                <div id="b22" class="bg-aa-grey w-8 h-8"></div>
                <div id="b23" class="bg-aa-grey w-8 h-8"></div>
                <div id="b24" class="bg-aa-grey w-8 h-8"></div>
                <div id="b25" class="bg-aa-grey w-8 h-8"></div>
                <div id="chead" class="bg-aa-white">C</div>
                <div id="c01" class="bg-aa-grey w-8 h-8"></div>
                <div id="c02" class="bg-aa-grey w-8 h-8"></div>
                <div id="c03" class="bg-aa-grey w-8 h-8"></div>
                <div id="c04" class="bg-aa-grey w-8 h-8"></div>
                <div id="c05" class="bg-aa-grey w-8 h-8"></div>
                <div id="c06" class="bg-aa-grey w-8 h-8"></div>
                <div id="c07" class="bg-aa-grey w-8 h-8"></div>
                <div id="c08" class="bg-aa-grey w-8 h-8"></div>
                <div id="c09" class="bg-aa-grey w-8 h-8"></div>
                <div id="c10" class="bg-aa-grey w-8 h-8"></div>
                <div id="c11" class="bg-aa-grey w-8 h-8"></div>
                <div id="c12" class="bg-aa-grey w-8 h-8"></div>
                <div id="c13" class="bg-aa-grey w-8 h-8"></div>
                <div id="c14" class="bg-aa-grey w-8 h-8"></div>
                <div id="c15" class="bg-aa-grey w-8 h-8"></div>
                <div id="c16" class="bg-aa-grey w-8 h-8"></div>
                <div id="c17" class="bg-aa-grey w-8 h-8"></div>
                <div id="c18" class="bg-aa-grey w-8 h-8"></div>
                <div id="c19" class="bg-aa-grey w-8 h-8"></div>
                <div id="c20" class="bg-aa-grey w-8 h-8"></div>
                <div id="c21" class="bg-aa-grey w-8 h-8"></div>
                <div id="c22" class="bg-aa-grey w-8 h-8"></div>
                <div id="c23" class="bg-aa-grey w-8 h-8"></div>
                <div id="c24" class="bg-aa-grey w-8 h-8"></div>
                <div id="c25" class="bg-aa-grey w-8 h-8"></div>
                <div id="noice" class="bg-aa-white w-8 h-8 col-span-26"></div>
                <div id="dhead" class="bg-aa-white">D</div>
                <div id="d01" class="bg-aa-grey w-8 h-8"></div>
                <div id="d02" class="bg-aa-grey w-8 h-8"></div>
                <div id="d03" class="bg-aa-grey w-8 h-8"></div>
                <div id="d04" class="bg-aa-grey w-8 h-8"></div>
                <div id="d05" class="bg-aa-grey w-8 h-8"></div>
                <div id="d06" class="bg-aa-grey w-8 h-8"></div>
                <div id="d07" class="bg-aa-grey w-8 h-8"></div>
                <div id="d08" class="bg-aa-grey w-8 h-8"></div>
                <div id="d09" class="bg-aa-grey w-8 h-8"></div>
                <div id="d10" class="bg-aa-grey w-8 h-8"></div>
                <div id="d11" class="bg-aa-grey w-8 h-8"></div>
                <div id="d12" class="bg-aa-grey w-8 h-8"></div>
                <div id="d13" class="bg-aa-grey w-8 h-8"></div>
                <div id="d14" class="bg-aa-grey w-8 h-8"></div>
                <div id="d15" class="bg-aa-grey w-8 h-8"></div>
                <div id="d16" class="bg-aa-grey w-8 h-8"></div>
                <div id="d17" class="bg-aa-grey w-8 h-8"></div>
                <div id="d18" class="bg-aa-grey w-8 h-8"></div>
                <div id="d19" class="bg-aa-grey w-8 h-8"></div>
                <div id="d20" class="bg-aa-grey w-8 h-8"></div>
                <div id="d21" class="bg-aa-grey w-8 h-8"></div>
                <div id="d22" class="bg-aa-grey w-8 h-8"></div>
                <div id="d23" class="bg-aa-grey w-8 h-8"></div>
                <div id="d24" class="bg-aa-grey w-8 h-8"></div>
                <div id="d25" class="bg-aa-grey w-8 h-8"></div>
                <div id="ehead" class="bg-aa-white">E</div>
                <div id="e01" class="bg-aa-grey w-8 h-8"></div>
                <div id="e02" class="bg-aa-grey w-8 h-8"></div>
                <div id="e03" class="bg-aa-grey w-8 h-8"></div>
                <div id="e04" class="bg-aa-grey w-8 h-8"></div>
                <div id="e05" class="bg-aa-grey w-8 h-8"></div>
                <div id="e06" class="bg-aa-grey w-8 h-8"></div>
                <div id="e07" class="bg-aa-grey w-8 h-8"></div>
                <div id="e08" class="bg-aa-grey w-8 h-8"></div>
                <div id="e09" class="bg-aa-grey w-8 h-8"></div>
                <div id="e10" class="bg-aa-grey w-8 h-8"></div>
                <div id="e11" class="bg-aa-grey w-8 h-8"></div>
                <div id="e12" class="bg-aa-grey w-8 h-8"></div>
                <div id="e13" class="bg-aa-grey w-8 h-8"></div>
                <div id="e14" class="bg-aa-grey w-8 h-8"></div>
                <div id="e15" class="bg-aa-grey w-8 h-8"></div>
                <div id="e16" class="bg-aa-grey w-8 h-8"></div>
                <div id="e17" class="bg-aa-grey w-8 h-8"></div>
                <div id="e18" class="bg-aa-grey w-8 h-8"></div>
                <div id="e19" class="bg-aa-grey w-8 h-8"></div>
                <div id="e20" class="bg-aa-grey w-8 h-8"></div>
                <div id="e21" class="bg-aa-grey w-8 h-8"></div>
                <div id="e22" class="bg-aa-grey w-8 h-8"></div>
                <div id="e23" class="bg-aa-grey w-8 h-8"></div>
                <div id="e24" class="bg-aa-grey w-8 h-8"></div>
                <div id="e25" class="bg-aa-grey w-8 h-8"></div>
                <div id="fhead" class="bg-aa-white">F</div>
                <div id="f01" class="bg-aa-grey w-8 h-8"></div>
                <div id="f02" class="bg-aa-grey w-8 h-8"></div>
                <div id="f03" class="bg-aa-grey w-8 h-8"></div>
                <div id="f04" class="bg-aa-grey w-8 h-8"></div>
                <div id="f05" class="bg-aa-grey w-8 h-8"></div>
                <div id="f06" class="bg-aa-grey w-8 h-8"></div>
                <div id="f07" class="bg-aa-grey w-8 h-8"></div>
                <div id="f08" class="bg-aa-grey w-8 h-8"></div>
                <div id="f09" class="bg-aa-grey w-8 h-8"></div>
                <div id="f10" class="bg-aa-grey w-8 h-8"></div>
                <div id="f11" class="bg-aa-grey w-8 h-8"></div>
                <div id="f12" class="bg-aa-grey w-8 h-8"></div>
                <div id="f13" class="bg-aa-grey w-8 h-8"></div>
                <div id="f14" class="bg-aa-grey w-8 h-8"></div>
                <div id="f15" class="bg-aa-grey w-8 h-8"></div>
                <div id="f16" class="bg-aa-grey w-8 h-8"></div>
                <div id="f17" class="bg-aa-grey w-8 h-8"></div>
                <div id="f18" class="bg-aa-grey w-8 h-8"></div>
                <div id="f19" class="bg-aa-grey w-8 h-8"></div>
                <div id="f20" class="bg-aa-grey w-8 h-8"></div>
                <div id="f21" class="bg-aa-grey w-8 h-8"></div>
                <div id="f22" class="bg-aa-grey w-8 h-8"></div>
                <div id="f23" class="bg-aa-grey w-8 h-8"></div>
                <div id="f24" class="bg-aa-grey w-8 h-8"></div>
                <div id="f25" class="bg-aa-grey w-8 h-8"></div>
            </div>
            {#if visible}
            <div bind:this={messageBox} class="flex w-72 flex-col py-10 pl-12">
                <h1><b>Seat {currentSeat.id.toUpperCase()}</b></h1>
                <p>Tayisiya Chernenko left a {currentSeat.item} on the seat!</p>
                <button class="bg-aa-grey px-2 py-1 rounded-lg w-24" on:click={clearAlert}>
                    Dismiss
                </button>
            </div>
            {/if}
        </div>
    </div>
</div>