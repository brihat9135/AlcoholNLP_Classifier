

@author Brihat Sharma

Introduction

Alcohol classifier to identify alcohol misuse from the Electronic Health Record of Emergency Department and Hospitalized Patients. The first 24hr of clinical notes are needed as an input, which should be first processed using Apache cTAKES to concept map the raw  with UMLS into Concept Unique Identifiers (CUIs). 

Original research article describing development and internal validation: https://www.ncbi.nlm.nih.gov/pubmed/30602031.  The classifier was trained against patients that completed the Alcohol Use Disorders Identification Test.

Dependencies Library: Pandas, os, pickle

Steps:

cTAKES:

1) Download cTAKES from https://ctakes.apache.org/downloads.cgi
2) cTAKES comes with default dictionary, this dictionary can also be cutomized creating own version. Our dictionary consists of rxnorms and snomedCT but default dictionary also works well
3) Process the input data using cTAKES, this will crete .txt files with CUIs which will be input data to the model



Model:

1) Open the Alcohol_Predict.py script and change the input and output directory
2) Run the sript as python3 Alcohol_predict.py
3) The result will be inside the output directory inside a csv file, first column represents the files, second column represents predicted labels and the third column represents predict probability. 1 as current alcohol misuse and 0 as no alcohol misuse for the second column.  
