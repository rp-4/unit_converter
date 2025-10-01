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
from CTkToolTip import *

# import local files
from _logging import _log


class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.tab1 = "Converter"
        self.tab2 = "Stackup Calc"
        self.add(self.tab1)
        self.add(self.tab2)

        ''' validate the entry to make sure it is numbers '''
        validation_command = self.register(self.only_numbers)

        ''' tab 1 frames '''
        ''' main frame on tab 1 where everything goes '''
        self.frame_t1_0 = Frame(master=self.tab(self.tab1), fg_color="transparent")
        self.frame_t1_0.pack(padx=(10,10), pady=(0,0),side=customtkinter.TOP, expand=True, fill=customtkinter.BOTH)


        ''' first frame where label goes '''
        self.frame_t1_01 = Frame(master=self.frame_t1_0, fg_color='transparent', width=450, height=40)
        self.frame_t1_01.pack(padx=(0,0), pady=(0,0),side=customtkinter.TOP, expand=False, fill=customtkinter.Y)

        ''' frame for input box '''
        self.frame_t1_02 = Frame(master=self.frame_t1_0, fg_color='transparent', width=400, height=40)
        self.frame_t1_02.pack(padx=(0,0), pady=(5,0), expand=False, fill=customtkinter.BOTH)

        ''' frame for buttons '''
        self.frame_t1_03 = Frame(master=self.frame_t1_0, fg_color='transparent', width=400)
        self.frame_t1_03.pack(padx=(0,0), pady=(5,5), expand=False, fill=customtkinter.BOTH)

        ''' frame for output '''
        self.frame_t1_04 = Frame(master=self.frame_t1_0, fg_color='transparent', width=200, height=40)
        self.frame_t1_04.pack(padx=(0,0), pady=(5,5), expand=False, fill=customtkinter.BOTH)

        ''' frame for inch output '''
        self.frame_t1_041 = Frame(master=self.frame_t1_04, fg_color='transparent', width=400, height=40)
        self.frame_t1_041.pack(padx=(0,0), pady=(5,0), expand=True, fill=customtkinter.BOTH)

        ''' frame for mm output '''
        self.frame_t1_042 = Frame(master=self.frame_t1_04, fg_color='transparent', width=400, height=40)
        self.frame_t1_042.pack(padx=(0,0), pady=(5,0), expand=True, fill=customtkinter.BOTH)


