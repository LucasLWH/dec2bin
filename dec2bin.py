def dec2bin(dec_val):
    opt_val = int(dec_val)
    unreversed_result = []
    final_result = ''
    while opt_val > 0:
        unreversed_result.append(str(opt_val %2))
        opt_val = opt_val//2
    reverse = unreversed_result[::-1]
    for elements in reverse:
        final_result += elements
    print('Base 2 Value:',final_result)

if __name__ == "__main__":
    print('You can also import this. Text Interface currently in use:')
    dec2bin(input('Enter decimal number: '))
