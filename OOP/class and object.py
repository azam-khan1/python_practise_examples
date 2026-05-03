class college:
    def __init__(self,name,roll,id):
        self.name = name
        self.roll = roll
        self.id = id

std = college("khan","233","ai")
print(std.name,std.id,std.roll)

class student:
    def __init__ (self,name,id):
        self.name = name
        self.id = id
std_name = input("enter student name: ")
std_id = input("enter student id : ")
std = student(std_name,std_id)
print(f"student name is {std_name} and his id is {std_id}")
