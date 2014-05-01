'''
Created on Apr 28, 2014

@author: sgk
'''
import subprocess

class Parse():
    
    record = []
    
    def __init__( self, url ):
        self.call_whois( url )
        
    def parse_lines( self, record ):
        #return whois_lines
        pass    
            
    def call_whois( self, url ):
        with subprocess.Popen(['whois', url], stdout = subprocess.PIPE ) as proc:
            print( proc.stdout.read() )
            print("------->")
        
        whois_lines = []
        whois_lines = self.parse_lines( self, self.record )
        return 
    
    def urlValidate( self ):
        pass

if __name__ == '__main__':
    p = Parse( 'colenelson.net' )

    