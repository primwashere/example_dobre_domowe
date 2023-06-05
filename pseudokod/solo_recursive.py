# funkcja suma_listy(lista)
#   czy lista jest pusta?
#       suma -> zwróć 0
#   w innym przypadku
#       suma -> lista[0]+lista[1]

def suma_listy(lista):
    sum=0
    if len(lista)==0:
        return sum
    else:
        for i in lista:
            sum+=i
        return sum

lista = [1, 2, 3]
print(suma_listy(lista))

#funkcja najwiekszy_elem_listy(lista)
#   czy lista zawiera jeden element?
#       maks -> tablica[0]
#   w innym przypadku
#       jeśli pierwszy element jest większy niż pozostałe
#           maks -> tablica[0]
#       w innym przypadku
#           maks -> najwiekszy_elem_listy(lista[1:])

def najwiekszy_elem_listy(lista):
    if len(lista)==1:
        return lista[0]
    else:
        if lista[0]>najwiekszy_elem_listy(lista[1:]):
            return lista[0]
        else:
            return najwiekszy_elem_listy(lista[1:])
lista=[1,8,3,4,10]
max_elem=najwiekszy_elem_listy(lista)
print(max_elem)

#funkcja policz_silnie(n)
#   czy n == 0 lub n == 1
#       zwróć 1
#   w innym przypadku
#       czy n<0
#           print "Nie da się policzyć silni z liczby ujemnej"
#       w innym przypadku
#           zwróć n*policz_silnie(n-1)

def policz_silnie(n):
    if n==0 or n==1:
        return 1
    else:
        if n<0:
            print("Nie da się policzyć silni z liczby ujemnej")
        else:
            return policz_silnie(n-1)*n
print(policz_silnie(4))

#funkcja fibonacci(n)
#   czy n<=1
#       zwróć n
#   w innym przypadku
#       zwróć fibonacci(n-2)+fibonacci(n-1)
# dla i do n
#   print(fibonacci(1))    

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-2)+fibonacci(n-1)
n=10
for i in range(n):
    print(fibonacci(i))


