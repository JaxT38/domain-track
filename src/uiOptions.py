'''
Created on May 19, 2014

@author: sgk

tkinter view functions related to the Options data model (class)
'''
import options
# TODO someone please explain to me why you have to import "tkinter.font" instead of tkFont??
# or just "tkinter"
import tkinter.font
import re
from datetime import datetime

class UiOptions( options.Options ):
    
    date = re.compile( '(\d+-\d+-\d+)' )

    def __init__( self, font ):
        '''
        params: tk font object - current font in use by display element 
        '''
        super().__init__()
        
        # mapping of heading to individual pixel lengths
        self.lengths = {}
        
        # find length of each header item
        for i in range( 0, len( self.displayItems )):
            self.lengths[self.displayItems[i]] = self.width( font, i )
        
    def width( self, font, index ):
        '''
        params: tk font object, Option index 
        return: width in pixels
        '''
        return font.measure( self.displayItems[index] )

    def height( self, font ):
        '''
        simple call to tkfont metrics for the given font object
        params: tk font object 
        return: height in pixels
        '''
        return font.metrics("linespace")
    
    # process option for color highlighting
    def addColorCode(self, domainRecords):
        
        for r in domainRecords:
            
            #print(self.date.search( r.record["Registrar Registration Expiration Date"] ))
            subjectDate = datetime.strptime( self.date.search( r.record["Registrar Registration Expiration Date"] ).group(), '%Y-%m-%d') 
            targetDate = datetime.strptime('2015-06-01', '%Y-%m-%d')
            if ( subjectDate <= targetDate  ):
                # set red
                r.record['colorCode'] = 'red'
            else:
                # set black
                r.record['colorCode'] = 'black'
            #print( r.record['colorCode'] )
        
if __name__ == "__main__":
    # root is unused but required to instantiate root.tk.call( font, ... )
    root = tkinter.Tk()
    
    #f = tkinter.font.Font( family = 'TkTextFont', size = 42, weight = 'normal'  )
    f = tkinter.font.Font()
    uo = UiOptions( f )
    
    for index in range( len(uo.displayItems) ):
        print( uo.width( f, index ), ", ", uo.height( f ) )
        
    print( "print lengths: " )
    print( uo.lengths )
    
    