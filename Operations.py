class Operations:
    def plotNormalTokenVsVocabularySizeForOne(self, Corpora1):
        import matplotlib.pyplot as plt
        plt.xlabel('Number of Tokens in Corpora')
        plt.ylabel('Number of Types')
        plt.title("Token vs Type Size")

        import math
        x = []
        y = []
        for i in range(math.floor(len(Corpora1) / 10000)):
            x.append(10000 * (i + 1))
            y.append(len(self.countTypeFrequencies(Corpora1[1:10000 * (i + 1)])))
        print("x = ", x)
        print("\n")
        print("y = ", y)
        plt.plot(x, y, "r")
        plt.show()


    def plotLogTokenVsVocabularySizeForOne(self, Corpora1, showBestFitLine):
        import matplotlib.pyplot as plt
        import numpy
        plt.xlabel('Log (Number of Tokens in Corpora)')
        plt.ylabel('Log (Number of Types)')
        plt.title("Token vs Type Size")
        import math
        x = []
        y = []
        for i in range(1, math.floor(len(Corpora1)/10000)):
            x.append(10000*(i+1))
            y.append(len(self.countTypeFrequencies(Corpora1[1:10000*(i+1)])))
        print("x = " , x)
        print("\n")
        print("y = ", y)
        plt.plot(numpy.log(x), numpy.log(y), "r--")
        if showBestFitLine:
            x = numpy.array(x)
            y = numpy.array(y)
            m, b = numpy.polyfit(numpy.log(x), numpy.log(y), 1)
            plt.plot(numpy.log(x), m*numpy.log(x)+b, "r", label = "Best Fitting Line. Slope is: " + str(round(m,4)))
        plt.show()


    def plotLogZipfsForOne(self, TypeFrequencies1):
        import numpy
        freqArray = []
        for letter, count in TypeFrequencies1.most_common(len(TypeFrequencies1)):
            freqArray.append(count)
        x = []
        y = []
        import matplotlib.pyplot as plt
        plt.figure(2)
        for i in range(1, len(freqArray)):
            x.append(i)
            y.append(freqArray[i])
        plt.xlabel('log(Rank of Type)')
        plt.ylabel('log(Frequency)')
        plt.title("Zipf's Law Plot")
        plt.plot(numpy.log(x), numpy.log(y), 'g')
        plt.show()

    def plotNormalZipfsForOne(self, TypeFrequencies1 ):

      import math
      freqArray = []
      for letter, count in TypeFrequencies1.most_common(len(TypeFrequencies1)):
          freqArray.append(count)
      x = []
      y = []
      import matplotlib.pyplot as plt
      plt.figure(1)
      for i in range(1, math.floor(len(freqArray)/300)):
          x.append(i)
          y.append(freqArray[i])
      plt.xlabel('Rank of Type')
      plt.ylabel('Frequency')
      plt.title("Zipf's Law Plot")
      plt.plot(x, y, 'g' )
      plt.show()

    def createRandomText(self):
        import string
        import random
        from random import seed
        from random import randint
        seed(1)

        numberOfWords = 1500000
        maxNumberofLettersInaWord = 4

        text = ""

        for i in range(numberOfWords):
                numberOfLetters = randint(1, maxNumberofLettersInaWord)
                text = text + " " + str(''.join(random.choices(string.ascii_uppercase +
                                               string.digits, k=numberOfLetters)))

        return text

    def plotLogTokenVsVocabularySizeForNine(self, Corpora1, Corpora2, Corpora3,Corpora4, Corpora5, Corpora6,
                                            Corpora7, Corpora8, Corpora9,
                                            Corpora1Name, Corpora2Name, Corpora3Name , showBestFitLine):
        import matplotlib.pyplot as plt
        import numpy

        plt.xlabel('Log (Number of Tokens in Corpora)')
        plt.ylabel('Log (Number of Types)')
        plt.title("Token vs Type Size")

        import math
        x = []
        y = []
        for i in range(1, math.floor(len(Corpora1)/10000)):
            x.append(10000*(i+1))
            y.append(len(self.countTypeFrequencies(Corpora1[1:10000*(i+1)])))
        print("x = " , x)
        print("\n")
        print("y = ", y)
        plt.plot(numpy.log(x), numpy.log(y), "r--", label = Corpora1Name + " - Idiot")
        if showBestFitLine:
            x = numpy.array(x)
            y = numpy.array(y)
            m, b = numpy.polyfit(numpy.log(x), numpy.log(y), 1)
            plt.plot(numpy.log(x), m * numpy.log(x) + b, "r",label = "Best Fitting Line. Slope is: " + str(round(m,4)))

        x = []
        y = []
        for i in range(1, math.floor(len(Corpora2)/10000)):
            x.append(10000*(i+1))
            y.append(len(self.countTypeFrequencies(Corpora2[1:10000*(i+1)])))
        print("x = " , x)
        print("\n")
        print("y = " , y)
        plt.plot(numpy.log(x), numpy.log(y), "r.", label = Corpora1Name + " - Karamazov Brothers")
        if showBestFitLine:
            x = numpy.array(x)
            y = numpy.array(y)
            m, b = numpy.polyfit(numpy.log(x), numpy.log(y), 1)
            plt.plot(numpy.log(x), m * numpy.log(x) + b, "r",label = "Best Fitting Line. Slope is: " + str(round(m,4)))

        x = []
        y = []
        for i in range(1, math.floor(len(Corpora3)/10000)):
            x.append(10000*(i+1))
            y.append(len(self.countTypeFrequencies(Corpora3[1:10000*(i+1)])))
        print("x = " , x)
        print("\n")
        print("y = " , y)
        plt.plot(numpy.log(x), numpy.log(y), "r*", label = Corpora1Name + " - Possessed")
        if showBestFitLine:
            x = numpy.array(x)
            y = numpy.array(y)
            m, b = numpy.polyfit(numpy.log(x), numpy.log(y), 1)
            plt.plot(numpy.log(x), m * numpy.log(x) + b, "r",label = "Best Fitting Line. Slope is: " + str(round(m,4)))

        x = []
        y = []
        for i in range(1, math.floor(len(Corpora4) / 10000)):
            x.append(10000 * (i + 1))
            y.append(len(self.countTypeFrequencies(Corpora4[1:10000 * (i + 1)])))
        print("x = ", x)
        print("\n")
        print("y = ", y)
        plt.plot(numpy.log(x), numpy.log(y), "g--", label=Corpora2Name + " - Bleak House")
        if showBestFitLine:
            x = numpy.array(x)
            y = numpy.array(y)
            m, b = numpy.polyfit(numpy.log(x), numpy.log(y), 1)
            plt.plot(numpy.log(x), m * numpy.log(x) + b, "g",label = "Best Fitting Line. Slope is: " + str(round(m,4)))

        x = []
        y = []
        for i in range(1, math.floor(len(Corpora5) / 10000)):
            x.append(10000 * (i + 1))
            y.append(len(self.countTypeFrequencies(Corpora5[1:10000 * (i + 1)])))
        print("x = ", x)
        print("\n")
        print("y = ", y)
        plt.plot(numpy.log(x), numpy.log(y), "g.", label=Corpora2Name + " - Dombey & Son")
        if showBestFitLine:
            x = numpy.array(x)
            y = numpy.array(y)
            m, b = numpy.polyfit(numpy.log(x), numpy.log(y), 1)
            plt.plot(numpy.log(x), m * numpy.log(x) + b, "g",label = "Best Fitting Line. Slope is: " + str(round(m,4)))

        x = []
        y = []
        for i in range(1, math.floor(len(Corpora6) / 10000)):
            x.append(10000 * (i + 1))
            y.append(len(self.countTypeFrequencies(Corpora6[1:10000 * (i + 1)])))
        print("x = ", x)
        print("\n")
        print("y = ", y)
        plt.plot(numpy.log(x), numpy.log(y), "g*", label=Corpora2Name + " - Our Mutual Friend" )
        if showBestFitLine:
            x = numpy.array(x)
            y = numpy.array(y)
            m, b = numpy.polyfit(numpy.log(x), numpy.log(y), 1)
            plt.plot(numpy.log(x), m * numpy.log(x) + b, "g",label = "Best Fitting Line. Slope is: " + str(round(m,4)))

        x = []
        y = []
        for i in range(1, math.floor(len(Corpora7) / 10000)):
            x.append(10000 * (i + 1))
            y.append(len(self.countTypeFrequencies(Corpora7[1:10000 * (i + 1)])))
        print("x = ", x)
        print("\n")
        print("y = ", y)
        plt.plot(numpy.log(x), numpy.log(y), "b--", label=Corpora3Name + " - Anna Karenine")
        if showBestFitLine:
            x = numpy.array(x)
            y = numpy.array(y)
            m, b = numpy.polyfit(numpy.log(x), numpy.log(y), 1)
            plt.plot(numpy.log(x), m * numpy.log(x) + b, "b",label = "Best Fitting Line. Slope is: " + str(round(m,4)))

        x = []
        y = []
        for i in range(1, math.floor(len(Corpora8) / 10000)):
            x.append(10000 * (i + 1))
            y.append(len(self.countTypeFrequencies(Corpora8[1:10000 * (i + 1)])))
        print("x = ", x)
        print("\n")
        print("y = ", y)
        plt.plot(numpy.log(x), numpy.log(y), "b.", label=Corpora3Name + " - Resurrection")
        if showBestFitLine:
            x = numpy.array(x)
            y = numpy.array(y)
            m, b = numpy.polyfit(numpy.log(x), numpy.log(y), 1)
            plt.plot(numpy.log(x), m * numpy.log(x) + b, "b",label = "Best Fitting Line. Slope is: " + str(round(m,4)))

        x = []
        y = []
        for i in range(1, math.floor(len(Corpora9) / 10000)):
            x.append(10000 * (i + 1))
            y.append(len(self.countTypeFrequencies(Corpora9[1:10000 * (i + 1)])))
        print("x = ", x)
        print("\n")
        print("y = ", y)
        plt.plot(numpy.log(x), numpy.log(y), "b*", label=Corpora3Name + " - War & Peace")
        if showBestFitLine:
            x = numpy.array(x)
            y = numpy.array(y)
            m, b = numpy.polyfit(numpy.log(x), numpy.log(y), 1)
            plt.plot(numpy.log(x), m*numpy.log(x)+b, "b",label = "Best Fitting Line. Slope is: " + str(round(m,4)))

        plt.legend()
        plt.show()



    def plotLogTokenVsVocabularySizeForThree(self, Corpora1, Corpora2, Corpora3, Corpora1Name,
                                             Corpora2Name, Corpora3Name, showBestFitLine):
        import matplotlib.pyplot as plt
        import numpy

        plt.xlabel('Log (Number of Tokens in Corpora)')
        plt.ylabel('Log (Number of Types)')
        plt.title("Token vs Type Size")

        import math
        x = []
        y = []
        for i in range(1, math.floor(len(Corpora1)/10000)):
            x.append(10000*(i+1))
            y.append(len(self.countTypeFrequencies(Corpora1[1:10000*(i+1)])))
        print("x = " , x)
        print("\n")
        print("y = ", y)
        plt.plot(numpy.log(x), numpy.log(y), "r--", label = Corpora1Name)
        if showBestFitLine:
            x = numpy.array(x)
            y = numpy.array(y)
            m, b = numpy.polyfit(numpy.log(x), numpy.log(y), 1)
            plt.plot(numpy.log(x), m*numpy.log(x)+b, "r", label = "Best Fitting Line. Slope is: " + str(round(m,4)))

        x = []
        y = []
        for i in range(1, math.floor(len(Corpora2)/10000)):
            x.append(10000*(i+1))
            y.append(len(self.countTypeFrequencies(Corpora2[1:10000*(i+1)])))
        print("x = " , x)
        print("\n")
        print("y = " , y)
        plt.plot(numpy.log(x), numpy.log(y), "g--", label = Corpora2Name)
        if showBestFitLine:
            x = numpy.array(x)
            y = numpy.array(y)
            m, b = numpy.polyfit(numpy.log(x), numpy.log(y), 1)
            plt.plot(numpy.log(x), m*numpy.log(x)+b, "g", label = "Best Fitting Line. Slope is: " + str(round(m,4)))

        x = []
        y = []
        for i in range(1, math.floor(len(Corpora3)/10000)):
            x.append(10000*(i+1))
            y.append(len(self.countTypeFrequencies(Corpora3[1:10000*(i+1)])))
        print("x = " , x)
        print("\n")
        print("y = " , y)
        plt.plot(numpy.log(x), numpy.log(y), "b--", label = Corpora3Name)
        if showBestFitLine:
            x = numpy.array(x)
            y = numpy.array(y)
            m, b = numpy.polyfit(numpy.log(x), numpy.log(y), 1)
            plt.plot(numpy.log(x), m*numpy.log(x)+b, "b", label = "Best Fitting Line. Slope is: " + str(round(m,4)))

        plt.legend()
        plt.show()

    def plotNormalTokenVsVocabularySizeForThree(self, Corpora1, Corpora2, Corpora3, Corpora1Name, Corpora2Name, Corpora3Name):
        import matplotlib.pyplot as plt
        plt.xlabel('Number of Tokens in Corpora')
        plt.ylabel('Number of Types')
        plt.title("Token vs Type Size")

        import math
        x = []
        y = []
        for i in range(math.floor(len(Corpora1)/10000)):
            x.append(10000*(i+1))
            y.append(len(self.countTypeFrequencies(Corpora1[1:10000*(i+1)])))
        print("x = " , x)
        print("\n")
        print("y = " , y)
        plt.plot(x, y, "r", label = Corpora1Name)

        x = []
        y = []
        for i in range(math.floor(len(Corpora2)/10000)):
            x.append(10000*(i+1))
            y.append(len(self.countTypeFrequencies(Corpora2[1:10000*(i+1)])))
        print("x = " , x)
        print("\n")
        print("y = " , y)
        plt.plot(x, y, "g", label = Corpora2Name)

        x = []
        y = []
        for i in range(math.floor(len(Corpora3)/10000)):
            x.append(10000*(i+1))
            y.append(len(self.countTypeFrequencies(Corpora3[1:10000*(i+1)])))
        print("x = " , x)
        print("\n")
        print("y = " , y)
        plt.plot(x, y, "b", label = Corpora3Name)
        plt.legend()
        plt.show()


    def plotNormalZipfsForThree(self, TypeFrequencies1,TypeFrequencies2, TypeFrequencies3, name1, name2, name3 ):

      import math

      freqArray = []
      for letter, count in TypeFrequencies1.most_common(len(TypeFrequencies1)):
          freqArray.append(count)
      x = []
      y = []
      import matplotlib.pyplot as plt
      plt.figure(1)
      for i in range(1, math.floor(len(freqArray)/300)):
          x.append(i)
          y.append(freqArray[i])
      plt.xlabel('Rank of Type')
      plt.ylabel('Frequency')
      plt.title("Zipf's Law Plot")
      plt.plot(x, y, 'g', label = name1 )

      freqArray = []
      for letter, count in TypeFrequencies2.most_common(len(TypeFrequencies2)):
          freqArray.append(count)
      x = []
      y = []
      for i in range(1, math.floor(len(freqArray)/300)):
          x.append(i)
          y.append(freqArray[i])
      plt.plot(x, y, 'r', label = name2)

      freqArray = []
      for letter, count in TypeFrequencies3.most_common(len(TypeFrequencies3)):
          freqArray.append(count)
      x = []
      y = []
      for i in range(1, math.floor(len(freqArray)/300)):
          x.append(i)
          y.append(freqArray[i])
      plt.plot(x, y, 'b', label = name3)
      plt.legend()
      plt.show()

    def plotLogZipfsForThree(self, TypeFrequencies1,TypeFrequencies2, TypeFrequencies3, name1, name2, name3 ):

      import numpy
      freqArray = []
      for letter, count in TypeFrequencies1.most_common(len(TypeFrequencies1)):
          freqArray.append(count)
      x = []
      y = []
      import matplotlib.pyplot as plt
      plt.figure(2)
      for i in range(1, len(freqArray)):
          x.append(i)
          y.append(freqArray[i])
      plt.xlabel('log(Rank of Type)')
      plt.ylabel('log(Frequency)')
      plt.title("Zipf's Law Plot")
      plt.plot(numpy.log(x), numpy.log(y), 'g', label = name1 )

      freqArray = []
      for letter, count in TypeFrequencies2.most_common(len(TypeFrequencies2)):
          freqArray.append(count)
      x = []
      y = []
      for i in range(1, len(freqArray)):
          x.append(i)
          y.append(freqArray[i])
      plt.plot(numpy.log(x), numpy.log(y), 'r', label = name2)

      freqArray = []
      for letter, count in TypeFrequencies3.most_common(len(TypeFrequencies3)):
          freqArray.append(count)
      x = []
      y = []
      for i in range(1, len(freqArray)):
          x.append(i)
          y.append(freqArray[i])
      plt.plot(numpy.log(x), numpy.log(y), 'b', label = name3)
      plt.legend()
      plt.show()

    def mergeCorpora(self, book1, book2, book3):
      file1 = open("C:/Users/enesk/PycharmProjects/NLPminiProject/Books/" + book1, encoding="utf8")
      text1 = file1.read()
      file1.close()
      file2 = open("C:/Users/enesk/PycharmProjects/NLPminiProject/Books/" + book2, encoding="utf8")
      text2 = file2.read()
      file2.close()
      file3 = open("C:/Users/enesk/PycharmProjects/NLPminiProject/Books/" + book3, encoding="utf8")
      text3 = file3.read()
      file3.close()
      text1 += "/n"
      text1 += text2
      text1 += "/n"
      text1 += text3
      return text1
    def writeFrequenciesToText(self, names, frequencies, dirName):
      for i in range(9):
          with open("Frequencies/" + dirName + names[i], 'w', encoding="utf8") as f:
              for k, v in frequencies[i].most_common():
                  f.write("{} {}\n".format(k, v))

    def writeFrequencyToText(self, name, frequency, dirName):
          with open("Frequencies/" + dirName + name, 'w', encoding="utf8") as f:
              for k, v in frequency.most_common():
                  f.write("{} {}\n".format(k, v))

    def createRandomCorpora (self, text):

      ##### split into words by white space
      words = text.split()
      # print(words[:100])
      ##### remove punctuation from each word
      import string
      table = str.maketrans('', '', string.punctuation)
      strippedWords = [w.translate(table) for w in words]
      # print(strippedWords[:100])

      ##### convert to lower case
      strippedWordsLower = [strippedWords.lower() for strippedWords in strippedWords]
      # print(strippedWordsLower[:100])
      return strippedWordsLower

    def createCorpora (self, bookName):
      ##### load text
      file = open("C:/Users/enesk/PycharmProjects/NLPminiProject/Books/" + bookName, encoding="utf8")
      text = file.read()
      # print(text)
      file.close()

      ##### split into words by white space
      words = text.split()
      # print(words[:100])
      ##### remove punctuation from each word
      import string
      table = str.maketrans('', '', string.punctuation)
      strippedWords = [w.translate(table) for w in words]
      # print(strippedWords[:100])

      ##### convert to lower case
      strippedWordsLower = [strippedWords.lower() for strippedWords in strippedWords]
      # print(strippedWordsLower[:100])
      return strippedWordsLower

    def removeStopWords(self, strippedWordsLower):
      ##### remove stopwords
      filename = 'stopwords.txt'
      file = open(filename, 'r+')
      stopWords = file.read()
      file.close()
      strippedWordsWOStopWords = [w for w in strippedWordsLower if not w in stopWords]
      return strippedWordsWOStopWords
      # print(strippedWordsWOStopWords[:100000])

    def countTypeFrequencies(self, strippedWords):
     from collections import Counter
     wordFrequencies = Counter(strippedWords)
     return wordFrequencies
     #print(wordFrequencies)
