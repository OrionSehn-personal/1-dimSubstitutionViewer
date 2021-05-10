import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections as mc
from Substitution import *


sub = {"a":"ab",
	   "b":"a" }
pfEigenVector = pfEigenVal(sub)
result = Substitution(sub, "a", 7)
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



c = np.array([(1,0,0,1),(0,1,1,1)])

linecol = mc.LineCollection(segments, linewidths=8, colors=c)
fig, ax = plt.subplots()
ax.add_collection(linecol)
ax.margins(0.1)
ax.autoscale
plt.grid()
plt.show()