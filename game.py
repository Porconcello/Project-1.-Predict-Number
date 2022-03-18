"""Игра угадай число.
Компьютер сам загадывает и угадывает число.
"""


import numpy as np


def random_predict(number:int=1)->int:
    """Рандомно угадываем число, двигаясь в нужном направлении

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min_value = 1
    max_value = 101
    while True:
        count += 1
        predict_number = np.random.randint(min_value,max_value) #предполагаемое число
        if number == predict_number:
            break #выход из цикла, угадали
        elif number>predict_number:
            min_value = predict_number
        elif number<predict_number:
            max_value=predict_number 
    return count


def score_game(random_predict)->int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Алгоритм угадывает число в среднем за {score} попыток')
    

#RUN
if __name__=='__main__':
    score_game(random_predict)