class quiz():
    def __init__(self):
        self.score = 0

    def start(self):
        # Subject: What's that pokemon?!
        y = input("What's that Pokemon?!? \n"
        "Do you know them all? \n"
        "Answer by entering a b c d or e")
        

    def q1(self):
        # Answer: It's Pikachu! 
        while True:
            y = input("Which pokemon is a rat, with a chubby belly (in the original card game)? \n"
            "A. It's Pikachu! \n"
            "B. It's Rattata! \n")
            y = y.lower()
            if y == True and y == "a":
                self.score += 1
                return False
            elif y == True and y == "b":
                return False
            else:
                print("Sorry, what was that?")
                return True


    def q2(self):
        # Answer: It's Psyduck!
        y = input("Which pokemon has non-stop headaches? \n"
        "A. It's Psyduck! \n"
        "B. It's Porygon! \n"
        )

    def q3(self):
        # Answer: It's Solgaleo!
        y = input("which pokemon was NOT released in Black and White? \n"
        "A. It's Zekrom! \n"
        "B. It's Solgaleo! \n"
        "C. It's Reshiram! \n")

    def q4(self):
        # Answer: It's Bulbasaur!
        y = input("Based off stats, who was the best pokemon to choose in the beggining of Pokemon Red and Blue? \n"
        "A. It's Squirtle! \n"
        "B. It's Charmander! \n"
        "C. It's Bulbasaur! \n")

    def q5(self):
        #Answer: It's Eevee!
        y = input("Which pokemon has the most options when it comes to evolution?  \n"
        "A. It's Pansear! \n"
        "B. It's Panpour! \n"
        "C. It's Pansage! \n"
        "D. It's Eevee! \n")

    def q6(self):
        # Answer: It's Gloom!
        y = input("When exposed to a leaf stone, what does Vileplume evolve into? \n"
        "A. It's Bellossom! \n"
        "B. It's Carnivine! \n"
        "C. Gloom \n"
        "D. Oddish \n")

    def q7(self):
        # Answer: They are all right (all tiny pokemon are cute, fight me)!
        y = input("Which pokemon is the cuttests? \n"
        "A. It's Jigglypuff! \n"
        "B. Is's Eevee! \n"
        "C. It's Buneary! \n"
        "D. It's Minccino! \n"
        "E. It's Rockruff! \n")

def run():
    x = quiz()
    x.q1()
    x.q2()
    x.q3()
    x.q4()
    x.q5()
    x.q6()
    x.q7()
    print(f"You got {x.score}/7 correct!")

run()
print("Thanks For Playing, and have a wonderful day!")