def print_formatted(number):
    """
    This function will convert and print the binary number.
    """
    n10 = number
    # convert n10 to octal
    number_binary = bin(n10)
    number_binary = number_binary[2:]
    n2_len = len(number_binary)
    # print every value in the list with the space from n2_len
    for i in range(1, n10 + 1):
        n8 = oct(i)
        n8 = n8[2:]
        # convert n10 to hexadecimal
        n16 = hex(i)
        n16 = n16[2:]
        # convert n10 to binary
        number_binary = bin(i)
        number_binary = number_binary[2:]
        print(str(i).rjust(n2_len), end=" ")
        print(str(n8).rjust(n2_len), end=" ")
        print(str(n16.upper()).rjust(n2_len), end=" ")
        print(str(number_binary).rjust(n2_len))


if __name__ == '__main__':
    n = 17
    print_formatted(n)
