import random
import string
import sys

def is_int(str):
    try:
        int(str)
    except ValueError:
        return print('Пожалуйста, введите количество символов цифрами, а не буквами'), sys.exit(0)

n = input('Введите количество символов вашего пароля: ')
is_int(n)

n1 = int(n)

password = ''
alphabet = string.ascii_letters

choice = input('Вы хотите добавить цифры в свой пароль?(да/нет): ')
if choice == 'да' or choice == 'ДА' or choice == 'Да':
    alphabet += string.digits

choice = input('Вы хотите добавить знаки в свой пароль?(да/нет): ')
if choice == 'да' or choice == 'ДА' or choice == 'Да':
    alphabet += string.punctuation
for i in range(n1+1):
    password += random.choice(alphabet)

print ('Ваш пароль:', password)

if n1 <= 8:
    print('Это слабый пароль')
elif n1 <= 16:
    print('Это хороший пароль')
elif 32 <= n1:
    print('Это великолепный пароль')


