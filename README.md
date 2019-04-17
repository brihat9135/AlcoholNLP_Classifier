This classifier is created by Loyola Medical Center

@author Brihat Sharma

Introduction

Alcohol classifer model detects patient with alcohol consumsion. Anc notes are needed as an input, which should be first processed using Apache cTAKES. 

Steps:

cTAKES:

1) Download cTAKES from https://ctakes.apache.org/downloads.cgi
2) 





Model:

1) Open the Alcohol_Predict.py script and change the input and output directory
2) run the sript as python3 Alcohol_predict.py
3) the result will be inside the output directory inside a csv file, first column represents the files and the second column represents predicted labels. 1 as detected and 0 as undetected. 
