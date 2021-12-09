# DEBUG:

# see on which frame you currently are by selecting everything (ctrl + a)
# fox.find_element(By.TAG_NAME,'a').send_keys(Keys.CONTROL, 'a')

from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep as slp
import re

def answerQuestions() -> None:
    q = set(re.findall("h5p-mcq\d", fox.page_source))                       # getting questions in set, so there's no repetitions
    ans = fox.find_elements(By.CLASS_NAME, "h5p-alternative-container")     # getting answers
    next = fox.find_elements(By.CLASS_NAME, "h5p-question-next")
    # finish = fox.find_element(By.CLASS_NAME, "h5p-question-finish.h5p-joubelui-button")
    for i in q:
        for j in q:
            t = fox.find_element(By.ID, j).text
            # !! getting the question "l'énoncé"
            if len(t) != 0:
                print(t * bool(len(t)), end='')
                for a in ans:
                    if a.is_displayed():
                        print("\t%s" %a.text)
                        a.click()
                        break
                try : # is it finished ?
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
fox.get("https://ecampus.paris-saclay.fr")

# print()
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
        slp(2)

qcm_site = re.findall("h[\W\w]+\d", src[i : i + 100])[0]
fox.execute_script('''window.open("%s","_blank");''' % qcm_site) # opening site in a new tab

fox.switch_to.window(fox.window_handles[1]) # switch to new tab

slp(3)

frame = re.findall("h5p-iframe-[\d]+", fox.page_source)[0]      # finding frame's name
fox.switch_to.frame(frame)                                      # and switching to it

# loop starts here, through every question, by pressing next button
answerQuestions()
