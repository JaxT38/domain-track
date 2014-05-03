'''
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
        
        self.lineHorizontal(0, 300, 25)
        self.lineVertical(1, 0, 60)
        self.lineVertical(60, 0, 60)
        
        
        
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
    
    def autoClearEntry( self ):
        pass
    
    def addNewUrlEntry( self ):
        pass

if __name__ == '__main__':
    root = tkinter.Tk()
    app = Ui(master=root)
    app.mainloop()
    
    