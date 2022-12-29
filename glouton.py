import time

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


def glouton(lst):
    start = time.time()
    lst = sorted(lst, key=lambda action: action[2], reverse=True)
    amount_max_wallet = 500
    wallet = []
    amount_wallet = 0
    benefits_wallet = 0
    amount_best_wallet = 0
    benefits_best_wallet = 0
    for action in lst:
        amount_wallet += action[1]
        benefits_wallet += action[1] * action[2]
        if amount_wallet <= amount_max_wallet:
            wallet.append(action[0])
            amount_best_wallet = amount_wallet
            benefits_best_wallet = benefits_wallet
    end = time.time()
    print("_" * 70, f"\nLe portefeuille d'actions le plus rentable est le suivant:")
    for share in wallet:
        print("-", share)
    print(f"\nLa valeur du portefeuille est de {amount_best_wallet}€ avec un bénéfice de {round(benefits_best_wallet, 2)}€"
          f"\nLe temps d'exécution du programme est de : {round((end - start))}s\n")


glouton(stock_market)





