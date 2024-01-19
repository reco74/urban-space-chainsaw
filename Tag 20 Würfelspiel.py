import random

def würfeln():
    return random.randint(1, 6)


def würfelspiel():    
    comWürfel = würfeln()
    spielWürfel = würfeln()


    print(f"Du hast eine {spielWürfel} gewürfelt")
    
    print(f"Der Computer hat eine {comWürfel} gewürfelt")

    if comWürfel > spielWürfel:
        print("Du verlierst")
    elif comWürfel < spielWürfel:
        print("Du gewinnst!!")
    else:
        print("Unentschieden!")

würfelspiel()