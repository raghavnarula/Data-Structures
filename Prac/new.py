def merging_2_sorted(a,b):
    # global c
	i = 0
	j = 0
	while i<len(a) and j <len(b):
		if a[i] >= b[j]:
			c.append(b[j])
			j += 1
		if a[i] < b[j]:
			c.append(a[i])
			i += 1


	print(i,j)

	if i!=len(a):
		for x in range(i,len(a)):
			c.append(a[x])

	if j!=len(b):
		for x in range(j,len(b)):
			c.append(b[x]