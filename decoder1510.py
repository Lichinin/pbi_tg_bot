import asyncio
import os
import time

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
from telegram import Bot

load_dotenv()


class Decoder1510:
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
        self.sefvice_name = None

    def get_decoder_data(self):
        url = f'http://{self.device_ip}/cgi-bin/decoder_status.cgi'
        tuner_response = requests.get(
            url,
            auth=HTTPBasicAuth(self.username, self.password)
        )
        soup = BeautifulSoup(tuner_response.text, 'xml')
        self.video_status = soup.find(
            'Video',
            {'value': '1'}
        ).find('status').get('value').strip()
        self.audio_status = soup.find(
            'Audio',
            {'value': '1'}
        ).find('status').get('value').strip()
        self.service_name = soup.find('service_name').get('value')

    async def send_message(self, message):
        bot = Bot(token=self.token)
        await bot.send_message(self.chat_id, message)

    def retry_check_status(self):
        time.sleep(1)
        self.get_decoder_data()
        if self.audio_status != 'OK' or self.video_status != 'OK':
            asyncio.run(self.send_message(
                f'{self.location}:\n'
                f'Приемник (IP: {self.device_ip}): ошибка декодирования\n'
                f'Сервис: {self.service_name}\n'
                f'Audio: {self.audio_status}\n'
                f'Video: {self.video_status}'
            ))

    def check_status(self):
        self.get_decoder_data()
        if self.audio_status != 'OK' or self.video_status != 'OK':
            self.retry_check_status()
