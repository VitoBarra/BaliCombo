#Hight leve Interaction With Data
from abc import abstractmethod
import BaliData.TrickData as td


class DataWRInterface:
    @abstractmethod
    def WriteData(self,bali):
        pass

    @abstractmethod
    def ReadData(self):
        pass

class TrickDataManager:
    def __init__(self,datManager):
        self.DatManager:DataWRInterface = datManager
    
    def GenerateData(self,n,m):
        t = td.Generate_random_data(n,m)
        self.DatManager.WriteData(t)
        return t
    
    def WriteData(self,bali):
        self.DatManager.WriteData(bali)
        
    def ReadData(self):
        return self.DatManager.ReadData()
