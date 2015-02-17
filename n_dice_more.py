from random import randint

n = input ("Enter Sides:")
result1 = randint(0, int(n))
result2 = randint(0, int(n))
result3 = randint(0, int(n))
print ("First Roll:")
input (result1)
print ("Second Roll:")
input (str(result2))
print ("Third Roll:")
input (str(result3))
input ("Total Sum:" + str(result1 + result2 + result3))
