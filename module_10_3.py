import threading
from consoleTextStyle import ConsoleTextStyle as CoTeSt
import random
import time


class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        for transaction in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)
            _deposit = random.randint(50, 500)
            self.balance += _deposit
            CoTeSt.colorful_text(f"Пополнение: {_deposit}. Баланс: {self.balance}", CoTeSt.Color.GREEN)


    def take(self):
        for transaction in range(100):
            time.sleep(0.001)
            _withdraw = random.randint(50, 500)
            print(f"{CoTeSt.ITALIC}Запрос на снятие средств {_withdraw}{CoTeSt.REGULAR}")
            if self.balance >= _withdraw:
                self.balance -= _withdraw
                print(f"Снятие: {_withdraw}. Баланс: {self.balance}")
            else:
                CoTeSt.colorful_text("Запрос отклонён, недостаточно средств", CoTeSt.Color.RED)
                self.lock.acquire()


if __name__ == "__main__":
    bk = Bank(100)

    # Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
    th1 = threading.Thread(target=Bank.deposit, args=(bk,))
    th2 = threading.Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    CoTeSt.colorful_text(f'Итоговый баланс: {bk.balance}', CoTeSt.Color.CYAN)