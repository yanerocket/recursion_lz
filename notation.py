def convert_to_base(n, base):
    if base < 2 or base > 16:
        return "Основание системы счисления должно быть от 2 до 16"

    digits = "0123456789ABCDEF"

    if n < base:
        return digits[n]
    else:
        return convert_to_base(n // base, base) + digits[n % base]

def main():

    print(convert_to_base(255, 16))
    print(convert_to_base(255, 2))

    print(convert_to_base(37, 9))

if __name__ == '__main__':
    main()

