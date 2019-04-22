

"""
Created on Mon April 15, 2019

@author: Brihat Sharma

"""

import pandas as pd
import os
import pickle


"""
1)Change the input and output directory below and run the script using python3 Alcohol_predict.pyvia command line or python IDE
2) inputdir and outputdir are on line 87 and 88
3)Make sure vectorizer and model pickles are in the same directory as this script file
"""


class ProcessData:


    #method to read file and keep them in a dataframe
    #takes inputdirectory as a parameter and outputs dataframe
    def dffiles(self, directory):
        txtfilesList = []
        patientL = []
        count = 0
        for file in os.listdir(directory):
            try:
                if file.endswith(".txt"):
                    txtfilesList.append(directory + str(file))
                    patientL.append(str(file))
                    count = count + 1
                else:
                    print("Not a text file")
            except Exception as e:
                raise e
                print("No Files found here!")
        print("Total files found", count)
        txtfilesTrain_df = pd.DataFrame({'Filename':patientL, 'FileList':txtfilesList})
        return txtfilesTrain_df



    #method to open file
    #return opened file with filename
    def openData(self, text_df):
        print(text_df)
        text_df['FileList'] = text_df.FileList.apply(lambda x: open(x, "r").read())
        text_df['FileList'] = text_df.FileList.apply(lambda x: ", ".join(x.split( )))
        return text_df



    #method to predict and output files
    #takes pickle files, data and outputdirectory as input and return dataframe
    def predict(self, pickleVectorizer, pickleModel, text_df, outputDir):
        vectorizer_pkl = open(pickleVectorizer, 'rb')
        vectorizer = pickle.load(vectorizer_pkl)

        logist_pkl = open(pickleModel, 'rb')
        logist = pickle.load(logist_pkl)
        
        X_test = vectorizer.transform(text_df.FileList)
        prediction = logist.predict(X_test)
        predictprobability = logist.predict_proba(X_test)[:, 1]

        documents = text_df.Filename.tolist()
        data_df = pd.DataFrame({'Filename': documents, 'Predictions': prediction, 'Prediction_Probability': predictprobability})
        data_df.to_csv(outputDir + 'AlcoholResult.csv', sep = '|', index = False)
        return data_df


if __name__ == "__main__":

    PD = ProcessData()

    """
    Change the inputDir and outputDir below. InputDir is where your input files exist, they should be text file such as .txt.
    A file named AlcoholResult will be created which will have filename and prediction result
    sep by |. 
    """

    inputDir = "/home/NLPShare/Opioid/Opioid_Annotated_Encounters/Data_CUIS/"
    outputDir = "/home/bsharma1/Alcohol/model/Output/"

    vectorizer = "Alcohol_Vectorizer.pkl"
    model = "Alcohol_logisticR_classifer.pkl"

    txtfilesTrain_df = PD.dffiles(inputDir)
    text_df = PD.openData(txtfilesTrain_df)
    data_df = PD.predict(vectorizer, model, text_df, outputDir)
    print("----------COMPLETED-----------")


        





