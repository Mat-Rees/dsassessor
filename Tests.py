# -*- coding: utf-8 -*-
"""
Tests for Automated Json Parsing Script
"""

import unittest, requests, json
from Json_Parser import JsonParser as JsonParser
import jsonpickle as jpick
from pandas.io.json import json_normalize


# from JsonParser import getValTest

# print (os.getcwd())

class Tests(unittest.TestCase): 
    
    jsonString = """
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
              
    jsonString2 = """ [{"A": {"B": 1}}] """
    jsonString3 = """ {"dummy": [{"A": {"B": 1}}]} """
    jsonString4 = """ {"response": [{"nested_response": [{"second_nest": {"final": 1}}]}]}"""
    
    jsonString5 = """
            {
              "meta": {
                "total-pages": 13
              },
              "data": [a,
              b,
              c],
              "links": {}
            }
              """
    
    jp = JsonParser()
    '''
    def test_quick(self):    
        jsonString = self.jsonString
        a = self.jp.getValTest(jsonString)    
        self.assertEqual(a, 13)
        
        
    def test_firstFlatteningString(self):
        jsonString = self.jsonString
        print(jsonString)
        testDF = self.jp.firstFlattening(jsonString)
        self.assertEqual(type(testDF.iloc[0]['data']), list)
        self.assertEqual(type(testDF.iloc[0]['links.self']), str)
        self.assertEqual((testDF.iloc[0]['links.first']), 'http://example.com/articles?page[number]=1&page[size]=1')
        
    
    def test_flatteningLoopEx1(self):
        jsonString = self.jsonString
        testDF = self.jp.flattenJsonProcess(jsonString)
        print(testDF)
        
    def test_flatteningLoopEx2(self):
        jsonString = self.jsonString2
        testDF = self.jp.flattenJsonProcess(jsonString)
        print(testDF)
        
    def test_flatteningLoopEx3(self):
        jsonString = self.jsonString3
        testDF = self.jp.flattenJsonProcess(jsonString)
        print(testDF)
        
    def test_flatteningLoopEx4(self):
        jsonString = self.jsonString4
        testDF = self.jp.flattenJsonProcess(jsonString)
        print(testDF)
        '''
        
    def test_FourSquareJSON(self):
            
        url = 'https://api.foursquare.com/v2/venues/explore'

        params = dict(client_id='QP4KVGMOART2DB3ND34KXJSWUTZWZIJ51XZPSZA1QCTTAAJ1',
          client_secret='SWZYXF14SYBUZSDA1JQ03E2C2VGISDHKYMVKZPCKERC5FPBQ',
          v='20180323',
          #midpoint of coords
          ll='51.51399612,-0.122826455',
          # radius 5km from centre, based on coords
          radius = '5000',
          query='coffee',
          # 'rating' is an invisble parameter, can get this from venue details
          # https://developer.foursquare.com/docs/api/venues/details
          # assumed that results are ranked according to rating
          limit=3)
        
        resp = requests.get(url=url, params=params)
        json.loads(resp.text)
     
        stringInput = JsonParser.jsonPretreatment(self, resp.text)
        print(resp.text)
        
        '''
        print("TTTTTTTTTTTTTTTTT")
        print(stringInput)
        # print(json.dumps(resp.text, indent=4, sort_keys=True))
        # print(json.dumps(stringInput, indent=4, sort_keys=True))
        
        json.loads(stringInput)
        '''
        
        
        '''
        try: #try parsing to dict
            dataform = str(resp.text).strip("'<>() ").replace('\'', '\"')
            struct = json.loads(dataform)
        except:
            print (repr(resp.text))
            print (sys.exc_info())
        '''
    
            
        # data = json.loads(stringInput)
        # print (json.dumps(data, indent=4, sort_keys=True))
        #print("printing data!!!")
        #print(data)
        '''     
        testDF = self.jp.flattenJsonProcess(stringInput)
        testDF.to_csv('testDFoutFINALLY.csv')
        '''
        # Make a new dataframe; load the multi-item list into it item-by-item
        
        #print(testDF)
       
        """
        
    def test_jsonPretreatment(self):
        testString = self.jsonString5
        res = self.jp.jsonPretreatment(testString)
        
        # print(res)
        
    def test_jString5(self):
        testString = self.jsonString5
        treatedString = self.jp.jsonPretreatment(testString)
        testDF = self.jp.flattenJsonProcess(treatedString)
        print(testDF)
        
        """
        
if __name__ == '__main__':
    unittest.main()



    
    # json = json.loads(jsonString)
    # print (json["meta"]["total-pages"])
    

