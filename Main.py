from Operations import Operations
authorBasedBooks = ["Author/Dostoyevski-Idiot.txt", "Author/Dostoyevski-KaramazovBrothers.txt" , "Author/Dostoyevski-Possessed.txt",
                    "Author/CharlesDickens-BleakHouse.txt", "Author/CharlesDickens-Dombey&Son.txt", "Author/CharlesDickens-OurMutualFriend.txt",
                    "Author/Tolstoy-AnnaKarenina.txt", "Author/Tolstoy-Resurrection.txt", "Author/Tolstoy-War&Peace.txt"]
genreBasedBooks = ["Genre/Detective-Moonstone.txt", "Genre/Detective-Sherlock.txt", "Genre/Detective-TwentyYearsDetective.txt",
                   "Genre/Biography-Life&LettersofRobertBrowning.txt", "Genre/Biography-LifeofFroude.txt", "Genre/Biography-LifeofWilliamEwart.txt",
                   "Genre/Myths-Assyria.txt", "Genre/Myths-China.txt", "Genre/Myths-Rome.txt" ]

authorBasedFrequencyTexts = ["Freq_Dostoyevski-Idiot.txt", "Freq_Dostoyevski-KaramazovBrothers.txt" , "Freq_Dostoyevski-Possessed.txt",
                    "Freq_CharlesDickens-BleakHouse.txt", "Freq_CharlesDickens-Dombey&Son.txt", "Freq_CharlesDickens-OurMutualFriend.txt",
                    "Freq_Tolstoy-AnnaKarenina.txt", "Freq_Tolstoy-Resurrection.txt", "Freq_Tolstoy-War&Peace.txt"]
genreBasedFrequencyTexts = ["Freq_Detective-Moonstone.txt", "Freq_Detective-Sherlock.txt", "Freq_Detective-TwentyYearsDetective.txt",
                   "Freq_Biography-Life&LettersofRobertBrowning.txt", "Freq_Biography-LifeofFroude.txt", "Freq_Biography-LifeofWilliamEwart.txt",
                   "Freq_Myths-Assyria.txt", "Freq_Myths-China.txt", "Freq_Myths-Rome.txt" ]

Corpora_authorBased = []
Corpora_genreBased = []
CorporaWOStopWords_authorBased = []
CorporaWOStopWords_genreBased = []

TypeFrequencies_authorBasedCorpora = []
TypeFrequencies_genreBasedCorpora = []
TypeFrequencies_authorBasedCorporaWOStopWords = []
TypeFrequencies_genreBasedCorporaWOStopWords = []

op = Operations()

########## PART C
for i in range(9):
    Corpora_authorBased.append(op.createCorpora(authorBasedBooks[i]))

for i in range(9):
    Corpora_genreBased.append(op.createCorpora(genreBasedBooks[i]))

########## PART D
for i in range(9):
    CorporaWOStopWords_authorBased.append(op.removeStopWords(Corpora_authorBased[i]))

for i in range(9):
    CorporaWOStopWords_genreBased.append(op.removeStopWords(Corpora_genreBased[i]))
########## PART E
for i in range(9):
    TypeFrequencies_authorBasedCorpora.append(op.countTypeFrequencies(Corpora_authorBased[i]))
    TypeFrequencies_genreBasedCorpora.append(op.countTypeFrequencies(Corpora_genreBased[i]))
    TypeFrequencies_authorBasedCorporaWOStopWords.append(op.countTypeFrequencies(CorporaWOStopWords_authorBased[i]))
    TypeFrequencies_genreBasedCorporaWOStopWords.append(op.countTypeFrequencies(CorporaWOStopWords_genreBased[i]))

op.writeFrequenciesToText(authorBasedFrequencyTexts, TypeFrequencies_authorBasedCorpora, "BeforeStopWord/AuthorBasedFrequencies/")
op.writeFrequenciesToText(genreBasedFrequencyTexts, TypeFrequencies_genreBasedCorpora, "BeforeStopWord/GenreBasedFrequencies/")
op.writeFrequenciesToText(authorBasedFrequencyTexts, TypeFrequencies_authorBasedCorporaWOStopWords, "AfterStopWord/AuthorBasedFrequencies/")
op.writeFrequenciesToText(genreBasedFrequencyTexts, TypeFrequencies_genreBasedCorporaWOStopWords, "AfterStopWord/GenreBasedFrequencies/")

