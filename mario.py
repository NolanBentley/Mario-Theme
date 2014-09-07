#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Mario, his song (c) Nintendo (plz dont sue)

try:
    from win32api import Beep # For Windows
except:
    def Beep(frequency, duration): # For linux
        sample = 8000
        half_period = int(sample/frequency/2)
        beep = chr(1)*half_period+chr(0)*half_period
        beep *= int(duration*frequency)
        audio = file('/dev/audio', 'wb')
        audio.write(beep)
        audio.close()


print """                   yyyyyyyyy
                 yy         yyy
              yyy   yyyyyyyy   yyy
            yyy   yy       yy    yy
          yyy     y MMM MMM y      yy
        yyy      y  MMMMMMM  y       y
       yyy     yyy  MM M MM  y       yy
     yyy      yyyy  MM M MM y  yyy     y
    yy      yyyyyyy MM   MM y  yyyyyy   y
   yy     yyyyy   y         y    yyyyyy  yy
  y      yyyyyy    yyyyyyyyy      yyyyy   y
 y      yyy      @@@ yyyyyy @@@     yyyy   y
 y   yyyyy      @   @      @   @    yyyyyy  y
  yyyyy         @ OO @    @ OO @     yyyyyyy
  @@            @ O  @    @  O @      yy @@
 @  @            @  ********  @         @  @
@    @            @*        *@         @    @
@  @ @            *          *         @ @  @
@  @@@    ####    *          *   ###   @@@  @
 @   @     #####   *        *  ####    @   @
 @@          ###### *      * ######       @@
  @@@        #######********######       @@
    @@@       ##################     @@@@
      @@          ############         @@
        @@           AAAAAA          @@
         @@         AAAAAAAA        @@
           @@@       AAAAAA      @@@
              @@      AAAA      @@
                @@            @@
                 @@@@@@@@@@@@@ """

freqtable = {  #Mapping Notes to Hz (googled these)
'a#5': 932,
'b5':  988,
'c6':  1046,
'c#6': 1109,
'd6':  1175,
'd#6': 1244,
'e6':  1318,
'f6':  1397,
'f#6': 1480,
'g6':  1568,
'g#6': 1661,
'a6':  1760,
'a#6': 1865,
'b6':  1975,
'c7':  2093
}

freqs = [    #The melody (the durations were calculated with FL studio.)
('g6', 2000),
('c6', 1009),
('e6', 2000),
('g6', 3021),
('c6', 1009),
('e6', 2000),
('g6', 1009),
('b5', 1008),
('d#6', 1008),
('g6', 1008),
('b6', 2000),
('a6', 7021),
('g6', 2000),
('a#5', 1009),
('d6', 2000),
('g6', 3021),
('a#5', 1009),
('d6', 2000),
('g6', 1009),
('c#6', 1008),
('e6', 1008),
('g6', 1008),
('b6', 2000),
('a6', 7021),
('b6', 1009),
('c7', 2000),
('b6', 1009),
('c7', 2000),
('a6', 4000),
('c7', 1009),
('b6', 2000),
('a6', 1009),
('g6', 2000),
('f#6', 1009),
('g6', 2000),
('e6', 4000),
('c#6', 1009),
('d6', 2000),
('e6', 1009),
('f6', 2000),
('e6', 1009),
('f6', 2000),
('b5', 4000),
('e6', 1009),
('d6', 2000),
('c6', 7021)
]

for i in freqs:
    Beep(freqtable[i[0]]/2, # Pitch in Hz    (divided by 2 because too high pitched)
                   i[1]/8)  # Duration in ms (divided by 8 to make it faster)