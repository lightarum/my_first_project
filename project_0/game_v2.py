"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""
import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число
    Args:
        number(int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    count = 0
    min1 = 1
    max1 = 101

    while True:
        count += 1
        mid1 = int((min1+max1) / 2)
        
        if number == mid1:
            break  # выход из цикла если угадали
        elif number > mid1:
            min1 = mid1
        else:
            max1 = mid1
        
    return(count)

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
print(__name__)
if __name__ == '__main__':
    score_game(random_predict)