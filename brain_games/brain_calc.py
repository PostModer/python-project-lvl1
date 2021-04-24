import random
import prompt
def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(name))
    print("What is the result of the expression?")
    for i in range(0, 3):
        a = random.randint(0, 15)
        b = random.randint(0, 15)
        list_of_operations = ["+", "-", "*"]
        operation = random.choice(list_of_operations)
        if operation == "+":
            true_answer = a + b
        elif operation == "-":
            true_answer = a - b
        else: 
            true_answer = a * b
        print("Question: {} {} {}".format(a, operation, b))
        answer = int(input("Your answer: "))
        if answer == true_answer:
            print("Correct!")
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'\nLet's try again, {}!".format(answer, true_answer, name))
            break
        if i == 2:
            print("Congratulations, {}".format(name))
    if __name__ == "__main__":
        main()


