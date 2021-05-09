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
def pfEigenVal(substitution):
	eigval = eigenValues(substitution)
	eigenVectors = eigval[1]
	for i in range(len(eigenVectors)):
		vector = eigenVectors[:,i]
		if (np.all(vector < 0)|(np.all(vector > 0))):
			return np.real(vector/(vector[len(substitution)-1]))

	print("PF EigenVector Not Found")
	return None

'''
isPisot(substitution)

Determines if a given substitution is "Pisot", that is all other vectors
other than the Perron-Frobenius, has a norm less than 1.

parameters: 
	substitution: a dictionary, describing the substitution

return: True or False

'''


def isPisot(substitution):
	#find PF eigenvalue
	eigval, eigenVectors = eigenValues(substitution)

	#Case 1: All eigenvalues are integers
	if (pisotCase1(eigval)): return True

	#Case 2: All eigenvalues (excepting the PF eigenvalue) are less than 1
	for i in range(len(eigenVectors)): #find PF eigenValue
		vector = eigenVectors[:,i]
		if (np.all(vector < 0)|(np.all(vector > 0))):
			eigenIndex = i
			break
	if (eigenIndex == len(eigenVectors)):
		print("PF EigenVector Not Found")
		return None
	
	eigval = np.delete(eigval, i, 0) #remove PF eigenvalue
	absval = np.abs(eigval)
	for value in absval:#check remaining eigenvalues
		if (value > 1):
			return False
	return True	


def pisotCase1(eigval):

	if (isinstance(eigval[0], float)): #if the array is of real floats
		for eigenValue in eigval:
			if (not eigenValue.is_integer()): return False
		return True

	if (isinstance(eigval[0], np.complex)): #if the array is complex
		print("cnum")

		for eigenValue in eigval:
			if (eigenValue.imag != 0): return False
		
		for eigenValue in eigval:
			if (not eigenValue.real.is_integer()): return False
		return True


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
# 	   "b":"a"}
# eigenval = eigenValues(sub)
# if (eigenval != None):
# 	print(f"Substitution: {sub}\nMatrix:\n{matrix(sub)}")
# 	print(f"PF EigenVector:\n{pfEigenVal(sub)}")

# print()
# sub = {"a":"ab",
# 	   "b":"c",
# 	   "c":"a"}
# eigenval = eigenValues(sub)
# if (eigenval != None):
# 	print(f"Substitution: {sub}\nMatrix:\n{matrix(sub)}")
# 	print(f"PF EigenVector:\n{pfEigenVal(sub)}")

# print()
# sub = {"a":"abcec",
# 	   "b":"cbbdaa",
# 	   "c":"abdcec",
# 	   "d":"ddacb",
# 	   "e":"abcde"}
# eigenval = eigenValues(sub)
# if (eigenval != None):
# 	print(f"Substitution: {sub}\nMatrix:\n{matrix(sub)}")
# 	curtime = time.time()
# 	print(f"PF EigenVector:\n{pfEigenVal(sub)}\nRight Eigenvectors: \n{eigenval[1]}")

# posttime = time.time()
# totaltime = posttime - curtime
# print(f"time: {totaltime}")

'''-----------------------------------------------------------
isPisot() Testing
-----------------------------------------------------------'''


# print()
# sub = {"a":"ab",
# 	   "b":"c",
# 	   "c":"a"}
# eigenval = eigenValues(sub)
# if (eigenval != None):
# 	print(f"Substitution: {sub}\nMatrix:\n{matrix(sub)}\nEigenValues: {eigenval[0]}\nRight Eigenvectors: \n{eigenval[1]}")
# 	print(f"PF EigenVector:\n{pfEigenVal(sub)}\nSubstitution is Pisot:{isPisot(sub)}")



print()
sub = {"a":"abb",
	   "b":"a"}
eigenval = eigenValues(sub)
if (eigenval != None):
	print(f"Substitution: {sub}\nMatrix:\n{matrix(sub)}\nEigenValues: {eigenval[0]}\nRight Eigenvectors: \n{eigenval[1]}")
	print(f"PF EigenVector:\n{pfEigenVal(sub)}\nSubstitution is Pisot:{isPisot(sub)}")



# print()
# sub = {"a":"abcec",
# 	   "b":"cbbdaa",
# 	   "c":"abdcec",
# 	   "d":"ddacb",
# 	   "e":"abcde"}
# eigenval = eigenValues(sub)
# if (eigenval != None):
# 	print(f"Substitution: {sub}\nMatrix:\n{matrix(sub)}\nEigenValues: {eigenval[0]}\nRight Eigenvectors: \n{eigenval[1]}")
# 	print(f"PF EigenVector:\n{pfEigenVal(sub)}\nSubstitution is Pisot:{isPisot(sub)}")