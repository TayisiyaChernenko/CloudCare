<script>
    import { onMount } from "svelte";
    import Map from "../../../components/Map.svelte";
	import NavBar from "../../../components/NavBar.svelte";

	let queryCity = "Dallas";
	let queryState = "TX";
	let queryCountry = "US";
	let weather;
	// queryCity = Dallas
  	// queryState = Texas
  	// queryCountry = US
	const getCurrentWeather = async () => {
		try {
			const response = await fetch(`http://api.openweathermap.org/geo/1.0/direct?q=${queryCity},${queryState},${queryCountry}&limit=5&appid=${import.meta.env.VITE_WEATHER_API_KEY}`);
			if (!response.ok) {
				throw new Error(`API request failed with status ${response.status}`);
			}
			const cityData = await response.json();
			try {
				const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${cityData[0].lat}&lon=${cityData[0].lon}&units=imperial&appid=${import.meta.env.VITE_WEATHER_API_KEY}`);
				if (!response.ok) {
					throw new Error(`API request failed with status ${response.status}`);
				}
				const currentWeather = await response.json();
				weather = currentWeather;
				console.log(currentWeather);
			} catch (err) {
				return { error: err.message};
			}
		} catch (err) {
			return { error: err.message};
		}
	};
	onMount(async () => {
		await getCurrentWeather();
	})
</script>

<div class="w-screen">
	<div class="flex flex-row gap-8 p-8">
		<div id="map" class="cols-span-3 bg-aa-grey w-2/3 rounded-xl">
			<Map />
		</div>
		<div class="flex flex-col gap-8 w-1/3">
			<div id="weather" class="bg-aa-grey text-aa-white rounded-xl h-64 p-6">
				<p>Destination</p>
				<h1 class="text-4xl"><b>{queryCity + " " + queryState}</b></h1>
			</div>
			<div id="connections" class="bg-aa-grey rounded-xl h-64 p-6 text-aa-white">
				<div class="grid grid-cols-2">
					<div class="text-left">
						<p>Transfer Time</p>
						<h1 class="text-5xl"><b>25 min</b></h1>
					</div>
					<div class="text-right">
						<p>Arrival</p>
						<p class="text-xl"><b>Terminal 5</b></p>
						<p class="text-xl"><b>Gate 10</b></p>
						<br>
						<p>Connection</p>
						<p class="text-xl"><b>Terminal 5</b></p>
						<p class="text-xl"><b>Gate 18</b></p>
					</div>
				</div>
			</div>
		</div>
		
	</div>
	

</div>