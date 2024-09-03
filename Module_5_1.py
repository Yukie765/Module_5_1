class House:
    def __init__(self, Name, Num_of_floors):
        self.name = Name
        self.num_of_floors = Num_of_floors

    def go_to(self, Floor):
        if Floor < 1 or Floor > self.num_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1,Floor+1):
                print(i)

new_house1 = House('ЖК Эльбрус', 30)
new_house2 = House('ЖК Горский', 18)
new_house3 = House('Домик в деревне', 2)
new_house2.go_to(5)
new_house3.go_to(10)