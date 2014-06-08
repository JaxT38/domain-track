'''
options.py - sets data display options for ui.py

Created on May 3, 2014

@author: nelsoncs
Possible options:

Domain Name
Registry Domain ID  
Registrar WHOIS Server
Registrar URL
Updated Date
Creation Date
Registrar Registration Expiration Date
Registrar
Registrar IANA ID
Registrar Abuse Contact Email
Registrar Abuse Contact Phone
Reseller 
Domain Status
Registry Registrant ID 
Registrant Name
Registrant Organization
Registrant Street
Registrant City
Registrant State/Province
Registrant Postal Code
Registrant Country
Registrant Phone
Registrant Phone Ext 
Registrant Fax 
Registrant Fax Ext 
Registrant Email
Registry Admin ID 
Admin Name
Admin Organization
Admin Street 
Admin City
Admin State/Province
Admin Postal Code
Admin Country
Admin Phone
Admin Phone Ext 
Admin Fax
Admin Fax Ext 
Admin Email 
Registry Tech ID 
Tech Name
Tech Organization 
Tech Street
Tech City
Tech State/Province
Tech Postal Code
Tech Country
Tech Phone
Tech Phone Ext 
Tech Fax
Tech Fax Ext 
Tech Email
Name Server ( Note: multiple nameservers possible )

'''

class Options():
    
    # TODO tick boxes to select displayed data
    displayItems = [
               "Domain Name",
               "Registrar URL",
               "Name Server",
               "Registrar Registration Expiration Date"
               ]

    def __init__( self ):
        '''
        Constructor
        '''
        pass

        
if __name__ == "__main__":
    opt = Options()
    
    print( opt.displayItems )

