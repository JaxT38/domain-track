'''
ui.py - creates a tkinter canvas, presents whois data fields as a table with a
        single line header and gird lines.  TODO: Sorts entries by date and colors 
        entries with less than one month expiration red and three months as orange.
        TODO - class has too much responsibility for data manipulation

Created on Apr 28, 2014

@author: nelsoncs
'''
import tkinter.font
import tkinter.ttk
import options
import uiMetrics

class Ui(tkinter.Frame):
    '''
    classdocs
    '''
    
    ''' 
    class (static) attributes for position of top left corner of table 
    '''
    corner_x = 10
    corner_y = 10
    width    = 800
    height   = 600
    buffer_y_lines = 3
    
    textAutoClear = False

    def __init__(self, domainData, master=None):
        
        # data items to display
        self.options = options.Options()
        self.data = domainData
        self.records = self.data.domainRecords
        
        # get default tkfont and will be used it to measure line lengths
        self.font    = tkinter.font.Font()
        
        self.metrics = uiMetrics.UiMetrics( self.records, self.font )
        
        self.current_x = self.corner_x
        self.current_y = self.corner_y
        self.gutter    = self.font.measure(" | ")
        self.setSize()
        
        self.createWidgets(master)
        #self.pack()
        
    #
    # event handlers
    #
    # TODO: better error handlling when whois times out or does other
    #       bad things
    def onEnterKey(self, event):
        print( "Enter key in text widget pressed." )
        # validate text
        
        # append conf file
        text = self.entryUrl.get()
        
        # TODO disallow duplicates: text
        config = getattr( self.data, "config" )
        config.appendConfFile( text )
        
        self.data.parseAndAppend( text )
        
        # re-sort records
        print( "Sorting by: ", getattr(self.data, "sortField" ))
        self.data.sort( getattr( self.data, "sortField" ) )
        
        # re-display all records
        self.resetTable()
        self.printTable()
        
    def autoClearEntry( self, event ):
        if self.textAutoClear == False:
            self.entryUrl.delete(0, tkinter.END)
            self.textAutoClear = True
            # print( "AutoClear in text widget. textAutoClear: ", self.textAutoClear )
    
    #
    # widgets
    #    
    
    def createWidgets(self, master=None):
        
        self.notebook = tkinter.ttk.Notebook(master)

        self.frameMain = tkinter.Frame(master)
        self.frameOptions = tkinter.Frame(master)
        
        self.notebook.add(self.frameMain, text = "Domains")
        self.notebook.add(self.frameOptions, text = "Options")
        self.notebook.pack()

        self.canvas = tkinter.Canvas(
                                     self.frameMain, 
                                     width  = self.width, 
                                     height = self.height
                                      )
        self.canvas.pack()

        self.entryUrl = tkinter.Entry(self.frameMain, background = 'white', width = 50)
        self.entryUrl.insert(0, "Enter a url: example.com")
        self.entryUrl.bind("<Return>", self.onEnterKey, 1)
        self.entryUrl.bind("<FocusIn>", self.autoClearEntry, 1)
        self.entryUrl.pack()
     
    #
    # data table/canvas related methods
    #
        
    # TODO pass canvas in as param
    def lineHorizontal(self, orig_x, distal_x, y):
        self.canvas.create_line(orig_x, y, distal_x, y)
        
    # TODO pass canvas in as param
    def lineVertical(self, x, orig_y, distal_y):
        self.canvas.create_line(x, orig_y, x, distal_y)
        
    def resetTable(self):
        self.current_x = self.corner_x
        self.current_y = self.corner_y
        self.canvas.delete("all")
        self.setSize()
        self.canvas.config(
                           width  = self.width, 
                           height = self.height
                           )
        self.pack()
        
    def lengthOfHeader(self):
        lengthOfHeader = 0
        
        for l in self.metrics.lengths:
            lengthOfHeader += self.metrics.lengths[l] + self.gutter
        lengthOfHeader -= self.gutter
        
        return lengthOfHeader
    
    def setSize(self):
        self.width     = self.lengthOfHeader() + (2 * self.corner_x)
        self.height    = self.metrics.height * (len( self.records ) + self.buffer_y_lines)
                
    # special processing for individual options
    def stripSpecial( self, field, text ):
        if field == "Registrar Registration Expiration Date" or field == "Creation Date":
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
        
        # print each record as a line in a table
        for r in self.records:
            # reset line beginning
            self.current_x = self.corner_x
            
            # move down one line
            self.current_y += self.metrics.height
            
            # 
            print( "Current record: ", r.record )
            
            colorCode = r.record['colorCode']
            
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
                                    font = self.font,
                                    fill = colorCode
                                    )
                # move over by field width
                self.current_x += self.metrics.lengths[field]
                self.current_x += self.gutter
                
                # print vertical separator
#                 self.lineVertical( self.current_x, 
#                                    self.current_y, 
#                                    self.current_y + self.metrics.height 
#                                    )

if __name__ == '__main__':
#     root = tkinter.Tk()
#     app = Ui(master=root)
#     app.mainloop()
    pass
    