########## PART F
mergedBook = op.mergeCorpora(authorBasedBooks[0],authorBasedBooks[1],authorBasedBooks[2])
with open ("C:/Users/enesk/PycharmProjects/NLPminiProject/Books/MergedBooks/" + 'MergedBook_Dostoyevski.txt', 'w', encoding="utf8") as fp:
    fp.write(mergedBook)

mergedBook = op.mergeCorpora(authorBasedBooks[3], authorBasedBooks[4], authorBasedBooks[5])
with open("C:/Users/enesk/PycharmProjects/NLPminiProject/Books/MergedBooks/" + 'MergedBook_CharlesDickens.txt', 'w',encoding="utf8") as fp:
    fp.write(mergedBook)

mergedBook = op.mergeCorpora(authorBasedBooks[6], authorBasedBooks[7], authorBasedBooks[8])
with open("C:/Users/enesk/PycharmProjects/NLPminiProject/Books/MergedBooks/" + 'MergedBook_Tolstoy.txt', 'w',encoding="utf8") as fp:
    fp.write(mergedBook)

mergedCorporaDostoyevski = op.createCorpora("/MergedBooks/MergedBook_Dostoyevski.txt")
mergedFreqDostoyevski = op.countTypeFrequencies(mergedCorporaDostoyevski)
op.writeFrequencyToText("MergedFreq_Dostoyevski" ,mergedFreqDostoyevski, "MergedFrequencies/" )

mergedCorporaCharles = op.createCorpora("/MergedBooks/MergedBook_CharlesDickens.txt")
mergedFreqCharles = op.countTypeFrequencies(mergedCorporaCharles)
op.writeFrequencyToText("MergedFreq_CharlesDickens" ,mergedFreqCharles, "MergedFrequencies/" )

mergedCorporaTolstoy = op.createCorpora("/MergedBooks/MergedBook_Tolstoy.txt")
mergedFreqTolstoy = op.countTypeFrequencies(mergedCorporaTolstoy)
op.writeFrequencyToText("MergedFreq_Tolstoy" ,mergedFreqTolstoy, "MergedFrequencies/" )

op.plotLogZipfsForThree(mergedFreqTolstoy, mergedFreqDostoyevski, mergedFreqCharles, "Tolstoy", "Dostoyevski", "Charles")
op.plotNormalZipfsForThree(mergedFreqTolstoy, mergedFreqDostoyevski, mergedFreqCharles, "Tolstoy", "Dostoyevski", "Charles")


op.plotLogZipfsForThree(TypeFrequencies_authorBasedCorpora[0],
                        TypeFrequencies_authorBasedCorpora[1],
                        TypeFrequencies_authorBasedCorpora[2],
                        "Idiot", "Karamazov Brothers", "Possessed")

op.plotLogZipfsForThree(TypeFrequencies_authorBasedCorpora[3],
                        TypeFrequencies_authorBasedCorpora[4],
                        TypeFrequencies_authorBasedCorpora[5],
                        "Bleak House", "Dombey & House", "Our Mutual Friend")

op.plotLogZipfsForThree(TypeFrequencies_authorBasedCorpora[6],
                        TypeFrequencies_authorBasedCorpora[7],
                        TypeFrequencies_authorBasedCorpora[8],
                        "AnnaKarenina", "Resurrection", "WarPeace")


########## PART G
op.plotNormalTokenVsVocabularySizeForThree(mergedCorporaCharles, mergedCorporaDostoyevski, mergedCorporaTolstoy,
                                     "Charles", "Dostoyevski", "Tolstoy")
op.plotLogTokenVsVocabularySizeForThree(mergedCorporaCharles, mergedCorporaDostoyevski, mergedCorporaTolstoy,
                                     "Charles", "Dostoyevski", "Tolstoy", False)
########## PART H
op.plotLogTokenVsVocabularySizeForThree(Corpora_authorBased[0], Corpora_authorBased[1], Corpora_authorBased[2],
                                     "Idiot", "Karamazov Brothers", "Possessed", False)
