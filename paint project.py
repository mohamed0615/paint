from pygame import *
from random import *
from math import *
from tkinter import *
from tkinter import filedialog

root=Tk()
root.withdraw() #hides the extra window


width,height=1250,750
screen=display.set_mode((width,height))
RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
LIGHT_GREEN=(169,255,169)
YELLOW=(255,255,0)
WHITE=(255,255,255)
BLACK=(0,0,0)

lineThickness = 2
count = 1
selectionCol = WHITE

#background layout
bgImg = image.load("images/mc bg.jpg")
smallbg = transform.scale(bgImg, (width, height))
screen.blit(smallbg, (0, 0))

                     
#defines rects for the canvas, palette and every tool and stamp
pencilRect = Rect(20, 220, 50, 50)
eraserRect = Rect(90, 220, 50, 50)
brushRect = Rect(20, 280, 50, 50)
sprayRect = Rect(90, 280, 50, 50)
circleRect = Rect(90, 340, 50, 50)
circlefillRect = Rect(160, 340, 50, 50)
squareRect = Rect(90, 400, 50, 50)
squarefillRect = Rect(160, 400, 50, 50)
lineRect = Rect(20, 340, 50, 50)
eyedropRect = Rect(20, 400, 50, 50)
stamp1Rect = Rect(16, 456, 46, 46)
stamp2Rect = Rect(86, 456, 46, 46)
stamp3Rect = Rect(16, 516, 46, 46)
stamp4Rect = Rect(86, 516, 46, 46)
stamp5Rect = Rect(16, 576, 46, 46)
stamp6Rect = Rect(86, 576, 46, 46)
stamp7Rect = Rect(16, 636, 46, 46)
stamp8Rect = Rect(86, 636, 46, 46)
bg1Rect = Rect(160, 220, 200, 100)
bg2Rect = Rect(160, 470, 200, 100)
bg3Rect = Rect(160, 590, 200, 100)
lineupRect = Rect(410, 10, 50, 50)
linedownRect = Rect(470, 10, 50, 50)
clearRect = Rect(530, 10, 50, 50)
fillRect = Rect(590, 10, 50, 50)
saveRect = Rect(1130, 10, 50, 50)
loadRect = Rect(1190, 10, 50, 50)
canvasRect = Rect(440,120,750,570)
paletteRect = Rect(10,10,260,180)

