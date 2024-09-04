import os
import time

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
from telegram import Bot

from bot import Aiobot

load_dotenv()


class Decoder2200:
    def __init__(self, device_ip, password, location):
        self.device_ip = device_ip
        self.username = os.getenv('USER')
        self.password = os.getenv(password)
        self.token = os.getenv('TELEGRAM_TOKEN')
        self.chat_id = os.getenv('CHAT_ID')
        self.location = location
        self.decoder_data = None
        self.video_status = None
        self.audio_status = None
        self.aiobot = Aiobot()

    def get_decoder_data(self):
        url = f'http://{self.device_ip}/cgi-bin/status.cgi'
        try:
            tuner_response = requests.get(
                url,
                auth=HTTPBasicAuth(self.username, self.password)
            )
            soup = BeautifulSoup(tuner_response.text, 'html.parser')
            self.decoder_data = [elem for elem in soup.text.split(';;')]
        except requests.exceptions.RequestException as e:
            print(f"Error getting decoder data {self.device_ip}: {e}")

    def check_video_status(self):
        try:
            if self.decoder_data[6] == '0':
                self.video_status = 'OK'
            elif self.decoder_data[6] == '8':
                self.video_status = 'Bad input TS'
            else:
                self.video_status = 'Unknown error'
        except Exception as e:
            print(f"Error getting decoder data {self.device_ip}: {e}")

    def check_audio_status(self):
        try:
            if self.decoder_data[7] == '0':
                self.audio_status = 'OK'
            elif self.decoder_data[7] == '8':
                self.audio_status = 'Bad input TS'
            else:
                self.audio_status = 'Unknown error'
        except Exception as e:
            print(f"Error getting decoder data {self.device_ip}: {e}")

    async def send_message(self, message):
        bot = Bot(token=self.token)
        await bot.send_message(self.chat_id, message)

    async def retry_check_status(self):
        time.sleep(1)
        print(f'Повторная проверка приемника {self.device_ip}')
        self.get_decoder_data()
        self.check_video_status()
        self.check_audio_status()
        if self.audio_status != 'OK' or self.video_status != 'OK':
            aiobot = Aiobot()
            async with aiobot.session:
                await aiobot.send_message(
                    f'{self.location}:\n'
                    f'Приемник (IP: {self.device_ip}): ошибка декодирования\n'
                    f'Сервис: {self.decoder_data[65]}\n'
                    f'Audio: {self.audio_status}\n'
                    f'Video: {self.video_status}'
                )

    async def check_status(self):
        print(f'Проверка приемника {self.device_ip}')
        self.get_decoder_data()
        self.check_video_status()
        self.check_audio_status()
        if self.audio_status is None or self.video_status is None:
            return
        if self.audio_status != 'OK' or self.video_status != 'OK':
            await self.retry_check_status()
