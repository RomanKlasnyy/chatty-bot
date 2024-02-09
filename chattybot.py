class Bot:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def greet(self):
        print('Hello! My name is ' + self.name + '.')
        print('I was created in ' + self.birth_year + '.')

    def remind_name(self):
        print('Please, remind me your name.')
        self.user_name = input()
        print('What a great name you have, ' + self.user_name + '!')

    def guess_age(self):
        print('Let me guess your age.')
        print('Enter remainders of dividing your age by 3, 5, and 7.')

        rem3 = int(input())
        rem5 = int(input())
        rem7 = int(input())
        age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

        print("Your age is " + str(age) + "; that's a good time to start programming!")

    def count(self):
        print('Now I will prove to you that I can count to any number you want.')

        num = int(input())
        curr = 0
        while curr <= num:
            print(curr, '!')
            curr += 1

    def test(self):
        print("Let's test your programming knowledge.")
        print('Why do we use methods?')
        print('1. To repeat a statement multiple times.')
        print('2. To decompose a program into several small subroutines.')
        print('3. To determine the execution time of a program.')
        print('4. To interrupt the execution of a program.')
        while True:
            answer = input()
            if answer == '2':
                print('Completed, have a nice day!')
                break
            else:
                print('Please, try again.')

    @staticmethod
    def end():
        print('Congratulations, have a nice day!')


if __name__ == "__main__":
    # Usage
    bot = Bot('Aid', '2020')
    bot.greet()
    bot.remind_name()
    bot.guess_age()
    bot.count()
    bot.test()
    Bot.end()
