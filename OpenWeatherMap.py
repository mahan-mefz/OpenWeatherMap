import requests
import time
import json

class WeatherApp:
    def __init__(self, api_key):
        """
        کلاس اصلی برای برنامه آب‌وهوا.
        
        پارامترها:
        api_key (str): کلید API از OpenWeatherMap
        """
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    def get_weather(self, city):
        """
        دریافت اطلاعات آب‌وهوایی یک شهر خاص.
        
        پارامترها:
        city (str): نام شهر
        
        خروجی:
        dict: داده‌های آب‌وهوایی یا None در صورت بروز خطا
        """
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric',
            'lang': 'fa'  # دریافت داده‌ها به زبان فارسی
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.RequestException as e:
            print(f"خطایی رخ داده است: {e}")
            return None

    def display_weather_info(self, city, weather_data):
        """
        نمایش اطلاعات آب‌وهوایی به صورت خوانا.
        
        پارامترها:
        city (str): نام شهر
        weather_data (dict): داده‌های آب‌وهوایی که از API دریافت شده است
        """
        if weather_data:
            print(f"آب‌وهوای فعلی در {city}:")
            print(f"دما: {weather_data['main']['temp']} درجه سانتی‌گراد")
            print(f"رطوبت: {weather_data['main']['humidity']}%")
            print(f"حداقل دما: {weather_data['main']['temp_min']}°C")
            print(f"حداکثر دما: {weather_data['main']['temp_max']}°C")
            print(f"وضعیت: {weather_data['weather'][0]['description']}")
            print("-" * 40)
        else:
            print(f"اطلاعات آب‌وهوا برای {city} در دسترس نیست.")

    def save_weather_to_file(self, city, weather_data, filename="weather_data.json"):
        """
        ذخیره اطلاعات آب‌وهوایی در یک فایل JSON.
        
        پارامترها:
        city (str): نام شهر
        weather_data (dict): داده‌های آب‌وهوایی که از API دریافت شده است
        filename (str): نام فایل خروجی
        """
        if weather_data:
            data_to_save = {
                'city': city,
                'temperature': weather_data['main']['temp'],
                'humidity': weather_data['main']['humidity'],
                'description': weather_data['weather'][0]['description'],
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            }
            
            try:
                with open(filename, 'a', encoding='utf-8') as f:
                    f.write(json.dumps(data_to_save, ensure_ascii=False) + "\n")
                print(f"اطلاعات آب‌وهوایی {city} ذخیره شد.")
            except Exception as e:
                print(f"خطا در ذخیره‌سازی: {e}")
    
    def run(self):
        """
        اجرای برنامه اصلی که چندین شهر از کاربر دریافت کرده و اطلاعات آب‌وهوایی را نمایش و ذخیره می‌کند.
        """
        cities = input("نام شهرها را با کاما جدا کنید: ").split(',')
        cities = [city.strip() for city in cities]  # حذف فاصله‌های اضافی
        
        for city in cities:
            weather_data = self.get_weather(city)
            self.display_weather_info(city, weather_data)
            self.save_weather_to_file(city, weather_data)


if __name__ == "__main__":
    api_key = "API_KEY_شخصی_خود"  # کلید API خود را اینجا وارد کنید
    app = WeatherApp(api_key)
    app.run()