def selection(array):
	tmp = float("inf")
	for j in range(0,len(array)-1):
		for i in range(j,len(array)):
			if tmp > array[i]:
				tmp = array[i]
				num = i
		array[num] = array[j]
		array[j]=tmp
		tmp=float("inf")
	print array


array = [21,2,6,89,4,8,55,80]
selection(array)