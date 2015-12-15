from graphics import *
import time
import operator

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
    def __init__(self, tit, art, lyr):
        self.tit = tit
        self.artist = art
        self.lyrics = lyr
        self.length = 0
        #calculates length of self.lyrics string
        for i in self.lyrics:
            self.length += 1
        self.freqs = []
        self.words = []
        #creats a list of tupels of words and frequencies from the self.lyrics string
        freqlyr = self.lyrics.lower()
        temp = ""
        for i in freqlyr:
            if i not in ['"','.',',','?','!',"'",'(',')']:
                temp = temp + i
        freqlyr = temp
        freqlyr = freqlyr.split()
        for i in freqlyr:
            if i in self.words:
                a = self.words.index(i)
                self.freqs[a] = (i,int(self.freqs[a][1]) + 1)
            else:
                self.words = self.words + [i]
                self.freqs = self.freqs + [(i,1)]
        self.topWords = sorted(self.freqs, key=operator.itemgetter(1), reverse=True)
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
    def getLyrics(self):
        return self.lyrics
    def setLyrics(self, newlyrics):
        self.lyrics = newlyrics
    def getSorted (self):
        return self.topWords
    def __str__(self):
        return self.tit, self.artist
    
#def findSongs():

#def findLyrics():
    
def makeBarGraph(song, wn):
    #clears the previous graph
    rect = Rectangle(Point(.25,.25), Point(6.1, 7.5))
    saver = Image(Point(2.75,3.25), '/Users/Elliot/Desktop/Songs/BaseImage.png')
    rect.setOutline('lightblue')
    rect.setFill('lightblue')
    rect.draw(wn)
    #graphs selected lyrics
    x = 1
    xaxis = Line(Point(.5, 1), Point(6, 1))
    yaxis = Line(Point(1, .5), Point(1, 7))
    xaxis.setWidth(2)
    yaxis.setWidth(2)
    for i in range(15):
        topWords = song.getSorted()
        maxh = topWords[0][1]
        bar = Rectangle(Point(x, (topWords[i][1]/maxh)*6+1), Point((x+.333),1))
        if i % 2 == 0:
            bar.setFill('lightgreen')
        else:
            bar.setFill('salmon')
        bar.draw(wn)
        
        #prints the Key# under the bar
        num = Text(Point(x+.1665,.75),str(i +1))
        num.draw(wn)
        #prints the number of times each word was said above the bar
        count = Text(Point(x+.1665, topWords[i][1]/maxh*6+1.25), topWords[i][1])
        count.draw(wn)
        x += .333
    xaxis.draw(wn)
    yaxis.draw(wn)
    wn.update()
    return saver
def makeWordCloud(song, wn):
    a
def makePieChart(song, wn):
    a
def makeIntroWin():
    introwin = GraphWin('Lyric Stats', 450, 300)
    introwin.setCoords(0.0, 0.0, 4.5, 3.0)
    logo = Image(Point(2.25, 1.5), '/Users/Elliot/Desktop/Songs/logo.png')
    logo.draw(introwin)
    time.sleep(2)
    introwin.close()
    
