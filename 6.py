def calculate_average(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)


numbers1 = [55, 105, 150, 202]
average1 = calculate_average(*numbers1)
print(f"sredn snach chisel {numbers1}: {average1}")