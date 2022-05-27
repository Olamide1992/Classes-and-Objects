class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
       # print("This is the student's info: His name is ", name, "age is ", age, "while his track is ", tracks, "and his score is ", score)
        
    #method
    def change_name(self, name):
        self.name = name
        print("This is the change_name function", self.name)
    def change_age(self, age):
        self.age = age
        print("This is the change_age function", self.age)
    def add_track(self, tracks):
        self.tracks.append(tracks)
        print("This is the add track function", self.tracks)
    def get_score(self):
        print("This is the get score function", self.score)


#calling a class
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
