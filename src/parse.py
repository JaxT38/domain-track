'''
Created on Apr 28, 2014

@author: nelsoncs
'''
import subprocess

class Parse():
    
    record = []
    
    def __init__( self, url ):
        self.callWhois( url )
        
    def parseLines( self, record ):
        #return whoisLines
        pass    
            
    def callWhois( self, url ):
        with subprocess.Popen(['whois', url], stdout = subprocess.PIPE ) as proc:
            print( proc.stdout.read() )
            print("------->")
        
        whoisLines = []
        whoisLines = self.parseLines( self, self.record )
        return 
    
    def urlValidate( self ):
        pass

if __name__ == '__main__':
    p = Parse( 'colenelson.net' )

    