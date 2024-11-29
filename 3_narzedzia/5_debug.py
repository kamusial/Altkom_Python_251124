def factorial(n):
    if n < 0:
        raise ValueError("Liczba musi być nieujemna")
    result = 1
    import ipdb
    ipdb.set_trace()
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    try:
        num = int(input("Podaj liczbę do obliczenia silni: "))
        print(f"Silnia z {num} wynosi: {factorial(num)}")
    except ValueError as e:
        print(f"Błąd: {e}")

if __name__ == "__main__":
    main()