op.plotLogTokenVsVocabularySizeForThree(Corpora_authorBased[3], Corpora_authorBased[4], Corpora_authorBased[5],
                                     "Bleak House", "Dombey & House", "Our Mutual Friend", False)
op.plotLogTokenVsVocabularySizeForThree(Corpora_authorBased[6], Corpora_authorBased[7], Corpora_authorBased[8],
                                     "AnnaKarenina", "Resurrection", "WarPeace", False)

op.plotLogTokenVsVocabularySizeForNine(Corpora_authorBased[0], Corpora_authorBased[1], Corpora_authorBased[2],
                                    Corpora_authorBased[3], Corpora_authorBased[4], Corpora_authorBased[5],
                                    Corpora_authorBased[6], Corpora_authorBased[7], Corpora_authorBased[8],
                                    "Dostoyevski", "Charles", "Tolstoy", False)

op.plotLogTokenVsVocabularySizeForThree(mergedCorporaCharles, mergedCorporaDostoyevski, mergedCorporaTolstoy,
                                     "Dostoyevski", "Charles", "Tolstoy", False)

########## PART I
op.plotLogTokenVsVocabularySizeForNine(Corpora_authorBased[0], Corpora_authorBased[1], Corpora_authorBased[2],
                                    Corpora_authorBased[3], Corpora_authorBased[4], Corpora_authorBased[5],
                                    Corpora_authorBased[6], Corpora_authorBased[7], Corpora_authorBased[8],
                                    "Dostoyevski", "Charles", "Tolstoy", True)

op.plotLogTokenVsVocabularySizeForThree(mergedCorporaCharles, mergedCorporaDostoyevski, mergedCorporaTolstoy,
                                     "Dostoyevski", "Charles", "Tolstoy", True)

########## PART J
mergedBook = op.mergeCorpora(genreBasedBooks[0],genreBasedBooks[1],genreBasedBooks[2])
with open ("C:/Users/enesk/PycharmProjects/NLPminiProject/Books/MergedBooks/" + 'MergedBook_Detective.txt', 'w', encoding="utf8") as fp:
    fp.write(mergedBook)

mergedBook = op.mergeCorpora(genreBasedBooks[3], genreBasedBooks[4], genreBasedBooks[5])
with open("C:/Users/enesk/PycharmProjects/NLPminiProject/Books/MergedBooks/" + 'MergedBook_Biography.txt', 'w',encoding="utf8") as fp:
    fp.write(mergedBook)

mergedBook = op.mergeCorpora(genreBasedBooks[6], genreBasedBooks[7], genreBasedBooks[8])
with open("C:/Users/enesk/PycharmProjects/NLPminiProject/Books/MergedBooks/" + 'MergedBook_Myths.txt', 'w',encoding="utf8") as fp:
    fp.write(mergedBook)

mergedCorporaDetective = op.createCorpora("/MergedBooks/MergedBook_Detective.txt")
mergedFreqDetective = op.countTypeFrequencies(mergedCorporaDetective)
op.writeFrequencyToText("MergedFreq_Detective" ,mergedFreqDetective, "MergedFrequencies/" )

mergedCorporaBiography = op.createCorpora("/MergedBooks/MergedBook_Biography.txt")
mergedFreqBiography = op.countTypeFrequencies(mergedCorporaBiography)
op.writeFrequencyToText("MergedFreq_Biography" ,mergedFreqBiography, "MergedFrequencies/" )

mergedCorporaMyths = op.createCorpora("/MergedBooks/MergedBook_Myths.txt")
mergedFreqMyths = op.countTypeFrequencies(mergedCorporaMyths)
op.writeFrequencyToText("MergedFreq_Myths" ,mergedFreqMyths, "MergedFrequencies/" )

##############

op.plotLogTokenVsVocabularySizeForThree(Corpora_genreBased[0], Corpora_genreBased[1], Corpora_genreBased[2],
                                     "Moonstone", "Sherlock", "TwentyYearsDetective", False)
op.plotLogTokenVsVocabularySizeForThree(Corpora_genreBased[3], Corpora_genreBased[4], Corpora_genreBased[5],
                                     "Robert Browning", "Froude", "William Ewart", False)
