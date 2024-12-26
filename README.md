# Аналитика заказов

## Описание

Класс `Analytics` предоставляет методы для анализа данных о заказах, включая определение наиболее популярных месяцев на основе дат совершения покупок.

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/nkurilov/mmk-test-kurilov.git

2.	Перейдите в директорию проекта

3.	Создайте и активируйте виртуальное окружение:
   python -m venv venv
source venv/bin/activate  # Для Windows используйте venv\Scripts\activate

pip install -r requirements.txt

## Использование

1.	Импортируйте класс Analytics
   from analytics import Analytics

2.	Создайте список объектов datetime с датами и временем совершённых покупок:

from datetime import datetime

purchase_dates = [
    datetime(2019, 12, 12, 14, 43),
    datetime(2019, 12, 1, 15, 5),
    datetime(2019, 11, 4, 9, 1)
]

3.	Создайте экземпляр класса Analytics и вызовите метод analyze:

analytics = Analytics()
result = analytics.analyze(purchase_dates)

4.	Выведите результат:

for date in result:
    print(date.strftime('%Y-%m-%d %H:%M'))
