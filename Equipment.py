import pickle


class Equipment():
    def __init__(self ,ID, quantity, name):
        self.ID = ID
        self.quantity = quantity
        self.name = name
        

    
    def serialize(self):
        with open('equipment.pickle', 'wb') as f:
            pickle.dump(Equipment, f)

    @staticmethod
    def deserialize():
        with open('equipment.pickle', 'rb') as f:
            return pickle.load(f)