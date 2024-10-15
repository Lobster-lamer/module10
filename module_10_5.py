import multiprocessing
import datetime
from consoleTextStyle import ConsoleTextStyle as CoTeSt


def read_info(_file_path):
    all_data = []
    with open(_file_path) as file:
        while 1:
            line = file.readline()
            if line is None or line == "":
                break
            all_data.append(line)
        print(f"Файл {_file_path} считан")


if __name__ == "__main__":
    filenames = [f'./files_for_5/file {number}.txt' for number in range(1, 5)]
    CoTeSt.colorful_text("Линейный вызов:", CoTeSt.Color.CYAN)
    start_time = datetime.datetime.now()
    for file_path in filenames:
        read_info(file_path)
    end_time = datetime.datetime.now()
    CoTeSt.colorful_text(f"Время работы при линейном вызове: {end_time - start_time}\n\n",
                         CoTeSt.Color.GREEN)

    # 0:00:03.174566

    CoTeSt.colorful_text("Многопроцессорный:", CoTeSt.Color.CYAN)
    start_time = datetime.datetime.now()
    with multiprocessing.Pool(processes=8) as pool:
        pool.map(read_info, filenames)
    end_time = datetime.datetime.now()
    CoTeSt.colorful_text(f"Время работы при многопроцессорном вызове: {end_time - start_time}",
                         CoTeSt.Color.GREEN)

    # 0:00:01.285807
