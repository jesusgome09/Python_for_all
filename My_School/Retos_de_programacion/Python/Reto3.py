#Escribe un programa que se encargue de comprobar si un número es o no primo.
#Hecho esto, imprime los números primos entre 1 y 100.
"""
for i in range(1,101):
    for divisor in range(2, i // 2+1):
        if i % divisor == 0:
            break
    else:
        if i > 1:
            print(i)
    
print("-"*50)
"""
#con ayudita para el for "divisor", pero aja, ni se que son los numeros primos jajaja

#el profe lo resolvio
     

#a el profe le aparece otro reto:
#disque la sucecion de fibonacci, lo pondre aqui:

"""
prev = 0 
next = 1

for index in range(51):
    print(prev)

    fib = prev + next
    prev = next
    next = fib
"""




    