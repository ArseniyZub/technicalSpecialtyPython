class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        return "Woof!"

class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def speak(self):
        return "Mew!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, **kwargs):
        if animal_type == 'dog':
            return Dog(**kwargs)
        elif animal_type == 'cat':
            return Cat(**kwargs)

dog_params = {'name': 'doggi', 'breed': 'Retriever'}
cat_params = {'name': 'catti', 'color': 'Gray'}

dog = AnimalFactory.create_animal('dog', **dog_params)
cat = AnimalFactory.create_animal('cat', **cat_params)

print(f"name: {dog.name} \n breed: {dog.breed} \n speak: {dog.speak()} \n ")  
print(f"name: {cat.name} \n color: {cat.color} \n speak: {cat.speak()}")  