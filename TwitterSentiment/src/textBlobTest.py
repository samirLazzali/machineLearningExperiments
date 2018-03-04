#!/usr/bin/env python
# -*- coding: utf-8 -*-

from textblob import TextBlob
#pip install -U textblob-fr
#http://textblob.readthedocs.io/en/dev/quickstart.html


text = '''
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
'''

#blob = TextBlob(text)
#blob.tags           
#blob.noun_phrases 

testimonial = TextBlob(text)
#print testimonial.sentiment.polarity

for sentence in testimonial.sentences:
    #print ("\n"+str(sentence))
    print sentence.sentiment #.polarity


doc =  '''
The sentiment property returns a namedtuple of the form Sentiment(polarity, subjectivity). 
The polarity score is a float within the range [-1.0, 1.0]. 
The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.
'''
#print doc

print ("Tests gry sentence :")
testsAngry = TextBlob('''
Keep net neutrality or face the wrath of millions if not billions of angry Americans, Africans, Europeans, Asians and Australians. You are the biggest evil orginasation since the Nazis. Not in my lifetime have I ever seen a force so evil itcould unite the whole world against it. I mean at least Hitler had alies, if you destroy net neutrality then even Google will start fighting you. Go back to your death star concentration camp you sith nazis.	'''	)
print testsAngry.sentiment

######################################################################################
#	Test testblob in French
######################################################################################
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer

tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())

blob1 = tb(u"Quelle belle matinée")
print blob1.sentiment
#(0.8, 0.8)

blob2 = tb(u"C'est une voiture terribles.")
print blob2.sentiment
#(-0.7, 0.6)
