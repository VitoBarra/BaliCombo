from BaliData.BaliTrickjsonManager import BaliTrickjsonManager
from BaliData.TrickData import CategoryEnum
from BaliData.TrickDataManager import TrickDataManager
from DebugAndTest import PrintClosure
import SerchUtil as su


FILE_NAME ="BaliData/TrickData.json";

tdm = TrickDataManager(BaliTrickjsonManager(FILE_NAME))


BaliTricks = tdm.GenerateData(5,65)
BaliTricks = tdm.ReadData();


BaliTricksFiltered = su.FilterParamether(BaliTricks,MinDif=4, MaxDif=5,MinLevel=1,MaxLevel=3,Category=[CategoryEnum.Desterity,CategoryEnum.Transaction])

#print("unfilter data: ",len(BaliTricks),"filtered data: ",len(e))


ToyTest = [BaliTricksFiltered[0],BaliTricksFiltered[1],BaliTricksFiltered[2],BaliTricksFiltered[3],BaliTricksFiltered[4],BaliTricksFiltered[5],BaliTricksFiltered[6],BaliTricksFiltered[7],BaliTricksFiltered[8]]



N_closure = su.GenerateNclosure(3,ToyTest) 



PrintClosure(N_closure)











