from enum import Enum
import random
            
class CategoryEnum(Enum):
    Desterity = 0
    Aerial = 1
    Transaction = 2
    HandleSwitch = 3
    Spin =4    


class LevelEnum(Enum):
    Begginer = 0
    Intermediate = 1
    Advanced = 2
    Expert = 3
    Master = 4
    
class Grip(Enum):
    Basic = 0
    Reversed =1
    Pen = 2

class Handle(Enum):
    Safe=0
    Bite =1

class GripHandle:
    def __init__(self,grip =Grip.Basic,handle =Handle.Safe) -> None:
        self.Grip = grip
        self.Handle = handle
        self.GripHandleCode = self.GetGripHandleCode()
    
    def __init__(self,grip:int =0,handle:int =0) -> None:
        self.Grip = Grip(grip)
        self.Handle = Handle(handle)
        self.GripHandleCode = self.GetGripHandleCode()
        
    def GetGripHandleCode(self):
        return (self.Grip.value + self.Handle.value)
    
    def to_dict(self):
        return (self.Grip, self.Handle)

class BaliTrick:
    def __init__(self, id=0, Name="PlaceHolder", StartGrip:GripHandle= GripHandle(), EndGrip:GripHandle=GripHandle(),
                 Difficulty=1, Coolness=1,Category=CategoryEnum.Desterity, level=LevelEnum.Begginer) -> None:
        self.id = id
        self.Name = Name
        self.StartGrip:GripHandle = StartGrip
        self.EndGrip:GripHandle = EndGrip
        self.Difficulty = Difficulty
        self.Coolness = Coolness
        self.Category = Category
        self.Level = level
        
    def __init__(self, id=0, Name="PlaceHolder", StartGrip:(int,int)=(0,0), EndGrip:(int,int)=(0,0),
                 Difficulty=1,  Coolness=1,Category:int=0, Level:int=0) -> None:
        self.id = id
        self.Name = Name
        self.StartGrip:GripHandle =  GripHandle(StartGrip[0],StartGrip[1])
        self.EndGrip:GripHandle = GripHandle(EndGrip[0],EndGrip[1])
        self.Difficulty = Difficulty
        self.Coolness = Coolness
        self.Category = CategoryEnum(Category)
        self.Level = LevelEnum(Level)
        
    def to_dict(self):
        return {
            "id": self.id,
            "Name": self.Name,
            "StartGrip": (self.StartGrip.Grip, self.StartGrip.Handle),
            "EndGrip": (self.EndGrip.Grip, self.EndGrip.Handle),
            "Difficulty": self.Difficulty,
            "Coolness": self.Coolness,
            "Category": self.Category,
            "Level": self.Level
        }
        
        
def Generate_random_data(n,m)-> list[BaliTrick]: 
    tricks = []
    for p in range(n):
        for o in range(len(CategoryEnum)):
            for r in range(m):
                trick = BaliTrick(id=p+o+r, Name="placeHolder"+str(p+o+r))
                trick.Level = random.choice(list(LevelEnum))
                trick.Category = CategoryEnum(o)
                trick.Difficulty = random.randint(1,10)
                trick.Coolness = random.randint(1,10)
                
                start_grip = GripHandle(random.choice(list(Grip)), random.choice(list(Handle)))
                end_grip = GripHandle(random.choice(list(Grip)), random.choice(list(Handle)))
                
                trick.StartGrip = start_grip
                trick.EndGrip = end_grip
                
                tricks.append(trick)
        
    return tricks