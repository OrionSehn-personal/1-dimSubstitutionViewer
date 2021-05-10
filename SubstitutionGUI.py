import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections as mc
from Substitution import *
import time

# sub = {"a":"ab",
# 	   "b":"a" }
curtime = time.time()

sub = { "a":"abcec",
		"b":"cbbdaa",
		"c":"abdcec",
		"d":"ddacb",
		"e":"abcde"}


pfEigenVector = pfEigenVal(sub)
result = Substitution(sub, "a", 3)
posttime = time.time()
totaltime = posttime - curtime
print(f"substitution time: {totaltime}")

curtime = time.time()
segments = []
xvalue = 0
keys = list(sub.keys())
for segment in result:
	newSegment = [(xvalue, 0)]
	xvalue += pfEigenVector[keys.index(segment),0]
	newSegment.append((xvalue, 0))
	segments.append(newSegment)

posttime = time.time()
totaltime = posttime - curtime
print(f"segmentlist time: {totaltime}")

# print(pfEigenVector)
# print(segments)
# print(result)
curtime = time.time()

colorlist = ["#e89f73", "#4c91d1", "#c28897", "#c4e0ef", "#a0a5b1"]
c = []
for segment in result:
	c.append(colorlist[keys.index(segment)])
posttime = time.time()
totaltime = posttime - curtime
print(f"color time: {totaltime}")

curtime = time.time()
linecol = mc.LineCollection(segments, linewidths=15, colors=c)
fig, ax = plt.subplots()
ax.add_collection(linecol)
ax.margins(0.01)
ax.autoscale
plt.grid()
posttime = time.time()
totaltime = posttime - curtime
print(f"draw time: {totaltime}")
plt.show()


