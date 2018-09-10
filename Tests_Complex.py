#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 17:41:19 2018

@author: mathewrees
"""

from Json_Parser_Complex import JsonParserComplex
import unittest

class TestsComplex(unittest.TestCase):
    
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
    jsonString5 = """ {"response": [{"nested_response": [{"second_nest": {"final": 1, "array":[]}}]}]}"""
    jsonString6 = """ {"response": [{"nestedresponse":[{"one":"1"}, {"two":"2"}]}]} """
    
    
    
    # jp = JsonParserComplex()
    '''
    def test_flatteningLoopEx1(self):
        jp = JsonParserComplex()
        jsonString = self.jsonString
        testDF = jp.processManager(jsonString)
        print(testDF)
    ''' 
    
    def test_flatteningLoopEx2(self):
        jp = JsonParserComplex()
        jsonString = self.jsonString2
        testDF = jp.processManager(jsonString)
        print(testDF)
        
  
    def test_flatteningLoopEx3(self):
        jp = JsonParserComplex()
        jsonString = self.jsonString3
        testDF = jp.processManager(jsonString)
        print(testDF)

        
    def test_flatteningLoopEx4(self):
        jp = JsonParserComplex()
        jsonString = self.jsonString4
        testDF = jp.processManager(jsonString)
        print(testDF)
    

    def test_flatteningLoopEx5(self):
        jp = JsonParserComplex()
        jsonString = self.jsonString5
        testDF = jp.processManager(jsonString)
        print(testDF)
    
 
    def test_flatteningLoopEx6(self):
        jp = JsonParserComplex()
        jsonString = self.jsonString6
        testDF = jp.processManager(jsonString)
        print(testDF)
 
        
if __name__ == '__main__':
    unittest.main()

    