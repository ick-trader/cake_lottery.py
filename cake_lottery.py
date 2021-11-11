import pandas as pd

datos = pd.read_excel('lottery.xlsx')
df = pd.DataFrame(datos)

def cant_dig(n):
    cant = 0
    while n != 0 :
        cant=cant + 1
        n = n // 10
    return cant

cont = 0 
nums = []

for i in df['Datos']:
    i= int(i)
    if cant_dig(i) == 5:
        i = str(i)
        i = '0' + i
    elif cant_dig(i) == 4:
        i = str(i)
        i = '00' + i
    elif cant_dig(i) == 3:
        i = str(i)
        i = '000' + i    

    i = int(i)
    #print(i)
    nums.append(i)
#print(f'\n {nums} \n')

pos_1 = []
pos_2 = []
pos_3 = []
pos_4 = []
pos_5 = []
pos_6 = []

for num in nums:
    pos_6.append(num % 10)
    pos_5.append((num // 10) % 10)
    pos_4.append((num // 100) % 10)
    pos_3.append((num // 1000) % 10)
    pos_2.append((num // 10000) % 10)
    pos_1.append((num // 100000) % 10)

'''


print('Los digitos de la posicion 1 son : \n')
for j in pos_1:
    print(j)

print('Los digitos de la posicion 2 son : \n')
for j in pos_2:
    print(j)

print('Los digitos de la posicion 3 son : \n')
for j in pos_3:
    print(j)

print('Los digitos de la posicion 4 son : \n')
for j in pos_4:
    print(j)

print('Los digitos de la posicion 5 son : \n')
for j in pos_5:
    print(j)

print('Los digitos de la posicion 6 son : \n')
for j in pos_6:
    print(j)    

'''

#print(f'Los digitos de la posicion 1 son: \n {pos_1} \n')

moda_1 = 0
moda_2 = 0
moda_3 = 0
moda_4 = 0
moda_5 = 0
moda_6 = 0

cont_0 = 0
cont_1 = 0
cont_2 = 0
cont_3 = 0
cont_4 = 0
cont_5 = 0
cont_6 = 0
cont_7 = 0
cont_8 = 0
cont_9 = 0


for k in pos_1:
    if k == 0 : 
        cont_0 = cont_0 + 1
    elif k == 1 : 
        cont_1 = cont_1 + 1
    elif k == 2 : 
        cont_2 = cont_2 + 1
    elif k == 3 : 
        cont_3 = cont_3 + 1
    elif k == 4 : 
        cont_4 = cont_4 + 1
    elif k == 5 : 
        cont_5 = cont_5 + 1
    elif k == 6 : 
        cont_6 = cont_6 + 1
    elif k == 7 : 
        cont_7 = cont_7 + 1
    elif k == 8 : 
        cont_8 = cont_8 + 1
    elif k == 9 : 
        cont_9 = cont_9 + 1

'''

moda_1 = 4
moda_2 = 2 
moda_3 = 0
moda_4 = 8
moda_5 = 4 / 8
moda_6 = 2

print(cont_0, cont_1 , cont_2, cont_3, cont_4, cont_5, cont_6, cont_7, cont_8, cont_9)    


'''

magic_num_1 = int( 420842 )
magic_num_2 = int( 420482 )

first_3 = []

for i in nums:
    if ((i // 100000) % 10) == 4 :
        if ((i // 10000) % 10) == 2:
            first_3.append(i)

print(first_3)

#print(cont_2)

# un 20 % de las veces acierto los primeros 2 digitos, ganando x 18 veces los 5 USD invertidos
# calcular la moda del primer digito, y de ahi ver las combinaciones siguientes a ese digito
# hacer un pool para dividir la inversion y minimizar el costo de entrada

'''
readfile = pd.read_csv(r'eth_data.csv')
readfile.to_excel(r'eth_data.xlsx',
index = None, header = True)
'''
