class quiz():
    def __init__(self):
        self.score = 0

    def start(self):
        # Subject: What's that pokemon?!
        print("What's that Pokemon?!? \n"
        "Do you know them all? \n"
        "Answer by entering a b c d or e")
        

    def q1(self):
        a = True
        while a == True:
            y = input("Which pokemon is a rat, with a chubby belly (in the original card game)? \n"
            "A. It's Pikachu! \n"
            "B. It's Rattata! \n")
            z = y.lower()
            if z == "a":
                self.score += 1
                print("It's Pikachu!")
                a = False
            elif z == "b":
                print("It's Pikachu!")
                a = False
            else:
                print("Sorry, what was that?")
                a = True


    def q2(self):
        a = True
        while a == True:
            y = input("Which pokemon has non-stop headaches? \n"
            "A. It's Psyduck! \n"
            "B. It's Porygon! \n")
            z = y.lower()
            if z == "a":
                self.score += 1
                print("It's Psyduck!")
                a = False
            elif z == "b":
                print("It's Psyduck!")
                a = False
            else:
                print("Sorry, what was that?")
                a = True

    def q3(self):
        a = True
        while a == True:
            y = input("which pokemon was NOT released in Black and White? \n"
            "A. It's Zekrom! \n"
            "B. It's Solgaleo! \n"
            "C. It's Reshiram! \n")
            z = y.lower()
            if z == "a":
                print("It's Solgaleo!")
                a = False
            elif z == "b":
                print("It's Solgaleo!")
                self.score += 1
                a = False
            elif z == "c":
                print("It's Solgaleo!")
                a = False
            else:
                print("Sorry, what was that?")
                a = True

    def q4(self):
        a = True
        while a == True:
            y = input("Based off stats, who was the best pokemon to choose in the beggining of Pokemon Red and Blue? \n"
            "A. It's Squirtle! \n"
            "B. It's Charmander! \n"
            "C. It's Bulbasaur! \n")
            z = y.lower()
            if z == "a":
                print("It's Bulbasaur!")
                a = False
            elif z == "b":
                print("It's Bulbasaur!")
                a = False
            elif z == "c":
                print("It's Bulbasaur!")
                self.score += 1
                a = False
            else:
                print("Sorry, what was that?")
                a = True

    def q5(self):
        a = True
        while a == True:
            y = input("Which pokemon has the most options when it comes to evolution?  \n"
            "A. It's Pansear! \n"
            "B. It's Panpour! \n"
            "C. It's Pansage! \n"
            "D. It's Eevee! \n")
            z = y.lower()
            if z == "a":
                print("It's Eevee!")
                a = False
            elif z == "b":
                print("It's Eevee!")
                a = False
            elif z == "c":
                print("It's Eevee!")
                a = False
            elif z == "d":
                print("It's Eevee!")
                self.score += 1
                a = False
            else:
                print("Sorry, what was that?")
                a = True

    def q6(self):
        a = True
        while a == True:
            y = input("When exposed to a leaf stone, what does Vileplume evolve into? \n"
            "A. It's Bellossom! \n"
            "B. It's Carnivine! \n"
            "C. Gloom \n"
            "D. Oddish \n")
            z = y.lower()
            if z == "a":
                print("It's Gloom!")
                a = False
            elif z == "b":
                print("It's Gloom!")
                a = False
            elif z == "c":
                print("It's Gloom!")
                self.score += 1
                a = False
            elif z == "d":
                print("It's Gloom!")
                a = False
            else:
                print("Sorry, what was that?")
                a = True

    def q7(self):
        a = True
        while a == True:
            y = input("Which pokemon is the cuttests? \n"
            "A. It's Jigglypuff! \n"
            "B. Is's Eevee! \n"
            "C. It's Buneary! \n"
            "D. It's Minccino! \n"
            "E. It's Rockruff! \n")
            z = y.lower()
            if z == "a":
                print("They are all right (all tiny pokemon are cute, fight me)!")
                self.score += 1
                a = False
            elif z == "b":
                print("They are all right (all tiny pokemon are cute, fight me)!")
                self.score += 1
                a = False
            elif z == "c":
                print("They are all right (all tiny pokemon are cute, fight me)!")
                self.score += 1
                a = False
            elif z == "d":
                print("They are all right (all tiny pokemon are cute, fight me)!")
                self.score += 1
                a = False
            elif z == "e":
                print("They are all right (all tiny pokemon are cute, fight me)!")
                self.score += 1
                a = False
            else:
                print("Sorry, what was that?")
                a = True

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