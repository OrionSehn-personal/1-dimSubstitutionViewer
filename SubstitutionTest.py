import time
import numpy as np
from Substitution import *
'''-----------------------------------------------------------
Substitution() Testing
-----------------------------------------------------------'''
def subsitutionTest():
	sub = {"a":"ab",
		"b":"a"}
	curtime = time.time()
	result = Substitution(sub, "a", 5)
	posttime = time.time()
	totaltime = posttime - curtime
	print(f"out: {result}\nlength:{len(result)}\ntime: {totaltime}")


	substitution = {"a": "ac", "b" : "bd", "c":"a", "d":"db"}
	curtime = time.time()
	result = Substitution(substitution, "a", 5)
	posttime = time.time()
	totaltime = posttime - curtime
	print(f"out: {result}\nlength:{len(result)}\ntime: {totaltime}")


	substitution = {"a":"ab", 
					"b":"bc",
					"c":"cd",
					"d":"da"}
	curtime = time.time()
	result = Substitution(substitution, "a", 5)
	posttime = time.time()
	totaltime = posttime - curtime
	print(f"out: {result}\nlength:{len(result)}\ntime: {totaltime}")


	sub = {"a":"ab",
		"b":"c",
		"c":"a"}
	curtime = time.time()
	result = Substitution(sub, "a", 10)
	posttime = time.time()
	totaltime = posttime - curtime
	print(f"out: {result}\nlength:{len(result)}\ntime: {totaltime}")



'''-----------------------------------------------------------
matrix() Testing
-----------------------------------------------------------'''
def matrixTest():
	sub = {"a":"ab",
		"b":"c",
		"c":"a"}
	print(f"Matrix:\n{matrix(sub)}")


	sub = {"a":"abb",
		"b":"ca",
		"c":"a"}
	print(f"Matrix:\n{matrix(sub)}")

'''-----------------------------------------------------------
eigenValues() Testing
-----------------------------------------------------------'''
def eigenValuesTest():
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

	print()
	sub = {"a":"abc",
		"b":"bbac",
		"c":"ccab"}
	result = Substitution(sub, "a", 5)
	eigenval = eigenValues(sub)
	if (eigenval != None):
		print(f"Substitution: {sub}\nMatrix:\n{matrix(sub)}\nEigenValues: {eigenval[0]}\nRight Eigenvectors: \n{eigenval[1]}")

	print()
	sub = {"a":"ab", 
					"b":"bc",
					"c":"cd",
					"d":"da"}
	result = Substitution(sub, "a", 5)
	eigenval = eigenValues(sub)
	if (eigenval != None):
		print(f"Substitution: {sub}\nMatrix:\n{matrix(sub)}\n5th Iteration: {result}\nEigenValues: {eigenval[0]}\nRight Eigenvectors: \n{eigenval[1]}")


'''-----------------------------------------------------------
pfEigenVal() Testing
-----------------------------------------------------------'''
def pfEigenValTest():
	print()
	sub = {"a":"ab",
		"b":"a"}
	eigenval = eigenValues(sub)
	if (eigenval != None):
		print(f"Substitution: {sub}\nMatrix:\n{matrix(sub)}")
		print(f"PF EigenVector:\n{pfEigenVal(sub)}")

	print()
	sub = {"a":"ab",
		"b":"c",
		"c":"a"}
	eigenval = eigenValues(sub)
	if (eigenval != None):
		print(f"Substitution: {sub}\nMatrix:\n{matrix(sub)}")
		print(f"PF EigenVector:\n{pfEigenVal(sub)}")

	print()
	sub = {"a":"abcec",
		"b":"cbbdaa",
		"c":"abdcec",
		"d":"ddacb",
		"e":"abcde"}
	eigenval = eigenValues(sub)
	if (eigenval != None):
		print(f"Substitution: {sub}\nMatrix:\n{matrix(sub)}")
		curtime = time.time()
		print(f"PF EigenVector:\n{pfEigenVal(sub)}\nRight Eigenvectors: \n{eigenval[1]}")

	posttime = time.time()
	totaltime = posttime - curtime
	print(f"time: {totaltime}")

'''-----------------------------------------------------------
isPisot() Testing
-----------------------------------------------------------'''

def isPisotTest():
	print()
	sub = {"a":"abbb",
		"b":"c",
		"c": "ab"}
	eigenval = eigenValues(sub)
	if (eigenval != None):
		print(f"Substitution: {sub}\nMatrix:\n{matrix(sub)}\nEigenValues: {eigenval[0]}")
		print(f"PF EigenVector:\n{pfEigenVal(sub)}\nSubstitution is Pisot:{isPisot(sub)}")


	print()
	sub = {"a":"abbb",
		"b":"a"}
	eigenval = eigenValues(sub)
	if (eigenval != None):
		print(f"Substitution: {sub}\nMatrix:\n{matrix(sub)}\nEigenValues: {eigenval[0]}")
		print(f"PF EigenVector:\n{pfEigenVal(sub)}\nSubstitution is Pisot:{isPisot(sub)}")


	print()
	sub = {"a":"abcec",
		"b":"cbbdaa",
		"c":"abdcec",
		"d":"ddacb",
		"e":"abcde"}
	eigenval = eigenValues(sub)
	if (eigenval != None):
		print(f"Substitution: {sub}\nMatrix:\n{matrix(sub)}\nEigenValues: {eigenval[0]}\nRight Eigenvectors: \n{eigenval[1]}")
		print(f"PF EigenVector:\n{pfEigenVal(sub)}\nSubstitution is Pisot:{isPisot(sub)}")


'''-----------------------------------------------------------
isValid() Testing
-----------------------------------------------------------'''
def isValidTest():
	sub = {"a":"ab",
		"b":"a"}
	print(f"substitution: {sub} is Valid: {isValid(sub)}")

	sub = {"a":"abbdb",
		"b":"c",
		"c": "ab"}
	print(f"substitution: {sub} is Valid: {isValid(sub)}")


'''-----------------------------------------------------------
Testing All 
-----------------------------------------------------------'''

def testAll():
	subsitutionTest()
	matrixTest()
	eigenValuesTest()
	pfEigenValTest()
	isPisotTest()
	isValidTest()


testAll()
