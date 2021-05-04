import random
import prompt
def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(name))
    print("What number is missing in the progression?")  
    for i in range(0, 3):
        start = random.randint(5, 15)
        end = random.randint(16, 100)
        step = random.randint(2, 10)
        prog = list(range(start, end, step))
        i_end = prog.index(prog[-1])
        index = random.randint(0, i_end)
        true_answer = prog.pop(index)
        prog.insert(index, '...')
        print('Question: {}'.format(prog))
        answer = int(input('Your answer: '))
        if answer == true_answer:
            print("Correct!")
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'\nLet's try again, {}".format(answer, true_answer, name))
            break
        if i == 2:
            print("Congratulations, {}".format(name))
    if __name__ == "__main__":
        main()

        