def openSongWin(num, lis):
    #decides how wide to make the window
    if 30 < num <= 60:
        w = 600
    elif 60 < num <= 90:
        w = 900
    elif 90 < num:
        w = 1200
    else:
        w = 300
    #decides how tall to make the window
    if num >= 30:
        h = 375
    else:
        h = num * 25
    #makes the window
    songWin = GraphWin('Songs', w, h)
    songWin.setCoords(0.0, 0.0, w, h)
    while songWin.isOpen:
        #creates the buttons with songs on them
        if 30 < num <= 60:
            buttons2 = [Button(songWin, Point(300, i*25+10), 300, 25, lis[i].getTitle()) for i in range(30, mun)]
        elif 60 < num <= 90:
            buttons3 = [Button(songWin, Point(450, i*25+10), 300, 25, lis[i].getTitle()) for i in range(60, num)]
        elif 90 < num:
            buttons4 = [Button(songWin, Point(600, i*25+10), 300, 25, lis[i].getTitle()) for i in range(90, 100)]
        else:
            buttons1 = [Button(songWin, Point(150, i*25+10), 300, 25, lis[i].getTitle()) for i in range(0, num)]
        #wait for a song to be selected and returns the song's number in the songlist
        pt = songWin.getMouse()
        i = 1
        #returns the button number that was clicked
        while i == 1:
            for butt in buttons1:
                if butt.clicked(pt):
                    songWin.close()
                    pos = buttons1.index(butt)
                    return lis[pos]
            for butt in buttons2:
                if butt.clicked(pt):
                    songWin.close()
                    pos = buttons2.index(butt)
                    return lis[pos]
            for butt in buttons3:
                if butt.clicked(pt):
                    songWin.close()
                    pos = buttons3.index(butt)
                    return lis[pos]
            for butt in buttons4:
                if butt.clicked(pt):
                    songWin.close()
                    pos = buttons4.index(butt)
                    return lis[pos]
        
def openGUI(lis):
    #initializes and sets up the first GUI.
    #Not nessicary but it looks cool
    #makeIntroWin()
    #initializes and sets up the main GUI
    win = GraphWin('Lyric Stats', 1100, 850, autoflush=False)
    win.setCoords(0.0, 0.0, 11.0, 8.5)
    win.setBackground('lightblue')
    #adds the "choose song" button
    choosefile = Button(win, Point(2,8), 3, .25, 'Select Song')
    #adds the save name entry box
    savename = Entry(Point(2, 7.75), 32)
    savename.setText('Enter Save Name for Graph')
    savename.draw(win)
    #adds the button to import a song (might not use this in finished project)
    addSong = Button(win, Point(3.75, 8), .5, .25, '+')
    #adds button to save the song stats and charts as pictures
    save = Button(win, Point(3.75, 7.75), .5, .25, 'S')
    #adds button to close the window
    exitbutton = Button(win, Point(4.25,7.875), .5, .5, 'exit')
    win.update()
    pt = win.getMouse()
    #closes window if the "exit" button is clicked
    while not exitbutton.clicked(pt):
        #opens the song chooser window if the button is clicked
        if choosefile.clicked(pt):
                a = openSongWin(len(lis), lis)
                choosefile.setLabel(str(a.getTitle()))
                pic = makeBarGraph(a, win)
                #makeWordCloud(song, win)
                #makePieChart(song, win)
        #if save.clicked(pt):
            #win.setCoords(0.0, 0.0, 1100, 850)
            #for y in range(50, 701):
                #for x in range(50, 551):
                    #p = Point(x, y)
                    #p.
                    #pic.
            #pic.save('/Users/Elliot/Desktop/' + savename.getText() + '.png')
            #print('Success!')
            #win.setCoords(0.0, 0.0, 11.0, 8.5)
        #looks for another click
        pt = win.getMouse()
    win.close()
    
def makeSongs():
    #initilizes the lists
    titList = []
    artList = []
    lyricList = []
    namelist = []
    songInfo = open('/Users/Elliot/Desktop/Songs/TopSongs.txt', 'r')
    for aline in songInfo:
        #splits the list of titles and artists into seperate lists
        a, b = aline.split('\t')
        titList = titList + [a]
        artList = artList + [b]
    for i in range(len(titList)):
        #makes a list of filenames
        namelist = namelist + ['song' + str(i)]
        namebase = '/Users/Elliot/Desktop/Songs/Lyrics'
        nameend = '.txt'
        name = namebase + str(i) + nameend
        #opens the lyric files and makes a string out of the lyrics
        file = open(name)
        text = file.read()
        #adds the lyrics to the list of lyrics
        lyricList = lyricList + [text]
    songs = [Song(titList[i], artList[i], lyricList[i]) for i in range(20)]
    return songs
    
def main():
    songs = makeSongs()
    openGUI(songs)

main()