op.plotLogTokenVsVocabularySizeForThree(Corpora_genreBased[6], Corpora_genreBased[7], Corpora_genreBased[8],
                                     "Assyria", "China", "Rome", False)

op.plotLogTokenVsVocabularySizeForNine(Corpora_genreBased[0], Corpora_genreBased[1], Corpora_genreBased[2],
                                    Corpora_genreBased[3], Corpora_genreBased[4], Corpora_genreBased[5],
                                    Corpora_genreBased[6], Corpora_genreBased[7], Corpora_genreBased[8],
                                    "Detective", "Biography", "Myths", False)

op.plotLogTokenVsVocabularySizeForThree(mergedCorporaDetective, mergedCorporaBiography, mergedCorporaMyths,
                                     "Detective", "Biography", "Myths", False)

op.plotLogTokenVsVocabularySizeForNine(Corpora_genreBased[0], Corpora_genreBased[1], Corpora_genreBased[2],
                                    Corpora_genreBased[3], Corpora_genreBased[4], Corpora_genreBased[5],
                                    Corpora_genreBased[6], Corpora_genreBased[7], Corpora_genreBased[8],
                                    "Detective", "Biography", "Myths", True)

op.plotLogTokenVsVocabularySizeForThree(mergedCorporaDetective, mergedCorporaBiography, mergedCorporaMyths,
                                     "Detective", "Biography", "Myths", True)

##### PART L
op.plotLogTokenVsVocabularySizeForNine(op.removeStopWords(Corpora_authorBased[0]),
                                       op.removeStopWords(Corpora_authorBased[1]),
                                       op.removeStopWords(Corpora_authorBased[2]),
                                       op.removeStopWords(Corpora_authorBased[3]),
                                       op.removeStopWords(Corpora_authorBased[4]),
                                       op.removeStopWords(Corpora_authorBased[5]),
                                       op.removeStopWords(Corpora_authorBased[6]),
                                       op.removeStopWords(Corpora_authorBased[7]),
                                       op.removeStopWords(Corpora_authorBased[8]),
                                       "Dosto", "Charles", "Tolstoy", True)

op.plotLogTokenVsVocabularySizeForThree(op.removeStopWords(mergedCorporaDostoyevski),
                                        op.removeStopWords(mergedCorporaCharles),
                                        op.removeStopWords(mergedCorporaTolstoy),
                                     "Dosto", "Charles", "Tolstoy", True)

op.plotLogTokenVsVocabularySizeForNine(op.removeStopWords(Corpora_genreBased[0]),
                                       op.removeStopWords(Corpora_genreBased[1]),
                                       op.removeStopWords(Corpora_genreBased[2]),
                                       op.removeStopWords(Corpora_genreBased[3]),
                                       op.removeStopWords(Corpora_genreBased[4]),
                                       op.removeStopWords(Corpora_genreBased[5]),
                                       op.removeStopWords(Corpora_genreBased[6]),
                                       op.removeStopWords(Corpora_genreBased[7]),
                                       op.removeStopWords(Corpora_genreBased[8]),
                                       "Detective", "Bio", "Myths", True)

op.plotLogTokenVsVocabularySizeForThree(op.removeStopWords(mergedCorporaDetective),
                                        op.removeStopWords(mergedCorporaBiography),
                                        op.removeStopWords(mergedCorporaMyths),
                                        "Detective", "Bio", "Myths",True)

########### PART M
randomText = op.createRandomText()
randomTextCorpora = op.createRandomCorpora(randomText)
print (randomTextCorpora)
frequenciesOfRandomText = op.countTypeFrequencies(randomTextCorpora)
print (frequenciesOfRandomText)
op.plotNormalZipfsForOne(frequenciesOfRandomText)
op.plotLogZipfsForOne(frequenciesOfRandomText)
op.plotNormalTokenVsVocabularySizeForOne(randomTextCorpora)
op.plotLogTokenVsVocabularySizeForOne(randomTextCorpora, False)
    # REFERENCES
    # https://machinelearningmastery.com/clean-text-machine-learning-python/
    # https://gist.github.com/larsyencken/1440509 -> stop words
