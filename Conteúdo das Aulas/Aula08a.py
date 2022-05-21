import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é igual a {}'.format(num, math.floor(raiz)))

import random
num = random.randint(1, 10)
print(num)

import emoji
print(emoji.emojize('Ola mundo :expressionless_face:', use_aliases=True))