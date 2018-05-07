from tkinter import filedialog
from tkinter import *



top = Tk()

width = 2000
height = 300
canvas = Canvas(top, width =width, height = height)

start =  50
lineInterval = 40

# stringValues = [0, 5, 10, 15, 19, 24] #starting at 0, each number is one half step
stringValues = [24,19,15,10,5,0]
def drawStaff():

    i = 0
    while i <5:
        canvas.create_line(0, start + i * lineInterval, width, start + i * lineInterval)
        i+=1

def noteFromChar(string, fret):
    if not fret.isdigit():
        return [-1,-1]
    num = int(fret)
    numPlusString = num + stringValues[string]

    isSharp = FALSE
    val = num%12
    sharpValues = [2,4,6,9,11]

    if val in sharpValues:
        isSharp = TRUE

    allSharps = []
    i = 0
    while i <3:
        for num in sharpValues:
            allSharps.append(num + i*12)
        i+=1


    sharpCount = 0

    for sharp in allSharps:
        if sharp < numPlusString:
            sharpCount+=1


    return [numPlusString-sharpCount, isSharp]

def convert():
    filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
    f  = open (filename, "r")
    lines = f.readlines()
    allChords = []
    length = len(lines[0])
    currString = 0
    fromLeft  = 0;
    while fromLeft<length:
        chord = [] #line or space number, isSharp
        currString = 0
        while currString < 6:
            note = noteFromChar(currString, lines[currString][fromLeft])
            if note[0] == -1 and note[1] == -1:
                currString+=1
                continue
            chord.append(note)
            currString += 1
        if chord:
            allChords.append(chord)
        fromLeft = fromLeft+1
    drawNote(allChords)

def drawNote(chords):
    bottomLine = 370
    noteHeight = lineInterval
    noteWidth = lineInterval
    modifier = 100
    chordNum = 0
    horInterval = 60
    lhsInterval = 70

    sharpVertInterval = noteHeight/32
    sharpHorizontalInterval = noteHeight/32
    sharpLineLength = noteHeight/4
    for chord in chords:
        for note in chord:
            lineNum =note[0]
            isSharp = note[1]
            lineUpSize = lineNum*lineInterval/2
            totalHor = chordNum*horInterval

            canvas.create_oval(lhsInterval + totalHor, bottomLine- lineUpSize , lhsInterval+noteWidth+totalHor, bottomLine - noteHeight - lineUpSize, fill="black")
            if isSharp:
                startx = lhsInterval + noteWidth + totalHor + sharpHorizontalInterval
                starty = bottomLine- lineUpSize-sharpHorizontalInterval-noteHeight

                canvas.create_line(startx+2, starty, startx, starty+sharpLineLength) #first vert line
                canvas.create_line(startx+4, starty, startx+2, starty+sharpLineLength) #second vert line

                starty = starty+sharpLineLength/3
                startx -=2
                canvas.create_line(startx+1, starty, startx+sharpLineLength+1, starty) #first vert line
                canvas.create_line(startx, starty+sharpLineLength/3, startx+sharpLineLength, starty+sharpLineLength/3) #first vert line







        chordNum+=1

button = Button(top, text = "choose file",command = convert)
canvas.pack()
button.pack()

# bottomLine = 270
# noteHeight = 40
#
# canvas.create_oval(70, bottomLine-noteHeight, 110, bottomLine, fill="black")

drawStaff()

# i = 0
# start2 = start + interval*6
# while i < 5:
#     canvas.create_line(0, start2 + i * interval, width, start2 + i * interval)
#     i += 1
# canvas.create_oval(50,50,50,80, fill = "yellow")
# canvas.create_rectangle(50, 20, 150, 80, fill="#476042")


top.mainloop()