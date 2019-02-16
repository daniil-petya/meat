import random

lsr = []

count = 0

for i in range(10):
   num = random.randint(-100, 100)
   lsr.append(num)
   if num%2 != 0:
     count+=1
     lsr.remove(num)


print(lsr)

input()