#####################################################################################################################################
        ''' tab 2 frames '''
        ''' main frame on tab 2 where everything goes '''
        self.frame_t2_0 = Frame(master=self.tab(self.tab2), fg_color="transparent")
        self.frame_t2_0.pack(padx=(10,10), pady=(10,0), side=customtkinter.TOP, expand=True, fill=customtkinter.BOTH)


        ''' first frame where Nominal input box goes '''
        self.frame_t2_01 = Frame(master=self.frame_t2_0, fg_color='transparent', height=50)
        self.frame_t2_01.pack(padx=(0,0), pady=(0,5), side=customtkinter.TOP, expand=False, fill=customtkinter.BOTH)


        ''' frame for Tolerance Selector '''
        self.frame_t2_02 = Frame(master=self.frame_t2_0, fg_color='transparent', width=400, height=40)
        self.frame_t2_02.pack(side="top", pady=10)


        ''' frame for + Tolerance input box '''
        self.frame_t2_03 = Frame(master=self.frame_t2_0, fg_color='transparent', width=400, height=40)
        self.frame_t2_03.pack(padx=(0,0), pady=(5,0), side=customtkinter.TOP, expand=False, fill=customtkinter.BOTH)


        ''' frame for - Tolerance input box '''
        self.frame_t2_04 = Frame(master=self.frame_t2_0, fg_color='transparent', width=400, height=40)
        self.frame_t2_04.pack(padx=(0,0), pady=(5,0), side=customtkinter.TOP, expand=False, fill=customtkinter.BOTH)


        ''' frame for generate button '''
        self.frame_t2_05 = Frame(master=self.frame_t2_0, fg_color='transparent', width=400, height=40)
        self.frame_t2_05.pack(padx=(0,0), pady=(15,0), side=customtkinter.TOP, expand=False, fill=customtkinter.BOTH)

        ''' frame for Max tolerance result '''
        self.frame_t2_06 = Frame(master=self.frame_t2_0, fg_color='transparent', width=400, height=40)
        self.frame_t2_06.pack(padx=(0,0), pady=(15,0), side=customtkinter.TOP, expand=False, fill=customtkinter.BOTH)

        ''' frame for Min tolerance result '''
        self.frame_t2_07 = Frame(master=self.frame_t2_0, fg_color='transparent', width=400, height=40)
        self.frame_t2_07.pack(padx=(0,0), pady=(5,0), side=customtkinter.TOP, expand=False, fill=customtkinter.BOTH)

        ''' frame for Gap when Both @ MMC tolerance result '''
        self.frame_t2_08 = Frame(master=self.frame_t2_0, fg_color='transparent', width=400, height=40)
        self.frame_t2_08.pack(padx=(0,0), pady=(15,0), side=customtkinter.TOP, expand=False, fill=customtkinter.BOTH)

        ''' frame for Gap when Both @ LMC tolerance result '''
        self.frame_t2_09 = Frame(master=self.frame_t2_0, fg_color='transparent', width=400, height=40)
        self.frame_t2_09.pack(padx=(0,0), pady=(5,0), side=customtkinter.TOP, expand=False, fill=customtkinter.BOTH)
 




        ''' tab 2 contetns '''
        ''' inputs for nominals '''
        self.nominal_lbl = customtkinter.CTkLabel(master=self.frame_t2_01, text="NOML", text_color = "Gray", font=("",20))
        self.nominal_lbl.pack(side="left", fill="both", expand=True, padx=(5,5), pady=0)


        self.hole_nominal_box = customtkinter.StringVar()
        self.hole_nominal_box = customtkinter.CTkEntry(master=self.frame_t2_01, placeholder_text="Hole Dia", border_color = "#3D839F",
                                                corner_radius=5, height=30, font=("",30), 
                                                validate="key", validatecommand= (validation_command,'%P'))
        self.hole_nominal_box.pack(side="left", fill="both", expand=True, padx=(0,5), pady=0)
        self.hole_nominal_tip = CTkToolTip(self.hole_nominal_box, delay=0.5, bg_color="#324A5E", message="Enter Hole Diameter or Slot Width")
        self.hole_nominal_tip.attributes("-topmost", True)

        self.shaft_nominal_box = customtkinter.StringVar()
        self.shaft_nominal_box = customtkinter.CTkEntry(master=self.frame_t2_01, placeholder_text="Shaft Dia",  border_color = "#3D839F",
                                                corner_radius=5, height=30, font=("",30), 
                                                validate="key", validatecommand= (validation_command,'%P'))
        self.shaft_nominal_box.pack(side="left", fill="both", expand=True, padx=(0,0), pady=0)
        self.shaft_nominal_tip = CTkToolTip(self.shaft_nominal_box, delay=0.5, bg_color="#324A5E", message="Enter Shaft Diameter or Key Width")
        self.shaft_nominal_tip.attributes("-topmost", True)


        ''' Tolerance type selector '''
        self.tol_selector_var = customtkinter.IntVar(value=0)
        self.tol_selector_sym = customtkinter.CTkRadioButton(master=self.frame_t2_02, text="Symmetry",
                                                             command=self.selected_tolerance, variable= self.tol_selector_var, value=1)

        self.tol_selector_bil = customtkinter.CTkRadioButton(master=self.frame_t2_02, text="Bilateral",
                                                             command=self.selected_tolerance, variable= self.tol_selector_var, value=2)
        self.tol_selector_sym.pack(in_=self.frame_t2_02, side="left", padx=5, pady=0)
        self.tol_selector_bil.pack(in_=self.frame_t2_02, side="left", padx=5, pady=0)
        self.tol_selector_sym.select()



        ''' input for + Tolerances '''
        self.plus_tolerance_lbl = customtkinter.CTkLabel(master=self.frame_t2_03, text="±TOL", text_color = "Gray", font=("",20))
        self.plus_tolerance_lbl.pack(side="left", fill="both", expand=True, padx=(5,5), pady=0)


        self.input_plus_tol_hole = customtkinter.StringVar()
        self.input_plus_tol_hole = customtkinter.CTkEntry(master=self.frame_t2_03, placeholder_text= 0, border_color = "green",
                                                corner_radius=5, height=30, font=("",30), 
                                                validate="key", validatecommand= (validation_command,'%P'))
        self.input_plus_tol_hole.pack(side="left", fill="both", expand=True, padx=(0,5), pady=0)

        self.input_plus_tol_shaft = customtkinter.StringVar()
        self.input_plus_tol_shaft = customtkinter.CTkEntry(master=self.frame_t2_03, placeholder_text= 0,  border_color = "green",
                                                corner_radius=5, height=30, font=("",30), 
                                                validate="key", validatecommand= (validation_command,'%P'))
        self.input_plus_tol_shaft.pack(side="left", fill="both", expand=True, padx=(0,0), pady=0)


        ''' input for - Tolerances '''
        self.min_tolerance_lbl = customtkinter.CTkLabel(master=self.frame_t2_04, text="        ", text_color = "Gray", font=("",20))
        self.min_tolerance_lbl.pack(side="left", fill="both", expand=True, padx=(5,5), pady=0)


        self.input_min_tol_hole = customtkinter.StringVar()
        self.input_min_tol_hole = customtkinter.CTkEntry(master=self.frame_t2_04, placeholder_text= 0, border_color = "#913030",
                                                corner_radius=5, height=30, font=("",30), 
                                                validate="key", validatecommand= (validation_command,'%P'))
        self.input_min_tol_hole.pack(side="left", fill="both", expand=True, padx=(0,5), pady=0)

        self.input_min_tol_shaft = customtkinter.StringVar()
        self.input_min_tol_shaft = customtkinter.CTkEntry(master=self.frame_t2_04, placeholder_text= 0, border_color = "#913030",
                                                corner_radius=5, height=30, font=("",30), 
                                                validate="key", validatecommand= (validation_command,'%P'))
        self.input_min_tol_shaft.pack(side="left", fill="both", expand=True, padx=(0,0), pady=0)


        ''' disabling both - tolerances for symmetry tolerance '''
        self.input_min_tol_hole.configure(state = "disabled")
        self.input_min_tol_shaft.configure(state = "disabled")


        ''' generat button for tolerances '''
        self.generate_bn = customtkinter.CTkButton(master=self.frame_t2_05, text="Generate", 
                                                 command=lambda: self.tol_calculations(), 
                                                     width=50, height=30, font=("", 25))
        self.generate_bn.pack(side="left", expand=True, padx=(0,5), pady=0, fill=customtkinter.Y)


        ''' Max tolerance result '''
        self.max_lbl = customtkinter.CTkLabel(master=self.frame_t2_06, text="MAX", text_color = "Gray", font=("",20))
        self.max_lbl.pack(side="left", fill="both", expand=True, padx=(5,5), pady=0)

        self.max_hole_op = customtkinter.CTkLabel(master=self.frame_t2_06, text=0, text_color = "#c3c3c3", font=("",30))
        self.max_hole_op.pack(side="left", fill="both", expand=True, padx=(5,5), pady=0)

        self.max_shaft_op = customtkinter.CTkLabel(master=self.frame_t2_06, text=0, text_color = "#c3c3c3", font=("",30))
        self.max_shaft_op.pack(side="left", fill="both", expand=True, padx=(5,5), pady=0)


        ''' Min tolerance result '''
        self.min_lbl = customtkinter.CTkLabel(master=self.frame_t2_07, text="MIN", text_color = "gray", font=("",20))
        self.min_lbl.pack(side="left", fill="both", expand=True, padx=(5,5), pady=0)

        self.min_hole_op = customtkinter.CTkLabel(master=self.frame_t2_07, text=0, text_color = "#c3c3c3", font=("",30))
        self.min_hole_op.pack(side="left", fill="both", expand=True, padx=(5,5), pady=0)

        self.min_shaft_op = customtkinter.CTkLabel(master=self.frame_t2_07, text=0, text_color = "#c3c3c3", font=("",30))
        self.min_shaft_op.pack(side="left", fill="both", expand=True, padx=(5,5), pady=0)


        ''' Gap when both are @ MMC tolerance result '''
        self.both_at_MMC_lbl = customtkinter.CTkLabel(master=self.frame_t2_08, text="Clearance @ MMC", text_color = "Gray", font=("",20))
        self.both_at_MMC_lbl.pack(side="left", fill="both", expand=True, padx=(5,5), pady=0)

        self.both_at_MMC_op = customtkinter.CTkLabel(master=self.frame_t2_08, text=0, text_color = "#c3c3c3", font=("",30))
        self.both_at_MMC_op.pack(side="left", fill="both", expand=True, padx=(5,5), pady=0)


        ''' Gap when both are @ LMC tolerance result '''
        self.both_at_LMC_lbl = customtkinter.CTkLabel(master=self.frame_t2_09, text="Clearance @ MMC", text_color = "Gray", font=("",20))
        self.both_at_LMC_lbl.pack(side="left", fill="both", expand=True, padx=(5,5), pady=0)

        self.both_at_LMC_op = customtkinter.CTkLabel(master=self.frame_t2_09, text=0, text_color = "#c3c3c3", font=("",30))
        self.both_at_LMC_op.pack(side="left", fill="both", expand=True, padx=(5,5), pady=0)




