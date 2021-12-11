# DEBUG:

# see on which frame you currently are by selecting everything (ctrl + a)
# fox.find_element(By.TAG_NAME,'a').send_keys(Keys.CONTROL, 'a')

from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep as slp
import re

import Question
from QuestionList import *

SLEEP = 1

corrige = "https://ecampus.paris-saclay.fr/mod/hvp/grade.php?id="
qcm = "https://ecampus.paris-saclay.fr/mod/hvp/view.php?id="

allQuestions = QuestionList()

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
                print(enonce, end='')
                if allQuestions.exists(enonce):
                    q = allQuestions.getQuestion(enonce)
                    if q.haveBonneReponse():
                        answerCorrectly(ans, q.getBonnesReponses)
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

fox = wd.Firefox(executable_path="/home/serge/spoc/geckodriver")
fox.get("https://ecampus.paris-saclay.fr/auth/saml2/login.php?wants&idp=a937ff1f50145fee098f32dc3907c247&passive=off")

with open('ids.txt', 'r') as file:
    ids = file.readlines()

for i in range(len(ids)):
    ids[i] = ids[i].split()[0]

input("Press enter after logging in")

# looping starts here
# for i in ids:
i = ids[0]
fox.get(qcm + i)
frame = re.findall("h5p-iframe-[\d]+", fox.page_source)[0]
fox.switch_to.frame(frame)
slp(SLEEP)

answerQuestions()
fox.get(corrige + i)
slp(SLEEP)

fox.find_element(By.LINK_TEXT, "Reporter").click()
questions = fox.find_elements(By.CLASS_NAME, "h5p-reporting-description.h5p-choices-task-description")
cut_ind = (fox.page_source).find(questions[0].text)
qes_rep = re.split("\<\/table\>", fox.page_source[cut_ind : ])[ : -1]
response_boxes = "h5p-choices-alternative"
responses = {}
for q in range(len(questions)):
    qes_rep[q] = re.split("\<tr\>", qes_rep[q])[1 :]
    for r in qes_rep[q]: # iterate the right number of times
        response_in_field = fox.find_element(By.CLASS_NAME, response_boxes).text

        qes_rep[q] = qes_rep[q][qes_rep[q].find(response_boxes) + len(repones_boxes) :]


q = 0
rep = fox.find_elements(By.CLASS_NAME, response_boxes)
response_in_field = fox.find_element(By.CLASS_NAME, response_boxes).text



input("Log fucking in and press enter on terminal")

fox.find_element(By.XPATH, "/html/body/nav/div/div[1]/section/div/div/div[1]/div[1]/div[2]").click()
print("Dans SPOC")
input("Allez a la page de QCM que vous devez faire and fucking press enter")

i = -1
while i == -1:
    src = fox.page_source              # getting page's html
    i = src.find("id=\"qcm\"")         # finding qcm's embed source
    if i == -1 :
        print("Can't see a qcm")
        slp(SLEEP)

qcm_site = re.findall("h[\W\w]+\d", src[i : i + 100])[0]
fox.execute_script('''window.open("%s","_blank");''' % qcm_site) # opening site in a new tab

fox.switch_to.window(fox.window_handles[1]) # switch to new tab

slp(SLEEP)

frame = re.findall("h5p-iframe-[\d]+", fox.page_source)[0]      # finding frame's name
fox.switch_to.frame(frame)                                      # and switching to it

# loop starts here, through every question, by pressing next button
answerQuestions()
