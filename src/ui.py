'''
ui.py - creates a tkinter canvas, presents whois data fields as a table with a
        single line header and gird lines.  TODO: Sorts entries by date and colors 
        entries with less than one month expiration red and three months as orange.

Created on Apr 28, 2014

@author: nelsoncs
'''
import tkinter

class Ui(tkinter.Frame):
    '''
    classdocs
    '''
    current_x = 0
    current_y = 0


    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.createWidgets(master)
        self.pack()
        
    def createWidgets(self, master=None):
        self.canvas = tkinter.Canvas(master, width = 300, height =600 )
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
        
    def printTableRow( self, record ):
        self.current_y += 30
        self.canvas.create_text(10, self.current_y, anchor = 'nw', state = 'normal', 
                                text = "Registrar Registration Expiration Date"
                                )
        self.current_y += 30
        self.canvas.create_text(10, self.current_y, anchor = 'nw', state = 'normal',
                                text = record['Registrar Registration Expiration Date']
                                )
    def printTable( self, records ):
        
        # determine fields sizes
        
        # determine total width
        
        # determine total height
        
        # print header
        
        # print records
        pass
    
    def autoClearEntry( self ):
        pass
    
    def addNewUrlEntry( self ):
        pass

if __name__ == '__main__':
    root = tkinter.Tk()
    app = Ui(master=root)
    app.mainloop()
    
    