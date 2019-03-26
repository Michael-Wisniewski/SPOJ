# Zadanie
# https://pl.spoj.com/problems/FR_09_16/
# Opis rozwiązania
# http://aroundpython.com/index.php/2019/03/09/gdzie-jest-czekolada/
textline = input()

cups = textline.split()

for i in range(5):
    cups[i] = int(cups[i])

i = 0
while i < 4:
    SM1 = cups[(i+1) % 5] + cups[(i+2) % 5]
    SB1 = cups[(i+3) % 5] + cups[(i+4) % 5]
    SM2 = cups[(i+1) % 5] + cups[(i+3) % 5]
    SB2 = cups[(i+2) % 5] + cups[(i+4) % 5]
    SM3 = cups[(i+1) % 5] + cups[(i+4) % 5]
    SB3 = cups[(i+2) % 5] + cups[(i+3) % 5]

    if SM1 == 2 * SB1 or SM1 == SB1 / 2 or\
       SM2 == 2 * SB2 or SM2 == SB2 / 2 or\
       SM3 == 2 * SB3 or SM3 == SB3 / 2:
        print(i+1)
        break
    
    i += 1

if i == 4:
    print(5)