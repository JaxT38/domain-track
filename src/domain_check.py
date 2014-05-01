'''
Created on Apr 28, 2014

@author: sgk
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

    def load_configured_data( self ):
        self.whois_lines = self.config.load_file()
        
        for line in self.whois_lines:
            self.ui.print_table_row( self, line )
        

if __name__ == '__main__':
    dc = DomainCheck()