#####################################################################################################################################
     
        ''' tab 1 contents '''
        ''' input label declaration '''
        self.input_lbl = customtkinter.CTkLabel(master=self.frame_t1_01, text="Enter Number:", text_color = "Gray", font=("",30))
        self.input_lbl.pack(padx=(10,10), pady=(0,0), side=customtkinter.LEFT,)

        ''' input box declaration '''
        self.input_box = customtkinter.StringVar()
        self.input_box = customtkinter.CTkEntry(master=self.frame_t1_02, 
                                                corner_radius=5, height=40, font=("",40), 
                                                validate="key", validatecommand= (validation_command,'%P'))
        self.input_box.pack(padx=(0,0), pady=(0,0), expand=False, fill=customtkinter.BOTH)

        
        ''' convert button '''
        self.convert_btn = customtkinter.CTkButton(master=self.frame_t1_03, text="Convert", command=lambda: self.convert_unit(event='e'), 
                                                   width=170, height=40, font=("", 30))
        self.convert_btn.pack(padx=(0,5), pady=(0,0), side=customtkinter.LEFT)

        ''' clear button '''
        self.clear_text_bn = customtkinter.CTkButton(master=self.frame_t1_03, text="Clear", command=self.clear_all, 
                                                     width=200, height=40, font=("", 30))
        self.clear_text_bn.pack(padx=(5,0), pady=(0,0), side=customtkinter.RIGHT)

        ''' inch copy button '''
        self.inch_cpy_bn = customtkinter.CTkButton(master=self.frame_t1_041, text="Copy", 
                                                   command=lambda: self.copy_to_clipboard(unit = "inch"), 
                                                     width=50, height=30, font=("", 20))
        self.inch_cpy_bn.pack(padx=(5,0), pady=(5,5), side=customtkinter.RIGHT)

        ''' mm copy button '''
        self.mm_cpy_bn = customtkinter.CTkButton(master=self.frame_t1_042, text="Copy", 
                                                 command=lambda: self.copy_to_clipboard(unit = "mm"), 
                                                     width=50, height=30, font=("", 20))
        self.mm_cpy_bn.pack(padx=(5,0), pady=(5,5), side=customtkinter.RIGHT)


        ''' input label declaration '''
        self.inch_lbl = customtkinter.CTkLabel(master=self.frame_t1_041, text="in:", text_color = "Gray", font=("",30))
        self.inch_lbl.pack(padx=(0,5), pady=(0,0), side=customtkinter.LEFT,)

        self.inch_op = customtkinter.CTkLabel(master=self.frame_t1_041, text="0", text_color = "white", font=("",30))
        self.inch_op.pack(padx=(0,5), pady=(0,0), side=customtkinter.LEFT,)
 

        self.mm_lbl = customtkinter.CTkLabel(master=self.frame_t1_042, text="mm:", text_color = "Gray", font=("",30))
        self.mm_lbl.pack(padx=(0,5), pady=(0,0), side=customtkinter.LEFT,)

        self.mm_op = customtkinter.CTkLabel(master=self.frame_t1_042, text="0", text_color = "white", font=("",30))
        self.mm_op.pack(padx=(0,5), pady=(0,0), side=customtkinter.LEFT,)


        

        ''' binding input box to enter key '''
        self.input_box.bind('<Return>', self.convert_unit)


        ''' declaring global variables '''
        self.inch_op_number = 0
        self.mm_op_number = 0
    
        self.initial_setting()
    
    ''' initially setting default values '''
    def initial_setting(self):
        print("initial settings")
        # self.input_plus_tol_shaft.insert(0, string=0)
        # # self.input_plus_tol_hole.insert((0, "0"))

    
    ''' validate the entry to make sure it is numbers '''
    def only_numbers(self, char):
        if char == "":
            return True
        pattern = r'^\d*\.?\d*$'
        return re.match(pattern, char) is not None


    def selected_tolerance(self):

        if self.tol_selector_var.get() == 1:
            self.plus_tolerance_lbl.configure(text="±TOL")
            self.min_tolerance_lbl.configure(text="        ")
            self.input_min_tol_shaft.configure(state="disabled", border_color = "#913030")
            self.input_min_tol_hole.configure(state="disabled", border_color = "#913030")
        elif self.tol_selector_var.get() == 2:
            self.plus_tolerance_lbl.configure(text="+TOL")
            self.min_tolerance_lbl.configure(text="-TOL")
            self.input_min_tol_shaft.configure(state="normal", border_color = "green")
            self.input_min_tol_hole.configure(state="normal", border_color = "green")


    def tol_calculations(self):

        # print(self.input_plus_tol_shaft.get(), type(self.input_plus_tol_shaft.get()))
        # enter 0 initially to tolerance input boxes  
        # check if it is symmetry or biletaral tolerance and then proceed 
        if self.tol_selector_var.get() == 1:
            self.get_values(tol_type=1)
            self.sym_tol_calculations()
        elif self.tol_selector_var.get() == 2:
            self.get_values(tol_type=2)
            self.bi_tol_calculations()

    def get_values(self, tol_type):
        try:
            self.shaft_nominal = float(self.shaft_nominal_box.get())
        except ValueError as e:
            # show error message
            self.shaft_nominal = 0

        try:
            self.hole_nominal = float(self.hole_nominal_box.get())
        except ValueError as e:
            # show error message
            self.hole_nominal = 0
        
        
        try:
            self.max_shaft = float(self.input_plus_tol_shaft.get())
        except ValueError as e:
            # show error message
            self.max_shaft = 0

        try:
            self.max_hole = float(self.input_plus_tol_hole.get())
        except ValueError as e:
            # show error message
            self.max_hole = 0

        if tol_type == 2:
            try:
                self.min_shaft = float(self.input_min_tol_shaft.get())
            except ValueError as e:
                # show error message
                self.min_shaft = 0

            try:
                self.min_hole = float(self.input_min_tol_hole.get())
            except ValueError as e:
                # show error message
                self.min_hole = 0       

    
    def bi_tol_calculations(self):

        # print(self.input_plus_tol_shaft.get(), type(self.input_plus_tol_shaft.get()))

        self.shaft_at_max = round(self.shaft_nominal + self.max_shaft, 4)
        self.hole_at_max = round(self.hole_nominal + self.max_hole, 4)

        self.shaft_at_min = round(self.shaft_nominal - self.min_shaft, 4)
        self.hole_at_min = round(self.hole_nominal - self.min_hole, 4)

        self.max_shaft_op.configure(text = self.shaft_at_max)
        self.max_hole_op.configure(text = self.hole_at_max)

        self.min_shaft_op.configure(text = self.shaft_at_min)
        self.min_hole_op.configure(text = self.hole_at_min)

        self.both_at_MMC_var = round(self.hole_at_min - self.shaft_at_max, 4)
        self.both_at_LMC_var = round(self.hole_at_max - self.shaft_at_min, 4)

        if self.both_at_MMC_var < 0:
            self.both_at_MMC_op.configure(text = self.both_at_MMC_var, text_color = "#D60404")
        elif self.both_at_MMC_var >= 0:
            self.both_at_MMC_op.configure(text = self.both_at_MMC_var, text_color = "green")
        
        if self.both_at_LMC_var < 0:
            self.both_at_LMC_op.configure(text = self.both_at_LMC_var, text_color = "#D60404")
        elif self.both_at_LMC_var >= 0:
            self.both_at_LMC_op.configure(text = self.both_at_LMC_var, text_color = "green")
        
        # print("MAX_1", self.shaft_at_max)
        # print("MAX_2", self.hole_at_max)

        # print("MIN_1", self.shaft_at_min)
        # print("MIN_2", self.hole_at_min)

    
    def sym_tol_calculations(self):

        # print(self.input_plus_tol_shaft.get(), type(self.input_plus_tol_shaft.get()))

        self.shaft_at_max = round(self.shaft_nominal + self.max_shaft, 4)
        self.hole_at_max = round(self.hole_nominal + self.max_hole, 4)

        self.shaft_at_min = round(self.shaft_nominal - self.max_shaft, 4)
        self.hole_at_min = round(self.hole_nominal - self.max_hole, 4)

        self.max_shaft_op.configure(text = self.shaft_at_max)
        self.max_hole_op.configure(text = self.hole_at_max)

        self.min_shaft_op.configure(text = self.shaft_at_min)
        self.min_hole_op.configure(text = self.hole_at_min)


        self.both_at_MMC_var = round(self.hole_at_min - self.shaft_at_max, 4)
        self.both_at_LMC_var = round(self.hole_at_max - self.shaft_at_min, 4)

        if self.both_at_MMC_var < 0:
            self.both_at_MMC_op.configure(text = self.both_at_MMC_var, text_color = "#D60404")
        elif self.both_at_MMC_var >= 0:
            self.both_at_MMC_op.configure(text = self.both_at_MMC_var, text_color = "green")
        
        if self.both_at_LMC_var < 0:
            self.both_at_LMC_op.configure(text = self.both_at_LMC_var, text_color = "#D60404")
        elif self.both_at_LMC_var >= 0:
            self.both_at_LMC_op.configure(text = self.both_at_LMC_var, text_color = "green")

        # print("SYM MAX_1", self.shaft_at_max)
        # print("SYM MAX_2", self.hole_at_max)

        # print("SYM MIN_1", self.shaft_at_min)
        # print("SYM MIN_2", self.hole_at_min)
       


        
        
            

    def convert_unit(self, event):
        _log("i", f"IN: {inspect.stack()[0][3]}: Unit conversion by enter key")
        try:
            input_number = float(self.input_box.get())
        except ValueError as e:
            input_number = 0

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



