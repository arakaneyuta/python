def binary(key,array):
	half = len(array)/2
	if key < half:
		for i in range(0,half):
			if array[i]==key:
				print ("Yes")
				break
			else: 
				print ("No")
				break

	elif key > half:
		for i in range(half+1,len(array)):
			if key == array[i]:
				print ("Yes")
			else: 
				print ("No")
				break

array = [1,2,3,4,5,6,7,8]
binary(1,array)