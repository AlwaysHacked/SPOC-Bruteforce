import csv

from Question import *

rep_delimiter = '~'

class QuestionList:
    questionList : list[Question]
    dataBase : str
    delimiter : str

    def __init__(self, dataBase="QuestionsReponses.csv", delimiter="¤"):
        self.dataBase = dataBase
        self.delimiter = delimiter
        self.questionList = []

    # def importDataFromCSV(self, fileName: str) -> None:
    #     self.dataBase = fileName
    #     with open(fileName, 'r', encoding='utf8') as file:
    #         lines = file.readlines()
    #         for i in lines:
    #             splitted_line = i.split(self.delimiter)
    #             question = splitted_line[0]
    #             reponses = splitted_line[1].split(rep_delimiter)
    #             self.questionList.append[Question(question, reponses)]

    def importDataFromCSV(self) -> None:
        # print(self.dataBase)
        # importDataFromCSV(self, self.dataBase)
        fileName = self.dataBase
        with open(fileName, 'r', encoding='utf8') as file:
            lines = file.readlines()
            index = 0
            for i in lines:
                splitted_line = i.split(self.delimiter)
                print(splitted_line)
                question = splitted_line[0]
                reponses = splitted_line[1].split(rep_delimiter)
                reponses[-1] = reponses[-1].split('\n')[0]
                self.addQuestion(Question(question))
                self.questionList[index].addMultipleReponses(reponses)
                index += 1


    def exportDataToCSV(self) -> None:
        with open(self.dataBase, 'w', encoding='utf8') as file:
            for i in range(len(self.questionList)):
                file.write(self.questionList[i].getQuestion() + self.delimiter + rep_delimiter.join(self.questionList[i].getAllReponses()) + '\n')

    # returns question's index in `questionList` if it exists
    # -1 if it doesn't
    def getQuestionIndex(self, enonce: str) -> int:
        for i in range(len(self.questionList)):
            if self.questionList[i].getQuestion() == enonce:
                return i
        return -1

    def addQuestion(self, q: Question) -> None:
        question_ind = self.getQuestionIndex(q.getQuestion())
        if question_ind >= 0 :
            if not (q.getReponse(0) in self.questionList[question_ind].getAllReponses()):
                self.questionList[question_ind].addReponse(q.getReponse())
        else:
            self.questionList.append(q)

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
        if self.exists(enonce):
            return self.questionList[self.getQuestionIndex(enonce)]

    def getQuestions(self) -> list[Question]:
        return self.questionList

    def showQuestions(self) -> None:
        for i in range(len(self.questionList)):
            print(i, self.questionList[i].getQuestion())

    def showQuestionsReponses(self) -> None:
        for i in range(len(self.questionList)):
            self.questionList[i].printQuestion()
            # print(self.questionList[i].getQuestion() + '\n\t' + '\n\t'.join(self.questionList[i].getAllReponses()), end = '\n\n')
