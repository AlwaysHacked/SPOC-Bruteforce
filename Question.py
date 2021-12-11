class Question:
    q: str
    br: list[str]
    mr: list[str]

    def __init__(self, q: str, br: list, mr: list):
        self.q = q
        self.r = r

    def getQuestion(self) -> str:
        return self.q

    def getBonnesReponses(self) -> list[str]:
        return self.br

    def getMauvaisesReponses(self) -> list[str]:
        return self.mr

    def haveBonneReponse(self) -> bool:
        return len(self.br) > 0

    def haveMauvaisesReponses(self) -> bool:
        return len(self.mv) > 0

    def addBonneReponse(self, rep: str) -> None:
        self.br.append(rep)

    def addBonnesReponses(self, rep: list[str]) -> None:
        for i in rep : self.br.append(i)

    def addMauvaiseReponse(self, rep: str) -> None:
        self.mr.append(rep)

    # def
    # def
