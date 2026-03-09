people = [
    {"name": "AliCe", "age": 30},
    {"name": "Leo", "age": 7},
    {"name": "BoB", "age": 25},
    {"name": "Mia", "age": 14},
    {"name": "CHarlie", "age": 35},
    {"name": "DiaNa", "age": 22},
    {"name": "ethan", "age": 17},
    {"name": "FiOna", "age": 42},
    {"name": "GABE", "age": 18},
    {"name": "Hannah", "age": 28}
]

def main():
    for person in people:
        person["name"] = person["name"].lower().capitalize()

    children = [person for person in people if person["age"] < 18]
    adults = [person for person in people if person["age"] >= 18]
    name3letters = [person for person in people if len(person["name"]) == 3]

    children.sort(key=lambda age: age["age"])
    adults.sort(key=lambda age: age["age"])
    name3letters.sort(key=lambda letter: letter["name"])

    for child in children:
        print(child["name"], child["age"])
    print("-----")
    for adult in adults:
        print(adult["name"], adult["age"])
    print("-----")
    for person in name3letters:
        print(person["name"], person["age"])

if __name__ == "__main__":
    main()
    