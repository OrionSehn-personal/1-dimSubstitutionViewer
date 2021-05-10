import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections as mc
from Substitution import *


sub = {"a":"ab",
	   "b":"a" }
pfEigenVector = pfEigenVal(sub)
result = Substitution(sub, "a", 9)
segments = []
xvalue = 0
keys = list(sub.keys())
for segment in result:
	newSegment = [(xvalue, 0)]
	xvalue += pfEigenVector[keys.index(segment),0]
	newSegment.append((xvalue, 0))
	segments.append(newSegment)

print(pfEigenVector)
print(segments)
print(result)
colorlist = ["#e89f73", "#4c91d1", "#c28897", "#c4e0ef", "#a0a5b1"]
c = []
for segment in result:
	c.append(colorlist[keys.index(segment)])

print(c)
linecol = mc.LineCollection(segments, linewidths=15, colors=c)
fig, ax = plt.subplots()
ax.add_collection(linecol)
ax.margins(0.1)
ax.autoscale
plt.grid()
plt.show()