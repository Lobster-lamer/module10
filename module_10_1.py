import time
from consoleTextStyle import ConsoleTextStyle as CoTeSt
import threading


def write_words(words_count, file_name):
    with open(file_name, "w") as _file:
        for word_number in range(words_count):
            _file.write(f"Какое-то слово № {word_number}\n")
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


words_files = {10: "example1.txt",
               30: "example2.txt",
               200: "example3.txt",
               100: "example4.txt"}

time_start = time.time()
for words, file in words_files.items():
    write_words(words, file)
time_end = time.time()
elapsed = round(time_end - time_start, 3)
CoTeSt.colorful_text(f"Время записи без использования потоков: "
                     f"{CoTeSt.colorful_str(str(elapsed), CoTeSt.Color.PURPLE)} {CoTeSt.Color.CYAN} сек",
                     CoTeSt.Color.CYAN)

first_thrade = threading.Thread(target=write_words, args=list(words_files.items())[0])
second_thrade = threading.Thread(target=write_words, args=list(words_files.items())[1])
third_thrade = threading.Thread(target=write_words, args=list(words_files.items())[2])
fourth_thrade = threading.Thread(target=write_words, args=list(words_files.items())[3])

first_thrade.start()
second_thrade.start()
third_thrade.start()
fourth_thrade.start()

time_start = time.time()

first_thrade.join()
second_thrade.join()
third_thrade.join()
fourth_thrade.join()

thread_time_end = time.time()
thread_elapsed = round(thread_time_end - time_start, 3)
CoTeSt.colorful_text(f"Время записи c использованим потоков: "
                     f"{CoTeSt.colorful_str(str(thread_elapsed), CoTeSt.Color.PURPLE)} {CoTeSt.Color.CYAN} сек",
                     CoTeSt.Color.CYAN)
