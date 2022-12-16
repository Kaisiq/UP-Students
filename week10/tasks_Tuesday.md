# Задачи върху ООП принципите в Python

## Задача №1:

Създайте клас `Vehicle`, който:
* притежава следните характеристики: `name`, `max_speed`, `mileage`, `__car_id`
* има следните свойства:
* * `get_car_id(self)` -> връща стойността на __car_id
* * `vehicle_capacity(self, capacity)` -> връща подходящо съобщение с информация за колата и нейната вместимост
* * `__repr__(self)` -> връща подходящо съобщение с данните на обектите от класа `Vehicle`

### Решение:
```py
class Vehicle:
    def __init__(self, name, max_speed, mileage, car_id):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.__car_id = car_id

    def get_car_id(self):
        return self.__car_id

    def vehicle_capacity(self, capacity):
        return f"The capacity of {self.name} is {capacity}"

    def __repr__(self):
        return f"{self.name}, {self.max_speed}, {self.mileage}, {self.__car_id}"


v1 = Vehicle("Volvo", 200, 2500, 12345)
print(v1)
print(v1.get_car_id())
print(v1.vehicle_capacity(5))
```

## Задача №2:
Създайте класовете `Bus` и `Train` (дъщерни класове на класа `Vehicle`), които:
* наследяват атрибутите на своя родителски клас и освен това притежават характеристиката `vehicletype`
* съдържат същите методи, но връщат различно съобщения спрямо тези в родителския клас

## Задача №3:
Създайте абстрактен клас `Objects3D`, който съдържа абстрактните методи `lsa`, `tsa` и `volume` (методи съответно за пресмятане на околна повърхнина, пълна повърхнина и обем на фигура). Създайте 3 подкласа на дадения клас (например `Cube`, `Pyramid`, `Cylinder`), на които да могат да се изчислят стойностите на `lsa`, `tsa`, `volume`.
