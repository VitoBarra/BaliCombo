
# a closure is a transitive transaction closure of a set of trick
from SerchUtil import CalcuateSequenceStat


def PrintClosure(closure):

    print("il numero di trick Trovti è :",CountTrinck(closure))
    for i in list(closure.keys()):
        print("con la transizione",i,":")
        for ComboTrick in closure[i]:
            comboId =[] 
            for trick in ComboTrick:
                comboId.append(trick.id)
            print("{",comboId,CalcuateSequenceStat(ComboTrick),"}",  end=",  ")
        print()
        
        
def CountTrinck(closure):
    n =0 
    for i in list(closure.keys()):
        n += len(closure[i])
    return n