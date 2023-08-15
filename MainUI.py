import tkinter 
import customtkinter
from BaliData.BaliTrickjsonManager import BaliTrickjsonManager
from BaliData.TrickDataManager import TrickDataManager 
from UIComponents.ParametherFrame import ParametherFrame 

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green




app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")


FILE_NAME ="BaliData/TrickData.json";
tdm = TrickDataManager(BaliTrickjsonManager(FILE_NAME))
#BaliTricks = tdm.GenerateData(5,65)
BaliTricks = tdm.ReadData();


ParametherFrame(app,BaliTricks,width = 200,height = 200)



app.mainloop()