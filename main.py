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


def brute_force(lst, i=1, best_wallet=None, benefits_wallet=0):
    benefits = 0
    if i <= len(lst):
        print(i)
        wallet = []
        montant_portefeuille = 0
        for action in lst[i:]:
            montant_portefeuille += action[1]
            print(montant_portefeuille)
            benefits += action[1] * action[2]
            print(benefits)
            if montant_portefeuille <= 500 and benefits > benefits_wallet:
                wallet.append(action[0])
                print(wallet)
                benefits_wallet = benefits
                best_wallet = wallet
        brute_force(lst, i + 1, best_wallet, benefits_wallet)
    return best_wallet, benefits_wallet


wallet, benefit = brute_force(stock_market)
print(wallet, benefit)
