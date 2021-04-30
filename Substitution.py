import time
import numpy as np
'''
Substitution(substitution, initialState, Iterations)

parameters:

substitution: a dictionary, describing the substitution
initialState: a String describing the intial state of the algorithm
Iterations: the number of iteraterations to run the algorithm for 

return: The n'th iteration of the subsitution
'''
def Substitution(substitution, initialState, Iterations):
	# print(f"iteration: {Iterations}")
	# print(f"state: {initialState}")
	# base case: end of iterations
	if (Iterations == 0):
		return initialState

	# replace each occurance of a character with its substitution
	newState = ""
	for char in initialState:
		newState = newState + substitution[char]
	
	#recursively call Substitution() with one less iteration
	return Substitution(substitution, newState, Iterations - 1)

def matrix(substitution):
	matString = ""
	for key in substitution:
		for row in substitution:
			count = substitution[row].count(key)
			matString = matString + " " + str(count)
		matString = matString + ";"
	matString = matString[1:-1]
	mat = np.mat(matString)
	return mat

def eigenValues(substitution):
	mat = matrix(substitution)
	try: 
		eigenval = np.linalg.eig(mat)
	except:
		print("Eigenvalue computation does not converge")
		return

	return eigenval




'''-----------------------------------------------------------
Substitution() Testing
-----------------------------------------------------------'''

# sub = {"a":"ab",
# 	   "b":"a"}
# curtime = time.time()
# result = Substitution(sub, "a", 5)
# posttime = time.time()
# totaltime = posttime - curtime
# print(f"out: {result}\nlength:{len(result)}\ntime: {totaltime}")


# substitution = {"a": "ac", "b" : "bd", "c":"a", "d":"db"}
# curtime = time.time()
# result = Substitution(substitution, "a", 5)
# posttime = time.time()
# totaltime = posttime - curtime
# print(f"out: {result}\nlength:{len(result)}\ntime: {totaltime}")


# substitution = {"a":"ab", 
# 				"b":"bc",
# 				"c":"cd",
# 				"d":"da"}
# curtime = time.time()
# result = Substitution(substitution, "a", 5)
# posttime = time.time()
# totaltime = posttime - curtime
# print(f"out: {result}\nlength:{len(result)}\ntime: {totaltime}")


# sub = {"a":"ab",
# 	   "b":"c",
# 	   "c":"a"}
# curtime = time.time()
# result = Substitution(sub, "a", 10)
# posttime = time.time()
# totaltime = posttime - curtime
# print(f"out: {result}\nlength:{len(result)}\ntime: {totaltime}")



'''-----------------------------------------------------------
matrix() Testing
-----------------------------------------------------------'''

# sub = {"a":"ab",
# 	   "b":"c",
# 	   "c":"a"}
# print(f"Matrix:\n{matrix(sub)}")


# sub = {"a":"abb",
# 	   "b":"ca",
# 	   "c":"a"}
# print(f"Matrix:\n{matrix(sub)}")

'''-----------------------------------------------------------
eigenValues() Testing
-----------------------------------------------------------'''

# print()
# sub = {"a":"ab",
# 	   "b":"a"}
# result = Substitution(sub, "a", 5)
# eigenval = eigenValues(sub)
# if (eigenval != None):
# 	print(f"Substitution: {sub}\nMatrix:\n{matrix(sub)}\nEigenValues: {eigenval[0]}\nRight Eigenvectors: \n{eigenval[1]}")

# print()
# sub = {"a":"ab",
# 	   "b":"c",
# 	   "c":"a"}
# result = Substitution(sub, "a", 5)
# eigenval = eigenValues(sub)
# if (eigenval != None):
# 	print(f"Substitution: {sub}\nMatrix:\n{matrix(sub)}\nEigenValues: {eigenval[0]}\nRight Eigenvectors: \n{eigenval[1]}")

# print()
# sub = {"a":"abc",
# 	   "b":"bbac",
# 	   "c":"ccab"}
# result = Substitution(sub, "a", 5)
# eigenval = eigenValues(sub)
# if (eigenval != None):
# 	print(f"Substitution: {sub}\nMatrix:\n{matrix(sub)}\nEigenValues: {eigenval[0]}\nRight Eigenvectors: \n{eigenval[1]}")

print()
sub = {"a":"ab", 
				"b":"bc",
				"c":"cd",
				"d":"da"}
result = Substitution(sub, "a", 5)
eigenval = eigenValues(sub)
if (eigenval != None):
	print(f"Substitution: {sub}\nMatrix:\n{matrix(sub)}\n5th Iteration: {result}\nEigenValues: {eigenval[0]}\nRight Eigenvectors: \n{eigenval[1]}")


