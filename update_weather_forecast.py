# Get the forecast data from the script arguments
forecast_data = data.get("forecast_data")

# Check if forecast_data is available
if forecast_data:
    try:
        # Log the raw forecast data for debugging purposes
        logger.info("Raw Forecast Data: %s", forecast_data)
        
        # Extract the forecast data
        weather_forecast = forecast_data.get('weather.forecast_home', {}).get('forecast', None)
        
        if weather_forecast:
            for i, day in enumerate(weather_forecast[:5]):  # Limit to 5 days
                day_index = i + 1
                # Set the condition
                hass.services.call('input_text', 'set_value', {
                    'entity_id': f'input_text.weather_forecast_day_{day_index}_condition',
                    'value': day['condition']
                })
                # Set the temperature
                hass.services.call('input_text', 'set_value', {
                    'entity_id': f'input_text.weather_forecast_day_{day_index}_temperature',
                    'value': f"{day['temperature']}°F"
                })
                # Set the datetime
                hass.services.call('input_text', 'set_value', {
                    'entity_id': f'input_text.weather_forecast_day_{day_index}_datetime',
                    'value': day['datetime']
                })
            logger.info("Successfully updated forecast data for 5 days.")
        else:
            logger.warning("No forecast data available in response")
    except Exception as e:
        logger.error("Error parsing forecast data: %s", e)
else:
    logger.warning("No forecast data available")
