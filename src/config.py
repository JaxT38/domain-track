'''
Created on May 1, 2014

@author: sgk
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
    def load_file(self):
        configFile = open( self.fileName, "r" )
        for eachLine in configFile:
            print( eachLine )
        configFile.close()
    
    # TODO error handling
    def save_file(self):
        pass
    
if __name__ == '__main__':
    c = Config()
    