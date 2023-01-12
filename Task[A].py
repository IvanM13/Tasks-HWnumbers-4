#  Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
from degreePol import degreePol

def GetNumber(message):
    isCorrect = False
    while isCorrect == False:
        try:
            number = int(input(message))
            isCorrect = True
        except ValueError:
            print("Введено не целое число. Повторите! ")
    return number

def GetPolynomial(number):
    poly_dict = {}
    for i in range(number+1):
        poly_dict[i] = str(randint(-100,101))
    return poly_dict

def Degree(key):
    result = ''
    if key == 0 or key  == 1: 
        return ''
    elif key < 10:
        return degreePol[key]
    else:
        degree = key
        for i in range(len(str(key))):
            result = degreePol[degree%10] + result
            degree//=10
        return result

def ResPolynominal(number):
    polynom = ''
    poly = GetPolynomial(number)
    for i in range(number,-1,-1):
        if int(poly[i]) > 0 and i < number and i != 0:
             polynom += '+' + poly[i]+ 'x' + Degree(i)
        elif  int(poly[i]) == 0:
            polynom += ''
        elif int(poly[i]) > 0 and i == 0:
            polynom += '+' + poly[i] + Degree(i)
        elif int(poly[i]) < 0 and i == 0:
             polynom += poly[i] + Degree(i)
        else:
            polynom += poly[i]+'x'+Degree(i)

    polynom+='=0'

    print(polynom)
    return polynom

numb = GetNumber('введите натуральную степень ')
poly = ResPolynominal(numb)
file = open('PolynominalTask[A].txt','w', encoding="utf-8")
try:
    file.write(poly)
    print('PolynominalTask[A].txt записан')
except:
    print('Запись в файл не удалась')
file.close()