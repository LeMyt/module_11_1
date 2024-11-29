# Работа с библиотекой Requests:
import requests

# Requests предоставляет удобные способы обработки различных типов ошибок:
try:
    url = 'https://example.com/wrong-url/'
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print("Http Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("Oops: Something Else", err)

# Можно получать данные о погоде с сервиса OpenWeatherMap
api_key = '5f598464f585b3f53a9cfe106978c966'
city_name = 'Москва'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=ru'

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    current_temperature = data['main']['temp']
    weather_description = data['weather'][0]['description']
    print(f"Текущая температура в {city_name}: {current_temperature}°C")
    print(f"Погодные условия: {weather_description}")
else:
    print(f"Ошибка при получении данных о погоде: {response.text}")

# Используя Requests можно загружать файлы с удаленных серверов:
url = 'https://i.postimg.cc/Hs1F46vq/input.png'
response = requests.get(url)

with open('input.png', 'wb') as file:
    file.write(response.content)

url2 = 'https://i.postimg.cc/59z22kFT/5348260338778368710.jpg'
response2 = requests.get(url2)

with open('image2.jpg', 'wb') as file:
    file.write(response2.content)


# Пример работы с библиотекой Pillow
from PIL import Image

# Конвертация изображения из .png в .jpg и поворот изображения

# Открываем исходный файл изображения
input_image = Image.open("input.png")

# Конвертируем изображение в формат JPEG
output_image = input_image.convert('RGB')

# Сохраняем изображение в формате JPEG
output_image.save("image1.jpg", format='JPEG', quality=100)

# Поворачиваем изображение на 90 градусов против часовой стрелки
output_image = output_image.rotate(90)

# Сохраняем изображение в формате JPEG под другим именем
output_image.save("image3.jpg", format='JPEG', quality=100)


# Объединение двух изображений

# Загружаем первое изображение
img1 = Image.open("image1.jpg")

# Загружаем второе изображение
img2 = Image.open("image2.jpg")

# Определяем размеры нового объединенного изображения
width = img1.width + img2.width
height = max(img1.height, img2.height)

# Создаем новое изображение с заданными размерами
new_img = Image.new('RGB', (width, height))

# Вставляем первое изображение в новую картинку
new_img.paste(img1, (0, 0))

# Вставляем второе изображение рядом с первым
new_img.paste(img2, (img1.width, 0))

# Сохраняем полученное изображение
new_img.save("merged_image.jpg")

print('Скаченные и обработанные картинки можно посмотреть в папке с файлом текущего модуля')