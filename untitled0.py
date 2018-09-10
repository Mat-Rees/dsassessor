#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json, re

from Json_Parser import JsonParser

from pandas.io.json import json_normalize
"""
from pandas.io.json import json_normalize
Created on Thu Sep  6 09:34:32 2018

@author: mathewrees
"""
# before processing:

theString = r'''
{"meta":{"code":200,"requestId":"5b90e6544434b96363a0aa7b"},"response":{"suggestedFilters":{"header":"Tap to show:","filters":[{"name":"Open now","key":"openNow"}]"},"warning":{"text":"There aren't a lot of results for \"coffee.\" Try something more general, reset your filters, or expand the search area."},"headerLocation":"London","headerFullLocation":"London","headerLocationGranularity":"city","query":"coffee","totalResults":250,"suggestedBounds":{"ne":{"lat":51.558996165000046,"lng":-0.05065172783334977},"sw":{"lat":51.46899607499996,"lng":-0.19500118216665024}},"groups":[{"type":"Recommended Places","name":"recommended","items":[{"reasons":{"count":0,"items":[{"summary":"This spot is popular","type":"general","reasonName":"globalInteractionReason"}]"},"venue":{"id":"4ac518edf964a520c1ac20e3","name":"Monmouth Coffee Company","contact":"Nan","location":{"address":"27 Monmouth St","lat":51.514314,"lng":-0.126824,"labeledLatLngs":[{"label":"display","lat":51.514314,"lng":-0.126824}]","distance":279,"postalCode":"WC2H 9EU","cc":"GB","city":"Holborn and Covent Garden","state":"Greater London","country":"United Kingdom","formattedAddress":"["27 Monmouth St","Holborn and Covent Garden","Greater London","WC2H 9EU","United Kingdom"]"},"categories":[{"id":"4bf58dd8d48988d1e0931735","name":"Coffee Shop","pluralName":"Coffee Shops","shortName":"Coffee Shop","icon":{"prefix":"https:\/\/ss3.4sqi.net\/img\/categories_v2\/food\/coffeeshop_","suffix":".png"},"primary":true}]","verified":false,"stats":{"tipCount":0,"usersCount":0,"checkinsCount":0,"visitsCount":0},"beenHere":{"count":0,"lastCheckinExpiredAt":0,"marked":false,"unconfirmedCount":0},"photos":{"count":0,"groups":"Nan"},"hereNow":{"count":0,"summary":"Nobody here","groups":"Nan"}},"referralId":"e-0-4ac518edf964a520c1ac20e3-0"},{"reasons":{"count":0,"items":[{"summary":"This spot is popular","type":"general","reasonName":"globalInteractionReason"}]"},"venue":{"id":"5551ea51498eb30c143b565e","name":"The Black Penny","contact":"Nan","location":{"address":"34 Great Queen St","lat":51.51519097792153,"lng":-0.12154506230333152,"labeledLatLngs":[{"label":"display","lat":51.51519097792153,"lng":-0.12154506230333152}]","distance":159,"postalCode":"WC2B 5AA","cc":"GB","city":"London","state":"Greater London","country":"United Kingdom","formattedAddress":"["34 Great Queen St","London","Greater London","WC2B 5AA","United Kingdom"]"},"categories":[{"id":"4bf58dd8d48988d1e0931735","name":"Coffee Shop","pluralName":"Coffee Shops","shortName":"Coffee Shop","icon":{"prefix":"https:\/\/ss3.4sqi.net\/img\/categories_v2\/food\/coffeeshop_","suffix":".png"},"primary":true}]","verified":false,"stats":{"tipCount":0,"usersCount":0,"checkinsCount":0,"visitsCount":0},"beenHere":{"count":0,"lastCheckinExpiredAt":0,"marked":false,"unconfirmedCount":0},"photos":{"count":0,"groups":"Nan"},"hereNow":{"count":0,"summary":"Nobody here","groups":"Nan"}},"referralId":"e-0-5551ea51498eb30c143b565e-1"},{"reasons":{"count":0,"items":[{"summary":"This spot is popular","type":"general","reasonName":"globalInteractionReason"}]"},"venue":{"id":"4b2a3cc8f964a52061a624e3","name":"The Tea House","contact":"Nan","location":{"address":"15 Neal Street","crossStreet":"Long Acre","lat":51.51362061083395,"lng":-0.12464211361385549,"labeledLatLngs":[{"label":"display","lat":51.51362061083395,"lng":-0.12464211361385549}]","distance":132,"postalCode":"WC2H 9PU","cc":"GB","city":"Covent Garden","state":"Greater London","country":"United Kingdom","formattedAddress":"["15 Neal Street (Long Acre)","Covent Garden","Greater London","WC2H 9PU","United Kingdom"]"},"categories":[{"id":"4bf58dd8d48988d1dc931735","name":"Tea Room","pluralName":"Tea Rooms","shortName":"Tea Room","icon":{"prefix":"https:\/\/ss3.4sqi.net\/img\/categories_v2\/food\/tearoom_","suffix":".png"},"primary":true}]","verified":false,"stats":{"tipCount":0,"usersCount":0,"checkinsCount":0,"visitsCount":0},"beenHere":{"count":0,"lastCheckinExpiredAt":0,"marked":false,"unconfirmedCount":0},"photos":{"count":0,"groups":"Nan"},"hereNow":{"count":0,"summary":"Nobody here","groups":"Nan"}},"referralId":"e-0-4b2a3cc8f964a52061a624e3-2"}]"}]"}}
'''
#jsonOb = json.loads(theString)
#print(json.dumps(jsonOb, indent=4, sort_keys=True))


