import random
M = []
k1 = 0
k2 = 0
k3 = 0
k4 = 0
k5 = 0

for i in range(0,15):
    M.append(random.randint(1,5))
    print(M[i])
    if M[i] == 1:
        k1 +=1
    elif M[i] == 2:
        k2 +=1
    elif M[i] == 3:
        k3 +=1
    elif M[i] == 4:
        k4 +=1
    elif M[i] == 5:
        k5 +=1

    N = [k1,k2,k3,k4,k5]
    N.sort()

if N[4] == k1:
   print('Больше всего 1')
elif M[4] == k2:
    print('Больше всего 2')
elif N[4] == k3:
    print('Больше всего 3')
elif N[4] == k4:
    print('Больше всего 4')
elif M[4] == k5:
    print('Больше всего 5')
