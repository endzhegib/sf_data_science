"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Рамдомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    min_number = 1 #хранение максимального диапазона числа
    max_number = 101 #хранение минимального диапазона числа
    
    while True:
        count += 1
        predict_number = np.random.randint(min_number, max_number) #предполагаемое число
        
        if predict_number == number:
            break #выход из цикла, если угадали
       
        if predict_number > number and predict_number < max_number:
            max_number = predict_number #корректировка максимального диапазона
            
        if predict_number < number and predict_number > min_number:
            min_number = predict_number #корректировка минимального диапазона
            
    return(count)

def score_game(random_predict) ->int:
    """За какое кол-во попыток в среднем из 1000 подходов угадывает алгоритм random_predict

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее кол-во попыток
    """
    
    count_ls=[] #список сохранения кол-ва попыток
    np.random.seed(1) #фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) #загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) #находим среднее кол-во попыток
    
    print(f'Ваш алгоритм угадывает число в среднем за {score} попыток')
    return(score)

if __name__ == '__main__':
    score_game(random_predict)