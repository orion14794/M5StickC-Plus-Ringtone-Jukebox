# The following RTTTL tunes were extracted from the following:
# https://github.com/onebeartoe/media-players/blob/master/pi-ezo/src/main/java/org/onebeartoe/media/piezo/ports/rtttl/BuiltInSongs.java
# most of which originated from here:
# http://www.picaxe.com/RTTTL-Ringtones-for-Tune-Command/
#

SONGS = [
    'SavageLove:d=4,o=5,b=150:4b,4f,4e,4p,8g,8b,8b,8b,8g,8b,8b,8b,4b,4f,4e,4p,8e,8b,8b,8b,8g,8b,8c6,8b,4b,4f,4e,4p,8g,8b,8b,8b,8g,8b,8b,8b,4c6,4f,4e,8p,8e,8g,8b,8b,8b,8p,8b,8e6,8d6,4c6',
    'SMBMain Theme:d=4,o=5,b=125:a,8f.,16c,16d,16f,16p,f,16d,16c,16p,16f,16p,16f,16p,8c6,8a.,g,16c,a,8f.,16c,16d,16f,16p,f,16d,16c,16p,16f,16p,16a#,16a,16g,2f,16p,8a.,8f.,8c,8a.,f,16g#,16f,16c,16p,8g#.,2g,8a.,8f.,8c,8a.,f,16g#,16f,8c,2c6',
    'SMBTitle Music:d=4,o=5,b=125:8d7,8d7,8d7,8d6,8d7,8d7,8d7,8d6,2d#7,8d7,p,32p,8d6,8b6,8b6,8b6,8d6,8b6,8b6,8b6,8d6,8b6,8b6,8b6,16b6,16c7,b6,8a6,8d6,8a6,8a6,8a6,8d6,8a6,8a6,8a6,8d6,8a6,8a6,8a6,16a6,16b6,a6,8g6,8d6,8b6,8b6,8b6,8d6,8b6,8b6,8b6,8d6,8b6,8b6,8b6,16a6,16b6,c7,e7,8d7,8d7,8d7,8d6,8c7,8c7,8c7,8f#6,2g6',
    'SMBtheme:d=4,o=5,b=100:16e6,16e6,32p,8e6,16c6,8e6,8g6,8p,8g,8p,8c6,16p,8g,16p,8e,16p,8a,8b,16a#,8a,16g.,16e6,16g6,8a6,16f6,8g6,8e6,16c6,16d6,8b,16p,8c6,16p,8g,16p,8e,16p,8a,8b,16a#,8a,16g.,16e6,16g6,8a6,16f6,8g6,8e6,16c6,16d6,8b,8p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16g#,16a,16c6,16p,16a,16c6,16d6,8p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16c7,16p,16c7,16c7,p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16g#,16a,16c6,16p,16a,16c6,16d6,8p,16d#6,8p,16d6,8p,16c6',
    'SMBwater:d=8,o=6,b=225:4d5,4e5,4f#5,4g5,4a5,4a#5,b5,b5,b5,p,b5,p,2b5,p,g5,2e.,2d#.,2e.,p,g5,a5,b5,c,d,2e.,2d#,4f,2e.,2p,p,g5,2d.,2c#.,2d.,p,g5,a5,b5,c,c#,2d.,2g5,4f,2e.,2p,p,g5,2g.,2g.,2g.,4g,4a,p,g,2f.,2f.,2f.,4f,4g,p,f,2e.,4a5,4b5,4f,e,e,4e.,b5,2c.',
    'SMBunderground:d=16,o=6,b=100:c,c5,a5,a,a#5,a#,2p,8p,c,c5,a5,a,a#5,a#,2p,8p,f5,f,d5,d,d#5,d#,2p,8p,f5,f,d5,d,d#5,d#,2p,32d#,d,32c#,c,p,d#,p,d,p,g#5,p,g5,p,c#,p,32c,f#,32f,32e,a#,32a,g#,32p,d#,b5,32p,a#5,32p,a5,g#5',
    'Picaxe:d=4,o=6,b=101:g5,c,8c,c,e,d,8c,d,8e,8d,c,8c,e,g,2a,a,g,8e,e,c,d,8c,d,8e,8d,c,8a5,a5,g5,2c',
    'The Simpsons:d=4,o=5,b=160:c.6,e6,f#6,8a6,g.6,e6,c6,8a,8f#,8f#,8f#,2g,8p,8p,8f#,8f#,8f#,8g,a#.,8c6,8c6,8c6,c6',
    'Indiana:d=4,o=5,b=250:e,8p,8f,8g,8p,1c6,8p.,d,8p,8e,1f,p.,g,8p,8a,8b,8p,1f6,p,a,8p,8b,2c6,2d6,2e6,e,8p,8f,8g,8p,1c6,p,d6,8p,8e6,1f.6,g,8p,8g,e.6,8p,d6,8p,8g,e.6,8p,d6,8p,8g,f.6,8p,e6,8p,8d6,2c6',
    'TakeOnMe:d=4,o=4,b=160:8f#5,8f#5,8f#5,8d5,8p,8b,8p,8e5,8p,8e5,8p,8e5,8g#5,8g#5,8a5,8b5,8a5,8a5,8a5,8e5,8p,8d5,8p,8f#5,8p,8f#5,8p,8f#5,8e5,8e5,8f#5,8e5,8f#5,8f#5,8f#5,8d5,8p,8b,8p,8e5,8p,8e5,8p,8e5,8g#5,8g#5,8a5,8b5,8a5,8a5,8a5,8e5,8p,8d5,8p,8f#5,8p,8f#5,8p,8f#5,8e5,8e5',
    'Entertainer:d=4,o=5,b=140:8d,8d#,8e,c6,8e,c6,8e,2c.6,8c6,8d6,8d#6,8e6,8c6,8d6,e6,8b,d6,2c6,p,8d,8d#,8e,c6,8e,c6,8e,2c.6,8p,8a,8g,8f#,8a,8c6,e6,8d6,8c6,8a,2d6',
    'Muppets:d=4,o=5,b=250:c6,c6,a,b,8a,b,g,p,c6,c6,a,8b,8a,8p,g.,p,e,e,g,f,8e,f,8c6,8c,8d,e,8e,8e,8p,8e,g,2p,c6,c6,a,b,8a,b,g,p,c6,c6,a,8b,a,g.,p,e,e,g,f,8e,f,8c6,8c,8d,e,8e,d,8d,c',
    'Xfiles:d=4,o=5,b=125:e,b,a,b,d6,2b.,1p,e,b,a,b,e6,2b.,1p,g6,f#6,e6,d6,e6,2b.,1p,g6,f#6,e6,d6,f#6,2b.,1p,e,b,a,b,d6,2b.,1p,e,b,a,b,e6,2b.,1p,e6,2b.',
    'Looney:d=4,o=5,b=140:32p,c6,8f6,8e6,8d6,8c6,a.,8c6,8f6,8e6,8d6,8d#6,e.6,8e6,8e6,8c6,8d6,8c6,8e6,8c6,8d6,8a,8c6,8g,8a#,8a,8f',
    '20thCenFox:d=16,o=5,b=140:b,8p,b,b,2b,p,c6,32p,b,32p,c6,32p,b,32p,c6,32p,b,8p,b,b,b,32p,b,32p,b,32p,b,32p,b,32p,b,32p,b,32p,g#,32p,a,32p,b,8p,b,b,2b,4p,8e,8g#,8b,1c#6,8f#,8a,8c#6,1e6,8a,8c#6,8e6,1e6,8b,8g#,8a,2b',
    'Bond:d=4,o=5,b=80:32p,16c#6,32d#6,32d#6,16d#6,8d#6,16c#6,16c#6,16c#6,16c#6,32e6,32e6,16e6,8e6,16d#6,16d#6,16d#6,16c#6,32d#6,32d#6,16d#6,8d#6,16c#6,16c#6,16c#6,16c#6,32e6,32e6,16e6,8e6,16d#6,16d6,16c#6,16c#7,c.7,16g#6,16f#6,g#.6',
    'MASH:d=8,o=5,b=140:4a,4g,f#,g,p,f#,p,g,p,f#,p,2e.,p,f#,e,4f#,e,f#,p,e,p,4d.,p,f#,4e,d,e,p,d,p,e,p,d,p,2c#.,p,d,c#,4d,c#,d,p,e,p,4f#,p,a,p,4b,a,b,p,a,p,b,p,2a.,4p,a,b,a,4b,a,b,p,2a.,a,4f#,a,b,p,d6,p,4e.6,d6,b,p,a,p,2b',
    'StarWars:d=4,o=5,b=45:32p,32f#,32f#,32f#,8b.,8f#.6,32e6,32d#6,32c#6,8b.6,16f#.6,32e6,32d#6,32c#6,8b.6,16f#.6,32e6,32d#6,32e6,8c#.6,32f#,32f#,32f#,8b.,8f#.6,32e6,32d#6,32c#6,8b.6,16f#.6,32e6,32d#6,32c#6,8b.6,16f#.6,32e6,32d#6,32e6,8c#6',
    'GoodBad:d=4,o=5,b=56:32p,32a#,32d#6,32a#,32d#6,8a#.,16f#.,16g#.,d#,32a#,32d#6,32a#,32d#6,8a#.,16f#.,16g#.,c#6,32a#,32d#6,32a#,32d#6,8a#.,16f#.,32f.,32d#.,c#,32a#,32d#6,32a#,32d#6,8a#.,16g#.,d#',
    'TopGun:d=4,o=4,b=31:32p,16c#,16g#,16g#,32f#,32f,32f#,32f,16d#,16d#,32c#,32d#,16f,32d#,32f,16f#,32f,32c#,16f,d#,16c#,16g#,16g#,32f#,32f,32f#,32f,16d#,16d#,32c#,32d#,16f,32d#,32f,16f#,32f,32c#,g#',
    'A-Team:d=8,o=5,b=125:4d#6,a#,2d#6,16p,g#,4a#,4d#.,p,16g,16a#,d#6,a#,f6,2d#6,16p,c#.6,16c6,16a#,g#.,2a#',
    'Flinstones:d=4,o=5,b=40:32p,16f6,16a#,16a#6,32g6,16f6,16a#.,16f6,32d#6,32d6,32d6,32d#6,32f6,16a#,16c6,d6,16f6,16a#.,16a#6,32g6,16f6,16a#.,32f6,32f6,32d#6,32d6,32d6,32d#6,32f6,16a#,16c6,a#,16a6,16d.6,16a#6,32a6,32a6,32g6,32f#6,32a6,8g6,16g6,16c.6,32a6,32a6,32g6,32g6,32f6,32e6,32g6,8f6,16f6,16a#.,16a#6,32g6,16f6,16a#.,16f6,32d#6,32d6,32d6,32d#6,32f6,16a#,16c.6,32d6,32d#6,32f6,16a#,16c.6,32d6,32d#6,32f6,16a#6,16c7,8a#.6',
    'Jeopardy:d=4,o=6,b=125:c,f,c,f5,c,f,2c,c,f,c,f,a.,8g,8f,8e,8d,8c#,c,f,c,f5,c,f,2c,f.,8d,c,a#5,a5,g5,f5,p,d#,g#,d#,g#5,d#,g#,2d#,d#,g#,d#,g#,c.7,8a#,8g#,8g,8f,8e,d#,g#,d#,g#5,d#,g#,2d#,g#.,8f,d#,c#,c,p,a#5,p,g#.5,d#,g#',
    'Gadget:d=16,o=5,b=50:32d#,32f,32f#,32g#,a#,f#,a,f,g#,f#,32d#,32f,32f#,32g#,a#,d#6,4d6,32d#,32f,32f#,32g#,a#,f#,a,f,g#,f#,8d#',
    'Smurfs:d=32,o=5,b=200:4c#6,16p,4f#6,p,16c#6,p,8d#6,p,8b,p,4g#,16p,4c#6,p,16a#,p,8f#,p,8a#,p,4g#,4p,g#,p,a#,p,b,p,c6,p,4c#6,16p,4f#6,p,16c#6,p,8d#6,p,8b,p,4g#,16p,4c#6,p,16a#,p,8b,p,8f,p,4f#',
    'MahnaMahna:d=16,o=6,b=125:c#,c.,b5,8a#.5,8f.,4g#,a#,g.,4d#,8p,c#,c.,b5,8a#.5,8f.,g#.,8a#.,4g,8p,c#,c.,b5,8a#.5,8f.,4g#,f,g.,8d#.,f,g.,8d#.,f,8g,8d#.,f,8g,d#,8c,a#5,8d#.,8d#.,4d#,8d#.',
    'LeisureSuit:d=16,o=6,b=56:f.5,f#.5,g.5,g#5,32a#5,f5,g#.5,a#.5,32f5,g#5,32a#5,g#5,8c#.,a#5,32c#,a5,a#.5,c#.,32a5,a#5,32c#,d#,8e,c#.,f.,f.,f.,f.,f,32e,d#,8d,a#.5,e,32f,e,32f,c#,d#.,c#',
    'MissionImp:d=16,o=6,b=95:32d,32d#,32d,32d#,32d,32d#,32d,32d#,32d,32d,32d#,32e,32f,32f#,32g,g,8p,g,8p,a#,p,c7,p,g,8p,g,8p,f,p,f#,p,g,8p,g,8p,a#,p,c7,p,g,8p,g,8p,f,p,f#,p,a#,g,2d,32p,a#,g,2c#,32p,a#,g,2c,a#5,8c,2p,32p,a#5,g5,2f#,32p,a#5,g5,2f,32p,a#5,g5,2e,d#,8d',
    'Angofmus:d=4,o=6,b=125:d,8c,8a#5,c,8a5,g5,8c,8a5,f5,8d.,16c,8a#5,f.5,8d5,2a#5,d,8c,8a#5,c,8a5,g5,8c,8a5,f5,8d.,16c,8a#5,f.5,8d5,2a#5,8a#5,8a5,8g5,8f5,8d#5,8d5,8d5,2g5,8g5,8f5,8d#5,8d#.5,16d5,8c5,d5,8p,8a#5,8a5,8g5,8f5,8d#5,8d5,8d5,g.5,8g5,8a5,a#5,8p,d.,2c',
    'APowers:d=8,o=6,b=140:f,c#7,c#7,a#,a#,4p,f,c#7,c#7,a#,a#,4p,f,c#7,c#7,a#,a#,4p,f,c#7,c#7,g,g,4p,f,c#7,c#7,g,g,4p,f,c#7,c#7,a#,a#,4p,f,c#7,c#7,a#,a#,4p,c#7,c#7,a#,c#7,c#7,4p,c#7,c#7,a#,c#7,c#7,4p,f,c#7,c#7,4a#',
    'Shanghai:d=8,o=5,b=140:f#,a,2b,16p,f#,a,2e,16p,f#,a,b,4d6,b,4a,d,f#,2e,16p,e,f#,2a,16p,e,f#,4b4,16p,b4,d,4e.,f#,e,c#,b4,d,2a4',
    'Blue:d=8,o=5,b=140:a,a#,d,g,a#,c6,f,a,4a#,g,a#,d6,d#6,g,d6,c6,a#,d,g,a#,c6,f,a,4a#,g,a#,d6,d#6,g,d6,c6,a#,d,g,a#,c6,f,a,4a#,g,a#,d6,d#6,g,d6,c6,a#,d,g,a#,a,c,f,2g',
    'OCanada:d=4,o=5,b=160:2g,a#,8p,8a#,2d#.,f,g,g#,a#,c6,2f.,p,2g,a,8p,8a,2a#.,c6,d6,d6,c6,c6,2a#.,8f.,16g,g#.,8g,f,8g.,16g#,a#.,8g#,g,8g#.,16a#,c6,a#,g#,g,2f.,8f.,16g,g#.,8g,f,8g.,16g#,a#.,8g#,g,g,f,a#,8a#,8a,8g,8a,2a#',
    'OCanada:d=4,o=5,b=160:2g,a#,8p,8a#,2d#.,f,g,g#,a#,c6,2f.,p,2g,a,8p,8a,2a#.,c6,d6,d6,c6,c6,2a#.,8f.,16g,g#.,8g,f,8g.,16g#,a#.,8g#,g,8g#.,16a#,c6,a#,g#,g,2f.,8f.,16g,g#.,8g,f,8g.,16g#,a#.,8g#,g,g,f,a#,8a#,8a,8g,8a,2a#,2p,2g,a#.,8a#,2d#,2p,2g#,c6,8p,8c6,2f,2p,2a#,b,8p,8b,c6,g#,g,f,2d#,2f,2g,2p,2a#,d#6,8p,8d#6,c6,g#,g,f,2a#,2d,1d#',
    'Cherrypk:d=4,o=5,b=140:8d,8g,8b,2d6,8c6,8b,8c6,b,8a,2c6,8p,8d6,8e6,8f#6,8e6,8d6,8c6,8b,2d6,8p,8d,8g,8b,8d6,8c6,8b,8c6,b,8a,2e6,8p,d6,b.,8a,2g',
    'Wolves:d=4,o=5,b=180:2f,c,f,2a,2f,2f.6,g6,8f6,2c6,2d.6,8c6,8a#,2c6,2f,2a#.,8g,8f,2g,8p,2f,c,f,2a,f.,16p,32a#,32c6,32d6,32e6,2f6,g6,f6,2c6,2d.6,e6,8f6,8f6,c.7,2c7,2a.6,g6,f6,2f.6',
    'Dingdong:d=8,o=6,b=160:4a5,d,4d,f#,4b,f#,a,p,4a,b,4a,f#,4g,f#,e,p,4b5,e,4e,g,4c#7,4b,a,4g,g,4f#,e,4c#,4e,2d.,4p,4b,4b,a,g,a,b,a,p,4e,f#,4g#,e,4a.,4p,4b.,4a.,4g.,4p,e,p,4c#7,b,4a,b,a.,16g,4p,4a,b,4f#.,16e,2d',
    'Eternity:d=8,o=6,b=70:d#,16d,d#,16d,d#,16d,d#,a#5,g#5,16g5,g#5,16a#5,4c.,p,a#5,16a5,a#5,g5,4d#.,p,c,16a#5,c,g#5,4f.',
    'EyeOnMe:d=4,o=6,b=125:8g5,c,d,e,8g,2e,8d,8e,2c,8a5,8c,2d.,8g5,c,d,e,8g,2b,8b,8c7,a,8p,8g,8a,2g.,8g,c.7,8c7,c7,8b,a,2g,8e,8g,a.,a.,g,8f,8d,2e,e.,8d,8e,f,8e,d,c.,8p,8a5,8b5,2c,8p,8d,8e,g,2d',
    'Fido:d=16,o=6,b=800:f,4p,f,4p,f,4p,f,4p,c,4p,c,4p,c,4p,c,1p,1p,1p,1p',
    'Fido:d=8,o=7,b=500:f,f6,f,f6,f,f6,c,c6,c,c6,c,c6,c,c6,c,c6,c,c6,c,c6,c,c6,c,c6,c,c6,c,c6,c,c6,c,c6,c,c6,c,2p',
    'Firstlover:d=8,o=5,b=125:f,g#,a#,c#6,4f6,d#6,c#6,4d#6,g#6,2f6,f,g#,a#,c#6,4f6,d#6,c#6,2c#6,f,g#,a#,c#6,4f6,d#6,c#6,4d#6,g#6,2f6,f,g#,a#,c#6,4f6,d#.6,4g#6,2a#.6',
    'Godfather:d=4,o=5,b=160:8g,8c6,8d#6,8d6,8c6,8d#6,8c6,8d6,c6,8g#,8a#,2g,8p,8g,8c6,8d#6,8d6,8c6,8d#6,8c6,8d6,c6,8g,8f#,2f,8p,8f,8g#,8b,2d6,8p,8f,8g#,8b,2c6,8p,8c,8d#,8a#,8g#,g,8a#,8g#,8g#,8g,8g,8b4,2c',
    'Gump:d=4,o=7,b=125:8e6,8f6,8g6,g6,e6,g.6,8c,g6,e.6,8f6,8g6,8a6,a6,8f6,2a6,8p,8f6,8g6,8a6,a6,f6,a6,8d,b6,g.6,8e6,8f6,8g6,8g6,8c,2g6,8p,8a6,8b6,8c,c,a6,c.,8a6,c,a.6,8f6,8g6,8a6,a6,f6,2a6,8p,8f6,8g6,8a6,a6,f6,d.6,8e6,f6,d6,2c6',
    'Gypsy:d=16,o=5,b=125:8e,8e6,d6,c6,b,c6,4b,a,b,c6,d6,8c6,8b,8b,b,g,8b,g,b,f#,b,e,b,8d#,8b,8b,8b4,d#,e,f#,b,8a,g,f#,8b4,8b,8b,8b4,d#,e,f#,a,8g,f#,g,8a,8e6,8e6,e6,c6,8e6,c6,e6,b,e6,a,e6,8g,8e6,8e6,e6,b,8e6,b,e6,g,a,b,c6',
    'HBday:d=4,o=5,b=125:8d.,16d,e,d,g,2f#,8d.,16d,e,d,a,2g,8d.,16d,d6,b,g,f#,2e,8c.6,16c6,b,g,a,2g',
    'Hidamari:d=4,o=5,b=112:8g#6,g#.6,8g#6,8g6,8g#6,8a#6,g#.6,8p,8g#6,8g6,8f6,8d#6,8g#,f.6,8f6,8d#6,8c#6,8c6,8a#,2c.6,8d#6,d#.6,8d#6,8c#6,8c6,8a#,8c6,g#,8p,8g#,g#,c6,a#.,8a#,f.,8a#,g#.,8g#,g,p,c.6,8c6,c#.6,8c#6,8d#6,8g#6,8g6,8g#6,g6,8c.7,g#.6,8g#6,g6,8g#6,f6,8f6,8f6,c7,p,c.6,8d#6,g#6,8p,8d#6,8c#6,8c#6,8c6,g#,a#,2g#.',
    'Justcall:d=4,o=5,b=160:8c6,c6,2a,8c6,2b,8g,b,2c6,8p,8c6,c6,2a,8c6,b.,8a,g,a,2e,8p,8c6,c6,2a,8c6,2b,8g,b,2c6,8c6,c6,a.,8g,f,d,e,d,c,d,2c',
    'Intel:d=16,o=5,b=320:d,p,d,p,d,p,g,p,g,p,g,p,d,p,d,p,d,p,a,p,a,p,a,2p',
    'Knock:d=32,o=5,b=100:e,4p,e,p,e,8p,e,4p,e,8p,e,4p',
    'Laputa:d=4,o=6,b=125:8c,8d,d#.,8d,d#,g,2d.,g5,c.,8a#5,c,d#,2a#.5,g5,g#.5,8g5,8g#5,d#.,g.5,8f#5,8g5,d#.,d.,8a5,a5,d,2d,p,8c,8d,d#.,8d,d#,g,2d.,g5,c.,8a#5,c,d#,2a#.5,g5,g#.5,8d#,d,d#,f,8g,d#,p,8d#,8d,c,d,b5,2c',
    'Legend:d=4,o=5,b=160:g,8g,8a,b,b,c6,c6,2b,a,8a,8b,a,g,f#,g,2e,g,8g,8a,b,b,c6,c6,b,8b,8d6,e6,d6,8b,8a,g,a,a,2g',
    'LeungChuk:d=4,o=6,b=140:2b5,d.,8e,g.,8a,8e,8g,d,d.7,8g7,8e7,8d7,8b,8d7,1a,a.,8b,f#,e,d.,8e,g,a,b5,g,8e,8d,8e,8g,1d,b.,8d7,f#,a,8e,8g,2d.,8b5,d,8b5,8d,8e,8f#,8a,2e.,8d,8e,g.,8a,d7,b,a,8b,8a,g,8f#,8e,2b5,2g,8e.,16g,8e,8d,8b5,8d,8e,8g,1d',
    'LoveYouMor:d=4,o=5,b=160:8g,8c6,8d6,8e6,8e6,8d6,8c6,8e6,8e6,8d6,8c6,d6,e.6,8a,8c6,8d6,8e6,8e6,8d6,8c6,8e6,8e6,8d6,8c6,d6,e6,8p,8c6,8c6,8c6,8c6,8c6,8c6,8c6,d6,8e6,e.6,8d6,c.6,8p,8c6,a,8c6,f.6,8p,8f6,e6,c6,8p',
    'Lovecall:d=8,o=6,b=125:a5,f#,16e,d.,c#,4d.,c#,d,16c#,b.5,a5,4b5,f#5,f#5,b5,16a5,g.5,f#5,4g.5,16a5,16g5,e5,f#5,g5,a5,4e.5,a5,f#,16e,d.,e,4d.,c#,d,16c#,b.5,a5,4b5,f#5,f#5,b5,16a5,g.5,f#5,g5,a5,b5,c#,2d,p,c#,b5,c#,2d',
    'MetalGear:d=8,o=6,b=125:4e5,4d5,2c5,d5,e5,a4,4e5,2d5,c5,d5,4e.5,a5,g5,e5,4c5,2d5,e5,a5,2c,b5,c,d,4c,2a5,g5,a5,4b.5,c,4b5,a5,g5,1a5,4b5,4a5,2g5,a5,b5,e5,4b5,2a5,g5,a5,4b.5,e,d,b5,4g5,2a5,b5,e,2g,f#,g,a,4g,2e,d,e,4f#.,g,4f#,e,d,1e',
    'MImp:d=32,o=5,b=125:d6,d#6,d6,d#6,d6,d#6,d6,d#6,d6,d#6,d6,d#6,d6,d#6,d6,d#6,d6,d#6,d6,d#6,e6,f#6,d#6,8g.6,8g.,8g.,8a#,8c6,8g.,8g.,8f,8f#,8g.,8g.,8a#,8c6,8g.,8g.,8f,8f#,16a#6,16g6,2d6,16a#6,16g6,2c#6,16a#6,16g6,2c6,16a#,8c.6,4p,16a#,16g,2f#6,16a#,16g,2f6,16a#,16g,2e6,16d#6,8d.6',
    'Moonheart:d=4,o=5,b=140:c.,8e,g.,8c,b.4,8e,g.,8g,a.,8b,c.6,8a,2g,8e,8d,c.,8c,8c,8p,8e,8d,c.,8c,8c,8p,8d,8e,d.,8a4,b.4,16c,16d,2c',
    'MusicBox:d=8,o=6,b=200:c,c,g5,c,e,c,e,g,c,c7,b,a,4g,p,g,f,d,b5,g5,b5,d,f,e,c,a,4g,p,c,g5,c,e,c,e,g,c,c7,b,a,4g,p,g,f,d,b5,g5,b5,d,b5,c,g5,e,4c',
    'Musofnite:d=4,o=6,b=140:c#,e5,b5,e5,8a5,8b5,8c#,8d,b5,e,c#,e5,b5,e5,8a5,8b5,8c#,8d,b5,e,8f#,8a,8a,8a,b,8a,8g#,8f#,8a,8a,8a,b,8a,8g#,8f#,8a,8a,8a,8b,8a,8f#,8c#,e,8p,8c#,8c#,8b5,8b5,8c#,8d,8e,8c#,8b5,2a5',
    'HappyNY:d=8,o=6,b=125:a#5,c,c#,d#,4f#,4f,f,a#,a#,f,4f,4d#,d#,f#,f,d#,4d#,4c#,c#,c,a#5,a5,4a#5,4a#5,d#.,16f,c#.,16f,c,f,a#5,f,d#.,16f,c#.,16f,c,f,a#5,p',
    'HappyNY:d=8,o=6,b=200:4d,4f,4d.,c,4d,4f,4d.,c,4d,4f,4f,4g5,2a#5,4p,4d,4a#,4g.,f,4d,4a#,4g.,g,4a#.,a#,c7,a#,4g,2f,4p,f,p,f,g,4f,d,c,f,p,g5,p,a#5,4p,a#,p,2a#,g,f,4g,4a#,4d.,p,4d.,f,4g,4a#,4f.,g,4f,4d,4c.,d,4c,4a#5,4a#5,2g5,4f5,2g5',
    'HappyNY:d=8,o=6,b=125:g#,a#,g#,f#,g#,a#,g#,f#,d#,16d#,16c#,d#,f#,g#,f#,g#,p,f#,g#,f#,d#,c#,d#,f#.,16d#,c#,f#,f#,a#5,4g#5,4p,d#.,16c#,b5,c#,d#,c#,4d#,c#,f#,f#,a#5,4g#5,4p,d#,16d#,16c#,b5,c#,d#,c#,4d#,c#,f#,f#,a#5,4g#5,4p',
    'HappyNY:d=8,o=5,b=200:4c.,d,4e,4g,a,g,4p,c6,b,c6,4d6,4c6,4b,4c6,2a,p,a,b,c6,4d6,4c6,4b,4c6,2g,p,g,f,g,4a,4g,4e,4g,2d,p,d,e,f,4a,4g,4b,4d6,2c6',
    'HappyNY:d=16,o=5,b=140:8e,8g,8c6,8p,8e,8g,8c6,8p,8e6,8d6,8c6,4a,4f,8p,8d,8f,8b,8p,8d,8f,8b,8p,8d6,8b,8a,4g,4e,8p,8e,8g,8c6,8p,8e,8g,8c6,8p,8e6,8d6,8c6,4c6,4a,8p,8d6,8c6,8d6,4b,8a,8g,8p,8f,8e,8d,4c.',
    'HappyNY:d=4,o=5,b=225:c#6,d6,2d#6,c#6,a#,2f#,f,f#,2g#,f#,d#,2c#.,f,g#,2c#6,d#6,d#.6,8c#6,c#6,f,2f#.,p,f#6,f6,2d#6,2f#6,2b,2d#6,c#.6,8d#6,c#6,a#,2c#6,f#6,f6,2d#6,2f#6,f.6,8d#6,f6,f#6,2g#6',
    'OldFlame:d=4,o=5,b=160:b,8e,8g,b,a,g,8a,8g,2e,b,e6,8d6,8b,a,2b,8p,a,8g,8e,g,a,b,8e6,8d6,2b,8a,8b,8a,8g,f#,8g,8f#,2e,8p,e.6,8f#6,g6,f#6,8e6,8f#6,8e6,8d6,2e6,b,e6,8d6,8b,a,2b,8p,a,8g,8e,g,a,b,8e6,8d6,2b,8a,8b,8a,8g,f#,8g,8f#,2e',
    'Olympics:d=8,o=6,b=125:4a.,p,4c7,p,c7,4f,4g,4a,4f,4g,g.,16g,4g,a,g,f,16f,16g,a,f,4g.,p,4a.,p,4c7,p,c7,4f,4g,4a,4f,4g,g.,16g,4g,a,g,f,16f,16g,a,g,2f',
    'Olympics:d=16,o=6,b=80:g,e,e,g,g,e,32a,32g,f,g,e,e,g,g,8e.,g,e,e,g,g,e,32a,32g,f,g,e,e,g,g,8e.,g,e,e,g,g,e,32a,32g,f,g,e,e,g,g,e,p,g,a,g,32a,32g,f,2c7,8f.,f,1c7',
    'PacMan:d=16,o=6,b=140:b5,b,f#,d#,8b,8d#,c,c7,g,f,8c7,8e,b5,b,f#,d#,8b,8d#,32d#,32e,f,32f,32f#,g,32g,32g#,a,8b',
    'Phantom:d=4,o=5,b=140:c,f,c,d#.,8c#,2c#,a#4,d#,8a#4,2c,c,f,c,d#.,8c#,2c#,a#4,d#.,8a#4,2c,p,c,f,g#,c.6,8a#,2a#,a#,d#.6,8a#,2c6,p,c6,2f.6,8d#6,8c#6,8c6,8a#,8g#,8g,8f,2e,c#,c#.,8c,2c',
    'Urgent:d=8,o=6,b=500:c,e,d7,c,e,a#,c,e,a,c,e,g,c,e,a,c,e,a#,c,e,d7',
    'Mosaic:d=8,o=6,b=400:c,e,g,e,c,g,e,g,c,g,c,e,c,g,e,g,e,c',
    'Mosaic:d=8,o=6,b=400:c,e,g,e,c,g,e,g,c,g,c,e,c,g,e,g,e,c,p,c5,e5,g5,e5,c5,g5,e5,g5,c5,g5,c5,e5,c5,g5,e5,g5,e5,c5',
    'Saboten:d=8,o=5,b=140:d,b,4b.,p,a,b,a,g,2g,e,e,g,e,2d,p,b,c6,2d.6,p,d6,d6,e6,e6,d6,d6,4b.,g,2a.,p,d,d,2b,p,b,a,a,2g,p,e,e,g,e,2d,p,b,b,4a,4a.,p,a,a,g,2e,p,g,4a,2g.',
    'SilentBond:d=16,o=5,b=90:d,b,a,4b.,a,g,8a,b,8a,d,g,8f#,8g.,g,a,8f#,e,8d.,b4,c,b4,c,8g.,8c,8d.,8g.,d,8e,f#,8g,8b,a,4a.',
    'Snowman:d=8,o=5,b=200:2g,4e.,f,4g,2c6,b,c6,4d6,4c6,4b,a,2g.,b,c6,4d6,4c6,4b,a,a,g,4c6,4e.,g,a,4g,4f,4e,4d,2c.,4c,4a,4a,4c6,4c6,4b,4a,4g,4e,4f,4a,4g,4f,2e.,4e,4d,4d,4g,4g,4b,4b,4d6,d6,b,4d6,4c6,4b,4a,4g,4p,2g',
    'StElmo:d=8,o=6,b=140:4d#.,2c7,p,g#,4a#,4c7,4c7,4a#,2c#7,p,4d#.,2c7,g#,a#,4c7,4c7,4a#,2c#7,p,g#,a#,c7,4c#7,p,4c#,d#,f,4g,p,g,g#,a#,4c7,p,4c,c#,d#,f,p,g#,a#,c7,4c#7,p,4c#,d#,f,g,p,g,g#,4a#.,2f,2g#',
    'Stubborn:d=16,o=5,b=90:a#,a#,a#,a#,a#,c6,8d6,32p,4f6,8d#6,8d#6,a#,d#6,8p,4d.6,8p,a#,a#,8a#,8d6,4f6,8p,f6,8g6,8f6,8f6,d#6,4f6,8p,a#,a#,8a#,8f6,4f6,8p,8f6,8g6,32p,8a#.6,8g6,4f6,p,d6,d6,d6,d#6,d6,4a#,8p,f,f,4d6,2c6,8a#,8a,4a#',
    'Sweetie:d=4,o=5,b=125:e6,8g6,8a6,e.6,8c6,8d6,16d6,16c6,8d6,8g6,2e6,8d6,8d6,8d6,8e6,8d6,8c6,8a,8g,c.6,8e6,8d6,8c6,8a,8g,2c6,8p,2e6,g,8a,16g,16a,2c6',
    'Titanic:d=8,o=6,b=125:e,f#,2g#,16f#,16g#,16f#,e,f#,2b,32c#7,32b,a,g#,4e,2c#,2b5,d#,f#,f#,2g#,16a,16g#,16f#,16e,4f#,2b,g#,b,2c#7,2b,2f#',
    'Titanic:d=4,o=6,b=140:2e,2f#,16p,b5,2b,a,8g#,f#,8p,g#.,8a,2g#,f#,16p,8e,d#,e,8p,8d#,2c#,2b5,p,2e,2f#,16p,b5,2b,a,8g#,f#,8p,g#,a,2g#,f#,e,d#,e,16p,d#,2e,f#,g#,16a,16g#,8f#,f#,e,2e',
    'ToLoveUM:d=4,o=5,b=125:8a,8b,2c#6,b,8a,2b,8p,8a,a.,g#,8f#,g#.,8p,g#,8e,f#,8d6,c#6,b,a,8b,g#.,8g#,2a',
    'Triple:d=8,o=5,b=635:c,e,g,c,e,g,c,e,g,c6,e6,g6,c6,e6,g6,c6,e6,g6,c7,e7,g7,c7,e7,g7,c7,e7,g7',
    'Voyager:d=4,o=6,b=140:2c#,2f#5,2f#,f,c#,c#,d#,d#,c#,2a#,f#,8p,8d#,8c#,8f#5,2f#5,8p,8c#,8g#5,8c#5,2c#5,g#5,1f#5,8p,2f#5,g#5,a#5,b5,c#,d,e,2f#,b5,f#,1g,2f#,b5,f#,2g,b5,g,2g#.,a#,2g#,2c#',
    'Windsong:d=4,o=6,b=140:a#5,c,8d,d,8d,8d,8p,8d,8g5,8d#,d#,8d#,d#.,8p,8c,8c,8c,8c,f,d#,2d,d,c,8a#5,a#.5,a#5,g5,8c,8c,8c,8c,c,g5,8a5,8a5,8a5,8a#5,c,a#5,2a5',
    'Wishever:d=4,o=6,b=112:e,8e,8c#,b5,8c#,8e,2e,e,8e,8c#,b5,8c#,8f#,2f#,g#,8e,8c#,g#,8e,8c#,f#.,8e,2c#,a,a,8c#,e,2f#,8p,f#,b5,d#,c#,2e',
    'XFile:d=16,o=6,b=355:e.,p,e.,p,e.,p,e.,p,b.,p,b.,p,b.,p,b.,p,a.,p,a.,p,a.,p,a.,p,b.,p,b.,p,b.,p,b.,p,d.7,p,d.7,p,d.7,p,d.7,p,b.,p,b.,p,b.,p,b.,p,b.,p,b.,p,b.,p,b.,p,b.,p,b.,p,b.,p,b.,p',
    'axelf:d=4, o=5, b=160:f#, 8a., 8f#, 16f#, 8a#, 8f#, 8e, f#, 8c.6, 8f#, 16f#, 8d6, 8c#6, 8a, 8f#, 8c#6, 8f#6, 16f#, 8e, 16e, 8c#, 8g#, f#.',
    'Blink182:d=4,o=5,b=63:32f, 32g, 32a, 32a#, 8a, 32g, 32a, 32a#, 16a, 16g, 32d, 32g, 32a, 32a#, 8a, 32g, 32a, 32a#, 16a, 16g, 32f, 32g, 32a, 32a#, 8a, 32g, 32a, 32a#, 16a, 16g, 32d, 32g, 32a, 32a#, 8a, 32g, 32a, 32a#, 16a, 16g',
    'Bond007:d=4, o=5, b=320:c, 8d, 8d, d, 2d, c, c, c, c, 8d#, 8d#, 2d#, d, d, d, c, 8d, 8d, d, 2d, c, c, c, c, 8d#, 8d#, d#, 2d#, d, c#, c, c6, 1b., g, f, 1g.',
    'DavyCrockett:d=4, o=5, b=160:f, 8f., 16g, 8a., 16g, 8f., 16c, d, f, 2c, f, g, a, 8g., 16f, g, 8g., 16a, 2g, c, 8c., 16c, f, 8c., 16c, d, 8d., 16d, 2g, e, 8e., 16e, e, 8e., 16d, c, 8d., 16e, 2f, a, 2c.6, d.6, 8d6, 8c6, a., 8c., 16c, 8c., 16c, e, g, 2f., p, a, 2c.6, d.6, 8d6, 8c6, a., 8c., 16c, 8c., 16c, e, g, 2f.',
    'Eminem:d=4,o=5,b=80:16f, 16f6, p, 16g, 16g6, p, 16a#, 16a#6, p, 16g#, 16p, 16f#6, 16p, 16f6, 16d#6, 16p',
    'Aerosmith:d=4, o=5, b=125:2p, 16a, 16p, 16a, 16p, 8a., 16p, a, 16g, 16p, 2g, 16p, p, 8p, 16g, 16p, 16g, 16p, 16g, 8g., 16p, c6, 16a#, 16p, a, 8g, f, g, 8d, 8f., 16p, 16f, 16p, 16c,',
    '90210:d=4, o=5, b=140:8f, 8a#, 8c6, d.6, 2d6, p, 8f, 8a#, 8c6, 8d6, 8d#6, f6, f.6, 2a#., 8f, 8a#, 8c6, 8d6, 8d#6, 8f6, 8g6, f6, 8d#6, d#6, d6, 2c.6, 8a#, a, a#., g6, 8f6, 8d#6, 8d6, 8d#6, 8d6, 8a#, f',
    'DawsonsCreek:d=4,o=5,b=90:16g4, 16f, 8g, 8g, 8g, 16e, 8g, 8g., 16c, 16e, 8g, 8g, 8g, 16e, 8d, 8c., 16g, 16g, 16f, 8g, 8g, 8g, 16e, 8g, 8g., 16c, 8g, 8g, 16c6, 8c6, 8d6, 8g, 8g., p, 16d6, 8d6, 8d6, 8c6, b, p, 16d6, 8d6, 8d6, 8c6, b',
]

def find(name):
    for song in SONGS:
        song_name = song.split(':')[0]
        if song_name == name:
            return song
