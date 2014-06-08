'''
Created on May 19, 2014

@author: sgk
tkinter functions related to the Ui view (class)
'''

import tkinter.font
import src.domainData
import src.uiOptions

class UiMetrics():
    '''
    classdocs
    '''

    def __init__(self, domainRecords, font):
        '''
        Constructor
        '''
        # mapping of records by heading to longest length in pixels for current
        # set of records
        self.lengths = {}
        
        # access lengths of Options for table headings
        self.font = font
        self.option = src.uiOptions.UiOptions( self.font )
                
        self.domainRecords = domainRecords
        
        # initalize map (dict) keys - simplifies the following nested clause
        for option in self.option.displayItems:
            self.lengths[option] = self.option.lengths[option]
        
        # find longest option items
        length = 0
        for option in self.option.displayItems:
            for i in range(0, len( self.domainRecords )):
                length = self.font.measure(
                                           self.domainRecords[i].record[option], 
                                           self.font._root.focus_displayof()
                                           )
                if length > self.lengths[option]: self.lengths[option] = length
        
        self.height = self.option.height( self.font )
        
        
if __name__ == "__main__":
    # root is unused but required to instantiate root.tk.call( font, ... )
    root = tkinter.Tk()
    
    #f = tkinter.font.Font( family = 'TkTextFont', size = 42, weight = 'normal'  )
    f = tkinter.font.Font()
    
    d = src.domainData.DomainData()
    
    um = UiMetrics( d.domainRecords, f )
    
    print( "lengths: " )
    print( um.lengths )
    