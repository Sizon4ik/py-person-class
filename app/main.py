class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(person.get("name"), person.get("age")))

    for info in people:
        if info.get("wife") is not None:
            wife_name = info.get("wife")
            husband_name = info.get("name")
            for person in person_list:
                if person.name == husband_name:
                    person.wife = Person.people.get(wife_name)
                if person.name == wife_name:
                    person.husband = Person.people.get(husband_name)

    return person_list
