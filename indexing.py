# -------------------------------------------------------------------------
# AUTHOR: Jeremiah
# FILENAME: indexing.py
# SPECIFICATION: description of the program
# FOR: CS 4250.01 Assignment #1
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

# Importing some Python libraries
import csv
import math

documents = []

# Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            documents.append(row[0])

# Conducting stopword removal. Hint: use a set to define your stopwords.
# --> add your Python code here
stopWords = {"I", "and", "She", "her", "They", "their"}

# Conducting stemming. Hint: use a dictionary to map word variations to their stem.
# --> add your Python code here
stemming = {
    "cats": "cat",
    "dogs": "dog",
    "loves": "love"
}

# Identifying the index terms.
# --> add your Python code here
terms = []
totalWordsInEachDoc = []
individualWordCountInEachDoc = []


def isStopWord(word):
    for stopWord in stopWords:
        if word == stopWord:
            return True
    return False


def ifHasStemConvertToStem(word):
    if stemming.get(word) is not None:
        return stemming.get(word)
    return word


for document in documents:
    totalsWordsInDocument = 0
    documentWords = []
    for word in document.rsplit(" "):
        if not isStopWord(word):
            usableWord = ifHasStemConvertToStem(word)
            totalsWordsInDocument += 1
            wordSeen = False
            for seenWord in documentWords:
                if usableWord is seenWord[0]:
                    seenWord[1] += 1
                    wordSeen = True
            if not wordSeen:
                documentWords.append([usableWord, 1])
            wordSeen = False
            for term in terms:
                if usableWord == term[0]:
                    term[1] += 1
                    wordSeen = True
            if not wordSeen:
                terms.append([usableWord, 1])
    totalWordsInEachDoc.append(totalsWordsInDocument)
    individualWordCountInEachDoc.append(documentWords)


# Building the document-term matrix by using the tf-idf weights.
# --> add your Python code here
docTermMatrix = []
for doc in totalWordsInEachDoc:
    docTermMatrix.append([])

for term in terms:
    termTF = []
    termUniqueCountInAllDocs = 0
    termIDF = 0
    termTFIDF = []
    for i, document in enumerate(documents):
        wordInDoc = False
        for word in individualWordCountInEachDoc[i]:
            if term[0] == word[0]:
                tf = word[1]/totalWordsInEachDoc[i]
                wordInDoc = True
                termUniqueCountInAllDocs += 1
                termTF.append(tf)
        if not wordInDoc:
            termTF.append(0)

    termIDF = math.log10(totalWordsInEachDoc.__len__()/termUniqueCountInAllDocs)

    for i, tf in enumerate(termTF):
        docTermMatrix[i].append(tf * termIDF)
# Printing the document-term matrix.
# --> add your Python code here
print("Document #", end=" ")
for term in terms:
    print(term[0].rjust(6, " "), end=" ")
print()

for r, row in enumerate(docTermMatrix):
    print(f"Document {r + 1}", end=" ")
    for c, column in enumerate(docTermMatrix[0]):
        print(f"{docTermMatrix[r][c]:.4f}", end=" ")
    print()
