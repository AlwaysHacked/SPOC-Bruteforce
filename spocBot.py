# DEBUG:

# see on which frame you currently are by selecting everything (ctrl + a)
# fox.find_element(By.TAG_NAME,'a').send_keys(Keys.CONTROL, 'a')

from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep as slp
import re

import sys

from Question import *
from QuestionList import *

SLEEP = 1
WAIT_MAX = 5

corrige = "https://ecampus.paris-saclay.fr/mod/hvp/grade.php?id="
qcm = "https://ecampus.paris-saclay.fr/mod/hvp/view.php?id="

allQuestions = QuestionList()

error_message = '''
Need an argument for execution.
`python3 %s db` to make/update the datalist
`python3 %s answer` to answer the question with existing datalist\
''' % (sys.argv[0], sys.argv[0])

number_of_iterations = 0

if len(sys.argv) == 1:
    print(error_message)
    sys.exit(1)
if sys.argv[1] == "db":
    number_of_iterations = 7
elif sys.argv[1] == "answer" or sys.argv[1] == 'a':
    number_of_iterations = 1
    allQuestions.importDataFromCSV()
else:
    print(error_message)

def answerRandomly(answerButtons) -> None:
    '''Marks all the visible answerButtons
    Usefull if checkbox, no distinction is made'''
    for a in answerButtons:
        if a.is_displayed():
            a.click()

def answerCorrectly(answerButtons, correctAnswers: list[str]) -> None:
    '''Clicks on correct answer(s)'''
    count = 0
    for a in answerButtons:
        if a.is_displayed() and a.text in correctAnswers :
            a.click()
            count += 1
            if count == len(correctAnswers):
                return

def answerQuestions() -> None:
    '''shitty shit'''
    global allQuestions
    questions = set(re.findall("h5p-mcq\d", fox.page_source))               # getting questions in set, so there's no repetitions
    ans = fox.find_elements(By.CLASS_NAME, "h5p-alternative-container")     # getting answers
    next = fox.find_elements(By.CLASS_NAME, "h5p-question-next")
    for i in questions:
        for j in questions:
            enonce = fox.find_element(By.ID, j).text
            # !! getting the question -> "l'énoncé"
            if len(enonce) != 0:
                if allQuestions.exists(enonce):
                    q = allQuestions.getQuestion(enonce)
                    # if q.haveBonneReponse():
                    answerCorrectly(ans, q.getAllReponses())
                else:
                    answerRandomly(ans)
                try : # no more questions?
                    fox.find_element(By.CLASS_NAME, "h5p-question-finish.h5p-joubelui-button").click()
                    return
                except :
                    print("", end='')
                    # continue
                for n in next:
                    if n.is_displayed():
                        n.click()
                        break

with open('ids.txt', 'r') as file:
    ids = file.readlines()

for i in range(len(ids)):
    ids[i] = ids[i].split()[0]
print(ids)

fox = wd.Firefox(executable_path="/home/serge/spoc/geckodriver")
fox.get("https://ecampus.paris-saclay.fr/auth/saml2/login.php?wants&idp=a937ff1f50145fee098f32dc3907c247&passive=off")
wait = WebDriverWait(fox, WAIT_MAX)


input("Press enter after logging in")
for i in ids:
    # slp(1)
    for k in range(number_of_iterations):
        # slp(5)
        fox.get(qcm + i)
        fox.implicitly_wait(SLEEP)
        frame = re.findall("h5p-iframe-[\d]+", fox.page_source)[0]
        fox.switch_to.frame(frame)

        answerQuestions()

        # slp(5)
        fox.get(corrige + i)

        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Reporter"))).click()
        questions = fox.find_elements(By.CLASS_NAME, "h5p-reporting-description.h5p-choices-task-description")
        questions = [i.text for i in questions]
        cut_ind = (fox.page_source).find(questions[0])
        qes_rep = re.split("\<\/table\>", fox.page_source[cut_ind : ])[ : -1]

        responses = fox.find_elements(By.CLASS_NAME, "h5p-choices-alternative")
        responses = [i.text for i in responses]
        rep_index = 0

        for q in range(len(questions)):
            # slp(3)
            qes_rep[q] = re.split("h5p-choices-alternative", qes_rep[q])[1 :]
            for r in qes_rep[q]: # iterate the right number of times
                if "correct" in r :
                    allQuestions.addQuestion(Question(questions[q], responses[rep_index]))
                    # print('\t' + r)
                rep_index +=1
            # allQuestions.showQuestionsReponses()
            allQuestions.exportDataToCSV()
            # slp(3)

if __name__ == '__main__':
    pass
