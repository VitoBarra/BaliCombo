
from BaliData.TrickData import BaliTrick


def GenerateTrickGroup(BaliTricks):
    TrickGroup = {}
    for trick in BaliTricks:
        key = (trick.StartGrip.GetGripHandleCode(), trick.EndGrip.GetGripHandleCode())
        if key not in TrickGroup:
            TrickGroup[key] = []
        TrickGroup[key].append(trick)
    
    return TrickGroup


def FilterParamether(BaliTricks:list[BaliTrick], MinDif=0,MaxDif=10,MinLevel=0,MaxLevel=5,Category = []):
    return [trick for trick in BaliTricks if MinDif<=trick.Difficulty<=MaxDif and MinLevel<=trick.Level.value<=MaxLevel and all(trick.Category.value != cat.value for cat in Category)  ]
