'''
Created on Apr 28, 2014

@author: nelsoncs
'''
import tkinter
import src.ui
import src.config

class DomainCheck():
    
    def __init__( self ):
        self.parser = src.parse.Parse( self )
        self.config = src.config.Config( self )
        
        self.load_configured_data()
        
        self.root = tkinter.Tk()
        ui = src.ui.Ui( master=self.root )
        ui.mainloop()

    def loadConfiguredData( self ):
        self.whoisLines = self.config.loadFile()
        
        for line in self.whoisLines:
            self.ui.print_table_row( self, line )
        

if __name__ == '__main__':
    dc = DomainCheck()