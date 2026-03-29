import termcolor
from logic import * # logic is from CS50 course

class Detective:
    def __init__(self):
        self.suspects = [
            "Col. Mustard",
            "Prof. Plum",
            "Ms. Scarlet"
        ]
        self.knowledge = And(Or(
            Symbol(self.suspects[0]), 
            Symbol(self.suspects[1]), 
            Symbol(self.suspects[2])          
        ))

    def eliminate_suspect(self, name:str):
        for suspect in range(0, len(self.suspects)):
            if name == self.suspects[suspect]:
                self.suspects.pop(suspect)
                self.knowledge.add(Not(Symbol(name)))
                print(f"{name} is removed from suspect list")
                return 
        print(f"{name} is not in suspect list")

    def _check_knowledge(self):
        for suspect in self.suspects:
            if model_check(self.knowledge, Symbol(suspect)):
                termcolor.cprint(f"{suspect}: KILLER", "green")
            elif not model_check(self.knowledge, Not(Symbol(suspect))):
                print(f"{suspect}: MAYBE")

    def who_is_the_killer(self):
        if len(self.suspects) == 0:
            self._check_knowledge()
            print(f"Logic error, nobody left")
        elif len(self.suspects) == 1:
            self._check_knowledge()
            print(f"Killer found: {self.suspects[0]}")
        else:
            self._check_knowledge()
            print("Not enough proof for now")

print("-----")
detective = Detective()
detective.who_is_the_killer()
print("-----")
detective.eliminate_suspect("Elon Musk") # to check names outside of suspect list
print("-----")
detective.who_is_the_killer()
print("-----")
detective.eliminate_suspect("Ms. Scarlet") 
detective.who_is_the_killer()
print("-----")
detective.eliminate_suspect("Prof. Plum") 
detective.who_is_the_killer() # killer is Col. Mustard
print("-----")
detective.eliminate_suspect("Col. Mustard") 
detective.who_is_the_killer() # checking the logic error
print("-----")