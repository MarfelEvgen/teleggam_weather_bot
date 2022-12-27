import logging
import requests
from config import *
from aiogram import Bot, Dispatcher, executor, types


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def message(message: types.Message):
    emoji_code = {
        'Thunderstorm': 'Thunderstorm \U000026a1',
        'Rain': 'Rain \U00002614',
        'Snow': 'Snow \U00002744',
        'Mist': 'Mist \U0001f32b',
        'Clear': 'Clear \U00002600',
        'Clouds': 'Clouds \U00002601',
    }
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={openweather_token}&units=metric'
        )
        data = r.json()

        city = data['name']
        current_weather = data['main']['temp']
        wind = data['wind']['speed']
        weather_description = data['weather'][0]['main']
        if weather_description in emoji_code:
            print_emoji = emoji_code[weather_description]
        else:
            pass

        await message.reply(
            f'In the {city} now👇🏻\n\nAir temperature: {current_weather}°C. {print_emoji}\nWind speed:'
            f' {wind}m/s\n\n*** Have a nice '
            f'day '
            f'***')

    except:
        await message.repl('Check the city name')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)