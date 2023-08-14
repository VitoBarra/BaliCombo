from enum import Enum
import json
import BaliData.TrickData as td
import BaliData.TrickDataManager as tdm

class BaliTrickjsonManager(tdm.DataWRInterface):
    def __init__(self,filename):
        self.FileName = filename
   
    @staticmethod  
    def enum_converter(obj):
        if isinstance(obj, Enum):
            return obj.value
        raise TypeError("Object of type %s is not JSON serializable" % type(obj))

    
    def WriteData(self,bali):
    # Writing the modified data back to JSON
        with open(self.FileName, "w") as json_file:
                json.dump([trick.to_dict() for trick in bali], json_file,default=BaliTrickjsonManager.enum_converter)
    
    def ReadData(self)->list[td.BaliTrick]:
        BaliTricks = []
        with open(self.FileName, "r") as json_file:
            Tricks_Json = json.load(json_file)
            for trick in Tricks_Json:
                BaliTricks.append(td.BaliTrick(**trick))
        return BaliTricks
