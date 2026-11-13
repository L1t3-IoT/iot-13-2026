"""Лабораторна робота №5, варіант 21: погода."""
# pylint: disable=too-many-arguments

from enum import Enum


class WeatherType(Enum):
    """Тип погоди."""

    SUNNY = 1
    CLOUDY = 2
    RAINY = 3
    FOGGY = 4
    SNOWY = 5
    WINDY = 6


class Weather:
    """Запис про погоду."""

    def __init__(self, day, city, country, temp, *,
                 humidity, wind_speed, weather_type):
        """Конструктор."""
        self.__day = day
        self.__city = city
        self.__country = country
        self.__temp = temp
        self.__humidity = humidity
        self.__wind_speed = wind_speed
        self.__weather_type = weather_type

    def __del__(self):
        """Деструктор."""
        print(f"Видалено запис: день {self.__day}, {self.__city}")

    def __str__(self):
        """Опис запису для людини."""
        return (f"День {self.__day}: {self.__city}, {self.__country}, "
                f"{self.__temp} °C, вологість {self.__humidity}%, "
                f"вітер {self.__wind_speed} м/с, "
                f"{self.__weather_type.name}")

    def get_day(self):
        """День."""
        return self.__day

    def get_city(self):
        """Місто."""
        return self.__city

    def get_country(self):
        """Країна."""
        return self.__country

    def get_temp(self):
        """Температура."""
        return self.__temp

    def get_humidity(self):
        """Вологість."""
        return self.__humidity

    def get_wind_speed(self):
        """Швидкість вітру."""
        return self.__wind_speed

    def get_weather_type(self):
        """Тип погоди."""
        return self.__weather_type

    @staticmethod
    def is_lviv_weather(humidity, weather_type):
        """Перевіряє, чи погода типова для Львова."""
        if humidity > 80 and weather_type == WeatherType.RAINY:
            print("The typical day in Lviv")
        else:
            print("You're lucky, man")


class WeatherCalendar:
    """Календар погоди: набір записів Weather."""

    def __init__(self):
        """Конструктор."""
        self.__records = []

    def __del__(self):
        """Деструктор."""
        print("Календар погоди видалено")

    def add_weather(self, weather):
        """Додає запис про погоду."""
        self.__records.append(weather)

    def find_max_temperature(self, day):
        """Максимальна температура за день або None."""
        temps = [record.get_temp() for record in self.__records
                 if record.get_day() == day]
        if not temps:
            print("Not enough data")
            return None
        return max(temps)

    def sort_by_day(self):
        """Сортує записи за днем."""
        self.__records.sort(key=lambda record: record.get_day())

    def print_records(self):
        """Виводить усі записи."""
        for record in self.__records:
            print(record)


def main():
    """Демонструє роботу класів Weather і WeatherCalendar."""
    calendar = WeatherCalendar()
    lviv = Weather(3, "Львів", "Україна", 4.5,
                   humidity=85, wind_speed=5.0,
                   weather_type=WeatherType.RAINY)
    calendar.add_weather(lviv)
    calendar.add_weather(Weather(1, "Київ", "Україна", 9.0,
                                 humidity=60, wind_speed=3.5,
                                 weather_type=WeatherType.SUNNY))
    calendar.add_weather(Weather(2, "Одеса", "Україна", 12.5,
                                 humidity=70, wind_speed=6.0,
                                 weather_type=WeatherType.CLOUDY))
    calendar.add_weather(Weather(1, "Львів", "Україна", 6.0,
                                 humidity=82, wind_speed=4.0,
                                 weather_type=WeatherType.RAINY))
    calendar.add_weather(Weather(3, "Варшава", "Польща", 8.0,
                                 humidity=75, wind_speed=2.5,
                                 weather_type=WeatherType.FOGGY))
    calendar.add_weather(Weather(2, "Краків", "Польща", 5.5,
                                 humidity=50, wind_speed=7.5,
                                 weather_type=WeatherType.SUNNY))

    print("Записи до сортування:")
    calendar.print_records()
    calendar.sort_by_day()
    print("\nЗаписи після сортування за днем:")
    calendar.print_records()

    print()
    for day in (1, 3, 10):
        max_temp = calendar.find_max_temperature(day)
        if max_temp is not None:
            print(f"Максимальна температура за день {day}: {max_temp} °C")

    print()
    Weather.is_lviv_weather(85, WeatherType.RAINY)
    Weather.is_lviv_weather(60, WeatherType.SUNNY)
    lviv.is_lviv_weather(lviv.get_humidity(), lviv.get_weather_type())
    print()


if __name__ == "__main__":
    main()
