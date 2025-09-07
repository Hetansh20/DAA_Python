def knapSack(W, wt, val, n): 
	gain = 0
	
	ratio = [0 for i in range(n)] 
	for i in range(n): 
		ratio[i] = val[i]/wt[i]
		
	# Sort the products of ratio in decending order 
	# for i in range(n): 
	# 	for j in range(i+1, n): 
	# 		if ratio[i] < ratio[j]: 
	# 			ratio[i], ratio[j] = ratio[j], ratio[i] 
	# 			val[i], val[j] = val[j], val[i] 
	# 			wt[i], wt[j] = wt[j], wt[i]
	
	# Initialize a loop from 0 to N 
	# for i in range(n): 
	# 	if wt[i] <= W: 
	# 		gain += val[i] 
	# 		W -= wt[i] 
	# 	else:
	# 		gain += val[i] * ( W / wt[i])
	# 		break
	
	zipped = zip(ratio, val, wt)
	zipped = sorted(list(zipped),reverse = True)
	
	for i in range(n):
		if zipped[i][2] <= W:
			gain += zipped[i][1]
			W -=zipped[i][2]
            
	return gain

price = [10, 5, 3, 2, 8, 7, 11]
weight = [2, 3, 1, 4, 3, 2, 7]
W = 5
n = 7

print(knapSack(W, weight, price, n))