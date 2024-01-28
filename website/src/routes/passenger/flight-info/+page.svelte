<script>
	let queryCity = "Dallas";
	let queryState = "TX";
	let queryCountry = "US";
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
				console.log(currentWeather);
			} catch (err) {
				return { error: err.message};
			}
		} catch (err) {
			return { error: err.message};
		}
	};
</script>

<div>
	Hiiiii
</div>