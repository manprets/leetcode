mylist = [4,6,9,1,2,7,5,3]
print(mylist)

mylist.sort()

length = len(mylist)

arrPairSum = 0
for j in range(0,length,2):
	arrPairSum += mylist[j]

print('arrPairSum: ', arrPairSum)

