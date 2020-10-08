# python3

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    first_max_number = max(numbers)
    numbers.pop(numbers.index(first_max_number))
    second_max_number = max(numbers)

    return first_max_number * second_max_number


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
