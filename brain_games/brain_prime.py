import random
import prompt
def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(name))
    print('Answer "yes" if the number is prime, otherwise answer "no".')
    for i in range(0, 3):
        number = random.randint(0, 101)
        counter = 0
        for s in range(1, number + 1):
            if number % s == 0:
                counter += 1
        if counter == 2:
            true_answer = "yes"
        else:
            true_answer = "no"
        print("Question: {}".format(number))
        answer = str(input("Your answer: "))
        if answer == true_answer:
            print("Correct!")
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'\nLet's try again, {}".format(answer, true_answer, name))
            break
        if i == 2:
            print("Congratulations, {}".format(name))
    if __name__ == "__main__":
        main()