import pickle

class Person:
    def __init__(self, name, ID, age):
        self.name = name
        self.ID = ID
        self.age = age
        
    def serialize(self):
        with open('person.pickle', 'wb') as f:
            pickle.dump(Person, f)

    @staticmethod
    def deserialize():
        with open('person.pickle', 'rb') as f:
            return pickle.load(f)