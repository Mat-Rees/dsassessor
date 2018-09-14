#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 11:08:55 2018

@author: mathewrees
"""

import json, traceback
import pandas as pd
import re, requests
from pandas.io.json import json_normalize





class JsonParserComplex():
    
    def __init__(self):
        
        self.masterDF = pd.DataFrame()
        self.processStatus = "Active"
        
        
    
    def processManager(self, jString):
        
        DF = JsonParserComplex.treatAndFlatten(self, jString)
        print("OUTPUT FROM FIRST FLATTEN")
        print(DF)
        
        while self.processStatus == "Active":
            
            col, cellVal, instructionInt = JsonParserComplex.checkColumnTypes(self, DF)
            print("col: {0}, val: {1} and type {3}, Instruction Integer: {2}".format(col, cellVal, instructionInt, type(cellVal)))
            
            
            if instructionInt == 0:
                print("Json is flattened, ending process")
                self.processStatus = "Off"
                
            
            elif instructionInt == 1:
                DF = JsonParserComplex.processListOfOneJson(self, col, cellVal)
                
                
            elif instructionInt == 2:
                print("DOING MANY JSON SUBPROCESS")
                DF = JsonParserComplex.processListOfManyJson(self, col, cellVal)
                break
                
                
                
            
        # elif instructionInt = 1: do subprocess
        # elif instructionInt = 2: do subprocess
        # elif inst.... etc
        print('Result Int is: {0}:'.format(instructionInt))
        return DF
    
    
    
    
    # Takes a jsonString, makes a Dataframe and appends it to the master
    # The first step executes this
    # Other steps will use this method, but will need to regenerate column names
    # before appending it to the master dataframe
    def treatAndFlatten(self, jString):
        treatedString = JsonParserComplex.pretreatJsonString(self, jString)
        tempDF = JsonParserComplex.tryFlatten(self, treatedString)
        self.masterDF = self.masterDF.append(tempDF)
        DF = self.masterDF.append(tempDF)
        return DF
    
    
    def tryFlatten(self, treatedString):
        jsonObj = json.loads(treatedString)
        DF = json_normalize(jsonObj)
        return DF
    
    
    # Replaces empty jsons and empty arrays
    def pretreatJsonString(self, jsonString):
        treatedString = jsonString.replace('\n', ' ')
        treatedString = treatedString.replace("{}", "\"Nan\"")
        treatedString = treatedString.replace("[]", "\"Nan\"")
        #treatedString = treatedString.replace(r'""', "\"Nan\"")
        return treatedString
    
    
    
    def checkColumnTypes(self, DF):
        
        
        print("Checking DataFrame Column's data types")
        print(type(DF))
        if DF is None:
            print("THIS IS A NONE TYPE")
            return 4
        else:
            for column in DF.columns:
                print(type(DF.iloc[0][column]))
                elementVal = DF.iloc[0][column]
                elementDataType = type(elementVal)
                
                
                if elementDataType is list:
                    if len(elementVal) == 1:
                        print("Dataframe contains a list of with single json, sending to subprocess")
                        return column, DF, 1 # More Processing
                    
                    elif len(elementVal) > 1 and type(elementVal[0]) is dict:
                        print("Dataframe contains a list of jsons, sending to subprocess")
                        return column, DF, 2
                    
                    elif len(elementVal) > 1 and type(elementVal[0]) is str:
                        print("Dataframe contains a list of strings, sending to subprocess")
                        return column, DF, 3
                
                else:   
                    return column, DF, 0 
                
        
    
    def processListOfOneJson(self, originCol, oneJson):
        # for singe json
        print("Run the pretreatment and tryFlatten")
        print("val is: {0} ".format(oneJson))
        newDF = json_normalize(oneJson.iloc[0][originCol])
        print(newDF)
        # Create a dict for updating then update the column headers using this dictionary
        # Append the new column headers to the original column header for a more consistent index
        colList = newDF.columns.tolist()
        print("colList is: {0}".format(colList))
        
        preString = "{0}.".format(originCol)
        newColList = [preString + item for item in colList]
        columnSwap = dict(zip(colList, newColList))
        updatedDF = newDF.rename(index=str, columns=columnSwap)
        
        print("PRINT MASTER DF")
        print(self.masterDF)
        
        DF = self.masterDF
        print(DF.index)
        DF.to_csv('DF.csv')
        updatedDF.to_csv('updatedDF.csv')
        
        print(updatedDF.index)
        
        # DF = DF.drop(originCol, axis=1)
        DF.index = updatedDF.index
        # DF.index = updatedDF.index
        
        expandedDF = pd.concat([DF,updatedDF], axis=1)
        expandedDF = expandedDF.drop(originCol, axis=1)
        
        # self.masterDF = self.masterDF.drop(col, axis=1)
        DF = expandedDF
        # expandedDF.to_csv("output.csv")
        # make the new, expanded dataframe
        # 
        self.masterDF = DF
        self.masterDF.to_csv('masterDF.csv')
        print("checkpoint: processManager with instructionInt = 1")
        print(self.masterDF)
        return DF
 
    
    
    def processListOfManyJson(self, originCol, jsonList):
        # loop through all the items in the list and do a Json_Normalize
        # Json_Normalize should then be replaced with 
        extractedVal = jsonList.iloc[0][originCol]
        
        for item in extractedVal:
            
            df = json_normalize(item)
            self.masterDF = self.masterDF.append(df)
            print(self.masterDF)
        
        
        
    def processListOfStrings():
        return DF
        
    def processListOfLists():
        return DF
    
    

    
    def addColumnNameDetails(self):
        return "?"
    
    def addColumns(self, inDF):
        return outDF
    
    def addRows(self, inDF):
        return outDF

'''
url = 'https://api.foursquare.com/v2/venues/explore'

params = dict(client_id='QP4KVGMOART2DB3ND34KXJSWUTZWZIJ51XZPSZA1QCTTAAJ1', 
              client_secret='SWZYXF14SYBUZSDA1JQ03E2C2VGISDHKYMVKZPCKERC5FPBQ',
              v='20180323',
              ll='51.51399612,-0.122826455',
              radius = '5000',
              query='coffee',
              limit=3)
        
resp = requests.get(url=url, params=params)

jpc = JsonParserComplex()
treatedString = jpc.pretreatJsonString(resp.text)
DF = jpc.tryFlatten(treatedString)
'''