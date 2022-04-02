from select import select
import streamlit as st
from PIL import Image
from Substitution import *
import matplotlib.pyplot as plt
from matplotlib import collections as mc
from matplotlib import cm
import time



def analyzeSubstitution(sub, iterations=4, initialState='a', debug=False):


    if (debug == True):
        curtime = time.time()
 
    pfEigenVector = pfEigenVal(sub)
    result = Substitution(sub, initialState, iterations)

    if (debug == True):
        print("Analysis time breakdown:")
        posttime = time.time()
        totaltime = posttime - curtime
        print(f"substitution time: {totaltime}")

    if (debug == True):
        curtime = time.time()
 
    segments = []
    xvalue = 0
    borderPercent = 0.03
    keys = list(sub.keys())
    for segment in result:
        segmentLength = pfEigenVector[keys.index(segment),0]
        segmentBoundary = segmentLength * borderPercent
        newSegment = [(xvalue + segmentBoundary, 0)]
        xvalue += segmentLength
        newSegment.append((xvalue - segmentBoundary, 0))
        segments.append(newSegment)
 
    if (debug == True):
        posttime = time.time()
        totaltime = posttime - curtime
        print(f"segmentlist time: {totaltime}")
 
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
    
 
    legendList = []
    legendCol = []
    xvalue = 0
    borderPercent = 0.01
    for segment in keys:
        segmentLength = pfEigenVector[keys.index(segment),0]
        segmentBoundary = segmentLength * borderPercent
        newSegment = [(xvalue + segmentBoundary, 0)]
        xvalue += segmentLength
        newSegment.append((xvalue - segmentBoundary, 0))
        legendList.append(newSegment)
        legendCol.append(colorlist[keys.index(segment)])

    if (debug == True):
        curtime = time.time()
    fig, ax = plt.subplots(2, 1)
    legendCol = mc.LineCollection(legendList, linewidths=10, colors=legendCol)
    ax[0].add_collection(legendCol)
    ax[0].margins(0.01)
    ax[0].set_ylim(-1,1)
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
    ax[1].grid()
    ax[1].yaxis.set_visible(False)
    fig.suptitle("Substitution Segment Diagram for: " + str(sub).replace("'", ""), fontsize = 16)
    

    if (debug == True):
        posttime = time.time()
        totaltime = posttime - curtime
        print(f"draw time: {totaltime}")
        print("--------------------------------------------------------------")

    return fig


standardSubs = [["Fibonacci", {"a":"ab", "b":"a"}], 
                ["2-component Rauzy Fractal", {"a":"acb", "b":"c", "c":"a"}],
                ["A->AB, B->C, C->A", {"a":"ab", "b":"c", "c":"a"}],
                ["Central Fibonacci", {"a":"ac", "b":"db", "c":"b", "d":"a"}],
                ["Infinite component Rauzy Fractal", {"a":"baca", "b":"aac", "c":"a"}],
                ["Kidney and its dual", {"a":"ab", "b":"cb", "c":"a" }],
                ["Kolakoski-(3,1) symmmetric variant, dual", {"a":"aca", "b":"a", "c":"b"}],
                ["Kolakoski-(3,1) variant A, with dual", {"a":"bcc", "b":"ba", "c":"bc"}],
                ["Kolakoski-(3,1) variant B, with dual", {"a":"abcc", "b":"a", "c":"bc"}],
                ["Kolakoski-(3,1), with dual", {"a":"abc", "b":"ab", "c":"b"}],
                ["Non-invertible connected Rauzy Fractal", {"a":"bacb", "b":"abc", "c":"ba"}],
                ["Non-reducible 4-letter", {"a":"aad", "b":"cd", "c":"cb", "d":"ab"}],
                ["Period Doubling", {"a":"ab", "b":"aa"}],
                ["Smallest PV", {"a":"bc", "b":"c", "c":"a"}],
                ["Thue Morse", {"a":"ab", "b":"ba"}],
                ["Tribonacci", {"a":"ab", "b":"ac", "c":"a"}]
]

standardSubs = dict(standardSubs)


st.set_page_config(layout="wide")

st.title("Substitution Viewer")


colA, colB = st.columns((2,1))
with colA: 
    selectedSub = st.selectbox("Select a Substitution", standardSubs.keys())

with colB: 
    st.caption("Made by Orion Sehn, with help from Dr.Nicolae Strungaru and Dr.Christopher Ramsey")
    st.caption("Feel free to reach out to me at sehno@mymacewan.ca")

st.markdown('''---''')
st.header("Substitution Definition")


colC, colD , colE= st.columns((5, 1, 5))

variable_list = []

with colC:
    rule_counter = 0
    for rule in standardSubs[selectedSub]:
        rule_counter += 1
        variable_list.append(st.text_input(f"Tile {rule_counter}", value=rule))

with colD:
    st.text("")
    image = Image.open("right_arrow.png")
    for i in range(len(standardSubs[selectedSub])):
        st.image(image, width=93 )

replace_list = []
with colE:
    rule_counter = 0
    for rule in standardSubs[selectedSub]:
        rule_counter += 1
        replace_list.append(st.text_input(f"Replace Tile Rule {rule_counter}", value=standardSubs[selectedSub][rule]))


sub = {}

for i in range(len(variable_list)):
    sub[variable_list[i]] = replace_list[i]

st.markdown('''---''')

if not isValid(sub):
    st.subheader(f"{sub} is not a valid substitution")

else:
    colF, colG = st.columns(2)
    #substitution info
    with colF:

        st.header("Substitution Info")
        st.markdown('''---''')
        pfEigenVector = pfEigenVal(sub)
        st.subheader("Matrix:")
        st.text(matrix(sub))
        st.subheader("Perron-Frobenius Eigenvector:")
        st.text(pfEigenVector)
        st.subheader("Eigenvalues:")
        st.text(eigenValues(sub)[0])
        st.subheader(f"Substitution is Pisot: {isPisot(sub)}")
    
    with colG:
        st.header("Segment Diagram")
        st.markdown('''---''')
        st.pyplot(analyzeSubstitution(sub))
    
    st.markdown('''---''')

    
