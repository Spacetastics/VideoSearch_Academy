#This imports the library tkinter what is used to make the GUI
import tkinter
#This creates the main window
ResourceMachine=tkinter.Tk()
#This is the name for the windows
ResourceMachine.title("VideoSearch Academy")
#This is what determines the window size
ResourceMachine.geometry("1000x600")
tkinter.Grid.rowconfigure(ResourceMachine, 0, weight=0)
tkinter.Grid.columnconfigure(ResourceMachine, 1, weight=4)

sRequest=tkinter.StringVar()
#This is the search bar
searchBar2 = tkinter.Entry(ResourceMachine,textvariable=sRequest, font=('calibre',10,'normal'))
searchBar2.grid(row=1, column=1, sticky="nsew")


#This is what prints what the user searched
def sQuery():

   sRequest = searchBar2.get()
   print("You Searched:",sRequest)
#This is the name for the search bar
searchBar1 = tkinter.Label(ResourceMachine, text="What Is Your Topic",font=("comic sans ms",17,"bold")).grid(row=0, column=1, sticky="nsew")
#searchBar1.pack()
#.grid(row=0, column=1)
#searchBar2 = tkinter.Entry(ResourceMachine,textvariable=sRequest, font=('calibre',10,'normal')).grid(row=0, column=1)
nRequest=tkinter.IntVar()

#searchButtom1 = tkinter.Button (ResourceMachine, text="Search",command=lambda:[sQuery(), nQuery()]).grid(column=1,row=2)
#This is the selector for number of results per page
searchNumberName=tkinter.Label(ResourceMachine,text="Results Per Page")
searchNumber=tkinter.Spinbox( ResourceMachine, from_=5, to=20,textvariable=nRequest,width=2)
searchNumber.grid(row=10,column=1, sticky="ns")
searchNumberName.grid(row=9,column=1, sticky="nsew")
#this is how many search results will be on the page at a time
def nQuery():

   nRequest = searchNumber.get()
   print(nRequest,"results")
#this shows what option of video length is picked
def lChoice():
   lenChoice= "U Picked " + str(choice1.get())
   #tkinter.Label(ResourceMachine, text=choice1)
   print(lenChoice)
choice1 = tkinter.StringVar()

# C1= tkinter.Radiobutton(ResourceMachine,text="Shorter Than 4 Minutes", variable=choice1, value="short",command=lChoice)
# C2= tkinter.Radiobutton(ResourceMachine,text="Between 4 and 20 Minutes", variable=choice1, value="medium",command=lChoice)
# C3= tkinter.Radiobutton(ResourceMachine,text="Longer Than 20 Minutes", variable=choice1, value="long",command=lChoice)
# C4= tkinter.Radiobutton(ResourceMachine,text="Any Length", variable=choice1, value="any",command=lChoice)
C1= tkinter.Radiobutton(ResourceMachine,text="Shorter Than 4 Minutes", variable=choice1, value="short")
C2= tkinter.Radiobutton(ResourceMachine,text="Between 4 and 20 Minutes", variable=choice1, value="medium")
C3= tkinter.Radiobutton(ResourceMachine,text="Longer Than 20 Minutes", variable=choice1, value="long")
C4= tkinter.Radiobutton(ResourceMachine,text="Any Length", variable=choice1, value="any")
C1.grid(row=5,column=1)
C2.grid(row=6,column=1)
C3.grid(row=7,column=1)
C4.grid(row=8,column=1)
#select does not simulate a click invoke does
C4.select()
#C4.invoke()
label = tkinter.Label(ResourceMachine)
#label=Label(ResourceMachine)
#add page numbers and pages

sSpace=tkinter.Label ( ResourceMachine, text="----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
sSpace.grid(row=14,column=1)
#this is the search button
searchButton1 = tkinter.Button (ResourceMachine, text="Search",bg="light sky blue",activebackground="deep sky blue",command=lambda:[sQuery(), nQuery(),lChoice()]).grid(column=1,row=2, sticky="ns")

#this checks if the selected page is a valid number
def pageMaker():
   pNumber = pNumMaker.get()

   #pNumber2= int(pNumber)
   if pNumber.isdigit()==True:

      print(pNumber)

   else:
      pass
#this is the name for the page selector
pNumName=tkinter.Label(ResourceMachine,text="Page #:",anchor="center")
pNumName.grid(row=11,column=1, sticky="nsew")
pNumber=tkinter.IntVar()
#this is the text box for the page selector
pNumMaker = tkinter.Entry(ResourceMachine,textvariable=pNumber,font=('calibre',10,'normal'))
pNumMaker.grid(row=12, column=1, sticky="ns")
#thios is the go to the selected page button

pageButton1 = tkinter.Button (ResourceMachine, text="Go",bg="light sky blue",activebackground="deep sky blue",command=pageMaker).grid(column=1,row=13, sticky="ns")
#this is a function that gets the page number selected and prints it
def pNVal():

   sRequest = searchBar2.get()
   print(sRequest)
#This is what keeps the program constantly checking for new changes
ResourceMachine.mainloop()
