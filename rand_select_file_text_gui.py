'''
Created on Jun 14, 2015

@author: Ben
'''
import tkinter, PIL.ImageTk
from tkinter import messagebox
from tkinter import filedialog
import rand_select_file_text, helpmenu


class RandSelectFileTextGUI():
    ''' GUI of RandSelectFileText '''
    BACKGROUND = '#f4f4f4'


    def __init__(self, param: rand_select_file_text.RandSelectFileText()):
        ''' Constructor '''
        self.RandSelectFileText = param
        self._root_exec()
        
        self.frame1_resolution = {'width': 512, 'height': 512 * 13/20}
        self.frame = None
        
        self.frame_blank_resolution = {'width': 512, 'height': 512 * 1/20}
        self.frame_blank = None
        
        self.frame2_resolution = {'width': 512, 'height': 512 * 6/20}
        self.frame2 = None
        
        self.MenuObj = {'about': None, 'help': None, 'option': None}
        
        self.menu_bar()
        self.newset()
        self._ROOT.protocol("WM_DELETE_WINDOW", self.quit)
        
        self._ROOT.mainloop()
        
        
    #===========================================================================
    # MENU 
    #===========================================================================
    def menu_bar(self)->None:
        ''' Displays menu '''
        menubar = tkinter.Menu(self._ROOT)
        self._filemenu(menubar)
        self._actionmenu(menubar)
        self._helpmenu(menubar)
        self._ROOT.config(menu=menubar)
        
    
    #===========================================================================
    # DISPLAY
    #===========================================================================
    def newset(self)->None:
        ''' main screen '''
        self._frame_exec()
        self._frame_blank_exec()
        self._frame_exec2()    
        self._frame_objects1()
        self._frame_objects2()
    
        
    #===========================================================================
    # OPTION
    #===========================================================================
    def loadset(self)->None:
        ''' Load text file with specified parameters ''' 
        ftypes = [('Text files', '*.txt')]
        dialog = tkinter.filedialog.askopenfilename(filetypes=ftypes, defaultextension="*.txt")
        if dialog != '':
            self.RandSelectFileText.load_set(dialog)
            _new_tar_dest = self.RandSelectFileText.destination['target']
            _new_exc_dest = self.RandSelectFileText.destination['exclude']
            self.entry_tar_dest.delete(0, tkinter.END)
            self.entry_tar_dest.insert(0, _new_tar_dest)
            self.entry_exc_dest.delete(0, tkinter.END)
            self.entry_exc_dest.insert(0, _new_exc_dest)
    
    
    def saveset(self)->None:
        ''' Save text file with specified parameters '''
        ftypes = [('Text files', '*.txt')]
        dialog = tkinter.filedialog.asksaveasfilename(filetypes=ftypes, defaultextension="*.txt")
        if dialog != '':
            self.RandSelectFileText.save_set(dialog)
        
        
    def makedefault(self)->None:
        ''' Save text file with specified parameters to default.txt '''  
        self.RandSelectFileText.make_default()
        
    
    def quit(self)->None:
        ''' Shutdowns all active windows and closes the application '''
        self._ROOT.destroy()
        
        
    #===========================================================================
    # ACTION
    #===========================================================================
    def run(self)->None:
        ''' Runs program and selects a random word in the wordset '''
        try:
            text_font = 'Arial', 16
            word = self.RandSelectFileText.pick_word(self.RandSelectFileText.destination['target'], self.RandSelectFileText.destination['exclude'])
            self.text_result = tkinter.Label(self.frame2, font=text_font, text=word, width = 25, height = 3)
            self.text_result.grid(row=1, column=0, padx=10, pady=10, sticky=tkinter.E + tkinter.W + tkinter.S)
        except FileNotFoundError:
            tkinter.messagebox.showerror("Invalid Path Error", "One or both of your paths to Select or Exclude names are invalid.\n\nPress OK to continue.")
        except UnicodeDecodeError:
            tkinter.messagebox.showerror("Invalid File Error", "One or both of your paths to Select or Exclude names points to an unreadable file.\n\nPress OK to continue.")
        except:
            tkinter.messagebox.showerror("Unknown Error", "An unknown error has occurred.\n\nPress OK to continue.")
    
        
    #===========================================================================
    # INSTRUCTION
    #===========================================================================
    def about(self)->None:
        ''' Displays information about program '''
        helpmenu.About(self.MenuObj) 
    
    def help(self)->None:
        ''' Displays information on how to use '''
        helpmenu.Help(self.MenuObj) 
        
    
    #===========================================================================
    # PRIVATE
    #===========================================================================
        #=======================================================================
        # Menu
        #=======================================================================
    def _filemenu(self, menubar: 'menubar') -> None:
        ''' Displays the cascade labeled File '''
        filemenu = tkinter.Menu(menubar, tearoff = 0)
        filemenu.add_command(label='Load Set', command=self.loadset) 
        filemenu.add_command(label='Save Set', command=self.saveset)
        filemenu.add_command(label='Make Default', command=self.makedefault)
        filemenu.add_separator()
        filemenu.add_command(label='Quit', command=self.quit)
        menubar.add_cascade(label='File', menu = filemenu)
        
        
    def _actionmenu(self, menubar: 'menubar') -> None:
        ''' Displays the casade labeled Action '''
        actionmenu = tkinter.Menu(menubar, tearoff = 0)
        actionmenu.add_command(label='Run', command=self.run)
        menubar.add_cascade(label='Action', menu=actionmenu)
        
        
    def _helpmenu(self, menubar: 'menubar') -> None:
        ''' Displays the cascade labeled Help '''
        helpmenu = tkinter.Menu(menubar, tearoff = 0)
        helpmenu.add_command(label='Help', command = self.help)
        helpmenu.add_separator()
        helpmenu.add_command(label='About', command=self.about)
        menubar.add_cascade(label='Help', menu=helpmenu)
        
        
        #===========================================================================
        # DISPLAY
        #===========================================================================
    def _change_resolution(self, event) -> None:
        self.resolution['width'] = self._ROOT.winfo_width()
        self.resolution['height'] = self._ROOT.winfo_height()
        
        
    def _frame1_change_resolution(self, event) -> None:
        self.frame1_resolution['width'] = self.frame.winfo_width()
        self.frame1_resolution['height'] = self.frame.winfo_height()
        
        
    def _frame_blank_change_resolution(self, event) -> None:
        self.frame_blank_resolution['width'] = self.frame_blank.winfo_width()
        self.frame_blank_resolution['height'] = self.frame_blank.winfo_height()
        
        
    def _frame2_change_resolution(self, event)->None:
        self.frame2_resolution['width'] = self.frame2.winfo_height()
        self.frame2_resolution['height'] = self.frame2.winfo_width()
    
    
    def _root_exec(self)->None:
        self.resolution = {'width': 512, 'height': 512}
        self._ROOT = tkinter.Tk()
        self._ROOT.configure(background='white', 
                width=self.resolution['width'], height=self.resolution['height'])
        self._ROOT.bind('<Configure>', self._change_resolution)
        self._ROOT.rowconfigure(0, weight = 2)
        self._ROOT.rowconfigure(1, weight = 1)
        self._ROOT.columnconfigure(0, weight = 1)
        
        
    def _frame_exec(self)->None:
        self.frame = tkinter.Frame(self._ROOT, 
                    width = self.frame1_resolution['width'], height = self.frame1_resolution['height'],
                    background = RandSelectFileTextGUI.BACKGROUND)
        self.frame.grid(row=0, column=0, padx=0, pady=0, sticky=tkinter.NSEW)
        self.frame.bind('<Configure>', self._frame1_change_resolution)
        
        self.frame.rowconfigure(0, weight = 1)
        self.frame.rowconfigure(1, weight = 3)
        self.frame.rowconfigure(2, weight = 1)
        self.frame.rowconfigure(3, weight = 3)
        self.frame.columnconfigure(0, weight = 25)
        self.frame.columnconfigure(1, weight = 1)
        self.frame.columnconfigure(2, weight = 1)
        

    def _frame_blank_exec(self)->None:
        self.frame_blank = tkinter.Frame(self._ROOT, 
                    width = self.frame_blank_resolution['width'], height = self.frame_blank_resolution['height'],
                    background = RandSelectFileTextGUI.BACKGROUND)
        self.frame_blank.grid(row=1, column=0, padx=0, pady=0, sticky=tkinter.NSEW)
        self.frame_blank.bind('<Configure>', self._frame_blank_change_resolution)
        
        
    def _frame_exec2(self) -> None:
        self.frame2 = tkinter.Frame(self._ROOT, 
                    width = self.frame2_resolution['width'], height = self.frame2_resolution['height'],
                    background = RandSelectFileTextGUI.BACKGROUND)
        self.frame2.grid(row=2, column=0, padx=0, pady=0, sticky=tkinter.NSEW)
        self.frame2.bind('<Configure>', self._frame2_change_resolution)
        
        self.frame2.rowconfigure(0, weight = 1)
        self.frame2.rowconfigure(1, weight = 5)
        self.frame2.columnconfigure(0, weight = 25)
        self.frame2.columnconfigure(1, weight = 5)
        self.frame2.columnconfigure(2, weight = 1)
        
    
    def _frame_objects1(self)->None:
        default_font = 'Lucida', 14
        str_tar_dest = "List to Randomly Select"
        str_exc_dest = "List to Exclude"
        file_image = PIL.ImageTk.PhotoImage(file="file.gif")
        folder_image = PIL.ImageTk.PhotoImage(file="folder.gif")
        
        def modifybyentry_target(strvar):
            self.RandSelectFileText.destination['target'] = strvar.get()
            
        def modifybyentry_exclude(strvar):
            self.RandSelectFileText.destination['exclude'] = strvar.get()
            
        label_tar_dest = tkinter.Label(self.frame, text=str_tar_dest, 
                        font = default_font, justify = tkinter.LEFT,
                        width = len(str_tar_dest), height = 1, bg=RandSelectFileTextGUI.BACKGROUND)
        label_tar_dest.grid(row=0, column=0, padx=0, pady=0, sticky=tkinter.NSEW)
        
        str_tar_dest = tkinter.StringVar()
        str_tar_dest.trace("w", lambda name, index, mode, str_tar_dest=str_tar_dest: modifybyentry_target(str_tar_dest))
        self.entry_tar_dest = tkinter.Entry(self.frame, width = 50, textvariable = str_tar_dest)
        self.entry_tar_dest.grid(row=1, column=0, padx=10, pady=5, sticky=tkinter.E + tkinter.W + tkinter.N)
        self.entry_tar_dest.insert(0, self.RandSelectFileText.destination['target'])
        
        button_tar_dest_file = tkinter.Button(self.frame, image=file_image, justify=tkinter.LEFT, command=self._command_tar_destination1) 
        button_tar_dest_file.image = file_image
        button_tar_dest_file.grid(row=1, column=1, padx=0, pady=0, sticky=tkinter.E  + tkinter.N)
        
        button_tar_dest_folder = tkinter.Button(self.frame, image=folder_image, justify=tkinter.LEFT, command=self._command_tar_destination2) 
        button_tar_dest_folder.image = folder_image
        button_tar_dest_folder.grid(row=1, column=2, padx=5, pady=0, sticky=tkinter.E  + tkinter.N)
        
        label_exc_dest = tkinter.Label(self.frame, text=str_exc_dest, 
                        font = default_font, justify = tkinter.LEFT,
                        width = len(str_exc_dest), height = 1, bg=RandSelectFileTextGUI.BACKGROUND)
        label_exc_dest.grid(row=2, column=0, padx=0, pady=0, sticky=tkinter.NSEW)
        
        str_exc_dest = tkinter.StringVar()
        str_exc_dest.trace("w", lambda name, index, mode, str_exc_dest=str_exc_dest: modifybyentry_exclude(str_exc_dest))
        self.entry_exc_dest = tkinter.Entry(self.frame, width = 50, textvariable = str_exc_dest)
        self.entry_exc_dest.grid(row=3, column=0, padx=10, pady=5, sticky=tkinter.E + tkinter.W + tkinter.N)
        self.entry_exc_dest.insert(0, self.RandSelectFileText.destination['exclude'])
        
        button_exc_dest_file = tkinter.Button(self.frame, image=file_image, justify=tkinter.LEFT, command=self._command_exc_destination1) 
        button_exc_dest_file.image = file_image
        button_exc_dest_file.grid(row=3, column=1, padx=0, pady=0, sticky=tkinter.E  + tkinter.N)
        
        button_exc_dest_folder = tkinter.Button(self.frame, image=folder_image, justify=tkinter.LEFT, command=self._command_exc_destination2)
        button_exc_dest_folder.image = folder_image
        button_exc_dest_folder.grid(row=3, column=2, padx=5, pady=0, sticky=tkinter.E + tkinter.N)
        
        
    def _frame_objects2(self)->None:
        str_result = "Result"
        str_run = "RUN"
        default_font = 'Lucida', 14
        text_font = 'Arial', 16
        
        label_result = tkinter.Label(self.frame2, text=str_result,
                                     font = default_font, justify = tkinter.LEFT, 
                                     width = len(str_result), height = 1, bg=RandSelectFileTextGUI.BACKGROUND)
        label_result.grid(row=0, column=0, padx=0, pady=0, sticky=tkinter.E + tkinter.W + tkinter.S)
        
        self.text_result = tkinter.Label(self.frame2, font=text_font, width = 25, height = 3)
        self.text_result.grid(row=1, column=0, padx=10, pady=10, sticky=tkinter.E + tkinter.W + tkinter.S)
        
        run_button = tkinter.Button(self.frame2, text=str_run, command=self.run,
                                    width = 10, height = 5)
        run_button.grid(row=1, column=1, padx=5, pady=5, sticky = tkinter.E + tkinter.W + tkinter.S)
        
        #=======================================================================
        # COMMANDS
        #=======================================================================
    def _command_tar_destination1(self):
        ''' Command to browse for path of filename to copy '''
        dialog = tkinter.filedialog.askopenfilename()
        if dialog != '':
            self.entry_tar_dest.delete(0, tkinter.END)
            self.entry_tar_dest.insert(0, dialog)
            self.RandSelectFileText.destination['target'] = dialog
            
    def _command_tar_destination2(self):
        ''' Command to browse for path of filename to copy '''
        dialog = tkinter.filedialog.askdirectory()
        if dialog != '':
            self.entry_tar_dest.delete(0, tkinter.END)
            self.entry_tar_dest.insert(0, dialog)
            self.RandSelectFileText.destination['target'] = dialog
        

    def _command_exc_destination1(self):
        ''' Command to browse for path of filename to save '''
        dialog = tkinter.filedialog.askopenfilename()
        if dialog != '':
            self.entry_exc_dest.delete(0, tkinter.END)
            self.entry_exc_dest.insert(0, dialog)
            self.RandSelectFileText.destination['exclude'] = dialog
            
    def _command_exc_destination2(self):
        ''' Command to browse for path of filename to save '''
        dialog = tkinter.filedialog.askdirectory()
        if dialog != '':
            self.entry_exc_dest.delete(0, tkinter.END)
            self.entry_exc_dest.insert(0, dialog)
            self.RandSelectFileText.destination['exclude'] = dialog