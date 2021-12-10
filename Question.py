class Question:
    q: str
    br: list[str]
    mr: list[str]

    def __init__(self, q: str, br: list, mr: list):
        self.q = q
        self.r = r

    def getQuestion() -> str:
        return q

    def getBonnesReponses() -> list[str]:
        return br

    def getMauvaisesReponses() -> list[str]:
        return mr

    def haveBonneReponse() -> bool:
        return len(br) > 0

    def haveMauvaisesReponses() -> bool:
        return len(mv) > 0

    def addBonneReponse(rep: str) -> None:
        br.append(rep)

    def addBonnesReponses(rep: list[str]) -> None:
        for i in rep : br.append(i)

    def addMauvaiseReponse(rep: str) -> None:
        mr.append(rep)

    # def
    # def
