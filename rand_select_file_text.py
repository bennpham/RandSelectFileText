'''
Created on Jun 14, 2015

@author: Ben
'''
import glob, inspect, random, os
import create_new_default


class RandSelectFileText(object):
    ''' Handles inputs of directories and text files and printing a random string '''


    def __init__(self):
        ''' Constructor '''
        
        self.destination = {"target": "", "exclude": ""}
        
        self._current_directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        
        self._load_default()
        
        
    def pick_word(self, add_path:str, del_path:str)->str:
        ''' Pick a random word from the set of word and return it '''
        wordset = set()
        self._add_wordset(wordset, add_path)
        self._del_wordset(wordset, del_path)
        
        if len(wordset) != 0:
            return random.sample(wordset, 1)[0];
        
    
    def make_default(self)->None:
        ''' Overwrites old default.txt with new values '''
        create_new_default.create_new_default(self._current_directory + "\\default.txt", self.destination)
        
    
    def load_set(self, select_file: str)->None:
        '''
        Load parameters with text file into class with new values if text
        contains valid parameters somewhere inside
        '''
        with open(select_file, 'r') as file:
            for line in file:
                if line[0:20] == 'TARGET DESTINATION =':
                    self.destination['target'] = line[20:].rstrip().lstrip()
                elif line[0:21] == 'EXCLUDE DESTINATION =': 
                    self.destination['exclude'] = line[21:].rstrip().lstrip()
                    
    
    def save_set(self, file:str)->None:
        ''' Save current parameters to a text file of your choice '''
        create_new_default.create_new_default(file, self.destination)
        
        
    def _load_default(self)->None:
        '''
        - Check if default.txt exists
            * If default.txt doesn't exist, creates one and load in default empty parameters
            * If default.txt exists, gets default settings and load it in init
        '''
        if (len(glob.glob(self._current_directory + "\\default.txt")) == 0):
            create_new_default.create_new_default("default.txt", self.destination)
        else:
            self.load_set("default.txt")
                
                
    def _add_wordset(self, wordset:set, path:str)->None:
        if path == '':
            return
        elif os.path.isdir(path):
            for item in os.listdir(path):
                wordset.add(os.path.splitext(item)[0])
        elif os.path.isfile(path):
            with open(path) as file:
                for item in file:
                    if item.strip() != '':
                        wordset.add(item.rstrip('\n'))
        
        
    def _del_wordset(self, wordset:set, path:str)->None:
        if path == '':
            return
        elif os.path.isdir(path):
            for item in os.listdir(path):
                item_to_remove = os.path.splitext(item)[0]
                if item_to_remove in wordset:
                    wordset.remove(item_to_remove)
        elif os.path.isfile(path):
            with open(path) as file:
                for item in file:
                    if item.strip().rstrip('\n') in wordset:
                        wordset.remove(item.strip().rstrip('\n'))
                