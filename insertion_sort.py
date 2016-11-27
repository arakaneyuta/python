def insertion(array):
	for j in range(0,len(array)):
		for i in range(j,0,-1):
			if array[i] < array[i-1]:
				array[i],array[i-1] = array[i-1],array[i]
	print array

array = [42, 21, 10, 2, 30, 66, 100, 89, 43]
insertion(array)