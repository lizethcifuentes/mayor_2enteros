# programa para verificar cual de los dos numeros enteros es el mayor

print("-----------------------------------------")
print("----------MAYOR 2 ENTEROS----------------")
print("-----------------------------------------")



# input
x = int (input("digite el valor de x: "))
y = int (input("digite el valor de y: "))


#processing 
if x == y:
    # ouput
    print("los numeros son iguales...")
else:
    if x > y:
       mayor = x
    else:
       mayor = y
       #ouput
    print("el mayor entre " + str(x) + " y " + str(y) + "es" + str(mayor))