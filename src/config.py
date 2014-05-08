'''
config.py - configuration file class

Created on May 1, 2014

@author: nelsoncs

TODO convert .conf to 'ini' style ie. [url], [group] etc.
'''

class Config():
    '''
    classdocs
    '''

    def __init__( self, fileName ):
        '''
        Constructor
        '''
        self.fileBuffer = []
        
        self.fileName = fileName
        self.loadConfFile( fileName )
    
    # TODO better error handling, allow user to browse if default is not found
    def loadConfFile( self, fileName ):
        try:
            configFile = open( fileName, "r" )
        except IOError:
            print( 'File I/O error.' )
        else:
            print( fileName )
            for line in configFile:
                self.fileBuffer.append( line )        
            configFile.close()
        
    # TODO error handling, check location if not saving under default name
    # TODO allow alternate conf file name
    def appendConfFile( self, url ):
        try:
            configFile = open( self.fileName, "a" )
        except (IOError, BlockingIOError):
            print( 'File I/O error when opening ', configFile )
        else:
            try:
                written  = configFile.write( url + "\n" )
            except ( IOError, BlockingIOError ):
                print( 'File I/O error when writing to ', configFile )
            else:
                print( "written bytes = ", written, ' to ', configFile )
                configFile.close()

    
if __name__ == '__main__':
    '''
    Basic tests for the Config class
    '''
    c = Config( 'domain_check.conf'  )
    c.appendConfFile( 'tesla.com' )
    print( c.fileName )
    print( c.fileBuffer )
