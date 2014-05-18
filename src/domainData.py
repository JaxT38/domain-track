'''
domainData.py - Creates a list of records.  Each record is a dict mapping containing data fields
             a given whois record.

Created on May 4, 2014

@author: nelsoncs
'''
import operator
import src.config
import src.parse
import src.options

class DomainData():
    '''
    classdocs
    '''

    def __init__( self ):
        '''
        Constructor
        '''
        self.domainRecords = []
        self.sortField     = "Registrar Registration Expiration Date"
    
        # load the config file
        self.config = src.config.Config( 'domain_track.conf' )
        
        # parse the config data
        self._parseConfiguredData( self.config )
        
        # sort before display
        self.sortConfiguredData( self.sortField )
    
    def _parseConfiguredData( self, config ):
        print( config.fileBuffer )
        for domain in config.fileBuffer:
            print( domain, "-------------------------------" )
            p = src.parse.Parse( domain.strip() )
            self.domainRecords.append( p )
            
    def sortConfiguredData( self, sortKey ):
        self.domainRecords.sort( key = lambda ddl: ddl.record[sortKey] )
        pass
    
    # print only items found in options
    def printRecord( self, record ):
        options = src.options.Options()
        print("printRecord()")
        for key in options.displayItems:
            print( record[key] )

if __name__ == '__main__':
    dd = DomainData()
    print("repr(DomainData):")
    repr(dd)
    str(dd)
    print("--------------------------***")
    print( dd.domainRecords )
    print("--------------------------###")
    
    options = src.options.Options()
    
    for r in dd.domainRecords:
        dd.printRecord( r.record )
        
    l = lambda ddl: dd.domainRecords[ddl].record["Domain Name"]

    print( "\nlambda test: " + l( 0 ))  
    
            