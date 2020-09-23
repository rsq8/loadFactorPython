#This program calculates the load factor with a GUI
import tkinter
import tkinter.messagebox

#create window
def main():
    root = tkinter.Tk()
    root.title("Flight dispatch program")
    root.resizable(height=False, width=False)

    #create mainframe
    mainframe = tkinter.Frame(root, borderwidth=1, padx=5, pady=5)
    mainframe.pack()

    #create other frames
    #fr1 = tkinter.Frame(mainframe)
    #fr1.pack()

    #label and entry widgets (grid=row,column,columnspan,sticky, pack=side:left, right, top, bottom)
    fr1label = tkinter.Label(mainframe, text="APS weight")
    fr1label.grid(row=1, column=1, sticky=tkinter.W)
    fr1text = tkinter.Entry(mainframe)
    fr1text.grid(row=1, column=2, columnspan=2, sticky=tkinter.W)

    fr2label = tkinter.Label(mainframe, text="pilot")
    fr2label.grid(row=2, column=1, sticky=tkinter.W)
    fr2text = tkinter.Entry(mainframe)
    fr2text.grid(row=2, column=2, columnspan=2, sticky=tkinter.W)

    fr3label = tkinter.Label(mainframe, text="copilot")
    fr3label.grid(row=3, column=1, sticky=tkinter.W)
    fr3text = tkinter.Entry(mainframe)
    fr3text.grid(row=3, column=2, columnspan=2, sticky=tkinter.W)

    fr4label = tkinter.Label(mainframe, text="fuel")
    fr4label.grid(row=4, column=1, sticky=tkinter.W)
    fr4text = tkinter.Entry(mainframe)
    fr4text.grid(row=4, column=2, columnspan=2, sticky=tkinter.W)

    fr5label = tkinter.Label(mainframe, text="paxw")
    fr5label.grid(row=5, column=1, sticky=tkinter.W)
    fr5text = tkinter.Entry(mainframe)
    fr5text.grid(row=5, column=2, columnspan=2, sticky=tkinter.W)

    fr6label = tkinter.Label(mainframe, text="Baggage Weight")
    fr6label.grid(row=6, column=1, sticky=tkinter.W)
    fr6text = tkinter.Entry(mainframe)
    fr6text.grid(row=6, column=2, columnspan=2, sticky=tkinter.W)

    fr7label = tkinter.Label(mainframe, text="Freight Weight")
    fr7label.grid(row=7, column=1, sticky=tkinter.W)
    fr7text = tkinter.Entry(mainframe)
    fr7text.grid(row=7, column=2, columnspan=2, sticky=tkinter.W)

    #create buttons (define the commands first. .get for entry method only works without parameters)
    def disposable_weight():
        crew = int(fr2text.get()) + int(fr3text.get())
        b = 26500 - int(fr1text.get()) - crew
        c = str(b)
        return tkinter.messagebox.showinfo("Disposable Weight", c + "lbs")

    def payload_available():
        crew = int(fr2text.get()) + int(fr3text.get())
        disposableweight = 26500 - int(fr1text.get()) - crew
        payload = disposableweight - int(fr4text.get())
        b = str(payload)
        return tkinter.messagebox.showinfo("Payload", b + "" + "lbs")
    
    def takeoff_weight():
        luggage = int(fr6text.get()) + int(fr7text.get())
        a = str(luggage)
        if luggage > 1000:
            tkinter.messagebox.showwarning("Excess Luggage", a + 'lbs' + "excceds the maximum allowable 1000lbs weight in the baggage compartment")
        takeoffweight = int(fr1text.get()) + int(fr2text.get()) + int(fr3text.get())  + int(fr4text.get()) + int(fr5text.get()) + int(fr6text.get()) + int(fr7text.get())
        b = str(takeoffweight)
        if takeoffweight > 26500:
            tkinter.messagebox.showwarning("Excess Weight", b + "lbs"+ "exceeds the maximum allowable 26500lbs weight for the S92")
        else:
            tkinter.messagebox.showinfo("take-offweight", "the take-off weight is:" + b + "lbs")


    button1 = tkinter.Button(mainframe, text="Disp Weight", command=disposable_weight)
    button1.grid(row=8, column=1, columnspan=2, sticky=tkinter.W)
    button2 = tkinter.Button(mainframe, text="Payload", command=payload_available)
    button2.grid(row=8, column=2, columnspan=2, sticky=tkinter.W)
    button2 = tkinter.Button(mainframe, text="TO weight", command=takeoff_weight)
    button2.grid(row=8, column=3, columnspan=2, sticky=tkinter.W)

    #create menu(s)
    bar = tkinter.Menu(root)
    def quit():
        root.destroy()
    filemenu = tkinter.Menu(bar, tearoff=0)
    filemenu.add_command(label="Exit", command=quit)
    bar.add_cascade(label="File", menu=filemenu)
    root.config(menu=bar)
    def help():
        print("All measeurements for the aircraft are in lbs. Time should be entered in the 24hr format. hrs and mins to be separated by a space.")
    filemenu = tkinter.Menu(bar, tearoff=0)
    filemenu.add_command(label="About", command=help)
    bar.add_cascade(label="Help", menu=filemenu)
    root.config(menu=bar)
  

    tkinter.mainloop()


if __name__=="__main__":
    main()
