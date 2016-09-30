# Sample list of inputs
x = [2,4,6,8,10]
# Sample list of desired outputs
y = [5,9,13,17,21]
P0 = 0 
P1 = 1
# Rate of change for P0 and P1
rate = 0.01

def hypothesis (P0,P1,X):
	return P0 + P1*X

#Cost function
def change0 (P0,P1,x,y):
	totalCost = 0
	for i in range(len(y)):
		totalCost += (hypothesis(P0,P1,x[i]) - y[i])*(1/len(y))
	return totalCost
	
def change1 (P0,P1,x,y):
	totalCost = 0
	for i in range(len(y)):
		totalCost += (hypothesis(P0,P1,x[i]) - y[i])*(1/len(y)) * x[i]
	return totalCost
	
def main (P0,P1,x,y,rate):
	# Number of iterations
	for i in range(1,100000):
		# The main algorithm, Google "Gradient Descent" for explanation
		temp0 = P0 
		temp1 = P1 
		P0 = temp0 - rate*change0(temp0,temp1,x,y)
		P1 = temp1 - rate*change1(temp0,temp1,x,y)
	P0 = round(P0,3)
	P1 = round(P1,3)
	
	print("P0: " + str(P0))
	print("P1: " + str(P1))
	print("Please enter X")

	while True:
		example = input()
		if example == "exit":
			print("PROGRAM COMPLETE")
			break
		print(hypothesis(P0,P1,float(example)))

main(P0,P1,x,y,rate)