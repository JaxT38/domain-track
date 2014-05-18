'''
options.py - sets data display options for ui.py

Created on May 3, 2014

@author: nelsoncs
'''

class Options():
    '''
    classdocs
    '''

    def __init__( self ):
        '''
        Constructor
        '''
            # TODO tick boxes to select displayed data
        self.displayItems = [
                   "Domain Name",
                   "Registrar URL",
                   "Name Server",
                   "Registrar Registration Expiration Date"
                   ]
    
    def itemWidth( self ):
        pass
    
    def itemHeight( self ):
        pass
    
    
        
if __name__ == '__main__':
    pass