#  Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

from degreePol import degreePol

def Coefficiens(polynom):
    k = {}
    polynom=polynom.strip().replace('+',' +').replace('-', ' -').replace('=', ' =').split(' ')
    for i in range(len(polynom)):
        if '**' in polynom[i]:
            k[int(polynom[i].split('*')[-1])] = polynom[i].split('*')[0].replace('+', '')
        elif polynom[i].endswith('*x'):
            k[1] = polynom[i].split('*')[0].replace('+', '')
        elif polynom[i].replace('-', '').replace('+', '').isdigit():
            k[0]=polynom[i].replace('+', '')
    return k

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

def ResultPoly(polyOne, polySeck):
    polynom = ''
    resultCoef = {}
    polyOne= Coefficiens(polyOne)
    polySeck= Coefficiens(polySeck)
    number = max(max(polyOne.keys()),max(polySeck.keys()))
    for i in range(number, -1, -1):
        resultCoef[i] = int(polyOne.get(i))+ int(polySeck.get(i))
    for i in range(len(resultCoef)-1, -1, -1):
        if i == len(resultCoef)-1 and resultCoef[i] != 0:
            polynom+=str(resultCoef[i])+'*x'+Degree(i)
        elif resultCoef[i] > 0 and i > 1:
            polynom+='+'+str(resultCoef[i])+'*x'+Degree(i)
        elif resultCoef[i] < 0 and i > 1:
            polynom+=str(resultCoef[i])+'*x'+Degree(i)
        elif resultCoef[i] > 0 and i == 1:
            polynom+='+'+str(resultCoef[i])+'*x'
        elif resultCoef[i] < 0 and i == 1:
            polynom+=str(resultCoef[i])+'*x'
        elif resultCoef[i] > 0 and i == 0:
            polynom+='+'+str(resultCoef[i])
        elif resultCoef[i] < 0 and i == 0:
            polynom+=str(resultCoef[i])
    polynom+='=0'
    polynom=polynom.replace('-1*x', '-x').replace('+1*x', '+x')
    return polynom

fileFirst = open('PolynomTask[B1].txt','r', encoding="utf-8")
firstpoly = fileFirst.readline()
print(firstpoly)
fileTwo = open('PolynomTask[B2].txt','r', encoding="utf-8")
secondpoly = fileTwo.readline()
print(secondpoly)
result_poly = ResultPoly(firstpoly, secondpoly)
print(result_poly)
polynom = open('ResultPoly[B].txt','w', encoding="utf-8")
polynom.write(result_poly)
polynom.close()