#loads the pictures for the palette, tools and stamps
paletteImg = image.load("images/palette.png")
smallPalette = transform.scale(paletteImg, (260, 180))
pencilImg = image.load("images/pencil.png")
smallPencil = transform.scale(pencilImg, (50, 50))
cursorPencil = transform.scale(pencilImg, (20, 20))
eraserImg = image.load("images/eraser.png")
smallEraser = transform.scale(eraserImg, (50, 50))
brushImg = image.load("images/brush.png")
smallBrush = transform.scale(brushImg, (50, 50))
sprayImg = image.load("images/spray.png")
smallSpray = transform.scale(sprayImg, (50, 50))
circleImg = image.load("images/circle.png")
smallCircle = transform.scale(circleImg, (50, 50))
circleFilled = image.load("images/circle filled.png")
smallCircleFill = transform.scale(circleFilled, (50, 50))
squareImg = image.load("images/square.png")
smallSquare = transform.scale(squareImg, (50, 50))
squareFilled = image.load("images/square filled.png")
smallSquareFill = transform.scale(squareFilled, (50, 50))
lineImg = image.load("images/line.png")
smallLine = transform.scale(lineImg, (50, 50))
eyedropImg = image.load("images/eyedropper.png")
smallEyedrop = transform.scale(eyedropImg, (50, 50))
lineupImg = image.load("images/up.png")
smallLineup = transform.scale(lineupImg, (50, 50))
linedownImg = image.load("images/down.png")
smallLinedown = transform.scale(linedownImg, (50, 50))
zoomImg = image.load("images/zoom.png")
smallZoom = transform.scale(zoomImg, (50, 50))
clearImg = image.load("images/clear.png")
smallClear = transform.scale(clearImg, (50, 50))
stamp1 = image.load("images/stamp 1.png")
smallStamp1 = transform.scale(stamp1, (46, 46))
stamp2 = image.load("images/stamp 2.png")
smallStamp2 = transform.scale(stamp2, (46, 46))
stamp3 = image.load("images/stamp 3.png")
smallStamp3 = transform.scale(stamp3, (46, 46))
stamp4 = image.load("images/stamp 4.png")
smallStamp4 = transform.scale(stamp4, (46, 46))
stamp5 = image.load("images/stamp 5.png")
smallStamp5 = transform.scale(stamp5, (46, 46))
stamp6 = image.load("images/stamp 6.png")
smallStamp6 = transform.scale(stamp6, (46, 46))
stamp7 = image.load("images/stamp 7.png")
smallStamp7 = transform.scale(stamp7, (46, 46))
stamp8 = image.load("images/stamp 8.png")
smallStamp8 = transform.scale(stamp8, (46, 46))
bg1Img = image.load("images/bg 1.png")
smallBg1 = transform.scale(bg1Img, (200, 100))
drawBg1 = transform.scale(bg1Img, (750, 570))
bg2Img = image.load("images/bg 2.jfif")
smallBg2 = transform.scale(bg2Img, (200, 100))
drawBg2 = transform.scale(bg2Img, (750, 570))
bg3Img = image.load("images/bg 3.png")
smallBg3 = transform.scale(bg3Img, (200, 100))
drawBg3 = transform.scale(bg3Img, (750, 570))
saveImg = image.load("images/save.png")
smallSave = transform.scale(saveImg, (50, 50))
loadImg = image.load("images/load.png")
smallLoad = transform.scale(loadImg, (50, 50))
fillImg = image.load("images/fill.png")
smallFill = transform.scale(fillImg, (50, 50))

#list that holds the tools
tools = [pencilRect, eraserRect, brushRect, sprayRect, squareRect, squarefillRect, lineRect, circleRect, circlefillRect, eyedropRect, stamp1Rect, stamp2Rect, stamp3Rect, stamp4Rect, stamp5Rect, stamp6Rect, stamp7Rect, stamp8Rect, bg1Rect, bg2Rect, bg3Rect]
#list that holds the selection marker for the tools
m = [       0,          0,          0,          0,          0,          0,              0,      0,              0,          0,          0,          0,          0,          0,          0,          0,          0,              0,      0,          0,      0]

#list that holds special tools like save and load
specialTools = [lineupRect, linedownRect, clearRect, saveRect, loadRect, fillRect]
#list that holds the selection marker for the special tools
specialM = [        0,          0,              0,      0,          0,      0]


running=True
mode = "up" #variable for the mode of the mouse
tool="" #variable contains the tools currently selected
col=BLACK #default starting color for all tools
bgcol=WHITE #default starting color for the canvas
radius=10 #default radius for all circle use in tools like the brush and eraser
def distance(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2) #this function calculates the distance between two points 
#draws the canvas onto the window
draw.rect(screen,WHITE,canvasRect) #draws the canvas
screenCap=screen.subsurface(canvasRect).copy()#takes a screenshot of the canvas only

