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
import src.parse

class DomainCheck():
    
    def __init__( self ):
        # load the config file
        self.config = src.config.Config( 'domain_check.conf' )
        
        #setup tkinter window
        self.root = tkinter.Tk()
        ui = src.ui.Ui( master=self.root )
        
        # parse the config data
        self.loadConfiguredData( self.config, ui )
        
        ui.mainloop()

    '''
    
    '''
    def loadConfiguredData( self, config, ui ):
        print( config.fileBuffer )
        for domain in config.fileBuffer:
            print( domain )
            p = src.parse.Parse( domain.strip() )
            #print( p.record )
            print( "Registrar Registration Expiration Date",  p.record['Registrar Registration Expiration Date'])
            ui.printTableRow( p.record )

if __name__ == '__main__':
    dc = DomainCheck()