def linear(key,array):
	for i in range(0,len(array)-1):
		if array[i]==key:
			print ("Yes")
		else: 
			print ("No")
			break


array=[2,1,3,4,5]
linear(6,array)