
# a closure is a transitive transaction closure of a set of trick
def PrintClosure(closure):

    print("il numero di trick Trovti è :",CountTrinck(closure))
    for i in list(closure.keys()):
        print("con la transizione",i,":")
        for tricks in closure[i]:
            combo =[] 
            for trick in tricks:
                combo.append(trick.id)
            print(combo, end=",  ")
        print()
        
        
def CountTrinck(closure):
    n =0 
    for i in list(closure.keys()):
        n += len(closure[i])
    return n