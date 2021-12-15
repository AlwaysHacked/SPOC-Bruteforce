class Question:
    q: str
    r: list[str]

    def __init__(self, q: str, r=[]):
        self.q = q
        self.r = ([] if r == [] else [r])
        # self.r = (r == [] ? [] : [r])

    def getQuestion(self) -> str:
        return self.q

    def getAllReponses(self) -> list[str]:
        return self.r

    def getReponse(self, i: int) -> str:
        return self.r[i]

    def addReponse(self, rep: str) -> None:
        self.r.append(rep)

    def addMultipleReponses(self, rep: list[str]) -> None:
        for i in rep : self.r.append(i)

    def printQuestion(self) -> None:
        print(self.q + '\n\t' + '\n\t'.join(self.r), end = '\n\n')
