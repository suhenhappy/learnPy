import numpy as np
import test
import testPc3

str="ss "
print(str)
str=str.rstrip()
print(str)



lists = ['1','2','3']
for i in lists:
    print(i)

for i in range(1,10,2):
    print(i)

list_range = list(range(1,5))
print(list_range)
print(min(list_range))
print(max(list_range))
print(sum(list_range))


print(list_range[1:3])


print(list_range[:])

list_range_cp = list_range
list_range.append('6')

print(list_range_cp)

print('6' not in list_range)

test_if_v = 5
if test_if_v > 4:
    print("dy")
elif test_if_v< 3:
    print("xy")
else:
    print('==')

alien_0 = {'a':'1','b':'2'}
print(alien_0['a'])
print(alien_0['b'])

for key,value in alien_0.items():
    print("key:"+key+",VALUE:"+value)


for key in alien_0:
    print("key:"+key)

def testFunc():
    print("123456")
testFunc()

def testFunc2(*val):
    print(val)

testFunc2("2","3")



