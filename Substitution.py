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
	return mat.transpose()

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
	if (pisotCase1(eigval)): return True #helper funciton to handle Case 1

	#Case 2: All eigenvalues (excepting the PF eigenvalue) are less than 1
	#find PF eigenValue
	for i in range(len(eigenVectors)): 
		vector = eigenVectors[:,i]
		if (np.all(vector < 0)|(np.all(vector > 0))):
			eigenIndex = i
			break
	if (eigenIndex == len(eigenVectors)):
		print("PF EigenVector Not Found")
		return None
	#exclude PF eigenvalue
	eigval = np.delete(eigval, i, 0) 
	absval = np.abs(eigval)
	for value in absval:#check remaining eigenvalues against 1
		if (value > 0.99999999999999): #check slightly lower than 1, because of float rounding
 			return False

	return True	
'''-----------------------------------------------------------
Helper function to handle Case 1 for the Pisot Condition:
That all eigenvalues are integers. 
-----------------------------------------------------------'''

def pisotCase1(eigval):

	if (isinstance(eigval[0], float)): #if the array is of real floats
		for eigenValue in eigval:
			if (not eigenValue.is_integer()): return False
		return True

	if (isinstance(eigval[0], np.complex)): #if the array is complex
		#Rounds both imaginary portions, and real portions to see if
		#All portions are integers (within 15 decimal points)
		for eigenValue in eigval:
			if (round(eigenValue.imag, 15) != 0): return False
			if (not round(eigenValue.real,15).is_integer()): return False
		return True
