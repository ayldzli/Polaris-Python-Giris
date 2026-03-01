from random import randint

class Assistant:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.__process_count = 0

    def __str__(self):
        return f"{self.name}"

    def greet(self, user):
        print(f"Hi {user}, I am {self.name}. How can I help you?")
        self.__process_count += 1

    def is_this_true(self, question):
        print(f"You asked: {question}")
        random_num = randint(1, 2)
        if random_num == 1:
            print("Yes")
        else:
            print("No")
        self.__process_count += 1

    def status_report(self):
        print(f"You called me for {self.__process_count} times so far.")

def test():
    grok = Assistant("Grok")
    print(grok)
    grok.status_report()
    grok.greet("0_0")
    grok.greet("o_0")
    grok.status_report()
    grok.is_this_true("Is MATE the best club in YTU?")
    grok.status_report()
    grok.__process_count = 10 #process count dışarıdan değiştirilemiyor
    grok.status_report()

if __name__ == "__main__":
    test()