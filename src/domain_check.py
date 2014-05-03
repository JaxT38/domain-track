'''
domain_check.py - Parses sys utility 'whois' output for a set of domain name 
                  urls and puts up a tkinter canvas object showing urls, registrars
                  and expiration dates.
                  A simple configuration file (domain_check.conf) is used to retain
                  a search list.
                  Written for linux and unices, but might work on windows with:
                  http://technet.microsoft.com/en-us/sysinternals/bb897435.aspx.
                  Untested on windows.
                  Each class has a __main__ for basic tests, run the program using
                  'python domain_check.py'.  Written for python 3.4.


Created on Apr 28, 2014

@author: nelsoncs
'''
import tkinter
import src.ui
import src.config

class DomainCheck():
    
    def __init__( self ):
        self.parser = src.parse.Parse( self )
        self.config = src.config.Config( self, 'domain_check.conf' )
        
        self.load_configured_data()
        
        self.root = tkinter.Tk()
        ui = src.ui.Ui( master=self.root )
        ui.mainloop()

    def loadConfiguredData( self ):
        self.whoisLines = self.config.loadConfFile()
        
        for line in self.whoisLines:
            self.ui.print_table_row( self, line )
        

if __name__ == '__main__':
    dc = DomainCheck()