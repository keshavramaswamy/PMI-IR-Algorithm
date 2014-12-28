from __future__ import division
import urllib
import json
from math import log


def hits(word1,word2=""):
    query = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=%s"
    if word2 == "":
        results = urllib.urlopen(query % word1)
    else:
        results = urllib.urlopen(query % word1+" "+"AROUND(10)"+" "+word2)
    json_res = json.loads(results.read())
    google_hits=int(json_res['responseData']['cursor']['estimatedResultCount'])
    return google_hits


def so(phrase):
    num = hits(phrase,"excellent")
    #print num
    den = hits(phrase,"poor")
    #print den
    ratio = num / den
    #print ratio
    sop = log(ratio)
    return sop

input_phrase = raw_input("Enter Input Phrase")

print so(input_phrase)