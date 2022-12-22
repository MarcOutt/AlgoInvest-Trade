import time

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


def dynamic(amount_max, stocks):
    matrice = [[0 for x in range(amount_max + 1)] for x in range(len(stocks) + 1)]

    for i in range(1, len(stocks) + 1):
        stocks[i - 1].append(stocks[i - 1][1] * stocks[i - 1][2])
        for amount in range(1, amount_max + 1):
            if stocks[i - 1][1] <= amount:
                matrice[i][amount] = max(stocks[i - 1][3] + matrice[i - 1][amount - stocks[i - 1][1]], matrice[i - 1][amount])
            else:
                matrice[i][amount] = matrice[i-1][amount]

    amount = amount_max
    n = len(stocks)
    stocks_selection = []
    amount_wallet = 0
    while amount >= 0 and n >= 0:
        stock = stocks[n - 1]
        if matrice[n][amount] == matrice[n-1][amount-stock[1]] + stock[3]:
            stocks_selection.append(stock[0])
            amount_wallet += stock[1]
            amount -= stock[1]
        n -= 1
    return stocks_selection, amount_wallet, matrice[-1][-1]


start = time.time()
wallet, amount_wallet, benefits = dynamic(500, stocks_market)
end = time.time()


print(f"Le portefeuille d'actions le plus rentable est le suivant: \n{wallet}\nd'une valeur de "
      f"{amount_wallet}€ et avec un bénéfice de {benefits}€")

print("\nLe temps d'execution du programme est de :",
      (end-start) * 10**3, "ms")