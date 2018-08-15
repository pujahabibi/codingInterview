class AnimalShelter:
    def __init__(self):
        self.items = []
    def enqueue(self, type, name):
        item = {"Type": type, "Name": name}
        self.items.append(item)
    def is_empty(self):
        return self.items == []
    def dequeueAny(self):
        if self.is_empty() == True:
            return "The animal shelter is already empty"
        self.items.pop(0)
    def dequeueCat(self):
        for i in range(len(self.items)):
            if self.items[i]['Type'] == "Cat":
                del self.items[i]
                break
    def dequeueDog(self):
        for i in range(len(self.items)):
            if self.items[i]['Type'] == "Dog":
                del self.items[i]
                break
    def len_shelter(self):
        return len(self.items)

am = AnimalShelter()
am.enqueue("Cat", "Kitty")
am.enqueue("Dog", "Reggie")
am.enqueue("Dog", "John")
am.enqueue("Dog", "Don")
am.enqueue("Cat", "Roger")
print(am.items)
am.dequeueDog()
print(am.items)