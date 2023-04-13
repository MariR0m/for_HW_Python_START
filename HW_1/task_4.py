# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

N = int(input('Введите количество долек в ширину: '))
M = int(input('Введите количество долек в длинну: '))
K = int(input('Сколько долек хотим отломить: '))

if K == N or K == M or K % N == 0 or K % M == 0:
    print('Yes')
else: print('No')