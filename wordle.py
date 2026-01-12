###############################################################################################################
# ilos naweri

    mwvane = "\033[92m"
    yviteli = "\033[93m"
    nacrisferi = "\033[90m"
    reset = "\033[0m"

    result = [""] * 5
    used = [False] * 5

    for i in range(5):
        if guess[i] == secret_word[i]:
            result[i] = mwvane + "_" + reset
            used[i] = True

    for i in range(5):
        if result[i]:
            continue

        if guess[i] in secret_word:
            for j in range(5):
                if guess[i] == secret_word[j] and not used[j]:
                    result[i] = yviteli + "_" + reset
                    used[j] = True
                    break
            else:
                result[i] = nacrisferi + "_" + reset
        else:
            result[i] = nacrisferi + "_" + reset

    print(" ".join(result))

    if guess == secret_word:
        print(mwvane + "maige brat" + reset)
        break
else:
    print(f"waage brat ici sityva raiyooo haa? ai: {secret_word}")