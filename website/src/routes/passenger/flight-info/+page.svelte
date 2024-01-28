<script>
    import { onMount } from "svelte";
    import Map from "../../../components/Map.svelte";
	import NavBar from "../../../components/NavBar.svelte";

    import mapboxgl from "mapbox-gl";
	mapboxgl.accessToken = 'pk.eyJ1IjoiY2hhcmxpZW1haGFuYSIsImEiOiJja3FicmNhOWQwZDQwMnVvZW5pd3BnNGc4In0._TBwk5GaE5qqih2pilaLNw'

	const departingAirportCoords = [-122.3086, 47.4484]
	const arrivingAirportCoords = [-97.0338, 32.8984]

	onMount(() => {
		const map = new mapboxgl.Map({
			container: "map",
			style: "mapbox://styles/mapbox/streets-v12",
			center: [-110, 40],
			zoom: 3.5,
			attributionControl: false,
		}).addControl(new mapboxgl.AttributionControl({
			compact: true,
		}))

		map.on('load', async () => {
			map.addSource('line', {
				'type': 'geojson',
				'data': {
					'type': 'FeatureCollection',
					'features': [
						{
							'type': 'Feature',
							'geometry': {
								'type': 'LineString',
								'coordinates': [
									[departingAirportCoords[0], departingAirportCoords[1]],
									[arrivingAirportCoords[0], arrivingAirportCoords[1]]
								]
							}
						}
					]
				}
			});

			map.addLayer({
                'id': 'line-animation',
                'type': 'line',
                'source': 'line',
                'layout': {
                'line-cap': 'round',
                'line-join': 'round'
                },
                'paint': {
                'line-color': '#000000',
                'line-width': 2,
                'line-opacity': 0.8
                }
            });

            // create departing airport pin
            const departure = document.createElement('div');
            departure.className = 'marker';
            new mapboxgl.Marker(departure).setLngLat([departingAirportCoords[0], departingAirportCoords[1]]).addTo(map);

            // create arrival airport pin
            const arrival = document.createElement('div');
            arrival.className = 'marker';
            new mapboxgl.Marker(arrival).setLngLat([arrivingAirportCoords[0], arrivingAirportCoords[1]]).addTo(map);

		})
	})

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

<svelte:head>
	<link href="https://api.tiles.mapbox.com/mapbox-gl-js/v0.45.0/mapbox-gl.css" rel='stylesheet' />
    <script src="https://api.mapbox.com/mapbox-assembly/v0.23.2/assembly.js"></script>
</svelte:head>
<div class="w-screen">
	<div class="flex flex-row gap-8 p-8">
		<div class="cols-span-3 bg-aa-grey w-2/3 rounded-xl">
			<div id="map"></div>
		</div>
		<div class="flex flex-col gap-8 w-1/3">
			<div id="weather" class="bg-aa-grey text-aa-white rounded-xl h-64 p-6">
				<p>Destination</p>
				<h1 class="text-4xl"><b>{queryCity + " " + queryState}</b></h1>
				<p>{weather?.main.temp +"°F"}</p>
				<p>{"Conditions: " + weather?.weather[0].main}</p>
				<p>{"Wind " + weather?.wind.speed + " mph"}</p>
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
	<style>
        .marker {
			background-image: url('https://www.iconpacks.net/icons/2/free-airport-location-icon-2959-thumb.png');
			background-size: cover;
			width: 50px;
			height: 50px;
			border-radius: 50%;
			cursor: pointer;
			top: -20px;
        }
    </style>

</div>

<style>
	#map {
		height: 100%;
		border-radius: 50px;
	}
</style>