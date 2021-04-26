import random
import prompt
def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(name))
    print("Find the greatest common divisor of given number.")
    for i in range(0, 3):
        first_num = random.randint(1, 100)
        second_num = random.randint(1, 100)
        print("Question: {} {}".format(first_num, second_num))
        answer = int(input("Your answer: "))
        while first_num != 0 and second_num != 0:    
            if first_num > second_num:
                first_num = first_num % second_num
            else:
                second_num = second_num % first_num
        true_answer =  first_num + second_num
        if answer == true_answer:
            print("Correct!")
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'\nLet's try again, {}".format(answer, true_answer, name))
            break
        if i == 2:
            print("Congratulations, {}".format(name))
    if __name__ == "__main__":
        main()


                    


