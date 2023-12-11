class Developer:
    def __init__(self, name, age, level):
        self.name = name
        self.age= age
        self.level = level
        
    

    def get_infr(self):
        return (self.name, self.age)
    
    def code(self):
        print(f"My name is{self.name}, I am {self.age} years old.")

    def language(self, language):
        print(f"{self.name} codes in {language}")


    def __str__(self):
        info = f"name = {self.name}, level = {self.level}, years ={self.level}"
            
        return info

    
    @staticmethod
    def salary(age):
        if age < 24:
            print(3000)
        elif age<30:
            print(5000)

        
se1 = Developer("Ugo", 23, "lv1")
se2 = Developer("Ugo", 23, "lv1")
se3 = Developer("ij", 30, "lv5")

se1.code()
print(se2.get_infr())
se3.salary(25)
se2.language("Javascript")
Developer.code(se1)

print(se1)