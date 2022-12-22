from itertools import chain, combinations
import time


def comb_list(list_name):
    s = list(list_name)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def bruteforce(lst):
    best_wallet = ""
    best_amount_wallet = 0
    best_benefits = 0
    for solution in comb_list(lst):
        wallet = ""
        benefits_wallet = 0
        amount_wallet = 0
        for stock_market in solution:
            amount_wallet += stock_market[1]
            benefits_wallet += stock_market[2] * stock_market[1]
            wallet += f"{stock_market[0]}, "
        if amount_wallet <= 500 and best_benefits < benefits_wallet:
            best_wallet = wallet
            best_amount_wallet = amount_wallet
            best_benefits = benefits_wallet
    return best_wallet, best_amount_wallet, best_benefits


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

start = time.time()
wallet_stock_market, amount_wallet, benefits = bruteforce(stock_market)
end = time.time()
print(f"Le portefeuille d'actions le plus rentable est le suivant: \n{wallet_stock_market}\nd'une valeur de "
      f"{amount_wallet}€ et avec un bénéfice de {benefits}€")

print("\nLe temps d'execution du programme est de :",
      (end-start) * 10**3, "ms")
