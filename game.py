from itemsname import item_dnames, localnames, good
from matchdecode import hero


def main():
    print(item_dnames, localnames)
    guess = good[0]
    if str(guess) == str(good[0]):
        print("U won", good[0])
    else:
        print("U lost ", good[0])


if __name__ == '__main__':
    main()
