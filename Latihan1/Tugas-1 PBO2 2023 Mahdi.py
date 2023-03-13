#Mahdi
#210511030
#r1

class celcius:
    @staticmethod
    def to_fahrenheit(celcius):
        return (celcius * 9/5) + 32

    @staticmethod
    def to_kelvin(celcius):
        return celcius + 273.15

    @staticmethod
    def to_reamur(celcius):
        return celcius * 4/5

mycelcius = 80
myfarhenheit = celcius.to_fahrenheit(mycelcius)
mykelvin = celcius.to_kelvin(mycelcius)
myreamur = celcius.to_reamur(mycelcius)
print(myfarhenheit)
print(mykelvin)
print(myreamur)