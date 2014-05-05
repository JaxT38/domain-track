'''
data.py - Creates a list of records.  Each record is a dict mapping containing data fields
          from a given whois record.

Created on May 4, 2014

@author: nelsoncs
'''
import src.config
import src.parse

class DomainData():
    '''
    classdocs
    '''
    
    listOfRecords = []
    sortField     = "Registrar Registration Expiration Date"

    def __init__( self ):
        '''
        Constructor
        '''
        # load the config file
        self.config = src.config.Config( 'domain_check.conf' )
        
        # parse the config data and display in gui
        self._parseConfiguredData( self.config )
    
    def _parseConfiguredData( self, config ):
        print( config.fileBuffer )
        for domain in config.fileBuffer:
            print( domain )
            p = src.parse.Parse( domain.strip() )
            self.listOfRecords.append( p )
            
        self.sortConfiguredData( self.sortField )
            
    def sortConfiguredData( self, sortKey ):
        pass
    
# TODO better test
if __name__ == '__main__':
    dd = DomainData()
    print( dd.listOfRecords )
    dd.sortConfiguredData( dd.sortField )
    print( dd.listOfRecords )