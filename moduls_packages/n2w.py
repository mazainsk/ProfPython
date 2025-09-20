from num2words import num2words

def n2w(number):
    if is_number(number):
        return num2words(number, lang='ru')
    else:
        return ''

def is_number(s):
    try:
        float(s)  # Попытка преобразовать строку в число с плавающей точкой
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    while len(n := input('Введите число >> ')) > 0:
        print(n2w(n))