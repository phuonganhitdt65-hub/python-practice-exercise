def input_list():
    return list(map(int, input("Enter numbers separated by space: ").split()))

def exercise_1():
    numbers = input_list()
    print("Sum:", sum(numbers))

def exercise_2():
    numbers = input_list()
    print("Average:", sum(numbers) / len(numbers))
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))

def exercise_3():
    numbers = input_list()
    value = int(input("Enter value: "))
    print("Exists" if value in numbers else "Not exists")

def exercise_4():
    numbers = input_list()
    value = int(input("Enter value: "))
    if value in numbers:
        print("First index:", numbers.index(value))
    else:
        print("Not found")

def exercise_5():
    numbers = input_list()
    value = int(input("Enter value: "))
    if value in numbers:
        print("Last index:", len(numbers) - 1 - numbers[::-1].index(value))
    else:
        print("Not found")

def exercise_6():
    numbers = input_list()
    value = int(input("Enter value: "))
    print("Count:", numbers.count(value))

def exercise_7():
    numbers = input_list()
    value = int(input("Enter value: "))
    if value in numbers:
        numbers.remove(value)
    print("Updated list:", numbers)

def exercise_8():
    numbers = input_list()
    value = int(input("Enter value: "))
    numbers = [x for x in numbers if x != value]
    print("Updated list:", numbers)

def exercise_9():
    numbers = input_list()
    print("Unique set:", set(numbers))

def exercise_10():
    numbers = input_list()
    numbers.reverse()
    print("Reversed list:", numbers)

def exercise_11():
    numbers = input_list()
    numbers.sort()
    print("Ascending:", numbers)

def exercise_12():
    numbers = input_list()
    numbers.sort(reverse=True)
    print("Descending:", numbers)

def exercise_13():
    A = input_list()
    B = input_list()
    print("Intersection:", list(set(A) & set(B)))

def exercise_14():
    A = input_list()
    B = input_list()
    print("Union:", list(set(A) | set(B)))

def exercise_15():
    numbers = input_list()
    for x in set(numbers):
        print(x, "appears", numbers.count(x), "times")

def main():
    while True:
        print("\n--- MENU ---")
        print("1  - Sum of elements")
        print("2  - Average, Max, Min")
        print("3  - Check existence")
        print("4  - First index")
        print("5  - Last index")
        print("6  - Count occurrences")
        print("7  - Remove first occurrence")
        print("8  - Remove all occurrences")
        print("9  - Unique set")
        print("10 - Reverse list")
        print("11 - Sort ascending")
        print("12 - Sort descending")
        print("13 - Intersection of two lists")
        print("14 - Union of two lists")
        print("15 - Count each value")
        print("0  - Exit")

        choice = int(input("Choose exercise: "))

        if choice == 0:
            break
        elif choice == 1: exercise_1()
        elif choice == 2: exercise_2()
        elif choice == 3: exercise_3()
        elif choice == 4: exercise_4()
        elif choice == 5: exercise_5()
        elif choice == 6: exercise_6()
        elif choice == 7: exercise_7()
        elif choice == 8: exercise_8()
        elif choice == 9: exercise_9()
        elif choice == 10: exercise_10()
        elif choice == 11: exercise_11()
        elif choice == 12: exercise_12()
        elif choice == 13: exercise_13()
        elif choice == 14: exercise_14()
        elif choice == 15: exercise_15()
        else:
            print("Invalid choice")

main()
