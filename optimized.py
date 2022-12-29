import time
import csv


def read_csv_files(file):
    with open(file, 'r') as f:
        dataset = csv.reader(f)
        dataset_clean = clean_file(dataset)
    return dataset_clean


def clean_file(file):
    dataset = []
    for share in file:
        if share[1] == "0.0" or share[1].startswith('-') or share[1].startswith('price'):
            del share
        else:
            share[1] = float(share[1])
            share[2] = float(share[2])/100
            dataset.append(share)
    return dataset


def dynamic(amount_max, stocks):
    start = time.time()
    amount_max = amount_max*100
    matrice = [[0 for x in range(amount_max + 1)] for x in range(len(stocks) + 1)]
    for i in range(1, len(stocks) + 1):
        stocks[i - 1][1] = int(stocks[i - 1][1] * 100)
        stocks[i - 1][2] = stocks[i - 1][2] * 100
        stocks[i - 1].append(stocks[i - 1][1] * stocks[i - 1][2])
        for amount_max in range(1, amount_max + 1):
            if stocks[i - 1][1] <= amount_max:
                matrice[i][amount_max] = max(stocks[i - 1][3] + matrice[i - 1][amount_max - stocks[i - 1][1]],
                                         matrice[i - 1][amount_max])
            else:
                matrice[i][amount_max] = matrice[i-1][amount_max]

    n = len(stocks)
    stocks_selection = []
    amount_wallet = 0
    while amount_max >= 0 and n >= 0:
        stock = stocks[n - 1]
        if matrice[n][amount_max] == matrice[n-1][amount_max-stock[1]] + stock[3]:
            stocks_selection.append(stock[0])
            amount_wallet += stock[1]
            amount_max -= stock[1]
        n -= 1
    amount_wallet = amount_wallet / 100
    benefits = matrice[-1][-1] / 10000
    end = time.time()
    print("_" * 70, f"\nLe portefeuille d'actions le plus rentable est le suivant: {amount_wallet}€"
                    f"\nLa valeur du portefeuille est de {amount_wallet}€ avec un bénéfice de {round(benefits,2)}€"
                    f"\nLe temps d'exécution du programme est de : {round((end - start), 2)}s\n")


stocks_market = [
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

dataset1 = read_csv_files("dataset1.csv")
dataset2 = read_csv_files("dataset2.csv")

dynamic(500, stocks_market)
dynamic(500, dataset1)
dynamic(500, dataset2)




