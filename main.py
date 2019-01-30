from Tkinter import *

import tkMessageBox

class main:
    
    def __init__(self, master):
        
        self.master = master 
        self.master.title("TIC TAC TOE")
        self.label = Label(self.master, text = "OPTIONS", font=("Helvetica", 20), bg = "darkred", fg = "silver")
        self.label.pack(side = TOP, fill = X) 
        self.sin = Button(self.master, text = "Single Player",font=("Helvetica", 15),padx=32,pady=32, bg = "gold", fg = "blue", command = self.sgp)
        self.sin.pack(side = LEFT)
        self.mul = Button(self.master, text = "Multi Player",font=("Helvetica", 15), padx=32,pady=32,bg = "palegreen", fg = "maroon", command = self.mul)
        self.mul.pack(side = LEFT) 
        self.exit = Button(self.master, text = "QUIT",font=("Helvetica", 16),padx=32,pady=32,bg = "red", fg = "lightblue", command = self.quit).pack(side = LEFT)



    def quit(self):
        
        self.master.destroy()


    def sgp(self):
        
        self.master2 = Toplevel()
        self.master.withdraw()
        self.master2.deiconify()
        single_player(self.master2)

    def mul(self):
        
        self.master2 = Toplevel()
        self.master.withdraw()
        self.master2.deiconify()
        multi_player(self.master2)

