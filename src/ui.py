'''
ui.py - creates a tkinter canvas, presents whois data fields as a table with a
        single line header and gird lines.  TODO: Sorts entries by date and colors 
        entries with less than one month expiration red and three months as orange.
        TODO - class has too much responsibility for data manipulation

Created on Apr 28, 2014

@author: nelsoncs
'''
import tkinter
import src.options

class Ui(tkinter.Frame):
    '''
    classdocs
    '''

    def __init__(self, master=None):
        self.current_x = 10
        self.current_y = 10
    
        tkinter.Frame.__init__(self, master)
        self.createWidgets(master)
        self.pack()
        
        # data items to display
        self.options = src.options.Options()
        
    def createWidgets(self, master=None):
        self.canvas = tkinter.Canvas(master, width = 800, height =600 )
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

    def printTable( self, records ):
        
        # determine field sizes
        
        # determine total width
        
        # determine total height
        
        # print header
        for heading in self.options.displayItems:
            self.canvas.create_text(
                                    self.current_x, 
                                    self.current_y, 
                                    anchor = 'nw', 
                                    state = 'normal', 
                                    text = heading
                                    )
            self.current_x += 180
            
        # print separator
        self.lineHorizontal(10, 190 * len( self.options.displayItems ), 
                            (self.current_y + 15) 
                           )
            
        # print records
        self.current_y += 20
        for r in records:
            self.current_x = 10
            for key in self.options.displayItems:
                self.canvas.create_text(
                                    self.current_x, 
                                    self.current_y, 
                                    anchor = 'nw', 
                                    state = 'normal', 
                                    text = r.record[key]
                                    )
                self.current_x += 180
            self.current_y += 20
    
    def autoClearEntry( self ):
        pass
    
    def addNewUrlEntry( self ):
        pass

if __name__ == '__main__':
    root = tkinter.Tk()
    app = Ui(master=root)
    app.mainloop()
    
    