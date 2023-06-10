import random
import string
import secrets

print('')

n1 = int(input('Добро пожаловать на генератор надёжных (и незапоминающихся) паролей! Введи количество символов у первого будущего пароля: '))
n2 = int(input('А у второго пароля? '))
n3 = int(input('И наконец, у последнего пароля: '))

print('')
print('Генерирую первого пароля...')
print('')

if n1 >= 6:
    res1 = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(n1))
    print('Сгенерирован первый пароль! Вот:')
    print(str(res1))
else:
    print(f'Стоп... {n1} символов?! Это слишком мало для надёжного пароля!')

print('')
print('А я сейчас сгенерирую второго пароля...')
print('')

if n2 >= 6:
    res2 = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(n2))
    print('Сгенерирован второй пароль! Вот:')
    print(str(res2))
else:
    print(f'Стоп... {n2} символов?! Это слишком мало для надёжного пароля!')

print('')
print('И наконец, последний пароль...')
print('')

if n3 >= 6:
    res3 = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(n3))
    print('Сгенерирован последний пароль! Вот:')
    print(str(res3))
else:
    print(f'Стоп... {n3} символов?! Это слишком мало для надёжного пароля!')

print('')
print('Вот и 3 сгенерированные пароли!')
print('')