class App(customtkinter.CTk):
    _log("i", "\nUnit Converter initiated..............Developed by Rinkesh Patel with Love !!...............\n")
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

        self.width = 400
        self.height = 550
        
        self.geometry(f"{self.width}x{self.height}")
        self.minsize(self.width, self.height)
        self.title("Unit Converter v1.0.0")
        self.wm_attributes("-topmost", True) # always on-top configuration
        self.resizable(False, False)
        self.iconbitmap('src/logo.ico')
        self.grid_rowconfigure(0, minsize=200, weight=1)
        self.grid_columnconfigure(0,weight=0, pad=0)
        self.grid_columnconfigure(0, minsize=20, weight=1)

        
        

        

        
        self.tab_view = MyTabView(master=self, fg_color="transparent")
        self.tab_view.grid(row=0, column=0, sticky = "NWES")



        '''' developer's note '''
        
        
        self.madeBy = customtkinter.CTkLabel(master=self, text="Developed by Rinkesh Patel with 💙 for you !!")
        self.madeBy.grid(row=10, column=0, columnspan=4, pady=5)

        self.madeBy.bind("<Button-1>", lambda e: self.openWebsite("https://rinkeshpatel.com/"))

    def openWebsite(self,url):
        _log("i", f"IN: {inspect.stack()[0][3]}: Website accessed: {url}")
        webbrowser.open_new(url)

        

        

    

    
if __name__ == "__main__":
    _log("i", "\nSoftware initiated.............................................")
    app = App()
    app.mainloop()
