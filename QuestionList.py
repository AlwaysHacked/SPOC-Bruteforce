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

    def importDataFromCSV(fileName: str) -> None:
        self.dataBase = fileName
        with open(fileName, 'r', encoding='utf8') as file:
            lines = file.readlines()
            for i in lines:
                splitted_line = i.split(self.delimiter)
                question = splitted_line[0]
                reponses = splitted_line[1].split(rep_delimiter)
                questionList.append[Question(question, reponses)]

    def importDataFromCSV() -> None:
        importDataFromCSV(self.dataBase)

    def exportDataToCSV(dataBase: list[Question]) -> None:
        with open(self.dataBase, 'w', encoding='utf8') as file:
            file.write('\n'.join([x.q + self.delimiter + rep_delimiter.join(x.r) for x in dataList]))
            # for i in dataBase:
            #     sentence = i.q + self.delimiter                                     # writing question seperating with delimiter
            #     for k in len(i.r):
            #         sentence.append(i.r[k] + (rep_delimiter * (k+1) != len(i.r)))   # writing answers seperating with rep_delimiter
            #     file.write(sentence + '\n')

    def addQuestion(q: Question) -> None:
        questionList.append(q)

    # returns question's index in `questionList` if it exists
    # -1 if it doesn't
    def getQuestionIndex(enonce: str) -> int:
        for i in len(questionList):
            if self.quesionList(i).getQuestion() == enonce:
                return i
        return -1

    def exists(enonce: str) -> bool:
        return getQuestionIndex(enonce) >= 0  # if there is such question, index is in between [0, len - 1]

    def removeQuestion(q: Question) -> None:
        if exists(q):
            self.questionList.remove(q)

    def updateQuestion(q: Question) -> None:
        if exists(q):
            removeQuestion(q) # deleting by name
            addQuestion(q)    # adding the whole element

    def getQuestion(enonce: str) -> Question:
        if exists(q):
            return self.questionList[getQuestionIndex(enonce)]
