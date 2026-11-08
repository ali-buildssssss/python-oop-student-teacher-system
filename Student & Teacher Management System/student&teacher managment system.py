class user:
    def __init__(self,name,age,user_id):
        self.name=name
        self.age=age
        self.user_id=user_id
        
    def show_info(self):
        print(f"the Name is: {self.name} and age is: {self.age} and user_id is: {self.user_id}")
    
class student(user):
    def __init__(self, name, age, user_id,department):
        super().__init__(name, age, user_id)
        
        self.department=department
        
        self.__marks=[]
    def add_marks(self, *marks):
        for mark in marks:
            if 0<=mark>=0:
              self.__marks.append(mark)
              print("marks added successfully")
            else:
                print("marks could not added")
            
                
        
    def get_marks(self):
        return self.__marks
    
    def show_marks(self):
        
        print(f"the marks of the students is: {self.get_marks()}")
        
        
    def calculate_grade(self):
        if not self.__marks:
            print("no marks")
        else:
            average=sum(self.__marks)/len(self.__marks)
            print(f"the average is: {average}")
            
            if average>=90:
                print("A+")
            elif average>=80:
                print("A")
            elif average>=70:
                print("B")
            elif average>=70:
                print("c")
            elif average>=60:
                print("D")
            elif average>=50:
                print("E")
            else:
                print("F")
                
                
    def show_student_info(self):
        self.show_info()
        self.show_marks()
        print(f"the department is:{self.department}" )
        print("the average/grade is:")
        self.calculate_grade()
        
class teacher(user):
    def __init__(self, name, age, user_id,subject):
        super().__init__(name, age, user_id)
        
        self.subject=subject
        
    def teacher_info(self):
        self.show_info()
        
        print(f"the name of the subjec is: {self.subject}")
        
student1=student("Ali",20,101,"Software Engineering")
student2=student("usama",25,102,"BBA")
student3=student("Zain",21,103,"Computer Science")
    
    
teacher1=teacher("Haider",30,202,"physics")
teacher2=teacher("Usman",35,203,"chemistry")


while True:
    print("enter 1 for students list")
    print("enter 2 for for teacher list")
    print("enter 3 for add marks ")
    print("enter 4 for grade ")
    print("enter 5 for quiting")
    
    try:
        choices=int(input("enter choices: "))
    except ValueError:
        print("float and text is not allowed")
        continue
    print(f"you enter the integer: {choices}")
    
    
    if choices==1:
        
        students=[student1,student2,student3]
        
        for studentss in students:
            studentss.show_student_info()
    elif choices==2:
        
        teachers=[teacher1,teacher2]
        
        for teacherss in teachers:
            teacherss.teacher_info()

    
    elif choices==3:
        student1.add_marks(100,50,60)
        student2.add_marks(90,50,60)
        student3.add_marks(60,70,80)
        
    elif choices==4:
        student1.calculate_grade()
        student2.calculate_grade()
        student3.calculate_grade()
    elif choices==5:
        print("quiting...")
        break
    else:
        print("invalid choice")    


