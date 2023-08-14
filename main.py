from BaliData.BaliTrickjsonManager import BaliTrickjsonManager
from BaliData.TrickData import CategoryEnum
from BaliData.TrickDataManager import TrickDataManager
import SerchUtil as su


FILE_NAME ="BaliData/TrickData.json";

tdm = TrickDataManager(BaliTrickjsonManager(FILE_NAME))


#BaliTricks = tdm.GenerateData(5,65)
BaliTricks = tdm.ReadData();


e = su.FilterParamether(BaliTricks,MinDif=4, MaxDif=5,MinLevel=1,MaxLevel=3,Category=[CategoryEnum.Desterity,CategoryEnum.Transaction])

print("unfilter data: ",len(BaliTricks),"filtered data: ",len(e))










