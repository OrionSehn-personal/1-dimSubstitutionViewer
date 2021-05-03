import time
import numpy as np
'''
Substitution(substitution, initialState, Iterations)
	Performs a substitution in the matter described by the subsitution dictionary,
	and performs it a number of times described by the number of iterations, from
	some initial state described by initialState. returns the result of the 
	substitution.

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


'''
matrix(substitution)
	returns a Numpy matrix describing the given substitution. 

parameters: 
	substitution: a dictionary, describing the substitution

return: A Numpy matrix representing the substitution
'''

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

'''
eigenValues(substitution)
	finds both the eigenvalues and eigenvectors of the substitution 
	described by the given dictionary. returns both in a list. 

parameters: 
	substitution: a dictionary, describing the substitution

return: a list containing two entries
	[0] - An array containing the eigenvalues calculated
	[1] - A matrix containing the right eigenvectors of the matrix
'''

def eigenValues(substitution):
	mat = matrix(substitution)
	try: 
		eigenval = np.linalg.eig(mat)
	except:
		print("Eigenvalue computation does not converge")
		return

	return eigenval
'''
pfEigenVal(substitution)

finds the PF eigenvector of a given substitution

parameters: 
	substitution: a dictionary, describing the substitution

return: A matrix describing the PF eigenvecotr of the given matrix


'''
def pfEigenVal(subsitution):
	# eigval = eigenValues(substitution)
	# eigenVectors = eigval[1]
	# outvector = np.linalg.
	# for vector in eigval:
	# 	for 


	# for value in eigenValues:
	# 	if (value > 0):
	# 		return value
	# print("pfEigenValue was not found\n")
	return False


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

print()
sub = {"a":"ab",
	   "b":"a"}
result = Substitution(sub, "a", 5)
eigenval = eigenValues(sub)
if (eigenval != None):
	print(f"Substitution: {sub}\nMatrix:\n{matrix(sub)}\nEigenValues: {eigenval[0]}\nRight Eigenvectors: \n{eigenval[1]}")

print()
sub = {"a":"ab",
	   "b":"c",
	   "c":"a"}
result = Substitution(sub, "a", 5)
eigenval = eigenValues(sub)
if (eigenval != None):
	print(f"Substitution: {sub}\nMatrix:\n{matrix(sub)}\nEigenValues: {eigenval[0]}\nRight Eigenvectors: \n{eigenval[1]}")

# print()
# sub = {"a":"abc",
# 	   "b":"bbac",
# 	   "c":"ccab"}
# result = Substitution(sub, "a", 5)
# eigenval = eigenValues(sub)
# if (eigenval != None):
# 	print(f"Substitution: {sub}\nMatrix:\n{matrix(sub)}\nEigenValues: {eigenval[0]}\nRight Eigenvectors: \n{eigenval[1]}")

# print()
# sub = {"a":"ab", 
# 				"b":"bc",
# 				"c":"cd",
# 				"d":"da"}
# result = Substitution(sub, "a", 5)
# eigenval = eigenValues(sub)
# if (eigenval != None):
# 	print(f"Substitution: {sub}\nMatrix:\n{matrix(sub)}\n5th Iteration: {result}\nEigenValues: {eigenval[0]}\nRight Eigenvectors: \n{eigenval[1]}")


'''-----------------------------------------------------------
pfEigenVal() Testing
-----------------------------------------------------------'''

# print()
# sub = {"a":"ab",
# 	   "b":"c",
# 	   "c":"a"}
# result = Substitution(sub, "a", 5)
# eigenval = eigenValues(sub)
# if (eigenval != None):
# 	print(f"Substitution: {sub}\nMatrix:\n{matrix(sub)}\nEigenValues: {eigenval[0]}\nRight Eigenvectors: \n{eigenval[1]}")
# print(f"PF eigenValue: {pfEigenVal(eigenval[0])}\n")
