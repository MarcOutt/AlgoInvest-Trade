from itertools import chain, combinations
import time
import csv

def read_csv_files(file):
    """Lit un fichier csv"""
    with open(file, 'r') as f:
        dataset = csv.reader(f)
        dataset_clean = clean_file(dataset)
    return dataset_clean


def clean_file(file):
    """Nettoie les fichiers CSV"""
    dataset = []
    for share in file:
        if share[1] == "0.0" or share[1].startswith('-') or share[1].startswith('price'):
            del share
        else:
            share[1] = float(share[1])
            share[2] = float(share[2]) / 100
            dataset.append(share)
    return dataset


def bruteforce(lst):
    """Permet de sélectionner des actions pour créer un portefeuille avec un bénéfice optimisé avec un algorithme
    de type bruteforce"""
    start = time.time()
    best_wallet = []
    best_amount_wallet = 0
    best_benefits = 0
    s = list(lst)
    comb_list = chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
    for solution in comb_list:
        wallet = []
        benefits_wallet = 0
        amount_wallet = 0
        for stock_market in solution:
            amount_wallet += stock_market[1]
            benefits_wallet += stock_market[2] * stock_market[1]
            wallet.append(stock_market[0])
        if amount_wallet <= 500 and best_benefits < benefits_wallet:
            best_wallet = wallet
            best_amount_wallet = amount_wallet
            best_benefits = benefits_wallet
    end = time.time()
    print("_" * 70, f"\nLe portefeuille d'actions le plus rentable est le suivant:")
    for share in best_wallet:
        print("-", share)
    print(f"\nLa valeur du portefeuille est de {round(best_amount_wallet, 2)}€ avec un bénéfice de {round(best_benefits, 2)}€"
          f"\nLe temps d'exécution du programme est de : {round((end - start), 2)}s\n")


stock_market = [
        ["action_01", 20, 0.05],
        ["action_02", 30, 0.1],
        ["action_03", 50, 0.15],
        ["action_04", 70, 0.2],
        ["action_05", 60, 0.17],
        ["action_06", 80, 0.25],
        ["action_07", 22, 0.07],
        ["action_08", 26, 0.11],
        ["action_09", 48, 0.13],
        ["action_10", 34, 0.27],
        ["action_11", 42, 0.17],
        ["action_12", 110, 0.09],
        ["action_13", 38, 0.23],
        ["action_14", 14, 0.01],
        ["action_15", 18, 0.03],
        ["action_16", 8, 0.08],
        ["action_17", 4, 0.12],
        ["action_18", 10, 0.14],
        ["action_19", 24, 0.21],
        ["action_20", 114, 0.18],
    ]


print(" "*25, "ALGORITHME BRUTEFORCE")


dataset1 = read_csv_files("dataset1.csv")
dataset2 = read_csv_files("dataset2.csv")

bruteforce(stock_market)
bruteforce(dataset1)

