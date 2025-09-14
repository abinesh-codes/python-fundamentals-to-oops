# Single Inheritance
print ("Single Inheritance")

class parent:
    def show(self):
        print(f"Welcome to my channel")

class child(parent):
    def son(self):
        print(f"Take the chappel")

c = child()
c.show()
c.son()

# Multi-level Inheritance
print("Multi-level Inheritance")

class grandparent:
    def thatha(self):
        print("HI")

class parent(grandparent):
    def appa(self):
        print("Hello")

class child(parent):
    def daughter(self):
        print("Guy")

x = child()
x.thatha()
x.appa()
x.daughter()

# Multiple Inheritance
print("\nMultiple Inheritance")

class father:
    def appa(self):
        print("Appa")

class mother:
    def amma(self):
        print("Amma")

class child(father,mother):
    def paiyan(self):
        print("Magan")

z =child()
z.appa()
z.amma()
z.paiyan()

# Hierarchical Inheritance
print("\nHierarchical Inheritance")

class parent:
    def show(self):
        print("What Bro its very?")

class child1(parent):
    def skil(self):
        print("Wrong bro")

class child2(parent):
    def skill(self):
        print("What uncle ?")

d1 = child1()
d2 =child2()

d1.show()
d2.show()

d1.skil()
d2.skill()

# Hybrid Inheritance
print("\nHybrid Inheritance")

class A:
    def feature(self):
        print("Features from A")

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

X = D()  # Hybrid use the both the Multi-level + Multiple Inheritance
X.feature()




# Sample program of Inheritance
print("The sample for the whole concept in the inheritance")
# Single
class person:
    def __init__(self,name):
        self.name = name

class employee(person):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary = salary

# Multiple
class job:
    def __init__(self,role):
        self.role =role

class employeejob(employee,job):
    def __init__(self,name,salary,role):
        employee.__init__(self,name,salary)
        job.__init__(self,role)

#Multi-Level
class manager(employeejob):
    def __init__(self,name,salary,role,department):
        employeejob.__init__(self,name,salary,role)
        self.department = department

# Hierarchical Inheritance
class assistantmanager(employeejob):
    def __init__(self,name,salary,role,team_size):
        employeejob.__init__(self,name,salary,role)
        self.team_size = team_size

# Hybrid Inheritance

class seniormanager(manager,assistantmanager):
    def __init__(self,name,salary,role,department,team_size):
        manager.__init__(self,name,salary,role,department)
        assistantmanager.__init__(self,name,salary,role,team_size)

# Single Inheritance
emp = employee("John", 40000)
print(emp.name, emp.salary)

# Multiple Inheritance
emp2 = employeejob("Alice", 50000,"DevOps")
print(emp2.name, emp2.salary)

# Multilevel Inheritance
mgr = manager("Bob", 60000, "HR" , "Management")
print(mgr.name, mgr.salary, mgr.department)

# Hierarchical Inheritance
asst_mgr = assistantmanager("Charlie", 45000, "Dev",20)
print(asst_mgr.name, asst_mgr.salary, asst_mgr.team_size)

# Hybrid Inheritance
sen_mgr = seniormanager("David", 70000, "Finance", "SDE", 5)
print(sen_mgr.name, sen_mgr.salary, sen_mgr.department, sen_mgr.team_size)