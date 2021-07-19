import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections as mc
from Substitution import *
import time

#Defining drawing function
def analyzeSubstitution(sub, iterations, debug=False):
 
    '''-----------------------------------------------------------
    Substitution
    -----------------------------------------------------------'''
    if (debug == True):
        curtime = time.time()
 
    pfEigenVector = pfEigenVal(sub)
    result = Substitution(sub, "a", iterations)
    # print("--------------------------------------------------------------")
    # print(f"Substitution: \n{sub}")
    # print(f"Iterations: {iterations}")
    # print(f"Symbolic Representation: \n{result}")
    # print("--------------------------------------------------------------")
    # print(f"Matrix: \n{matrix(sub)}")
    # print(f"Perron-Frobenius Eigenvector: \n{pfEigenVector}")
    # print(f"Eigenvalues: \n{eigenValues(sub)[0]}")
    # print(f"Substitution is Pisot: {isPisot(sub)}")
    # print("--------------------------------------------------------------")

    if (debug == True):
        print("Analysis time breakdown:")
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
        print("--------------------------------------------------------------")

    plt.show()

'''-----------------------------------------------------------------------------
Edit this portion to plot a given substitution described in the following way:
-----------------------------------------------------------------------------'''


def substitutioninfo(sub):
    pfEigenVector = pfEigenVal(sub)
    print("--------------------------------------------------------------")
    print(f"Substitution: \n{sub}")
    print(f"Matrix: \n{matrix(sub)}")
    print(f"Perron-Frobenius Eigenvector: \n{pfEigenVector}")
    print(f"Eigenvalues: \n{eigenValues(sub)[0]}")
    print(f"Substitution is Pisot: {isPisot(sub)}")
    print("--------------------------------------------------------------")

def GUI():
    header = '''-----------------------------------------------------------------------------
    Subsitution Viewer - Orion Sehn 2021
-----------------------------------------------------------------------------'''

    options = '''
    1 - Define a Substitution
    2 - View info about the Substitution
    3 - View a symbolic text representaion of the Substitution
    4 - View a segment diagram of the substitution
    5 - View the diffraction pattern of the Substitution
    6 - Quit
    '''
    sub = {"a":"ab",
           "b":"a"}

    exit = False
    userinput = ""
    while (exit == False):
        print(header)
        print(options, "")
        userinput = input()
        if (userinput.strip() == "1"):
            print("Defining Substitution - (enter nothing to cancel)")
            numVar = input("Number of Variables: ")
            if (numVar != ""):
                asciicode = 97
                newsub = dict()
                for i in range(int(numVar)):
                    variable = chr(asciicode)
                    newsub[variable] = input(f"Substitute {variable} with: ").strip()
                    asciicode += 1
        #TODO check if the new substitution is "Valid"
        sub = newsub
        print("New substitution defined: ")
        print(sub)

        if (userinput.strip() == "2"):
            print("Printing info about the Substitution")
            substitutioninfo(sub)

        if (userinput.strip() == "3"):
            print("Printing a symbolic text representaion of the Substitution")
            print(Substitution(sub, "a", 5))


        if (userinput.strip() == "4"):
            print("Displaying a segment diagram of the substitution")
            iterations = 5
            analyzeSubstitution((sub), iterations)


        if (userinput.strip() == "5"):
            print("Displaying diffraction pattern of the Substitution")
            x, y = diffraction(sub)
            plt.plot(x, y)
            plt.show()

        if (userinput.strip() == "6"):
            print("Quit")
            return
        







sub = {"a":"abc",
       "b":"bc",
       "c":"a"}
 
# analyzeSubstitution(sub, iterations = 6, debug = True)

GUI()
