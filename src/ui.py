'''
ui.py - creates a tkinter canvas, presents whois data fields as a table with a
        single line header and gird lines.  TODO: Sorts entries by date and colors 
        entries with less than one month expiration red and three months as orange.
        TODO - class has too much responsibility for data manipulation

Created on Apr 28, 2014

@author: nelsoncs
'''
import tkinter
import tkinter.font
import src.options
import src.uiMetrics

class Ui(tkinter.Frame):
    '''
    classdocs
    '''
    
    ''' 
    class (static) attributes for position of top left corner of table 
    '''
    corner_x = 10
    corner_y = 10

    def __init__(self, records, master=None):
        
        # data items to display
        self.options = src.options.Options()
        self.records = records
        
        # get default tkfont and will be used it to measure line lengths
        self.font    = tkinter.font.Font()
        
        self.metrics = src.uiMetrics.UiMetrics( self.records, self.font )
        
        self.current_x = self.corner_x
        self.current_y = self.corner_y
        self.gutter  = self.font.measure(" | ")
        
        tkinter.Frame.__init__(self, master)
        self.createWidgets(master)
        self.pack()
        
    def createWidgets(self, master=None):
        self.canvas = tkinter.Canvas(
                                     master, 
                                     width = 1200, 
                                     height = 600,
                                     
                                      )
        self.canvas.pack()

        self.entryUrl = tkinter.Entry(master, background = 'white', width = 50)
        self.entryUrl.insert(0, "Enter a url: example.com")
        self.entryUrl.pack()
        
    # TODO pass canvas in as param
    def lineHorizontal(self, orig_x, distal_x, y):
        self.canvas.create_line(orig_x, y, distal_x, y)
        
    # TODO pass canvas in as param
    def lineVertical(self, x, orig_y, distal_y):
        self.canvas.create_line(x, orig_y, x, distal_y)
        
    def lengthOfHeader(self):
        lengthOfHeader = 0
        
        for l in self.metrics.lengths:
            lengthOfHeader += self.metrics.lengths[l] + self.gutter
        lengthOfHeader -= self.gutter
        
        return lengthOfHeader
    
                
    # special processing for individual options
    def stripSpecial( self, field, text ):
        if field == "Registrar Registration Expiration Date":
            text = text.replace( "z", " " )
            text = text.replace( "t", " " )
            
        return text

    def printTable( self ):
        '''
        
        '''
        
        # print header
        for heading in self.options.displayItems:
            self.canvas.create_text(
                                    self.current_x, 
                                    self.current_y, 
                                    anchor = 'nw', 
                                    state = 'normal', 
                                    text = heading.title(),
                                    font = self.font
                                    )
            self.current_x += self.metrics.lengths[heading]
            self.current_x += self.gutter
            
        self.current_x = self.corner_x    
        
        # print horizontal separator
        self.lineHorizontal(
                            self.current_x, 
                            self.current_x + self.lengthOfHeader(), 
                           (self.current_y + self.metrics.height) 
                           )
        print(self.current_x, " ",
                            self.current_x + self.lengthOfHeader(), " ",
                           (self.current_y + self.metrics.height))
        
        for r in self.records:
            # reset line beginning
            self.current_x = self.corner_x
            
            # move down one line
            self.current_y += self.metrics.height
            
            # print record
            for field in self.options.displayItems:
                textField = r.record[field].lower()
                
                # special processing for specific fields
                textField = self.stripSpecial( field, textField )
                
                # print field
                self.canvas.create_text(
                                    self.current_x, 
                                    self.current_y, 
                                    anchor = 'nw', 
                                    state = 'normal', 
                                    text = textField,
                                    font = self.font
                                    )
                # move over by field width
                self.current_x += self.metrics.lengths[field]
                self.current_x += self.gutter
                
                # print vertical separator
#                 self.lineVertical( self.current_x, 
#                                    self.current_y, 
#                                    self.current_y + self.metrics.height 
#                                    )
    
    def autoClearEntry( self ):
        pass
    
    def addNewUrlEntry( self ):
        pass

if __name__ == '__main__':
    root = tkinter.Tk()
    app = Ui(master=root)
    app.mainloop()
    
    