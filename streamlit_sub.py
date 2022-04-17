import streamlit as st
from PIL import Image
from Substitution import *
import matplotlib.pyplot as plt
from matplotlib import collections as mc
import time
from string import ascii_lowercase

def bmatrix(a):
    """Returns a LaTeX bmatrix

    :a: numpy array
    :returns: LaTeX bmatrix as a string
    """
    if len(a.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')
    lines = str(a).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{bmatrix}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv +=  [r'\end{bmatrix}']
    return '\n'.join(rv)


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
with st.expander("Introductory Explaination"):
    st.caption("A tile substitution is a method for constructing highly ordered tilings, most importantly, some substitutions generate aperiodic tilings.")
    st.caption("A substitution consists of a set of rules, which dictates what a tile will be substituted with on each iteration.")
    image = Image.open("house_rule.png")
    st.image(image, width=250)
    st.caption("This rule is applied to each tile in the tiling recursively with each iteration")
    image = Image.open("House_substitution_tiling.svg.png")
    st.image(image, width=500)
    st.caption("Eventually, these tiles will tile the plane.")
    image = Image.open("house_patch.gif")
    st.image(image)

    st.caption("This is a tool which visualizes most one dimensional substitutions. These follow many of the same rules, but are simpler as they are just line segments. Additionally some key associated information is shown, notably a Segment Diagram, the Substitution's PF Eigenvector, as well as a graph of its Bragg Diffraction Intensity Function.")
st.header("Substitution Definition")
num_variables = st.number_input("Number of Variables", value=len(standardSubs[selectedSub]), min_value=1, max_value=10)

colC, colD , colE= st.columns((5, 1, 5))

variable_list = []

selected_variables = list(standardSubs[selectedSub].keys())
selected_values = list(standardSubs[selectedSub].values())

with colC:
    for i in range(int(num_variables)):
            variable_list.append(st.text_input(f"Tile {i+1}", value=ascii_lowercase[i], disabled=True))

with colD:
    st.text("")
    image = Image.open("right_arrow.png")
    for i in range(int(num_variables)):
        st.image(image, width=93)

replace_list = []
with colE:
    for i in range(int(num_variables)):
        if i < len(selected_variables):
            replace_list.append(st.text_input(f"Replace Tile {i+1}", value=selected_values[i]))
        else:
            replace_list.append(st.text_input(f"Replace Tile {i+1}", value=""))

sub = {}

for i in range(len(replace_list)):
    sub[ascii_lowercase[i]] = replace_list[i]

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
        st.latex(bmatrix(np.transpose(matrix(sub))))
        st.subheader("Perron-Frobenius Eigenvector:")
        st.latex(bmatrix(pfEigenVector))
        st.subheader("Eigenvalues:")
        result = eigenValues(sub)[0]
        st.latex(bmatrix(np.asmatrix(result).T))
        st.subheader("Substitution is Pisot:")
        st.markdown(isPisot(sub))
    
    with colG:
        st.header("Segment Diagram")
        st.pyplot(analyzeSubstitution(sub, initialState="a"))
    
    st.markdown('''---''')


    colH, colI = st.columns(2)

    with colH:
        st.header("Substitution Intensity Function")
        x, y = diffraction(sub, initialState="a")
        fig, ax = plt.subplots()
        ax.plot(x, y)
        st.pyplot(fig)
    
    with colI:
        st.header("Substitution Projection")
        fig, ax = plt.subplots(1,1)
        x = projection(sub, initialstate="a")
        lowerbound = 0
        upperbound = 10
        img = ax.imshow(x, extent = [lowerbound,upperbound, lowerbound, upperbound])
        ax.yaxis.set_visible(False)
        fig.colorbar(img)
        st.pyplot(fig)


st.markdown('''---''')
st.caption("Repository availible at: https://github.com/funmaster524/1-dimSubstitutionViewer.git")
st.caption(
    '''
    References:

[1] Baake M., Grimm U, Aperiodic Order: Volume 1, A Mathematical Invitation ,
Cambridge University Press, 2013.

[2] Baake M., Grimm U., The singular continuous diffraction measure of the Thue-Morse
chain, J. Phys. A: Math. Theor. 41, 1-6, 2008.

[3] Baake M., Spindeler T. Strungaru N., Diffraction of compatible random substitutions
in one dimension , Indag. Math. 29, 1031-10711, 2018.

[4] Baake M., Strungaru N., Eberlein decomposition for PV inflation systems , preprint,
2020.

[5] Richard C., Strungaru N., Pure point diffraction and Poisson summation , Ann. Henri
Poincare 18, 3903–3931, 2017.

[6] Richard C., Strungaru N., A short guide to pure point diffraction in cut-and-project
sets , J. Phys. A: Math. Theor. 50, 2017.

[7] Strungaru N., On the Fourier analysis of measures with Meyer set support , J. Funct.
Anal. 278, 2020.

[8] D. Frettlöh, E. Harriss, F. Gähler: Tilings encyclopedia, https://tilings.math.uni-bielefeld.de/
'''
)