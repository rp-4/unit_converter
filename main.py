"""
Unit Converter Software
Developer: Rinkesh Patel
Contact: www.rinkesh.ca
Version: 1.0.0
Change Log: Please refer to Version.md file
"""

import customtkinter
from customtkinter import CTkFrame as Frame
import webbrowser
import inspect
import re
import os
import pyperclip

# import local files
from _logging import _log


class App(customtkinter.CTk):
    _log("i", "\nUnit Converter initiated..............Developed by Rinkesh Patel with Love !!...............\n")
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
        
        self.width = 350
        self.height = 350
        
        self.geometry(f"{self.width}x{self.height}")
        self.minsize(self.width, self.height)
        self.title("Unit Converter v1.0.0")
        self.wm_attributes("-topmost", True) # always on-top configuration
        self.resizable(False, False)
        self.iconbitmap('src/logo.ico')
        self.grid_rowconfigure(0, minsize=200, weight=1)
        self.grid_columnconfigure(0,weight=0, pad=0)
        self.grid_columnconfigure(0, minsize=20, weight=1)
        

        ''' validate the entry to make sure it is numbers '''
        validation_command = self.register(self.only_numbers)

        
        ''' main frame where everything goes '''
        self.frame_0 = Frame(self, fg_color="transparent",)
        self.frame_0.grid(row=0, column=0, sticky='NWE')

        ''' first frame where label goes '''
        self.frame_01 = Frame(master=self.frame_0, fg_color='transparent', width=400, height=100)
        self.frame_01.pack(padx=(0,10), pady=(10,0),side=customtkinter.TOP, expand=False, fill=customtkinter.BOTH)

        ''' frame for input box '''
        self.frame_02 = Frame(master=self.frame_0, fg_color='transparent', width=400, height=40)
        self.frame_02.pack(padx=(10,10), pady=(10,5), expand=True, fill=customtkinter.BOTH)

        ''' frame for buttons '''
        self.frame_03 = Frame(master=self.frame_0, fg_color='transparent', width=400, height=40)
        self.frame_03.pack(padx=(10,10), pady=(10,5), expand=True, fill=customtkinter.BOTH)

        ''' frame for output '''
        self.frame_04 = Frame(master=self.frame_0, fg_color='transparent', width=200, height=40)
        self.frame_04.pack(padx=(0,10), pady=(5,5), expand=True, fill=customtkinter.BOTH)

        ''' frame for inch output '''
        self.frame_041 = Frame(master=self.frame_04, fg_color='transparent', width=400, height=40)
        self.frame_041.pack(padx=(10,10), pady=(5,5), expand=True, fill=customtkinter.BOTH)

        ''' frame for mm output '''
        self.frame_042 = Frame(master=self.frame_04, fg_color='transparent', width=400, height=40)
        self.frame_042.pack(padx=(10,10), pady=(5,5), expand=True, fill=customtkinter.BOTH)

     

        ''' input label declaration '''
        self.input_lbl = customtkinter.CTkLabel(master=self.frame_01, text="Enter Number:", text_color = "Gray", font=("",30))
        self.input_lbl.pack(padx=(10,10), pady=(0,0), side=customtkinter.LEFT,)

        ''' input box declaration '''
        self.input_box = customtkinter.StringVar()
        self.input_box = customtkinter.CTkEntry(master=self.frame_02, 
                                                corner_radius=5, height=40, font=("",40), 
                                                validate="key", validatecommand= (validation_command,'%P'))
        self.input_box.pack(padx=(0,0), pady=(0,0), expand=False, fill=customtkinter.BOTH)

        
        ''' convert button '''
        self.convert_btn = customtkinter.CTkButton(master=self.frame_03, text="Convert", command=lambda: self.convert_unit(event='e'), 
                                                   width=150, height=40, font=("", 30))
        self.convert_btn.pack(padx=(0,5), pady=(5,5), side=customtkinter.LEFT)

        ''' clear button '''
        self.clear_text_bn = customtkinter.CTkButton(master=self.frame_03, text="Clear", command=self.clear_all, 
                                                     width=150, height=40, font=("", 30))
        self.clear_text_bn.pack(padx=(5,0), pady=(5,5), side=customtkinter.RIGHT)

        ''' inch copy button '''
        self.inch_cpy_bn = customtkinter.CTkButton(master=self.frame_041, text="Copy", 
                                                   command=lambda: self.copy_to_clipboard(unit = "inch"), 
                                                     width=50, height=30, font=("", 20))
        self.inch_cpy_bn.pack(padx=(5,0), pady=(5,5), side=customtkinter.RIGHT)

        ''' mm copy button '''
        self.mm_cpy_bn = customtkinter.CTkButton(master=self.frame_042, text="Copy", 
                                                 command=lambda: self.copy_to_clipboard(unit = "mm"), 
                                                     width=50, height=30, font=("", 20))
        self.mm_cpy_bn.pack(padx=(5,0), pady=(5,5), side=customtkinter.RIGHT)


        ''' input label declaration '''
        self.inch_lbl = customtkinter.CTkLabel(master=self.frame_041, text="in:", text_color = "Gray", font=("",30))
        self.inch_lbl.pack(padx=(0,5), pady=(0,0), side=customtkinter.LEFT,)

        self.inch_op = customtkinter.CTkLabel(master=self.frame_041, text="0", text_color = "white", font=("",30))
        self.inch_op.pack(padx=(0,5), pady=(0,0), side=customtkinter.LEFT,)
 

        self.mm_lbl = customtkinter.CTkLabel(master=self.frame_042, text="mm:", text_color = "Gray", font=("",30))
        self.mm_lbl.pack(padx=(0,5), pady=(0,0), side=customtkinter.LEFT,)

        self.mm_op = customtkinter.CTkLabel(master=self.frame_042, text="0", text_color = "white", font=("",30))
        self.mm_op.pack(padx=(0,5), pady=(0,0), side=customtkinter.LEFT,)


        '''' developer's note '''
        self.madeBy = customtkinter.CTkLabel(master=self, text="Developed by Rinkesh Patel with 💙 for you !!")
        self.madeBy.grid(row=10, column=0, columnspan=4, pady=5)

        self.madeBy.bind("<Button-1>", lambda e: self.openWebsite("https://rinkeshpatel.com/"))


        ''' binding input box to enter key '''
        self.input_box.bind('<Return>', self.convert_unit)

    
    ''' validate the entry to make sure it is numbers '''
    def only_numbers(self, char):
        if char == "":
            return True
        pattern = r'^\d*\.?\d*$'
        return re.match(pattern, char) is not None
        

    def openWebsite(self,url):
        _log("i", f"IN: {inspect.stack()[0][3]}: Website accessed: {url}")
        webbrowser.open_new(url)


    def convert_unit(self, event):
        _log("i", f"IN: {inspect.stack()[0][3]}: Unit conversion by enter key")
        input_number = float(self.input_box.get())
        self.inch_op_number = round(input_number / 25.4, 4)
        self.mm_op_number = round(input_number * 25.4, 4)
        self.op_numbers(inch=self.inch_op_number, mm=self.mm_op_number)

    def convert_unit_btn(self):
        _log("i", f"IN: {inspect.stack()[0][3]}: Unit conversion by button")
        self.convert_unit(event='e')


    def copy_to_clipboard(self, unit):
        if unit == "inch":
            pyperclip.copy(self.inch_op_number)
        elif unit == "mm":
            pyperclip.copy(self.mm_op_number)



    
    def clear_all(self):
        _log("i", f"IN: {inspect.stack()[0][3]}")
        self.input_box.delete(0, customtkinter.END)
    
    def op_numbers(self, inch="0", mm="0", color = "white"):
        self.inch_op.configure(text=inch,  text_color= color)
        self.mm_op.configure(text=mm,  text_color= color)
        _log("i", f"IN: {inspect.stack()[0][3]}: Number conversion")

    

    
if __name__ == "__main__":
    _log("i", "\nSoftware initiated.............................................")
    app = App()
    app.mainloop()