while running:
    click = False #variable detects if the mouse is clicked
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN:
            click = True #if the mouse is clicked then click will become true
            sx,sy=evt.pos #these variables represent the positions that the mouse was clicked at
            oldmx, oldmy = mx, my #these variables store the last position the mouse was clicked in
        if evt.type==MOUSEBUTTONUP:
            if evt.button == 1:
                #depending on the selected tool it draws a line, cirlce, square or clears the screen
                if tool=="line":
                    screen.set_clip(canvasRect) #any code that follows will only affect the canvas
                    screen.blit(screenCap,canvasRect) #place the screenshot in the canvas
                    draw.line(screen,col,(sx,sy),(mx,my), lineThickness) #draws a line from the postion the mouse was clicked to the current mouse position
                    screenCap=screen.subsurface(canvasRect).copy() #takes a screenshot of the current canvas with all drawn elements on it
                if tool=="circle":
                    screen.set_clip(canvasRect)
                    screen.blit(screenCap, canvasRect)
                    ellRect=Rect(oldmx, oldmy, mx-oldmx, my-oldmy) #this varaible contains the dimensions of the circle
                    ellRect.normalize() #normalizes the variable of the dimensions of the circle
                    draw.ellipse(screen, col, ellRect, lineThickness) #draws a circle using the dimensions in the variable ellRect
                    screenCap=screen.subsurface(canvasRect).copy()
                if tool=="square":
                    screen.set_clip(canvasRect)
                    screen.blit(screenCap, canvasRect)
                    draw.rect(screen, col, (oldmx, oldmy, mx-oldmx, my-oldmy), lineThickness) #draws a rectangle 
                    draw.rect(screen, col, (sx-lineThickness/2.5, sy-lineThickness/2.5, lineThickness, lineThickness)) #these lines draw squares at each corner of the rectangle to cover up any empty corners
                    draw.rect(screen, col, (mx-lineThickness/2.2, my-lineThickness/2.2, lineThickness, lineThickness)) #|
                    draw.rect(screen, col, (sx-lineThickness/2.5, my-lineThickness/2, lineThickness, lineThickness))   #|
                    draw.rect(screen, col, (mx-lineThickness/2, sy-lineThickness/2.5, lineThickness, lineThickness))   #V
                    screenCap=screen.subsurface(canvasRect).copy()
                if clearRect.collidepoint(mx, my): #if the clear tools is activated
                    screen.set_clip(canvasRect) 
                    screen.fill(WHITE)
                    screenCap=screen.subsurface(canvasRect).copy()
                       
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    
    #changes the mode from up and down
    if mode == "up" and mb[0] == 1: #if the mode is up and the mouse is clicked
        screenCap = screen.subsurface(canvasRect).copy() 
        mode = "down" #mode switches to down
        print("mouse clicked") #prints a message in the python shell

    if mode == "down" and mb[0] == 0: #if the mode is down and the mouse is released
        mode = "up" #mode switches to up
        print("mouse released") #prints a message in the python shell

    #draws the palette
    draw.rect(screen, BLACK, (5,5,270,190)) 
    draw.rect(screen, col, (5, 5, 270, 190), 5) #draws a border around the palette showing which color you have selected
    draw.rect(screen, WHITE, paletteRect) #draws clickable rectangle behind the palette
    screen.blit(smallPalette, paletteRect) #loads in the image of the palette

    #draws the rects and highlights them
    for i in range(len(m)): #this loops repeats 1 time for every element in the m list
        if tools[i].collidepoint(mx, my) and m[i]==0: #if the element in the tools list at the index of i is collideing with the mouse and is = 0
            m[i] = 1 #the element turns to 1
