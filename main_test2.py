# Task 2

import requests
from datetime import datetime

API_KEY = 'e3d8e449ae5c74fcc8eae68e3b39f7e1'  # Ganti API
CITY = 'Jakarta'
URL = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

def ambil_prakiraan_cuaca():
    response = requests.get(URL)
    data = response.json()

    if response.status_code != 200:
        print("Error saat mengambil data dari API OpenWeatherMap")
        return

    data_prakiraan = data['list']
    prakiraan_harian = {}

    for entry in data_prakiraan:
        tanggal_str = entry['dt_txt'].split(' ')[0]
        suhu = entry['main']['temp']

        if tanggal_str not in prakiraan_harian:
            prakiraan_harian[tanggal_str] = suhu

    print("Prakiraan Cuaca untuk Jakarta:")
    for tanggal, suhu in prakiraan_harian.items():
        tanggal_terformat = datetime.strptime(tanggal, '%Y-%m-%d').strftime('%a, %d %b %Y')
        print(f"{tanggal_terformat}: {suhu:.2f}°C")

ambil_prakiraan_cuaca()
