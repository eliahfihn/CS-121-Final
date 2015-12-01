from graphics import *
import time

class Button:
    def __init__(self, win, center, width, height, label):
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.active = True
    def clicked(self, p):
        return(self.active and
               self.xmin <= p.getX() <= self.xmax and
               self.ymin <= p.getY() <= self.ymax)
    def getLabel(self):
        return self.label.getText()
    def setLabel(self,val):
        self.label.setText(str(val))
    def deactivate(self):
        self.label.setFill('darkgray')
        self.rect.setWidth(1)
        self.active = False

class Song:
    def __init__(self, tit, artist):
        self.tit = tit
        self.artist = artist
        self.lyrics = ""
        self.length = 0
        #calculates length of self.lyrics string
        for i in self.lyrics:
            self.length += 1
        self.freqs = {}
        #creats a dictionary of words and frequencies from the self.lyrics string
        for i in self.lyrics:
            if i in self.freqs:
                self.freqs[i] = self.freqs[i] + 1
            else:
                self.freqs[i] = 1
    def getTitle(self):
        return self.tit
    def setTitle(self, newtit):
        self.tit = newtit
    def artist(self, newartist = '000'):
        if newartist != '000':
            self.artist = artist
        return self.artist
    def getLength(self):
        return self.lengh
    def getFreqs(self):
        return self.freqs
    def lyrics(self, newlyrics = "000"):
        if newlyrics != "000":
            self.lyrics = newlyrics
        return self.lyrics
    def __str__(self):
        return self.tit
    
#def findSongs():

#def findLyrics():
    
def makeBarGraph(song):
    a
def makeWordCloud(song):
    a
def makePieChart(song):
    a
def makeIntroWin():
    introwin = GraphWin('Lyric Stats', 450, 300)
    introwin.setCoords(0.0, 0.0, 4.5, 3.0)
    logo = Image(Point(2.25, 1.5), '/Users/Elliot/Desktop/Songs/logo.png')
    logo.draw(introwin)
    #time.sleep(2)
    introwin.close()
def openSongWin(num, songdict):
    if 15 < num <= 30:
        w = 200
    elif num <= 45:
        w = 300
    elif num <= 60:
        w = 400
    elif num <= 75:
        w = 500
    elif num <= 90:
        w = 600
    elif num > 90:
        w = 700
    else:
        w = 100
    if num >= 15:
        h = 375
        h2 = 375.0
    else:
        h = num * 25
        
    songWin = GraphWin('Songs', w, h)
    songWin.setCoords(0.0, 0.0, w, h)
    for i in range(num):
        title = songdict[i].title()
        title = Button(songWin, Point(w/2, i*25+10), 100, 25, title)
    
def openGUI(num, songdict):
    makeIntroWin()
    win = GraphWin('Lyric Stats', 1100, 850)
    win.setCoords(0.0, 0.0, 11.0, 8.5)
    win.setBackground('lightblue')
    choosefile = Button(win, Point(2,8), 3, .25, 'Select Song')
    savename = Entry(Point(2, 7.75), 32)
    savename.setText('Enter Save Name for Graph')
    savename.draw(win)
    addSong = Button(win, Point(3.625, 8), .25, .25, '+')
    save = Button(win, Point(3.625, 7.75), .25, .25, 'S')
    exitbutton = Button(win, Point(2,2), .5, .5, 'exit')
    pt = win.getMouse()
    while not exitbutton.clicked(pt):
        if choosefile.clicked(pt):
            song = openSongWin(num, songdict)
        pt = win.getMouse()
    #makeBarGraph(song)
    #makeWordCloud(song)
    #makePieChart(song)
        #defines regions of the GUI
        #if a
    win.close()
    
def makeSongs(num):
    songDict = {}
    namelist = []
    for i in range(num):
        #makes a list of filenames
        namelist = namelist + ['song' + str(i)]
        namebase = '/Users/Elliot/Desktop/Songs/Lyrics'
        nameend = '.txt'
        name = namebase + str(i) + nameend
        #opens the lyric files
        namelist[i] = open(name)
        #creates song objects and a dictionary
        aline = namelist[i].readline()
        print(aline)
        a, b = aline.split('\t')
        lName = 'song' + str(i)
        print(lName)
        songDict[i] = lName
        print(songDict[i])
        lName = Song(a, b)
        #adds lyrics to the song objects
        text = namelist[i].read()
        lName.lyrics
        #fixes title of song
        lName.setTitle = a
    print(songDict)
    print(songDict[1].title())
    return songDict
    
def main():
    songs = makeSongs(2)
    openGUI(2, songs)    

main()
