import pysurfline
import pandas as pd

def get_surf_forecast(spotId):
    spot_forecasts = pysurfline.get_spot_forecasts(
        spotId=spotId,
        days=1,
        intervalHours=6,
    )

    waves_df = spot_forecasts.get_dataframe()
    sunlight_df = spot_forecasts.get_dataframe("sunlightTimes")

    # Convert timestamp_dt column to datetime objects
    waves_df['timestamp_dt'] = pd.to_datetime(waves_df['timestamp_dt'])

    # Convert UTC time to local time using utcOffset
    waves_df['local_time'] = waves_df['timestamp_dt'] + pd.to_timedelta(waves_df['utcOffset'], unit='h')

    # Convert sunrise and sunset times to local time using sunriseUTCOffset and sunsetUTCOffset
    sunlight_df['sunrise_dt'] = pd.to_datetime(sunlight_df['sunrise_dt']) + pd.to_timedelta(sunlight_df['sunriseUTCOffset'], unit='h')
    sunlight_df['sunset_dt'] = pd.to_datetime(sunlight_df['sunset_dt']) + pd.to_timedelta(sunlight_df['sunsetUTCOffset'], unit='h')

    # Filter rows where local time is either 12:00 or 18:00
    filtered_df = waves_df[(waves_df['local_time'].dt.strftime('%H:%M') == '12:00') | (waves_df['local_time'].dt.strftime('%H:%M') == '18:00')]

    surf_forecast_string = ""

    # Add surf forecast lines
    for _, row in filtered_df.iterrows():
        surf_forecast_string += f"🌊 {row['local_time'].strftime('%-I%p')}: {row['surf_humanRelation']}\n"
    
    # Create surf forecast string with sunrise and sunset times
    surf_forecast_string += f"☀️ Sunrise: {sunlight_df['sunrise_dt'].dt.strftime('%-I:%M%p').iloc[0]}\n"
    surf_forecast_string += f"🌅 Sunset: {sunlight_df['sunset_dt'].dt.strftime('%-I:%M%p').iloc[0]}\n"

    return surf_forecast_string