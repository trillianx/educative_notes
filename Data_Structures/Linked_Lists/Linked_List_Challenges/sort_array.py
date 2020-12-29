def sort(testVariable, length):
	# Base case
	if length <= 1 :
		return
	
	# Recursive case
	# Sort first n-1 elements
	sort(testVariable, length - 1)

	# Insert last element at its correct position in sorted array
    # fetch the last element
	lastElement = testVariable[length - 1]
    # start finding its correct location from one element before it
	temp = length - 2 
	
	# Move elements of testVariable[0..i-1],
    # that are greater than key, to one position ahead of their current position 
	while (temp >= 0 and testVariable[temp] > lastElement):
		testVariable[temp + 1] = testVariable[temp]
		temp = temp - 1

    # place the element in its correct position
	testVariable[temp + 1] = lastElement 