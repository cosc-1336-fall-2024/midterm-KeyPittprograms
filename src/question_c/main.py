from question_c import get_sum_of_evens

def main():
    while True:
        quit = input("Do you want to quit? (Y/N): ").lower()
        if quit == 'n':
            num = int(input("give number: "))
            result = get_sum_of_evens(num)
            print(f"The sum of even numbers up to {num} is {result}")
        elif quit == 'y':
            print("Quit")
            break
        else:
            print("Invalid")    
main()            