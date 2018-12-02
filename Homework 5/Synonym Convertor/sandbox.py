import FileUtil
from PyDictionary import PyDictionary
from nltk.corpus import wordnet as wn
import nltk
import SynonymConvertor as sn

# fileName = "247Sports_McNair_ALAvsARK_wk6.txt"
# contents = FileUtil.readFile(fileName)
# print len(contents)

###############################################################################
# sentence = "The quick brown fox jumped over the lazy dog."
# syns = wn.synsets("program")
#
# for word in sentence.split():
#     print word
#
# # sentenceArr = sentence.split()
# # sentenceArr[0] = "AAAAAAA"
# # sentence = " ".join(sentenceArr)
# #
# # print sentence
# x = sn.getBestSynonym("good")
# print x
###############################################################################
# x = "The quick brown fox jumped over the lazy dog."
# y = sn.removeNonAscii(x)
# print x
# print y
###############################################################################
x = sn.getBestSynonym("now")
print x
