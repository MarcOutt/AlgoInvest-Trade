
# Projet d'Optimisation des Stratégies d'Investissement

## Sommaire
- [Introduction](#introduction)
- [Cahier des Charges](#cahier-des-charges)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Technologies Utilisées](#technologies-utilisées)
- [Partie 1: Algorithme pour maximiser les bénéfices](#partie-1-algorithme-pour-maximiser-les-bénéfices)
- [Partie 2: Optimisation de l'algorithme](#partie-2-optimisation-de-lalgorithme)
- [Partie 3: Backtesting et optimisation](#partie-3-backtesting-et-optimisation)
- [Comment exécuter le code](#comment-exécuter-le-code)

## Introduction
Ce projet a été développé dans le cadre d'un travail pour AlgoInvest&Trade, une société financière spécialisée dans l'investissement. L'objectif du projet est de concevoir un algorithme capable de maximiser les bénéfices réalisés par les clients après deux ans d'investissement en suggérant une liste d'actions à acheter.

## Cahier des Charges
Le cahier des charges du projet est le suivant :
- Concevoir un algorithme qui maximisera le profit réalisé par les clients après deux ans d'investissement.
- L'algorithme doit suggérer une liste des actions les plus rentables à acheter pour maximiser le profit d'un client au bout de deux ans.
- Chaque action ne peut être achetée qu'une seule fois.
- Aucune fraction d'action ne peut être achetée.
- Le montant total dépensé par client ne doit pas dépasser 500 euros.

## Prérequis
Avant d'exécuter le code, assurez-vous d'avoir les éléments suivants installés sur votre machine :
- Python 3.x
- Bibliothèque CSV de Python

## Installation

### 1. Télécharger le projet sur votre répertoire local : 
```
git clone https://github.com/MarcOutt/OC_p12.git
```
### 2. Mettre en place un environnement virtuel :
* Créer l'environnement virtuel: `python -m venv venv`
* Activer l'environnement virtuel :
    * Windows : `venv\Scripts\activate.bat`
    * Unix/MacOS : `source venv/bin/activate`
    
### 3. Installer les dépendances du projet
```
pip install -r requirements.txt
```


## Technologies Utilisées
- Python
- Bibliothèque CSV

## Partie 1: Algorithme pour maximiser les bénéfices
Dans cette partie, nous avons développé un algorithme de type brute force pour explorer toutes les combinaisons possibles d'actions afin de trouver le portefeuille d'actions le plus rentable respectant les contraintes données.

## Partie 2: Optimisation de l'algorithme
Suite aux exigences des clients pour obtenir une réponse plus rapide, nous avons optimisé l'algorithme de la partie 1 pour fournir une réponse en moins d'une seconde. Nous avons conçu un algorithme optimisé qui évite d'explorer toutes les combinaisons possibles, améliorant ainsi les performances globales du programme.

## Partie 3: Backtesting et optimisation
Dans cette partie, nous avons testé l'exactitude de l'algorithme en l'exécutant sur des ensembles de données historiques. Nous avons comparé les résultats de l'algorithme avec les choix effectués par Sienna, l'un des principaux conseillers financiers d'AlgoInvest&Trade.

## Comment exécuter le code
1. Placez-vous dans le répertoire contenant les fichiers téléchargés.
2. Pour exécuter l'algorithme de la partie 1 (brute force), tapez la commande suivante :
 ```
   python bruteforce.py
```
3. Pour exécuter l'algorithme de la partie 2 (optimisé), tapez la commande suivante :
 ```
   python optimized.py
```
4. Pour exécuter l'algorithme de la partie 3 (backtesting), tapez la commande suivante :
    ```
   python backtesting.py
```

