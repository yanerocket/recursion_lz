def Euclid(num1, num2):
    if num1 == 0:
        return num2
    return Euclid(num2 % num1, num1)
def main():
    number_1 = input("Введите первое число ")
    number_2 = input("Введите второе число ")
    print(f"Их наибольший общий делитель: {Euclid(int(number_1), int(number_2))}")

if __name__ == '__main__':
    main()

