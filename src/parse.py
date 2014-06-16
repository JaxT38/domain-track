'''
parse.py - uses subprocess.Popen to capture stdout from sys utility 'whois'
           and retain all lines containing ':', as a separator, for key:value pairs.

Created on Apr 28, 2014

@author: nelsoncs
'''
import subprocess

class Parse():
    
    def __init__( self, url ):
        self.whoisLines = []
        self.record = {}
        
        self.whoisLines = self.callWhois( url )
        self.parseLines( self.whoisLines )
        
    def parseLines( self, whoisLines ):       
        for element in whoisLines:
            if element.count( ': ' ) > 0:
                splitElement = element.split( sep = ': ', maxsplit = 1 )
                #print( splitElement )
                #print( splitElement[0], "  : ", splitElement[1] )
                splitElement[1] = splitElement[1].rstrip("/")
                self.record[splitElement[0]] = splitElement[1].strip()
            else:
                #print( "Skipped line", countLine )
                pass

    # TODO why does this declare a local var and return a list instead of no return value        
    def callWhois( self, url ):
        with subprocess.Popen(['whois', url], 
                              stdout = subprocess.PIPE,
                              universal_newlines = True 
                              ) as proc:
            whoisLines = proc.stdout.read().splitlines()
        return whoisLines
        
if __name__ == '__main__':
    '''
    Basic tests for the parse.py class
    '''
    
    p = Parse( 'colenelson.net' )
    print("repr(Parse):")
    repr(p)
    str(p)
    
    print("---------------------------")
    
    print( "whoisLines : " )
    print( p.whoisLines )
    print( "record : ")
    print( p.record )
    print( p.record["Domain Name"] )

    print("---------------------------")
    
    p = Parse('instrument.com')
    print( "whoisLines : " )
    print( p.whoisLines )
    print( "record : ")
    print( p.record )
    print( p.record["Domain Name"] )
    