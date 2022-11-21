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
    number = np.random.randint(1, 101)

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

print(random_predict(53))