
from BaliData.TrickData import BaliTrick, GripHandle


def GenerateTrickGroup(BaliTricks: list[BaliTrick]):
    TrickGroup = {}
    for trick in BaliTricks:
        key = (trick.StartGrip.GripHandleCode, trick.EndGrip.GripHandleCode)
        if key not in TrickGroup:
            TrickGroup[key] = []
        TrickGroup[key].append([trick])
    
    return TrickGroup


def FilterParamether(BaliTricks:list[BaliTrick], MinDif=0,MaxDif=10,MinLevel=0,MaxLevel=5,MinCool=1,MaxCool=10,Category = []):
    return [trick for trick in BaliTricks 
            if MinDif<=trick.Difficulty<=MaxDif and 
            MinLevel<=trick.Level.value<=MaxLevel and
            MinCool<=trick.Coolness<=MaxCool and
            all(trick.Category.value != cat.value for cat in Category)]

def GenerateClosure(TrickAccumulator,TrickGroup):
        resoults = {}
        for trickStart in list(TrickAccumulator.keys()):
            for trickEnd in list(TrickGroup.keys()):
                if trickStart[1] == trickEnd[0]:
                    newkey =(trickStart[0],trickEnd[1])
                    resoults[newkey] = []
                    for trick in TrickAccumulator[trickStart]:
                        for nextTrick in TrickGroup[trickEnd]:
                            resoults[newkey].append(trick+nextTrick)
                         
        return resoults
    
    
    
def GenerateNclosure(n,TrickList):
    TrickGroup = GenerateTrickGroup(TrickList)
    nClosure = TrickGroup.copy()
    for i in range(n):
        nClosure = GenerateClosure(nClosure,TrickGroup)
    return  nClosure

def CalcuateSequenceStat(TrickSequence:list[BaliTrick]):

    if len(TrickSequence)==0: return (0,0) 
    DefficutlyAverage = sum([trick.Difficulty for trick in TrickSequence])/len(TrickSequence)
    CoolnessAverage = sum([trick.Coolness for trick in TrickSequence])/len(TrickSequence)
    return (DefficutlyAverage,CoolnessAverage)

    
def Serch(closure,StartGrip:GripHandle,EndGrip:GripHandle):
    return closure[StartGrip.GripHandleCode,EndGrip.GripHandleCode]
    
    


#def GoalFunction(TrickSequence):
    


#\def HeuristicPruneFunction(NextTrickList):
    