#This is an example implementation of Euclidean Pearson Correlation
#It uses plotly and this may need to be installed on your own machine eg "pip install plotly==4.5.4"
#see https://plot.ly/python-api-reference/generated/plotly.graph_objects.Figure.html
#see plot.ly/
import plotly.graph_objects as  go
import plotly.offline  as  offline
import csv
import math

#Simple plotting function- but many more plots are available...
def plotme(xx,yy):
    fig = go.Figure(
       data=go.Pointcloud(x=xx, y=yy),
       layout=go.Layout(
          title=go.layout.Title(text="A Scatter Plot"))
    )
    offline.plot(fig, filename='file.html',auto_open=False)


#load a file- this will contain comma delimited values for correlation
def loadafile(flename):

    mytable =[]

    with open(flename) as values:
        g_reader = csv.reader(values, delimiter=',')
        for value in g_reader:
            test =list(value)
            #see https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
			#here we actually convert to a float but the syntax is nearly identical
            test = [float(i) for i in test]
            
            mytable.append(test)
    return mytable

#calculate Euclidean distance
def euclidean_distance(element1, element2):

    if(len(element1)!=len(element2)):
          print("values wrong length....")
          return -2

    d=0

    for x in range(0, len(element1)):
            d=d+(element1[x]-element2[x])**2
    d=math.sqrt(d)
    return d

#Find the most correlated pair of indexes using this method

def findClosest(mytable):
    dist=0.0
    val1=-1
    val2=-1

    for x in range(0,len(mytable)):
            for y in range(x+1,len(mytable)):
                mydist=euclidean_distance(mytable[x],mytable[y])

                if(val1==-1):
                    dist = mydist
                    val1 = x
                    val2 = y
                    continue

                if mydist<dist:
                    dist=mydist
                    val1=x
                    val2=y
    return val1, val2,dist

#It might be better to pass the distance/correlation function and use whatever method
#was passed to  find the most correlated
#This is a more elegant design but more complicated and so left as an exercise here....



#call the methods- just test examples...

test_vals1=[43,21,25,42,57,59]
test_vals2=[99,65,79,75,87,81]


dd=euclidean_distance(test_vals1,test_vals2)
print("test euclidean distance ",test_vals1," with ", test_vals2," is (to2dp)",round(dd,2))



#Load files-small file for testing, big file for final search
ed=loadafile("test_bigfile.csv")
#ed=loadafile("test_file1.csv")
#Find most cloest pair
ee=findClosest(ed)
#print simple results

print("Least distant in the table: ",ee[0],ee[1],ee[2])
#Plot the winning correlation
plotme(ed[ee[0]],ed[ee[1]])

#The expected answer is index 1 and 49 are 0 distance apart.  If you load the example file into Excel you can see
# that these two lines (line 2 and 50 in 1-indexed Excel) have identical rows of values.  This is why they plot as
# a straight line and have a Euclidean distance of 0.0!  For other examples, values may be returned that have
#distance much greater than 0, we only guarentee to find the closest values in terms of distance compared to the others
#In terms of actual euclidean distance even the closest values might be widely separated in space...

#Euclidean distance is another example of Order n2 (n squared) complexity operation- each row has to be compared
# to each other row so the overall number of comparisons made is the n, the number of rows, times n.  n is considered  much larger than the
# number of elements each row that need to be visited to calculate the distance.
#Also even though we calculate a triangular distance matrix (as the distance beteeen A and B is the same as between B and A
#This only save 50% of the compute time- so complexity is still O(n2)


