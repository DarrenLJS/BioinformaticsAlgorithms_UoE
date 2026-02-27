#pip install plotly==4.5.4
#see https://plot.ly/python-api-reference/generated/plotly.graph_objects.Figure.html
#see plot.ly/
import plotly.graph_objects as  go
import plotly.offline  as  offline
import csv
import math

#Simple plotting function
def plotme(xx,yy):
    fig = go.Figure(
       data=go.Scattergl(
            x=xx,
            y=yy,
            mode='markers'
        ),
       layout=go.Layout(
          title=go.layout.Title(text="A Scatter Plot"))
    )
    offline.plot(fig, filename='file.html',auto_open=False)


	
#load a file- this will contain comma delimited values for distance
def loadafile(flename):
    mytable =[]
    with open(flename, "r") as fle:
        lines = fle.readlines()
        for line in lines:
            a_list = line.strip().split(",")
            a_list = list(map(lambda x: float(x), a_list))
            mytable.append(a_list)
    return mytable

	
#calculate Euclidean distance
def euclidean_distance(element1, element2):

    if(len(element1)!=len(element2)):
          print("values wrong length....")
          return -1

    d = 0
    for i in range(len(element1)):
        d += (element1[i] - element2[i])**2
    d = math.sqrt(d)
    return d

	
#find the least distant pair of indexes using this method
def findClosest(mytable):
    dist=0.0
    val1=-1
    val2=-1
    a_list_dict = []
    for i in range(len(mytable)):
        for j in range(i+1, len(mytable)):
            a_dict = {}
            a_dist = euclidean_distance(mytable[i], mytable[j])
            if a_dist < 0:
                continue
            a_dict["val1"] = i
            a_dict["val2"] = j
            a_dict["dist"] = a_dist
            a_list_dict.append(a_dict)
    
    a_list_dict = sorted(a_list_dict, key = lambda x: x.get("dist"))
    print(a_list_dict)
    val1 = a_list_dict[0].get("val1")
    val2 = a_list_dict[0].get("val2")
    dist = a_list_dict[0].get("dist")
    return val1, val2, dist

#call the methods as the script loads...

#Test
#dd=euclidean_distance([4,5,6,7],[4,5,12,7])

#Load files-small file for testing, big file for final search
ed=loadafile("test_bigfile.csv")
#ed=loadafile("test_file1.csv")
print(ed)
#Find least distant
ee=findClosest(ed)
#print simple results
#print("result",dd)
print("result2",ee[0],ee[1],ee[2])
print(f"{ed[ee[0]]}\n{ed[ee[1]]}")
#Plot the winning distance
plotme(ed[ee[0]],ed[ee[1]])