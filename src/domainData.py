'''
domainData.py - Creates a list of records.  Each record is a dict mapping containing data fields
             a given whois record.

Created on May 4, 2014

@author: nelsoncs
'''
import src.config
import src.parse
import src.options

class DomainData():
    #
    #  Data as singletons (class attribute)
    #
    domainRecords = []
    
    '''
    http://data.iana.org/TLD/tlds-alpha-by-domain.txt
    '''
    validExtensions = "tlds-alpha-by-domain.txt"
    tldsNames = []

    def __init__( self, file ):
        self.configFile = file
        
        #TODO  tie to Options
        self.sortField = "Registrar Registration Expiration Date"
    
        # load the config file
        self.config = src.config.Config( self.configFile )
        
        # load acceptable tlds extensions
        self.loadTldsFile( self.validExtensions )
        
        # parse the config data
        self.parseMultiple( self.config )
        
        # sort before display
        # TODO pull out to a class for an "options" panel
        self.sort( self.sortField )
            
        # TODO better error handling, allow user to browse if default is not found
    def loadTldsFile( self, fileName ):
        try:
            tldsFile = open( fileName, "r" )
        except IOError:
            print( 'File I/O error trying to load: ', fileName )
        else:
            print( fileName )
            for line in tldsFile:
                self.tldsNames.append( line.strip().lower() )        
            tldsFile.close()
            print(self.tldsNames)
            
    def checkUrl(self, url):
        url = url.strip()
        
        if (url.rsplit( '.', 1 ))[-1].lower() in self.tldsNames:
            return True
        else:
            return False
        
    def parseAndAppend(self, domain):
        domain = domain.strip()
        print( "DomainData.parseAndAppend: ", domain )
                    
        if self.checkUrl( domain ) == True:
            p = src.parse.Parse( domain)
            self.domainRecords.append( p )
        else:
            print( "Malformed url: ", domain )
        
    def parseMultiple( self, config ):
        for domain in config.fileBuffer:
            self.parseAndAppend(domain)
            
    def sort( self, sortKey ):
        self.domainRecords.sort( key = lambda ddl: ddl.record[sortKey] )
    
    # print only items found in options
    def printRecord( self, record ):
        options = src.options.Options()
        print("printRecord()")
        for key in options.displayItems:
            print( record[key] )

if __name__ == '__main__':
    dd = DomainData("domain_track.conf")
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
    
            