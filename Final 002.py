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
    def getLyrics(self):
        return self.lyrics
    def setLyrics(self, newlyrics):
        self.lyrics = newlyrics
    def __str__(self):
        return self.tit, self.artist
    
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
    
def openSongWin(num, lis):
    if 30 < num <= 60:
        w = 600
    elif 60 < num <= 90:
        w = 900
    elif 90 < num:
        w = 1200
    else:
        w = 300
    if num >= 30:
        h = 375
    else:
        h = num * 25
        
    songWin = GraphWin('Songs', w, h)
    songWin.setCoords(0.0, 0.0, w, h)
    for i in range(num):
        title = lis[i].title()
        if i < 31:
            title = Button(songWin, Point(150, i*25+10), 300, 25, title)
        elif 30 < i < 61:
            title = Button(songWin, Point(300, i*25+10), 300, 25, title)
        elif 60 < i < 91:
            title = Button(songWin, Point(450, i*25+10), 300, 25, title)
        elif 90 < i:
            title = Button(songWin, Point(600, i*25+10), 300, 25, title)
    pt = songWin.getMouse()
    i = 1
    while i == 1:
        for i in range(num):
            title = lis[i].title()
            if title.clicked(pt):
                i = 0
                return title
    songWin.close()
    
def openGUI(lis):
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
            song = openSongWin(20, lis)
        pt = win.getMouse()
    #makeBarGraph(song)
    #makeWordCloud(song)
    #makePieChart(song)
    win.close()
    
def makeSongs():
    #initilizes the lists
    titList = []
    artList = []
    lyricList = []
    songInfo = open('/Users/Elliot/Desktop/Songs/TopSongs.txt', 'r')
    for aline in songInfo:
        #splits the list of titles and artists into seperate lists
        a, b = aline.split('\t')
        titList = titList + [a]
        artList = artList + [b]
    namelist = []
    for i in range(20):
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
    #Makes the top 20 songs with title and artist
    song0 = Song(titList[0], artList[0])
    song1 = Song(titList[1], artList[1])
    song2 = Song(titList[2], artList[2])
    song3 = Song(titList[3], artList[3])
    song4 = Song(titList[4], artList[4])
    song5 = Song(titList[5], artList[5])
    song6 = Song(titList[6], artList[6])
    song7 = Song(titList[7], artList[7])
    song8 = Song(titList[8], artList[8])
    song9 = Song(titList[9], artList[9])
    song10 = Song(titList[10], artList[10])
    song11 = Song(titList[11], artList[11])
    song12 = Song(titList[12], artList[12])
    song13 = Song(titList[13], artList[13])
    song14 = Song(titList[14], artList[14])
    song15 = Song(titList[15], artList[15])
    song16 = Song(titList[16], artList[16])
    song17 = Song(titList[17], artList[17])
    song18 = Song(titList[18], artList[18])
    song19 = Song(titList[19], artList[19])
    #adds lyrics to the top 20 songs
    song0.setLyrics(lyricList[0])
    song1.setLyrics(lyricList[1])
    song2.setLyrics(lyricList[2])
    song3.setLyrics(lyricList[3])
    song4.setLyrics(lyricList[4])
    song5.setLyrics(lyricList[5])
    song6.setLyrics(lyricList[6])
    song7.setLyrics(lyricList[7])
    song8.setLyrics(lyricList[8])
    song9.setLyrics(lyricList[9])
    song10.setLyrics(lyricList[10])
    song11.setLyrics(lyricList[11])
    song12.setLyrics(lyricList[12])
    song13.setLyrics(lyricList[13])
    song14.setLyrics(lyricList[14])
    song15.setLyrics(lyricList[15])
    song16.setLyrics(lyricList[16])
    song17.setLyrics(lyricList[17])
    song18.setLyrics(lyricList[18])
    song19.setLyrics(lyricList[19])
    print(song0.getTitle())
    return titList
    
def main():
    titList = makeSongs()
    openGUI(titList)    

main()
