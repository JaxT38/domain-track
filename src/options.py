'''
options.py - sets data display options for ui.py

Created on May 3, 2014

@author: nelsoncs
'''
# TODO someone explain to me why you have to import "tkinter.font" instead of tkFont??
# or just "tkinter"
import tkinter.font

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
    
    # params in are tk font object and option index 
    # returns width in pixels
    def width( self, font, index ):
        return font.measure( self.displayItems[index] )
    
    # params in are tk font object
    # returns line height in pixels
    def height( self, font ):
        return font.metrics("linespace")
        
if __name__ == "__main__":
    # root is unused but required to instantiate root.tk.call( font, ... )
    root = tkinter.Tk()
    
    #f = tkinter.font.Font( family = 'TkTextFont', size = 42, weight = 'normal'  )
    f = tkinter.font.Font()
    opt = Options()
    
    for index in range( len(opt.displayItems) ):
        print( opt.width( f, index ), ", ", opt.height( f ) )
