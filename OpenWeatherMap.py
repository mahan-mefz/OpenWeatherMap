import requests

def get_weather(city, api_key):
    """
    دریافت اطلاعات آب‌وهوا برای یک شهر خاص از طریق API.
    
    پارامترها:
    city (str): نام شهر
    api_key (str): کلید API از OpenWeatherMap
    
    خروجی:
    dict: اطلاعات آب‌وهوایی شهر
    """
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    
    # بررسی پاسخ از API
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception("اطلاعاتی برای این شهر پیدا نشد. لطفا نام شهر را بررسی کنید.")

def display_weather_info(city, weather_data):
    """
    نمایش اطلاعات آب‌وهوایی به صورت خوانا.
    
    پارامترها:
    city (str): نام شهر
    weather_data (dict): داده‌های آب‌وهوایی که از API دریافت شده است
    """
    print(f"آب‌وهوای فعلی در شهر {city}:")
    print(f"دما: {weather_data['main']['temp']} درجه سانتی‌گراد")
    print(f"رطوبت: {weather_data['main']['humidity']}%")
    print(f"وضعیت: {weather_data['weather'][0]['description']}")
    
def main():
    """
    برنامه اصلی که نام شهر را از کاربر دریافت کرده و اطلاعات آب‌وهوایی را نمایش می‌دهد.
    """
    api_key = "API_KEY_شخصی_خود"  # کلید API خود را اینجا وارد کنید
    city = input("نام شهر را وارد کنید: ")
    
    try:
        weather_data = get_weather(city, api_key)
        display_weather_info(city, weather_data)
    except Exception as e:
        print(e)

# اجرای برنامه
if __name__ == "__main__":
    main()