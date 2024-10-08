import os
#EJ 1
print("Ejercicio 1")
numeros= [8,6,40,4,5,6,7,8,9]
suma=0
for j in numeros:
    print(j)
    suma=suma+j
promedio=suma/len(numeros)
print("El promedio de los números de la lista es:",promedio)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

#EJ 2
print("Ejercicio 2")
nums = [12, 23, 5, 29, 92, 64]
#a
print("Punto 1")
ultimo = nums.pop()
nums.insert(0, ultimo)
print(nums)
#b
print("Punto 2")
segundo= nums.pop(1)
nums.append(segundo)
print(nums)
#c
print("Punto 3")
nums.insert(0,14)
print(nums)
#d
print("Punto 4")
sumas=0
for k in nums:
    sumas=sumas+k
print(nums)
print("La suma de todos los números es:",sumas)
#e
print("Punto 5")
for l in nums[:]:
    if l %2!=0:
        nums.remove(l)
print("La nueva lista sin impares es:",nums)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

#EJ 3
print("Ejercicio 3")
edades= [18,20,22,14,12,9,15,17,30,21]
edadesMayores=[]
contMayor=0
for edad in edades:
    if edad >=18:
        contMayor+=1
        edadesMayores.append(edad)
porc=(contMayor*100)/len(edades)
print("El porcentaje de mayores de edad fue del:"+str(porc)+"%")
print("La lista de mayores quedó así:",edadesMayores)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

#EJ 4
print("Ejercicio 4")
numrands= [10, 25, 33, 47, 58, 62, 74, 81, 92, 105, 118, 130, 145, 156, 170]
print(numrands[0])
print(numrands[14])
sumatoria=0
for num in numrands:
    sumatoria=sumatoria+num
print("La suma de la lista es:",sumatoria)
numrands.append(sumatoria)
print(numrands)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

#EJ 5
print("Ejercicio 5")
numeros = [5, 12, 23, 34, 41, 56, 67, 72, 89, 90, 101, 115, 126, 138, 144, 157, 168, 175, 182, 200]
sumaPar=0
sumaImpar=0
for q in numeros:
    if q %2==0:
        sumaPar=sumaPar+q
    else:
        sumaImpar=sumaImpar+q
print("La suma de los pares es:",sumaPar,"y la de los impares es:",sumaImpar)
numeros.extend([sumaPar,sumaImpar])
print(numeros)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

#EJ 6
print("Ejercicio 6")
numeross = [10, -5, 23, -1, 42, -17, -90, 15, -8, 37, -3, 58, 12, -22, 33, -40, 29, 7, -9, 18]
listaPos=[]
contPos=0
listaNeg=[]
contNeg=0
for num in numeross:
    if num>0:
        contPos+=1
        listaPos.append(num)
    else:
        contNeg+=1
        listaNeg.append(num)
print("La lista de los positivos:",listaPos)
print(contPos,"números positivos en total")
print("La lista de los negativos:",listaNeg)
print(contNeg,"números negativos en total")
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

#EJ 7
print("Ejercicio 7")
notas = [9, 8, 7, 10, 6, 5, 8, 4, 9, 3, 10, 6, 7, 5, 8, 9, 2, 10, 1, 4]
#a
sumaNotas=0
for nota in notas:
    sumaNotas=sumaNotas+nota
prom=sumaNotas/len(notas)
print("El promedio de notas es:",prom)
#b
cont7OMas=0
for nota in notas:
    if nota >=7:
        cont7OMas+=1
print("La cantidad de alumnos que se sacaron 7 o más fue de:",cont7OMas)
#c
notas.append(prom)
print("Lista de notas final:",notas)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

#EJ 8
print("Ejercicio 8")
numeros = [1, 5, 10, 15, 2, 7, 13, 18, 3, 12, 4, 9, 16, 1, 19]
numMin=999
contNumMin=0
for h in numeros:
    if h <numMin:
        numMin=h
for y in numeros:
    if y==numMin:
        contNumMin+=1
print("El valor mínimo es",numMin,"y apareció en la lista",contNumMin,"veces")
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')