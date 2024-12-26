from datetime import datetime
from collections import Counter

class Analytics:
    @staticmethod
    def analyze(purchase_dates):
        # Преобразуем список объектов datetime в список строк формата 'YYYY-MM-01 00:00'
        first_of_months = [
            datetime(purchase_date.year, purchase_date.month, 1, 0, 0)
            for purchase_date in purchase_dates
        ]
        
        # Подсчитываем количество повторений каждой даты
        date_counts = Counter(first_of_months)
        
        # Сортируем даты по убыванию частоты заказов, затем по возрастанию даты
        sorted_dates = sorted(
            date_counts.keys(),
            key=lambda date: (-date_counts[date], date)
        )
        
        return sorted_dates

# Пример использования
if __name__ == "__main__":
    # Список дат и времени совершённых покупок
    purchase_dates = [
        datetime(2019, 12, 12, 14, 43),
        datetime(2019, 12, 1, 15, 5),
        datetime(2019, 11, 4, 9, 1)
    ]
    
    # Создаём экземпляр класса Analytics
    analytics = Analytics()
    
    # Получаем отсортированный список дат
    result = analytics.analyze(purchase_dates)
    
    # Выводим результат
    for date in result:
        print(date.strftime('%Y-%m-%d %H:%M'))
