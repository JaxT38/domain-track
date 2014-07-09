'''
domain_track.py - Parses sys utility 'whois' output for a set of domain name 
                  urls and puts up a tkinter canvas object instance showing urls, 
                  registrars and expiration dates.
                  A simple configuration file (domain_check.conf) is used to retain
                  a search list.
                  Written for linux and unices, but might work on windows with:
                  http://technet.microsoft.com/en-us/sysinternals/bb897435.aspx.
                  Untested on windows.
                  Each class has a __main__ for basic tests. Written for python 3.4.
                  Run the main program using 'python domain_track.py'.

Created on Apr 28, 2014

@author: nelsoncs
'''
import tkinter
import src.ui
import src.domainData

class DomainTrack():
    
    title      = "Domain Tracker - NcsAppSoft.com - 2014 - v. 0.1"
    configFile = "domain_track.conf"
    
    def __init__( self ):
        # setup tkinter window
        self.root = tkinter.Tk()
        self.root.title( self.title )
        
        # source whois data from urls in config file
        dd = src.domainData.DomainData( self.configFile )
        
        # instantiate user interface
        ui = src.ui.Ui( dd, master=self.root )
        ui.printTable()
        
        ui.mainloop()  

if __name__ == '__main__':
    dc = DomainTrack()
    