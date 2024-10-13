from consoleTextStyle import ConsoleTextStyle as CoTeSt
import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.ENEMIES = 100

    def run(self):
        CoTeSt.colorful_text(f"{self.name}, на вас напали!", CoTeSt.Color.RED)
        days = 0
        while self.ENEMIES > 0:
            time.sleep(1)
            days += 1
            self.ENEMIES -= self.power
            if self.ENEMIES < 0:
                self.ENEMIES = 0
            print(f"{self.name} сражается {days}..., осталось {self.ENEMIES} воинов.")
        CoTeSt.colorful_text(f"{self.name} одержал победу!", CoTeSt.Color.GREEN)


if __name__ == "__main__":
    # Создание класса
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)

    # Запуск потоков и остановка текущего
    first_knight.start()
    second_knight.start()

    first_knight.join()
    second_knight.join()