import queue
import threading
import time
import random


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe:
    def __init__(self, *args):
        self.queue = queue.Queue()
        self.tables = list(args)
        self.unnocupied_tables = [True for i in range(len(self.tables))]

    def guest_arrival(self, *guests):
        for guest in guests:
            if any(self.unnocupied_tables):
                unnocupied_table_index = self.unnocupied_tables.index(True)
                self.tables[unnocupied_table_index].guest = guest
                print(f"{guest.name} сел(-а) за стол номер {self.tables[unnocupied_table_index].number}")
                self.unnocupied_tables[unnocupied_table_index] = False
                self.tables[unnocupied_table_index].guest.start()
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or not all(self.unnocupied_tables):
            for table_index in range(len(self.tables)):
                if self.tables[table_index].guest is not None and self.tables[table_index].guest._is_stopped:
                    print(f"{self.tables[table_index].guest.name} покушал(-а) и ушёл(ушла)")
                    self.tables[table_index].guest = None
                    self.unnocupied_tables[table_index] = True
                    print(f"Стол номер {self.tables[table_index].number} свободен")
                if not self.queue.empty() and self.tables[table_index].guest is None:
                    self.tables[table_index].guest = self.queue.get()
                    self.unnocupied_tables[table_index] = False
                    print(f"{self.tables[table_index].guest.name} вышел(-ла) из очереди и сел(-а) за стол номер "
                          f"{self.tables[table_index].number}")
                if self.tables[table_index].guest is not None and "initial" in str(self.tables[table_index].guest):
                    self.tables[table_index].guest.start()
            time.sleep(1)
        else:
            for table in self.tables:
                if table.guest is not None and table.guest._is_stopped:
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    table.guest = None
                    print(f"Стол номер {table.number} свободен")


if __name__ == "__main__":
    #Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()
