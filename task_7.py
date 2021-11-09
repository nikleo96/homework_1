import time


def print_promo():
    print("Реклама")


def start_promo(promo):
    while True:
        promo()
        time.sleep(5)
        start_promo(promo)

start_promo(print_promo)