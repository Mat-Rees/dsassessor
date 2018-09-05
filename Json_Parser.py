#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 11:08:55 2018

@author: mathewrees
"""

import json
import pandas as pd
import jsonpickle
from pandas.io.json import json_normalize


class JsonParser():
    
    #def __init__(self):
        # self.heDataFrame = None
        #self.processStatus = "on"
        
    # Converts Json String to Json
    # Won't use this as this is what json.loads does!
    def getValTest(self, jsonString):
        jsonRes = json.loads(jsonString)
        a = jsonRes["meta"]["total-pages"]
        # print (json["meta"]["total-pages"])
        return a
    
  
    # First Stage Flattening:
    # Takes a json response (as json object) and creates a flattened dataframe
    def firstFlattening(self, jsonInput):
        
        print("*****Datatype getting flattened is: {0}".format(type(jsonInput)))
        if isinstance(jsonInput, str):
            try:
                jsonObj = json.loads(jsonInput)
                flatdata = json_normalize(jsonObj)
                return flatdata
                
            except json.decoder.JSONDecodeError:
            
                print("More than one JSON object in the array")
                eachJsonDF = pd.DataFrame()
                # itemCounter = 0
                for eachJsonObject in jsonInput:
                    jsonObj = json.loads(eachJsonObject)
                    thisJsonDF = JsonParser.flattenJsonProcess(self, jsonObj)
                    eachJsonDF.append(thisJsonDF)
                    eachJsonDF.to_csv("testing_eachJsonDF.csv")
                flatdata = eachJsonDF
                return flatdata
            
        elif isinstance(jsonInput, dict):
            jsonObj = jsonInput
        
            flatdata = json_normalize(jsonObj)
            return flatdata
    
    

    # Further Flattening
    # Check the data-type of elements
    # If it's a dict (or array in Javascript notation),
    # flatten it again and rejoin the new dataframe to the existing data frame
    # with ammended titles to maintain the data's fully qualified column name
    def flatteningLoop(self, inputDF):
        
        for column in inputDF.columns:
            #print(type(inputDF.iloc[0][column]))
            elementVal = inputDF.iloc[0][column]
            elementDataType = type(elementVal)
           
            if elementDataType is list and len(elementVal) is 1:
                print("'{0}' column is a list that needs further flattening".format(column))
                # make the 1-element list into a dataframe
                
                nextDF = json_normalize(elementVal[0])
                # Create a dict for updating then update the column headers using this dictionary
                # Append the new column headers to the original column header for a more consistent index
                colList = nextDF.columns.tolist()
                preString = "{0}.".format(column)
                newColList = [preString + item for item in colList]
                columnSwap = dict(zip(colList, newColList))
                updatedDF = nextDF.rename(index=str, columns=columnSwap)
                inputDF.index = updatedDF.index
                expandedDF = pd.concat([inputDF,updatedDF], axis=1)
                expandedDF = expandedDF.drop(column, axis=1)
                # expandedDF.to_csv("output.csv")
                # make the new, expanded dataframe
                inputDF = expandedDF
                
            if elementDataType is list and len(elementVal) > 1:
                print("THE LIST IS MORE THAN 1 ITEM")
                # Make a new dataframe; load the multi-item list into it item-by-item
                masterDataFrame = pd.DataFrame()
              
                for item in elementVal:
                    oneDataFrame = self.flattenJsonProcess(item)
                    masterDataFrame.append(oneDataFrame)
                    masterDataFrame.to_csv("testingListDF.csv")
                    print(masterDataFrame)
                
                print(len(elementVal))
                return masterDataFrame
        
        return inputDF
        
     
        
    def checkColumnTypes(self, inputDF):
        print("Checking DataFrame Column's data types")
        print(type(inputDF))
        if (type(inputDF)) is None:
            print("THIS ISNT A TYPE ")
        
        for column in inputDF.columns:
            print(type(inputDF.iloc[0][column]))
            elementVal = inputDF.iloc[0][column]
            elementDataType = type(elementVal)
            
            if elementDataType is list:
                return 0
        return 1
    
            
    
    def checkAndLoop(self, inputDF):
        moreFlattening = JsonParser.checkColumnTypes(self, inputDF)
        if moreFlattening == 0:
            print("needs more flattening")
            outputDF = JsonParser.flatteningLoop(self, inputDF)
            outputDF.to_csv('testDFout.csv')
            return outputDF, "active"
        else:
            print("done")
            return inputDF, "done"
            
        
        
    def flattenJsonProcess(self, jsonInput):
        # self.processStatus = "on"
        mainDF = JsonParser.firstFlattening(self, jsonInput)
        loopingStatus = "active"
        while loopingStatus == "active":
            outputDF, loopingStatus = JsonParser.checkAndLoop(self, mainDF)
            mainDF = outputDF
            if loopingStatus == "done":
                break
            
        return mainDF
            

  
jString = """
            {
              "meta": {
                "total-pages": 13
              },
              "data": [
                {
                  "type": "articles",
                  "id": "3",
                  "attributes": {
                    "title": "JSON API paints my bikeshed!",
                    "body": "The shortest article. Ever.",
                    "created": "2015-05-22T14:56:29.000Z",
                    "updated": "2015-05-22T14:56:28.000Z"
                  }
                }
              ],
              "links": {
                "self": "http://example.com/articles?page[number]=3&page[size]=1",
                "first": "http://example.com/articles?page[number]=1&page[size]=1",
                "prev": "http://example.com/articles?page[number]=2&page[size]=1",
                "next": "http://example.com/articles?page[number]=4&page[size]=1",
                "last": "http://example.com/articles?page[number]=13&page[size]=1"
              }
            }
              """
        
jp = JsonParser()
resultDF = jp.flattenJsonProcess(jString)
resultDF.to_csv("output.csv")
print(resultDF)

'''
jp = JsonParser()
flatdata = jp.firstFlattening(jString)
flatterDF = jp.flatteningLoop(flatdata)
flatterDF.to_csv("output.csv")

print(flatterDF)

  '''      

