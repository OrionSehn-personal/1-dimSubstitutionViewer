import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections as mc
from Substitution import *
import time

def analyzeSubstitution(sub, iterations, debug=False):

	'''-----------------------------------------------------------
	Substitution
	-----------------------------------------------------------'''
	if (debug == True):
		curtime = time.time()

	pfEigenVector = pfEigenVal(sub)
	result = Substitution(sub, "a", iterations)
	print(f"Perron-Frobenius Eigenvector: \n{pfEigenVector}")
	print(f"Substitution is Pisot-Frobenius: {isPisot(sub)}")
	print(f"Symbolic Representation: \n{result}")

	if (debug == True):
		posttime = time.time()
		totaltime = posttime - curtime
		print(f"substitution time: {totaltime}")
	'''-----------------------------------------------------------
	SegmentList Construction
	-----------------------------------------------------------'''
	if (debug == True):
		curtime = time.time()

	segments = []
	xvalue = 0
	border = 0.05
	keys = list(sub.keys())
	for segment in result:
		newSegment = [(xvalue+border, 0)]
		xvalue += pfEigenVector[keys.index(segment),0]
		newSegment.append((xvalue-border, 0))
		segments.append(newSegment)

	if (debug == True):
		posttime = time.time()
		totaltime = posttime - curtime
		print(f"segmentlist time: {totaltime}")


	'''-----------------------------------------------------------
	ColorList Construction
	-----------------------------------------------------------'''
	if (debug == True):
		curtime = time.time()

	#setting up a list of colors to match the substitution result
	colorlist = ["#e89f73", "#4c91d1", "#c28897", "#c4e0ef", "#a0a5b1"]
	c = []

	while (len(keys)>len(colorlist)):
		colorlist.append((np.random.rand(3,)))
	
	for segment in result:
		c.append(colorlist[keys.index(segment)])

	if (debug == True):
		posttime = time.time()
		totaltime = posttime - curtime
		print(f"color time: {totaltime}")

	'''-----------------------------------------------------------
	Legend Construction
	-----------------------------------------------------------'''

	legendList = []
	legendCol = []
	border = 0.025
	xvalue = 0
	for segment in keys:
		newSegment = [(xvalue+border, 0)]
		xvalue += pfEigenVector[keys.index(segment),0]
		newSegment.append((xvalue-border, 0))
		legendList.append(newSegment)
		legendCol.append(colorlist[keys.index(segment)])


	'''-----------------------------------------------------------
	Drawing the Segments / Legend
	-----------------------------------------------------------'''
	if (debug == True):
		curtime = time.time()
	fig, ax = plt.subplots(2, 1)
	legendCol = mc.LineCollection(legendList, linewidths=10, colors=legendCol)
	ax[0].add_collection(legendCol)
	ax[0].margins(0.01)
	ax[0].set_ylim(-1,1)
	ax[0].autoscale
	ax[0].grid()
	ax[0].yaxis.set_visible(False)
	xvalue = 0
	for segment in keys:
		pfval = pfEigenVector[keys.index(segment),0]
		xvalue += pfval
		ax[0].text(xvalue - (pfval/2), 0.25, segment, fontsize=15)

	linecol = mc.LineCollection(segments, linewidths=10, colors=c)
	ax[1].add_collection(linecol)
	ax[1].margins(0.01)
	ax[1].autoscale
	ax[1].grid()
	ax[1].yaxis.set_visible(False)

	if (debug == True):
		posttime = time.time()
		totaltime = posttime - curtime
		print(f"draw time: {totaltime}")

	plt.show()
	
# sub = { "a":"abcec",
# 		"b":"cbbdaa",
# 		"c":"abdcec",
# 		"d":"ddacb",
# 		"e":"abcdef",
# 		"f" :"a"}
# analyzeSubstitution(sub, 4, debug=True)

sub = {"a":"ab",
	   "b":"a" }
analyzeSubstitution(sub, 5)

