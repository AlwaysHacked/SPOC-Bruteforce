import csv

import Question

rep_delimiter = '~'

class QuestionList:
    questionList : list[Question]
    dataBase : str
    delimiter : str

    def __init__(self, dataBase="dataFile.csv", delimiter="¤"):
        self.dataBase = dataBase
        self.delimiter = delimiter
        self.questionList = []

    def importDataFromCSV(self, fileName: str) -> None:
        self.dataBase = fileName
        with open(fileName, 'r', encoding='utf8') as file:
            lines = file.readlines()
            for i in lines:
                splitted_line = i.split(self.delimiter)
                question = splitted_line[0]
                reponses = splitted_line[1].split(rep_delimiter)
                self.questionList.append[Question(question, reponses)]

    def importDataFromCSV(self, ) -> None:
        importDataFromCSV(self.dataBase)

    def exportDataToCSV(self, dataBase: list[Question]) -> None:
        with open(self.dataBase, 'w', encoding='utf8') as file:
            file.write('\n'.join([x.q + self.delimiter + rep_delimiter.join(x.r) for x in dataList]))
            # for i in dataBase:
            #     sentence = i.q + self.delimiter                                     # writing question seperating with delimiter
            #     for k in len(i.r):
            #         sentence.append(i.r[k] + (rep_delimiter * (k+1) != len(i.r)))   # writing answers seperating with rep_delimiter
            #     file.write(sentence + '\n')

    def addQuestion(self, q: Question) -> None:
        self.questionList.append(q)

    # returns question's index in `questionList` if it exists
    # -1 if it doesn't
    def getQuestionIndex(self, enonce: str) -> int:
        for i in range(len(self.questionList)):
            if self.quesionList(i).getQuestion() == enonce:
                return i
        return -1

    def exists(self, enonce: str) -> bool:
        return self.getQuestionIndex(enonce) >= 0  # if there is such question, index is in between [0, len - 1]

    def removeQuestion(self, q: Question) -> None:
        if exists(q):
            self.questionList.remove(q)

    def updateQuestion(self, q: Question) -> None:
        if exists(q):
            self.removeQuestion(q) # deleting by name
            self.addQuestion(q)    # adding the whole element

    def getQuestion(self, enonce: str) -> Question:
        if self.exists(q):
            return self.questionList[getQuestionIndex(enonce)]
