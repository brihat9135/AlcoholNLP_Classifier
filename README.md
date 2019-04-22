This classifier is created by Loyola Medical Center

@author Brihat Sharma

Introduction

Alcohol classifer model to identify alcohol misuse. Anc notes are needed as an input, which should be first processed using Apache cTAKES. 

Dependencies Library: Pandas, os, pickle

Steps:

cTAKES:

1) Download cTAKES from https://ctakes.apache.org/downloads.cgi
2) cTAKES comes with default dictionary, this dictionary can also be cutomized creating own version. Our dictionary consists of rxnorms and snomedCT but default dictionary work well
3) Process the input data using cTAKES, this will crete .txt files with CUIs which will be input data to the model



Model:

1) Open the Alcohol_Predict.py script and change the input and output directory
2) Run the sript as python3 Alcohol_predict.py
3) The result will be inside the output directory inside a csv file, first column represents the files, second column represents predicted labels and the third column represents predict probability. 1 as detected and 0 as undetected for the second column.  
