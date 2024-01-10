
#Operadores aritmeticos
print("\nOperadores aritmeticos:\n")
print("suma\n2 + 2: ",2 + 2)
#resta
print("resta\n2 - 1: ",2 - 1)
#multiplicacion
print("Multiplicacion\n2 x 2: ",2 * 2)
#division
print("division\n2 / 2: ",2 / 2)
#modulo (lo que sobra de la division)
print("modulo\n2 % 2: ",2 % 2)
#potencia
print("potencia\n2 ^ 3: ",2 ** 3)
#floor division (redondea al entero mas cercano)
print("division redondeada\n3 // 2: ",3 // 2)

#operadores de comparacion
print("\nOperadores de comparacion:\n")
#es igual a 
print("igual a\n1 es igual a 1:", 1==1)
#es diferente de
print("diferente de\n1 es diferente a 1:", 1!=1)
#es mayor que
print("mayor que\n2 es mayor que 1:", 2>1)
#es menor que
print("menor que\n2 es menor que 4:", 2<4)
#es mayor o igual que
print("mayor o igual que\n2 es mayor o igual que 2:", 2>=2)
#es menor o igual que
print("menor o igual que\n2 es menor o igual que 4:", 2<=4)

#Operadores logicos
print("\nOperadores logicos\n")
#variables
a=True
b=False 
print("a=True\nb=False\n")
#and
print("and\nsi a y b ", a and b)
#or
print("or\nsi a o b ", a or b)
#not
print("not\nnot a ", not a )

#Operadores de identidad

print("\nOperadores de identidad\n")

a=True
b=a
print("a=True\nb=a\n")
#is
print("is\na is b ", a is b )
#is not
print("is not\nb is not a ", a is not b )

#Operadores de miembros
print("\nOperadores de miembros\n")
a={1,2}
b= {2}
print("a={1,2}\nb= 2")
#in
print("in\nb in a ", b in a )
#not in
print("not in\na not in b ", a not in b )

#Operadores de bits
print("\nOperadores de bits\n")
a = 5
b = 3
print("a=5\nb= 3")
#and
print("and\na and b: ", a & b)
#or
print("or\na or b:" , a | b)
#xor
print("xor\na xor b: ", a ^ b)
#Desplazamiento a la izquierda
print("Desplazamiento a la izq\na >> 1: ", a << 1)
#Desplazamiento a la derecha
print("Desplazamiento a la der\na >> 1: ", a >> 1)

#Estructuras de control condicionales
print("\nEstructuras de Control Condicionales:\n")
if a > b:
    print("a es mayor que b")
elif a == b:
    print("a es igual a b")
else:
    print("a es menor que b")

#Estructuras de control iterativas
print("\nEstructuras de control iterativas:\n")
for i in range(10):
    print(i, end=(" "))

#Estructuras de control de excepciones
print("\n\nEstructuras de control de excepciones:\n")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero")

print("\nejercicio opcional\n")
for i in range(10,56):
    if i!=16 and i%2==0 and i%3!=0:
        print(i, end=(" "))
