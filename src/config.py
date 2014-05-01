'''
Created on May 1, 2014

@author: nelsoncs
'''

class Config():
    '''
    classdocs
    '''

    file_buffer = []
    fileName   = 'domain_check.conf'

    def __init__( self ):
        '''
        Constructor
        '''
        pass
    
    # TODO error handling
    def loadFile(self):
        configFile = open( self.fileName, "r" )
        for eachLine in configFile:
            print( eachLine )
        configFile.close()
    
    # TODO error handling
    def saveFile(self):
        pass
    
if __name__ == '__main__':
    c = Config()
    