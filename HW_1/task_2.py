# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# *Попыталась сделать решение более или менее корректным и для нечетных чисел. 
#  Недостаточно данных в ТЗ, подумав логически можно прийти к выводу, что данная задача только для четных чисел, но это точно не прописано)

Number = int(input('Введите сколько журавликов сделали ребята: '))

print('Петя сделал ', a := round(Number / 6) , ', Катя сделала ' , Number - (a + a) , ', Сережа сделал ', a , '.')
