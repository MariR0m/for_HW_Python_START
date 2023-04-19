# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# side_a = int(input('Введите сколько монеток на столе лежат вверх решкой: '))
# side_b = int(input('Введите сколько монеток на столе лежат вверх гербом: '))

# if (side_a < 0 or side_b < 0) :
#     print ('Монеток не может быть меньше 0.')
# elif side_a <= side_b:
#     print ('Необходимо перевернуть', side_a, 'монеток.')
# elif side_b < side_a:
#     print ('Необходимо перевернуть', side_b, 'монеток.')

import random

n = int(input('Введите количество монеток: '))
count_a = count_b = 0

for _ in range(n):
    val = random.randint(0,1)
    print (val, end = "")
    if val == 0:
        count_a += 1
    else:
        count_b += 1
    
print ('')

if count_a <= count_b:
    print ('Необходимо перевернуть', count_a, 'монеток.')
elif count_a > count_b:
    print ('Необходимо перевернуть', count_b, 'монеток.')