#single player
class single_player:
    
    board = [ "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
    
    def __init__(self, root):

        
        self.root=root
        self.frame = Frame(root)
        self.frame.pack()

        self.button1 = Button(self.frame,padx=32,pady=32,bg="black",fg="white")
        self.button1.bind("<ButtonRelease-1>", self.task)
        self.button1.grid(row=0,column=0)

        self.button2 = Button(self.frame,padx=32,pady=32,bg="black",fg="white")
        self.button2.bind("<ButtonRelease-1>", self.task)
        self.button2.grid(row=0, column=1)

        self.button3 = Button(self.frame,padx=32,pady=32,bg="black",fg="white")
        self.button3.bind("<ButtonRelease-1>", self.task)
        self.button3.grid(row=0, column=2)

        self.button4 = Button(self.frame,padx=32,pady=32,bg="black",fg="white")
        self.button4.bind("<ButtonRelease-1>", self.task)
        self.button4.grid(row=1,column=0)

        self.button5 = Button(self.frame,padx=32,pady=32,bg="black",fg="white")
        self.button5.bind("<ButtonRelease-1>", self.task)
        self.button5.grid(row=1, column=1)

        self.button6 = Button(self.frame,padx=32,pady=32,bg="black",fg="white")
        self.button6.bind("<ButtonRelease-1>", self.task)
        self.button6.grid(row=1, column=2)

        self.button7 = Button(self.frame,padx=32,pady=32,bg="black",fg="white")
        self.button7.bind("<ButtonRelease-1>", self.task)
        self.button7.grid(row=2,column=0)

        self.button8 = Button(self.frame,padx=32,pady=32,bg="black",fg="white")
        self.button8.bind("<ButtonRelease-1>", self.task)
        self.button8.grid(row=2,column=1)

        self.button9 = Button(self.frame,padx=32,pady=32,bg="black",fg="white")
        self.button9.bind("<ButtonRelease-1>", self.task)
        self.button9.grid(row=2,column=2)

        self.button10=Button(self.frame,padx=32,pady=32,fg="black",bg="red")
        self.button10.bind("<ButtonRelease-1>",self.task)
        self.button10.grid(row=3,column=2)
        
        self.B = Button(self.frame,padx=32,pady=32,bg="white",fg="red")
        self.button10.bind("<ButtonRelease-1>",self.task)
        self.B.grid(row=3,column=0,columnspan=2)
        
        self.reset()
        
        self.view()
        
    def view(self):
        
        self.button1.config( text = self.board[0],font=('Helvetica 30 bold'),height=1,width=2)
        self.button2.config( text = self.board[1],font=('Helvetica 30 bold'),height=1,width=2)
        self.button3.config( text = self.board[2],font=('Helvetica 30 bold'),height=1,width=2)
        self.button4.config( text = self.board[3],font=('Helvetica 30 bold'),height=1,width=2)
        self.button5.config( text = self.board[4],font=('Helvetica 30 bold'),height=1,width=2)
        self.button6.config( text = self.board[5],font=('Helvetica 30 bold'),height=1,width=2)
        self.button7.config( text = self.board[6],font=('Helvetica 30 bold'),height=1,width=2)
        self.button8.config( text = self.board[7],font=('Helvetica 30 bold'),height=1,width=2)
        self.button9.config( text = self.board[8],font=('Helvetica 30 bold'),height=1,width=2)
        self.button10.config(text="BACK",font=('Helvetica 20 bold'),height=1,width=2)
        self.B.config(text="RESET",font=('Helvetica 20 bold '),height=1,width=7)
        
    def task(self, event):
        
        if event.widget == self.button1:
            self.playersj(0)
        if event.widget == self.button2 :
            self.playersj(1)
        if event.widget == self.button3 :
            self.playersj(2)
        if event.widget == self.button4 :
            self.playersj(3)
        if event.widget == self.button5:
            self.playersj(4)
        if event.widget == self.button6 :
            self.playersj(5)
        if event.widget == self.button7 :
            self.playersj(6)
        if event.widget == self.button8 :
            self.playersj(7)
        if event.widget == self.button9 :
            self.playersj(8)
        if event.widget == self.button10 :
            self.endProgram()
        if event.widget == self.B :
            self.reset()

    def playersj(self, pos):
        if self.board[pos] == "   ":
            
            self.board[pos] = "X"
            self.view()
            i=self.checkwin()
            if (i!=1):
               self.computersturn()
               self.view()
               self.checkwin()
            

        else:   
            tkMessageBox.showwarning("Invalid move",
                                    "move is not valid!")

    def checkwin(self):
        
       if (self.board[0] == self.board[1]=="X" and self.board[1] == self.board[2]=="X"
                or self.board[3] == self.board[4] =="X" and self.board[4] == self.board[5]=="X"
                or self.board[6] == self.board[7]=="X" and self.board[7] == self.board[8]=="X"
                or self.board[0] == self.board[3]=="X" and self.board[3] == self.board[6]=="X"
                or self.board[1] == self.board[4]=="X" and self.board[4] == self.board[7]=="X"
                or self.board[2] == self.board[5]=="X" and self.board[5] == self.board[8]=="X"
                or self.board[0] == self.board[4]=="X" and self.board[4] == self.board[8]=="X"
                or self.board[2] == self.board[4]=="X" and self.board[4] == self.board[6]=="X"):
         self.unbind()
         tkMessageBox.showwarning("RESULT","player wins")
         self.reset()
         self.bind()
         
         return 1
        
       if(self.board[0] == self.board[1]=="O" and self.board[1] == self.board[2]=="O"
                or self.board[3] == self.board[4] =="O" and self.board[4] == self.board[5]=="O"
                or self.board[6] == self.board[7]=="O" and self.board[7] == self.board[8]=="O"
                or self.board[0] == self.board[3]=="O" and self.board[3] == self.board[6]=="O"
                or self.board[1] == self.board[4]=="O" and self.board[4] == self.board[7]=="O"
                or self.board[2] == self.board[5]=="O" and self.board[5] == self.board[8]=="O"
                or self.board[0] == self.board[4]=="O" and self.board[4] == self.board[8]=="O"
                or self.board[2] == self.board[4]=="O" and self.board[4] == self.board[6]=="O"):
         self.unbind()
         tkMessageBox.showwarning("RESULT","computer wins")
         self.reset()
         self.bind()

       if(self.board[0] != "   " and self.board[1] != "   "
                  and self.board[2] != "   " and self.board[3] != "   " 
                  and self.board[4] != "   " and self.board[5] != "   "
                  and self.board[6] != "   " and self.board[7] != "   " 
                  and self.board[8] != "   "):
         self.unbind()
         tkMessageBox.showwarning("RESULT","game draw")
         self.reset()
         self.bind()
         return 1
        
    def computersturn(self):
        
       if(self.board[4]=="X"):
           if(self.board[1]=="X"):
               for j in [7,6 ,3,2, 5 ,8 ]:
                       if self.board[j] == "   ":
                           self.board[j] = "O"
                           return
           if(self.board[2]=="X"):
               for j in [6,0 ,3,5, 7 ,2 , 1 ,8 ]:
                       if self.board[j] == "   ":
                           self.board[j] = "O"
                           return

           if(self.board[6]=="X"):
               for j in [0, 2 ,1,7, 5, 3 , 8]:
                       if self.board[j] == "   ":
                           self.board[j] = "O"
                           return
           if(self.board[5]=="X"):
               for j in [3,6,2,1,7,8]:
                       if(self.board[j] == "   "):
                           self.board[j] = "O"
                           return

           if(self.board[7]=="X"):
               for j in [0, 1,2,6, 3,5 , 8]:
                       if self.board[j] == "   ":
                           self.board[j] = "O"
                           return
           if(self.board[8]=="X"):
               for j in [ 2,1,7,5, 3,6]:
                       if self.board[j] == "   ":
                           self.board[j] = "O"
                           return
           else: 
               for j in [0,5, 1, 7 ,2, 6 , 3 ,5 , 8]:
                       if self.board[j] == "   ":
                           self.board[j] = "O"
                           return
       
       elif(self.board[4]!="X" or self.board[4]=="   " ):
          if(self.board[2]=="X"):
              if(self.board[0]=="X" or self.board[0]=="   "):
               for j in [4, 0, 1,7, 2,5, 3, 6,8]:
                       if self.board[j] == "   ":
                           self.board[j] = "O"
                           return
          if(self.board[8]=="X"):
              if(self.board[6]=="X"or self.board[6]=="   "):
               for j in [4, 7, 1,3,5, 2]:
                       if self.board[j] == "   ":
                           self.board[j] = "O"
                           return
          else:
               for j in [4, 0, 8, 2, 6, 1, 3, 8, 5]:
                       if self.board[j] == "   ":
                           self.board[j] = "O"
                           return
       else:
               for j in [4, 0, 8, 2, 6, 1, 3, 8, 5]:
                       if self.board[j] == "   ":
                           self.board[j] = "O"
                           return                 
           
           
    def endProgram(self):
        self.master=Toplevel()
        self.root.withdraw()
        self.master.deiconify()
        main(self.master)
        
        
    def reset(self):
        
        for i in range(0,9):
            if(self.board[i]=="X" or self.board[i]=="O"):
                self.board[i]="   "
                
        self.button1.config( text = self.board[0],font=('Arial 30 bold'),height=1,width=2)
        self.button2.config( text = self.board[1],font=('Arial 30 bold'),height=1,width=2)
        self.button3.config( text = self.board[2],font=('Arial 30 bold'),height=1,width=2)
        self.button4.config( text = self.board[3],font=('Arial 30 bold'),height=1,width=2)
        self.button5.config( text = self.board[4],font=('Arial 30 bold'),height=1,width=2)
        self.button6.config( text = self.board[5],font=('Arial 30 bold'),height=1,width=2)
        self.button7.config( text = self.board[6],font=('Arial 30 bold'),height=1,width=2)
        self.button8.config( text = self.board[7],font=('Arial 30 bold'),height=1,width=2)
        self.button9.config( text = self.board[8],font=('Arial 30 bold'),height=1,width=2)
        


    def unbind(self):
        
        self.button1.unbind("<ButtonRelease-1>")
        self.button2.unbind("<ButtonRelease-1>")
        self.button3.unbind("<ButtonRelease-1>")
        self.button4.unbind("<ButtonRelease-1>")
        self.button5.unbind("<ButtonRelease-1>")
        self.button6.unbind("<ButtonRelease-1>")
        self.button7.unbind("<ButtonRelease-1>")
        self.button8.unbind("<ButtonRelease-1>")
        self.button9.unbind("<ButtonRelease-1>")
        self.button10.unbind("<ButtonRelease-1>")
        self.B.unbind("<ButtonRelease-1>")


    def bind(self):
        
        self.button1.bind("<ButtonRelease-1>",self.task)
        self.button2.bind("<ButtonRelease-1>",self.task)
        self.button3.bind("<ButtonRelease-1>",self.task)
        self.button4.bind("<ButtonRelease-1>",self.task)
        self.button5.bind("<ButtonRelease-1>",self.task)
        self.button6.bind("<ButtonRelease-1>",self.task)
        self.button7.bind("<ButtonRelease-1>",self.task)
        self.button8.bind("<ButtonRelease-1>",self.task)
        self.button9.bind("<ButtonRelease-1>",self.task)
        self.button10.bind("<ButtonRelease-1>",self.task)
        self.B.bind("<ButtonRelease-1>",self.task)

#multi player
class multi_player:
   
    def __init__(self,master):
        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack(fill="both", expand=True)
       
        self.canvas = Canvas(self.frame, width=300, height=300)
        self.canvas.pack(fill="both", expand=True)
        
        #Shows status of game
        self.label=Label(self.frame, text='TIC TAC TOE',font=("Helvetica", 16), height=3, bg='black', fg='white')
        self.label.pack(fill="both", expand=True)
        
        #frame to contain the buttons
        self.frameb=Frame(self.frame)
        self.frameb.pack(fill="both", expand=True)
        
        #Buttons to initiate the game
        self.Start1=Button(self.frameb, text='RESET',font=("Helvetica", 12), height=3, command=self.start1,bg='purple', fg='white')
        self.Start1.pack(fill="both", expand=True, side=LEFT)
        self.back = Button(self.frameb, text = '     BACK     ',font=("Helvetica", 12), command = self.back,bg = 'red', fg = 'white').pack(fill = "both", side = LEFT)
        self.start1()
        self.board()

    def back(self):
        self.master2=Toplevel()
        self.master.withdraw()
        self.master2.deiconify()
        main(self.master2)


    def start1(self):
        #Starts double player
        
        #clears canvas
        self.canvas.delete(ALL)
        self.label['text']=('TIC TAC TOE')
        
        #click to call the function
        self.canvas.bind("<ButtonPress-1>", self.dublayer)  
        self.board()
        #matrix formation
        self.TTT=[[0,0,0],[0,0,0],[0,0,0]]
        
        #number of terms to distinguish whose turn is there
        self.i=0
        
        #bollean can be changed to end the game
        self.j=True

   

    def end(self):
        #making click ineffective
        self.canvas.unbind("<ButtonPress-1>")
        self.j=False
 
    def board(self):
        #Creates the board
        self.canvas.create_rectangle(0,0,300,300, outline="black")
        self.canvas.create_rectangle(100,300,200,0, outline="black")
        self.canvas.create_rectangle(0,100,300,200, outline="black")
        
    def dublayer(self,event):
        for k in range(0,300,100):
            for j in range(0,300,100):
                #checks if the mouse input is in a bounding region
                if event.x in range(k,k+100) and event.y in range(j,j+100):
                    #checks if there is nothing in the bounding region
                    if self.canvas.find_enclosed(k,j,k+100,j+100)==():
                        #checks for first player
                        if self.i%2==0:
                            #draws circle
                            X=(2*k+100)/2
                            Y=(2*j+100)/2
                            X1=int(k/100)
                            Y1=int(j/100)
                            self.canvas.create_oval( X+25, Y+25, X-25, Y-25, width=4, outline="red")
                            self.TTT[Y1][X1]+=1
                            self.i+=1
                        else:
                            #draws the cross
                            X=(2*k+100)/2
                            Y=(2*j+100)/2
                            X1=int(k/100)
                            Y1=int(j/100)
                            self.canvas. create_line( X+20, Y+20, X-20, Y-20, width=4, fill="blue")
                            self.canvas. create_line( X-20, Y+20, X+20, Y-20, width=4, fill="blue")
                            self.TTT[Y1][X1]+=4
                            self.i+=1
        self.check()
                        
    def check(self):
        #horizontal check
        for i in range(0,3):
            if sum(self.TTT[i])==12:
                self.label['text']=('PLAYER 2 WINS!')
                self.end()
            if sum(self.TTT[i])==3:
                self.label['text']=('PLAYER 1 WINS!')
                self.end()
        #vertical check 
        self.ttt=[[row[i] for row in self.TTT] for i in range(3)]
        for i in range(0,3):            
            if sum(self.ttt[i])==12:
                self.label['text']=('PLAYER 2 WINS!')
                self.end()
            if sum(self.ttt[i])==3:
                self.label['text']=('PLAYER 1 WINS!')
                self.end()
        #check for diagonal wins
        if self.TTT[1][1]==4:
            if self.TTT[0][0]==self.TTT[1][1] and self.TTT[2][2]==self.TTT[1][1] :
                self.label['text']=('PLAYER 2 WINS!')
                self.end()
            if self.TTT[0][2]==self.TTT[1][1] and self.TTT[2][0]==self.TTT[1][1] :
                self.label['text']=('PLAYER 2 WINS!')
                self.end()
        if self.TTT[1][1]==1:
            if self.TTT[0][0]==self.TTT[1][1] and self.TTT[2][2]==self.TTT[1][1] :
                self.label['text']=('PLAYER 1 WINS!')
                self.end()
            if self.TTT[0][2]==self.TTT[1][1] and self.TTT[2][0]==self.TTT[1][1] :
                self.label['text']=('PLAYER 1 WINS!')
                self.end()
        #check for draws
        if self.j==True:
            a=0
            for i in range(0,3):
                a+= sum(self.TTT[i])
            #As the player starts with a circle(value=1),
            #There will be a total of 5(1) and 4(4)=21
            if a==21:
                self.label['text']=("GAME DRAW!")
                self.end()
#multi player end

root = Tk()
d= main(root)
root.mainloop()