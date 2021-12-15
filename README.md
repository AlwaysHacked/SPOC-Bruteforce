# SPOC vs Bruteforce

Un petit projet de bruteforce d'amateur

## Idée

Sachant qu'on a un nombre illimités d'essais de réponses aux QCM et que les questions des QCM varient aléatoirement, on crée une base de donnée avec toutes les questions et les *bonnes* réponses correspondantes

## Outils Python

Pour naviguer sur le web, faire des click ou autre, on utilise la bibliothèque **`Selenium`**

L'utilisation de la bibliothèque nécessite d'avoir **`geckodriver`** (jsp trop ce que c'est, mais il le faut)

## Format de la base de données

Les questions sont séparés des réponses par **`¤`**, et en cas de plusieurs réponses possibles, les réponses entre elles sont séparés par **`~`**
Chaque ligne comporte une question avec ses réponses

### Les modes du programme

Il y a 2 modes d'execution :
* `answer`  : répondre aux questions en utilisant la base fournie sous nom de *"QuestionsReponses.csv"*
* `db`      : itérer sur les qcm plusieurs fois et récolter toutes les bonnes réponses 

Pour lancer le script avec l'un des modes `python3 spocBot.py /mode\` 
