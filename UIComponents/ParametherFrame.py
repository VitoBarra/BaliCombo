import threading
import customtkinter
from DebugAndTest import PrintClosure 
import SerchUtil as su

class ParametherFrame(customtkinter.CTkFrame):
    def FilterAndCalculate(self):
        FilteredTrick= su.FilterParamether(self.tricks,
                            MinDif=  self.GetIntLabel(self.difMin),
                            MaxDif=  self.GetIntLabel(self.difMax),
                            MinLevel=self.GetIntLabel(self.levelMin),
                            MaxLevel=self.GetIntLabel(self.levelMax),
                            MinCool= self.GetIntLabel(self.coolMin),
                            MaxCool= self.GetIntLabel(self.coolMax),
                            Category=[])
        N_closure = su.GenerateNclosure(self.GetIntLabel(self.ClosureN)-1,FilteredTrick) 
        PrintClosure(N_closure)

    
    def button_function(self):
        thread1 = threading.Thread(target=self.FilterAndCalculate)
        thread1.start()
        
                
    @staticmethod
    def GetIntLabel(label):
        try:
            return int(label.get())
        except:
            return None

        
        
    def __init__(self,master,BaliTricks,**kwargs) -> None:
        super().__init__(master, **kwargs)    
        
        self.tricks = BaliTricks
        self.grid(row=4, column=4)

        self.minLabel = customtkinter.CTkLabel(master=self, text="Min")
        self.minLabel.grid(row=0, column=1)
        self.maxLaber = customtkinter.CTkLabel(master=self, text="Max")
        self.maxLaber.grid(row=0, column=2)

        self.difLabel = customtkinter.CTkLabel(master=self, text="Dif")
        self.difLabel.grid(row=1, column=0)
        self.levelLabel = customtkinter.CTkLabel(master=self, text="level")
        self.levelLabel.grid(row=2, column=0)
        self.coolenessLabel = customtkinter.CTkLabel(master=self, text="Cooleness")
        self.coolenessLabel.grid(row=3, column=0)

        self.difMin = customtkinter.CTkEntry(master=self)
        self.difMin.grid(row=1, column=1)
        self.difMin.insert(0,"3")
        self.difMax = customtkinter.CTkEntry(master=self)
        self.difMax.insert(0,"5")
        self.difMax.grid(row=1, column=2)

        self.levelMin = customtkinter.CTkEntry(master=self)
        self.levelMin.grid(row=2, column=1)
        self.levelMin.insert(0,"0")
        self.levelMax = customtkinter.CTkEntry(master=self)
        self.levelMax.grid(row=2, column=2)
        self.levelMax.insert(0,"3")

        self.coolMin = customtkinter.CTkEntry(master=self)
        self.coolMin.grid(row=3, column=1)
        self.coolMin.insert(0,"0")
        self.coolMax = customtkinter.CTkEntry(master=self)
        self.coolMax.grid(row=3, column=2)
        self.coolMax.insert(0,"10")

        
        
        self.ClosureLaber = customtkinter.CTkLabel(master=self, text="N trick")
        self.ClosureLaber.grid(row=4, column=0)
        
        self.ClosureN = customtkinter.CTkEntry(master=self)
        self.ClosureN.grid(row=4, column=1,columnspan=3,padx=10, pady=10)
        self.ClosureN.insert(0,"3")
        
        self.CalculateButton = customtkinter.CTkButton(master=self, text="Start Calculation", command=self.button_function)
        self.CalculateButton.grid(row=5, column=1,columnspan=2,padx=5, pady=4)
        
        