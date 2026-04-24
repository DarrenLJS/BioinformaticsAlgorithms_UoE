######################################################################
# A simple example of how to build a Decision Tree and Random        #
# Forest classifier using Python                                     #
# This gives a very basic outline- much more testing and development #
# of models is required to generate a well-performing model.         #
# So this is just a start...                                         #
# more detail see https://scikit-learn.org/stable/modules/tree.html  #
#                                                                    #
# Requires pandas, matplotlib, scikit-learn and graphviz             #
# Local install required for graphviz graphics                       #
# Simon Tomlinson Bioinformatics Algorithms                          #
######################################################################

#main libraries Note Graphviz need to be on the path as well
#You may need to change this if you use a different path
#for Graphviz

from sklearn.datasets import load_iris
from sklearn import tree
import graphviz
import pandas as pd

#graphviz needs to be found under windows-this sets the path
#which is not set by the current installer
import os
if os.name == 'nt':
    os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

#load the Iris data- the comes with sklearn see also (http://archive.ics.uci.edu/ml/index.php)
iris_data = load_iris()

#build a decision tree classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris_data.data,iris_data.target)

#make a plot of the tree
tree.plot_tree(clf.fit(iris_data.data, iris_data.target))
dot_data = tree.export_graphviz(clf, out_file=None,
feature_names=iris_data.feature_names,
class_names=iris_data.target_names,
filled=True, rounded=True,proportion=False,
special_characters=True)
graph = graphviz.Source(dot_data, format="png")
graph.render("my_decision_tree")
#This will write a graph of the decisions made by the algorithm
#in order to classify the samples

# print the label species
print("Target Names")
print(iris_data.target_names)

# print the names of the features
print("Feature Names (for the Data Items")
print(iris_data.feature_names)

# print the top iris_data items
print("Data Items")
print(iris_data.data[1:10])

# print the iris (species) targets to predict
print("Iris species to predict")
print(iris_data.target)

#build a table to store the data used for classification..
data=pd.DataFrame({
    'sepal length':iris_data.data[:,0], #names are keys!
    'sepal width':iris_data.data[:,1],
   'petal length':iris_data.data[:,2],
    'petal width':iris_data.data[:,3],
    'species':iris_data.target
})
print("Top of Data Table")
print(data.head())

#This pandas table provides the means to import other dataset
#just store the data as a CSV files and load data
#import pandas as pd
#mytab = pd.read_csv('mytab.csv')
#mytab.head()

# Import train_test_split function
from sklearn.model_selection import train_test_split

X=data[['sepal length', 'sepal width', 'petal length', 'petal width']]  # Features
y=data['species']  # Labels

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4) # 60% training and 40% test

#Import Random Forest Model
from sklearn.ensemble import RandomForestClassifier

#Create a RF classifier Classifier
clf=RandomForestClassifier(n_estimators=5000)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)
#Make the prediction
y_pred=clf.predict(X_test)

from sklearn import metrics
# Print model accuracy
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

print("***Completed successfully***")

