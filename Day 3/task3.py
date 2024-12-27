print('Bienvenido a Python Pizza Deliveries!')  
size = input('Que tamano de pizza quieres? S, M, L? ')
pepperoni = input('Quieres pepperoni? Y o N? ')
extra_cheese = input('Quieres extra queso? Y o N? ')
bill = 0

if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25
else:
    print('Tamano no valido') 
    
if pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3
   
if extra_cheese == 'Y':
    bill += 1
    
print(f'Tu cuenta es de ${bill}.')
    