# after processing

otherString = '''
{"meta":{"code":200,"requestId":"5b90e6ad351e3d44524f911d"},"response":{"suggestedFilters":{"header":"Tap to show:","filters":[{"name":"Open now","key":"openNow"}]},"warning":{"text":"There aren't a lot of results for \"coffee.\" Try something more general, reset your filters, or expand the search area."},"headerLocation":"London","headerFullLocation":"London","headerLocationGranularity":"city","query":"coffee","totalResults":250,"suggestedBounds":{"ne":{"lat":51.558996165000046,"lng":-0.05065172783334977},"sw":{"lat":51.46899607499996,"lng":-0.19500118216665024}},"groups":[{"type":"Recommended Places","name":"recommended","items":[{"reasons":{"count":0,"items":[{"summary":"This spot is popular","type":"general","reasonName":"globalInteractionReason"}]},"venue":{"id":"4ac518edf964a520c1ac20e3","name":"Monmouth Coffee Company","contact":{},"location":{"address":"27 Monmouth St","lat":51.514314,"lng":-0.126824,"labeledLatLngs":[{"label":"display","lat":51.514314,"lng":-0.126824}],"distance":279,"postalCode":"WC2H 9EU","cc":"GB","city":"Holborn and Covent Garden","state":"Greater London","country":"United Kingdom","formattedAddress":["27 Monmouth St","Holborn and Covent Garden","Greater London","WC2H 9EU","United Kingdom"]},"categories":[{"id":"4bf58dd8d48988d1e0931735","name":"Coffee Shop","pluralName":"Coffee Shops","shortName":"Coffee Shop","icon":{"prefix":"https:\/\/ss3.4sqi.net\/img\/categories_v2\/food\/coffeeshop_","suffix":".png"},"primary":true}],"verified":false,"stats":{"tipCount":0,"usersCount":0,"checkinsCount":0,"visitsCount":0},"beenHere":{"count":0,"lastCheckinExpiredAt":0,"marked":false,"unconfirmedCount":0},"photos":{"count":0,"groups":[]},"hereNow":{"count":0,"summary":"Nobody here","groups":[]}},"referralId":"e-0-4ac518edf964a520c1ac20e3-0"},{"reasons":{"count":0,"items":[{"summary":"This spot is popular","type":"general","reasonName":"globalInteractionReason"}]},"venue":{"id":"5551ea51498eb30c143b565e","name":"The Black Penny","contact":{},"location":{"address":"34 Great Queen St","lat":51.51519097792153,"lng":-0.12154506230333152,"labeledLatLngs":[{"label":"display","lat":51.51519097792153,"lng":-0.12154506230333152}],"distance":159,"postalCode":"WC2B 5AA","cc":"GB","city":"London","state":"Greater London","country":"United Kingdom","formattedAddress":["34 Great Queen St","London","Greater London","WC2B 5AA","United Kingdom"]},"categories":[{"id":"4bf58dd8d48988d1e0931735","name":"Coffee Shop","pluralName":"Coffee Shops","shortName":"Coffee Shop","icon":{"prefix":"https:\/\/ss3.4sqi.net\/img\/categories_v2\/food\/coffeeshop_","suffix":".png"},"primary":true}],"verified":false,"stats":{"tipCount":0,"usersCount":0,"checkinsCount":0,"visitsCount":0},"beenHere":{"count":0,"lastCheckinExpiredAt":0,"marked":false,"unconfirmedCount":0},"photos":{"count":0,"groups":[]},"hereNow":{"count":0,"summary":"Nobody here","groups":[]}},"referralId":"e-0-5551ea51498eb30c143b565e-1"},{"reasons":{"count":0,"items":[{"summary":"This spot is popular","type":"general","reasonName":"globalInteractionReason"}]},"venue":{"id":"4b2a3cc8f964a52061a624e3","name":"The Tea House","contact":{},"location":{"address":"15 Neal Street","crossStreet":"Long Acre","lat":51.51362061083395,"lng":-0.12464211361385549,"labeledLatLngs":[{"label":"display","lat":51.51362061083395,"lng":-0.12464211361385549}],"distance":132,"postalCode":"WC2H 9PU","cc":"GB","city":"Covent Garden","state":"Greater London","country":"United Kingdom","formattedAddress":["15 Neal Street (Long Acre)","Covent Garden","Greater London","WC2H 9PU","United Kingdom"]},"categories":[{"id":"4bf58dd8d48988d1dc931735","name":"Tea Room","pluralName":"Tea Rooms","shortName":"Tea Room","icon":{"prefix":"https:\/\/ss3.4sqi.net\/img\/categories_v2\/food\/tearoom_","suffix":".png"},"primary":true}],"verified":false,"stats":{"tipCount":0,"usersCount":0,"checkinsCount":0,"visitsCount":0},"beenHere":{"count":0,"lastCheckinExpiredAt":0,"marked":false,"unconfirmedCount":0},"photos":{"count":0,"groups":[]},"hereNow":{"count":0,"summary":"Nobody here","groups":[]}},"referralId":"e-0-4b2a3cc8f964a52061a624e3-2"}]}]}}
'''


#TEXTO = 'testing this'
#my_regex = "r'" + otherString
#print(my_regex)
'''
jp = JsonParser()
newStr = jp.jsonPretreatment(otherString)
print(newStr)
trimStr = newStr[newStr.index('{'):]
print("!!!!!!!!!!!!!!!!")
print(trimStr)
print("OOOOOOOOOOOO")
# trim2 = trimStr[trimStr.rindex('}')+1:]
trim2 = trimStr[:trimStr.rindex('}')]
print(trim2)
trimr= 'r"""' + trim2 + '"""'
print("LLLLLLLLLLL")
print(trimr)
jsonOb2 = json.loads(trimr)
print(json.dumps(jsonOb2, indent=4, sort_keys=True))
'''
'''
test = str(['one', 'two', 'three'])
print(type(test))
print(len(test))
print(test)
'''

# test2 = [{'one':'1'}, {'two':'2'}]
test2 = [{"one":"1"}]
print(test2)
print(type(test2))
print(len(test2))
jtest = json_normalize(test2[0])
print(jtest)

'''
print("test[0] is: {0}".format(type(test[0])))
print("test2[0] is: {0}".format(type(test2[0])))
'''
