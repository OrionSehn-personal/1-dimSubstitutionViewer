import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections as mc
from Substitution import *
import time

#Defining drawing function
def analyzeSubstitution(sub, iterations=5, initialState='a', debug=False):
 
    '''-----------------------------------------------------------
    Substitution
    -----------------------------------------------------------'''
    if (debug == True):
        curtime = time.time()
 
    pfEigenVector = pfEigenVal(sub)
    result = Substitution(sub, initialState, iterations)
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
    One Dimenstional Subsitution Viewer - Orion Sehn 2021
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
            if isValid(newsub):
                print("New substitution defined: ")
                print(newsub)
                sub = newsub
            else:
                print(f"Substitution {newsub} is not a valid substitution")

        if (userinput.strip() == "2"):
            print("Printing info about the Substitution")
            substitutioninfo(sub)

        if (userinput.strip() == "3"):
            errorFlag = False
            print("Printing a symbolic text representaion of the Substitution")
            custom = input("Enter c to enter custom parameters or press enter to use default settings (iterations = 5, initialstate 'a'): ")
            if (custom.strip() == "c"):

                iterations = input("Enter a number of iterations: ")
                initialState = input("Define an initial state ie. (abba): ")
                #Error checking input for validity
                try: 
                    iterations = int(iterations)
                except:
                    print("Iterations must be a natural number")
                    errorFlag = True
                if (errorFlag == False):
                    if (iterations < 0):
                        print("Iterations must be greater than or equal to 0")
                        errorFlag = True
                if (errorFlag == False):
                    for char in initialState:
                        if (char not in sub.keys()):
                            print(f"Initialstate: {initialState} is not valid")
                            errorFlag = True
                #Printing subsitution with custom parameters
                if (errorFlag == False):
                    print()
                    print(Substitution(sub, initialState, int(iterations)))

            else: 
                print(Substitution(sub, "a", 5))


        if (userinput.strip() == "4"):
            errorFlag = False
            print("Displaying a segment diagram of the substitution")
            custom = input("Enter c to enter custom parameters or press enter to use default settings (iterations = 5, initialstate 'a'): ")
            if (custom.strip() == "c"):            
                iterations = input("Enter a number of iterations: ")
                initialState = input("Define an initial state ie. (abba): ")
                #Error checking input for validity
                try: 
                    iterations = int(iterations)
                except:
                    print("Iterations must be a natural number")
                    errorFlag = True
                if (errorFlag == False):
                    if (iterations < 0):
                        print("Iterations must be greater than or equal to 0")
                        errorFlag = True
                if (errorFlag == False):
                    for char in initialState:
                        if (char not in sub.keys()):
                            print(f"Initialstate: {initialState} is not valid")
                            errorFlag = True

                if (errorFlag == False):
                    analyzeSubstitution(sub, iterations, initialState)   

            else: 
                analyzeSubstitution(sub)


        if (userinput.strip() == "5"):
            errorFlag = False
            print("Displaying diffraction pattern of the Substitution")
            custom = input("Enter c to enter custom parameters or press enter to use default settings(0 < x < 10, x interval = 0.01, k = 20): ")
            
            if (custom.strip() == "c"):
                xlower = input("Enter lower bound for x: ")
                xupper = input("Enter upper bound for x: ")
                xint = input("Enter value for x interval: ")
                k = input("Enter value for k: ")
                try:
                    int(xlower)
                    int(xupper)
                    float(xint)
                    int(k)
                except:
                    print("xlower, xupper and k must be natural numebrs, xint must be a decimal")
                    errorFlag = True

                if (errorFlag == False):
                    x, y = diffraction(sub, int(xlower), int(xupper), float(xint), int(k))
                    plt.plot(x, y)
                    plt.show()

            else:
                x, y = diffraction(sub)
                plt.plot(x, y)
                plt.show()

        if (userinput.strip() == "6"):
            print("Quit")
            return
        

GUI()
