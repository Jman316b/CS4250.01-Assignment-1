#-------------------------------------------------------------------------
# AUTHOR: Jeremiah
# FILENAME: indexing.py
# SPECIFICATION: description of the program
# FOR: CS 4250- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#Importing some Python libraries
import csv

documents = []

#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0])

#Conducting stopword removal. Hint: use a set to define your stopwords.
#--> add your Python code here
stopWords = {"and"}

#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
#--> add your Python code here
steeming = {
    "cats": "cat",
    "dogs": "dog",
    "loves": "love"
}

#Identifying the index terms.
#--> add your Python code here
terms = []
for document in documents:
    for term in document.rsplit(" "):
        stopWord = False
        for stopW in stopWords:
            if term == stopW:
                stopWord = True

        if not stopWord:
            notFound = True
            for index in terms:
                if term == index[0] or steeming.get(term) == index[0]:
                    index[1] += 1
                    notFound = False
            if notFound and steeming.get(term) != None:
                terms.append([steeming.get(term), 1])
            elif notFound:
                terms.append([term, 1])


#Building the document-term matrix by using the tf-idf weights.
#--> add your Python code here
docTermMatrix = []

#Printing the document-term matrix.
#--> add your Python code here