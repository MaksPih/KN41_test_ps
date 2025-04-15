def print_list_elements(numbers):
    for num in numbers:
        print(num)
    return True

if __name__ == "__main__":
    example = [1, 2, 3, 4, 5]
    print("Результат функції:", print_list_elements(example))