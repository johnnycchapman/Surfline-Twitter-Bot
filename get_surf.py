import pysurfline
import pandas as pd

def get_surf_forecast(spotId):
    try:
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

        # Ensure the sunlight DataFrame is not empty before accessing
        if not sunlight_df.empty:
            sunlight_df['sunrise_dt'] = pd.to_datetime(sunlight_df['sunrise_dt']) + pd.to_timedelta(sunlight_df['sunriseUTCOffset'], unit='h')
            sunlight_df['sunset_dt'] = pd.to_datetime(sunlight_df['sunset_dt']) + pd.to_timedelta(sunlight_df['sunsetUTCOffset'], unit='h')

        # Filter for specific forecast times (8 AM & 2 PM EST)
        filtered_df = waves_df[
            (waves_df['local_time'].dt.strftime('%H:%M') == '08:00') | 
            (waves_df['local_time'].dt.strftime('%H:%M') == '14:00')
        ]

        surf_forecast_string = ""

        for _, row in filtered_df.iterrows():
            surf_forecast_string += f"🌊 {row['local_time'].strftime('%-I%p')}: {row['surf_humanRelation']}\n"

        if not sunlight_df.empty:
            surf_forecast_string += f"☀️ Sunrise: {sunlight_df['sunrise_dt'].dt.strftime('%-I:%M%p').iloc[0]}\n"
            surf_forecast_string += f"🌅 Sunset: {sunlight_df['sunset_dt'].dt.strftime('%-I:%M%p').iloc[0]}\n"

        return surf_forecast_string
    except Exception as e:
        print(f"Error fetching forecast: {e}")
        return None
