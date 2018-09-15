import FeatureExtractor

ourFileName = "../Articles/1000_1.txt"
featureVector = FeatureExtractor.createFeatureVector(ourFileName)
normalizedVector = FeatureExtractor.normalize(featureVector)

i = 32
for num in normalizedVector:
    print (str(i) + " - " + str(num))
    i += 1

#frequencyVector = termFrequency(featureVector)
