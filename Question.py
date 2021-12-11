class Question:
    q: str
    r: list[str]


    def __init__(self, q: str, r: list):
        self.q = q
        self.r = [r]

    def getQuestion(self) -> str:
        return self.q

    def getAllReponses(self) -> list[str]:
        return self.r

    def getReponse(self):
        return self.r[0]

    # def haveReponse(self) -> bool:
    #     return len(self.r) > 0

    def addReponse(self, rep: str) -> None:
        self.r.append(rep)

    # def addReponse(self, q) -> None:
    #     self.r.append(q.getReponse())

    def addMultipleReponses(self, rep: list[str]) -> None:
        for i in rep : self.br.append(i)

    # def
    # def
