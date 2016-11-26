def babble(array):
	for j in range(0,len(array)-1):
		for i in range(0,len(array)-1):
			if array[i] > array[i+1]:
				tmp = array[i]
				array[i]=array[i+1]
				array[i+1]=tmp
	print array
	
array = [21,4,5,61,2,7,300,44,56]
babble(array)