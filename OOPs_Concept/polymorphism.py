# Sample 1
class it:
    def student(self):
        print("Abinesh")

class cse:
    def student(self):
        print("Yazhini")

std1 = it()
std = cse()

std1.student()
std.student()

# Sample 2
class dept1:
    def __init__(self,name,dept):
        self.name = name
        self.dept = dept

    def studs(self):
        return (f"Student name is {self.name} and from the department of {self.dept}")


class dept2:
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    def studs(self):
        return (f"Student name is {self.name} and from the department of {self.dept}")

std1 = dept1("Abinesh","IT")
std = dept2("Yazhini","CSE")

print(std1.studs())
print(std.studs())