##            if m[i] == 2: #if it is = 2
##                m=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
##                m[i]=2
        if tools[i].collidepoint(mx, my)==False and m[i]==1: #if the element is no longer colliding with the mouse and is = 1
            m[i]=0 #the element switches to 0
            
    for i in range(len(m)): #this loops repeats 1 time for every element in the m list
        if tools[i].collidepoint(mx, my) and mb[0]: #if the element of the tools list at the index of i is colliding with the mouse and is clicked
            m=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #all elements in the m list turn back to 0
            m[i] = 2 #the element at the index of i turns to 2
            
    for i in range(len(m)):
        screen.set_clip() #following code can affect all areas of the window
        if m[i] == 1: 
            draw.rect(screen, LIGHT_GREEN, tools[i]) #the rectangle behind the tool becomes light green
        elif m[i] == 2:
            draw.rect(screen, GREEN, tools[i]) #the rectagnle behind the tool becomes green
        else:
            draw.rect(screen, WHITE, tools[i]) #the rectangle behind the tool becomes white

    for i in range(len(specialM)): #this loop does the same thig as the loop above but only detects hovering and not clicking
        if specialTools[i].collidepoint(mx, my): 
            specialM[i] = 1
        if specialTools[i].collidepoint(mx, my)==False and specialM[i]==1:
            specialM[i]=0
    for i in range(len(specialM)):
        if specialM[i] == 1:
            draw.rect(screen, LIGHT_GREEN, specialTools[i])
        else:
            draw.rect(screen, WHITE, specialTools[i])

    #loads in the pictures       
    screen.blit(smallPencil, pencilRect)
    screen.blit(smallEraser, eraserRect)
    screen.blit(smallCircle, circleRect)
    screen.blit(smallCircleFill, circlefillRect)
    screen.blit(smallSquare, squareRect)
    screen.blit(smallSquareFill, squarefillRect)
    screen.blit(smallLine, lineRect)
    screen.blit(smallEyedrop, eyedropRect)
    screen.blit(smallLineup, lineupRect)
    screen.blit(smallLinedown, linedownRect)
    screen.blit(smallClear, clearRect)
    screen.blit(smallSave, saveRect)
    screen.blit(smallLoad, loadRect)
    screen.blit(smallFill, fillRect)
    screen.blit(smallBrush, brushRect)
    screen.blit(smallSpray, sprayRect)
    screen.blit(smallStamp1, stamp1Rect)
    screen.blit(smallStamp2, stamp2Rect)
    screen.blit(smallStamp3, stamp3Rect)
    screen.blit(smallStamp4, stamp4Rect)
    screen.blit(smallStamp5, stamp5Rect)
    screen.blit(smallStamp6, stamp6Rect)
    screen.blit(smallStamp7, stamp7Rect)
    screen.blit(smallStamp8, stamp8Rect)
    screen.blit(smallBg1, bg1Rect)
    screen.blit(smallBg2, bg2Rect)
    screen.blit(smallBg3, bg3Rect)


    if mb[0]:
        #if the mouse is clicked and the cursor is hovering over a certain tool the tool is selected
        #pencil
        if pencilRect.collidepoint(mx,my): #these statements change the variable "tool" depending on what tool you select
            tool="pencil"
        #eraser
        if eraserRect.collidepoint(mx,my):
            tool="eraser"
        #brush
        if brushRect.collidepoint(mx, my):
            tool="brush"
        #spray
        if sprayRect.collidepoint(mx, my):
            tool="spray"
        #circle
        if circleRect.collidepoint(mx, my):
            tool="circle"
        #filled circle
        if circlefillRect.collidepoint(mx, my):
            tool="filled circle"
        #square
        if squareRect.collidepoint(mx, my):
            tool="square"
        #filled square
        if squarefillRect.collidepoint(mx, my):
            tool="filled square"
        #line
        if lineRect.collidepoint(mx, my):
            tool="line"
        #eye dropper
        if eyedropRect.collidepoint(mx, my):
            tool="eye dropper"
        #stamp 1
        if stamp1Rect.collidepoint(mx, my):
            tool="stamp 1"
        #stamp 2
        if stamp2Rect.collidepoint(mx, my):
            tool="stamp 2"
        #stamp 3
        if stamp3Rect.collidepoint(mx, my):
            tool="stamp 3"
        #stamp 4
        if stamp4Rect.collidepoint(mx, my):
            tool="stamp 4"
        #stamp 5
        if stamp5Rect.collidepoint(mx, my):
            tool="stamp 5"
        #stamp 6
        if stamp6Rect.collidepoint(mx, my):
            tool="stamp 6"
        #stamp 7
        if stamp7Rect.collidepoint(mx, my):
            tool="stamp 7"
        #stamp 8
        if stamp8Rect.collidepoint(mx, my):
            tool="stamp 8"
        #bg 1
        if bg1Rect.collidepoint(mx, my):
            screen.set_clip(canvasRect)
            screen.blit(drawBg1, (canvasRect))
        #bg 2
        if bg2Rect.collidepoint(mx, my):
            screen.set_clip(canvasRect)
            screen.blit(drawBg2, (canvasRect))
        #bg 3
        if bg3Rect.collidepoint(mx, my):
            screen.set_clip(canvasRect)
            screen.blit(drawBg3, (canvasRect))
        #increases the thickness of the lines
        if lineupRect.collidepoint(mx, my): #this tool increases the thickness the thickness of lines up to a set limit
            if count < 8:
                lineThickness += 1
                count+=1
        #decreases the thickness of the lines
        if linedownRect.collidepoint(mx, my): #this tool decreases the thickness the thickness of lines down to a set limit
            if count > 1:
                lineThickness -= 1
                count -= 1
        #clears the canvas 
        if clearRect.collidepoint(mx, my): #this tool clears the canvas
            screen.set_clip(canvasRect)
            screen.fill(WHITE)
            bgcol = WHITE
        #fill
        if fillRect.collidepoint(mx, my):
            screen.set_clip(canvasRect)
            screen.fill(col)
            bgcol = col

        
    
    #using each tool
    if mb[0]==1 and canvasRect.collidepoint(mx, my): #if the mouse is clicked
        screen.set_clip(canvasRect)
        #pencil
        if tool=="pencil":
            screen.blit(screenCap, canvasRect)
            draw.line(screen,col,(newmx,newmy),(mx,my), lineThickness)
            screenCap=screen.subsurface(canvasRect).copy()
        #eraser
        if tool=="eraser":
            dx=mx-newmx 
            dy=my-newmy 
            dist = distance(newmx, newmy, mx, my) 
            for d in range(10,int(dist),10):
                dotX=dx*d/dist+newmx
                dotY=dy*d/dist+newmy
                draw.circle(screen,bgcol,(int(dotX),int(dotY)), lineThickness+7) #everything here is the same as the code below
            draw.circle(screen, bgcol, (mx, my), lineThickness+7)
            screenCap=screen.subsurface(canvasRect).copy()
        #brush
        if tool=="brush": 
            dx=mx-newmx 
            dy=my-newmy 
            dist = distance(newmx, newmy, mx, my) #this varaible holds the calculated distance between the old and new positons of the mouse (the newmx and newmy varaible hold the same value as the oldmx and oldmy)
            for d in range(10,int(dist),10): #this loop repeats depending on the distance between each point
                dotX=dx*d/dist+newmx #this variable holds the equation caculating the position of each dot on the x
                dotY=dy*d/dist+newmy #this variable does the smae but for the y
                draw.circle(screen,col,(int(dotX),int(dotY)), lineThickness+7) #draws a cricle on the positioins calculated by the variables above
            draw.circle(screen, col, (mx, my), lineThickness+7) #draws a circle on the position of the mouse
            screenCap=screen.subsurface(canvasRect).copy()
        #spray
        if tool=="spray":
            for i in range(15): #repeates 15 times
                rx = randint(-25, 25) #this variable is a random number between -25 and 25
                ry = randint(-25, 25) #sam as the on above
                if (rx)**2+(ry)**2<=25**2: #if the variables above to the exponents of and then added together are less than 25
                    draw.circle(screen, col, (mx- rx, my-ry), 1) #draw circles that are 1 pixel large in a random position in a radius 
            screenCap=screen.subsurface(canvasRect).copy()
        #circle
        if tool=="circle":
            screen.blit(screenCap, canvasRect)
            ellRect=Rect(oldmx, oldmy, mx-oldmx, my-oldmy)
            ellRect.normalize()
            draw.ellipse(screen, col, ellRect, lineThickness)
        #filled circle
        if tool == "filled circle":
            screen.blit(screenCap, canvasRect)
            ellRect=Rect(oldmx, oldmy, mx-oldmx, my-oldmy) #does everything like the circle code except the circle is filled
            ellRect.normalize()
            draw.ellipse(screen, col, ellRect)
        #square
        if tool=="square":
            screen.blit(screenCap, canvasRect)
            draw.rect(screen, col, (oldmx, oldmy, mx-oldmx, my-oldmy), lineThickness)
        #filled square
        if tool=="filled square":
            screen.blit(screenCap, canvasRect)
            ellRect=Rect(oldmx, oldmy, mx-oldmx, my-oldmy) #does everything as the square tool except the square is filled
            ellRect.normalize()
            draw.rect(screen, col, ellRect)
        #line
        if tool=="line":
            screen.blit(screenCap, canvasRect)
            draw.line(screen, col,(sx,sy),(mx,my), lineThickness) #draws a line from the postion the mouse is clicked to the the position it is released
        #eyedropper
        if tool=="eye dropper":
            col=screen.get_at((mx, my)) #the color variable is changesd to the color the mouse is clicked on
        #stamp 1
        if tool=="stamp 1":
            screen.blit(screenCap, canvasRect)
            screen.blit(smallStamp1, (mx-24, my-24)) #draws a picture at the place the mouse is clicked (repeats for all stamp tools)
        #stamp 2
        if tool=="stamp 2":
            screen.blit(screenCap, canvasRect)
            screen.blit(smallStamp2, (mx-24, my-24))
        #stamp 3
        if tool=="stamp 3":
            screen.blit(screenCap, canvasRect)
            screen.blit(smallStamp3, (mx-24, my-24))
        #stamp 4
        if tool=="stamp 4":
            screen.blit(screenCap, canvasRect)
            screen.blit(smallStamp4, (mx-24, my-24))
        #stamp 5
        if tool=="stamp 5":
            screen.blit(screenCap, canvasRect)
            screen.blit(smallStamp5, (mx-24, my-24))
        #stamp 6
        if tool=="stamp 6":
            screen.blit(screenCap, canvasRect)
            screen.blit(smallStamp6, (mx-24, my-24))
        #stamp 7
        if tool=="stamp 7":
            screen.blit(screenCap, canvasRect)
            screen.blit(smallStamp7, (mx-24, my-24))
        #stamp 8
        if tool=="stamp 8":
            screen.blit(screenCap, canvasRect)
            screen.blit(smallStamp8, (mx-24, my-24))


    zoomx, zoomy = mx-30, my-50 #variable holding the postion of the chosen color indicator
    if paletteRect.collidepoint(mx,my) and mb[0]: #if the mouse is in the palette and is clicked
        screen.set_clip(paletteRect) #following code only affects the palette
        col=screen.get_at((mx,my)) #the color variable switches to the color that mouse is on when it's clicked
        screen.blit(smallZoom, (zoomx, zoomy))             #these lines
        draw.circle(screen, col, (zoomx+33, zoomy+15), 10) #draw a picture above the mouse showing which color you are on

    #save and load
    if saveRect.collidepoint(mx,my) and click: #if the save button is clicked
        fname=filedialog.asksaveasfilename(defaultextension=".png") #this variable asks for a name for the file
        if fname != "": #if the file name is not blank
            image.save(screen.subsurface(canvasRect), fname) #save the drawing on the canvas as the file name
        print(fname) #print the file name in the python shell
    if loadRect.collidepoint(mx,my) and click: #if the load button is clicked
        fname=filedialog.askopenfilename() #this variable detects which file you select
        ind = fname.rfind(".") #this is the indicator for the file name
        ext = fname[ind+1:] #checks for the extention after the .
        if fname != "" and (ext == "png" or ext == "jpg" or ext == "jpeg"): 
            loadpic = image.load(fname) #this variable holds the image that will be load
            smallLoadpic = transform.scale(loadpic, (750,570)) #resizes the image to fit he canvas
            screen.blit(smallLoadpic, (440,120)) #draws the picture onto the canvas
        print(ext)

    #change the appearance of the cursor
##    if tool=="pencil":
##        screen.set_clip(canvasRect)
##        screen.blit(screenCap, canvasRect)
##        screenCap=screen.subsurface(canvasRect).copy()
##        screen.blit(cursorPencil, (mx-3, my-20))
    

##    print(m) #prints the m list       
    print("tool =", tool) #prints the selected tool
    newmx, newmy = mx, my #hold the same value as the oldmx and oldmy variables
    display.flip() #updates the window each time this loop repeats
            
quit()
