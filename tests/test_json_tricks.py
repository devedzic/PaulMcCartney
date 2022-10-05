from datetime import date

from json_tricks import dumps, loads

from music.musician import Musician
from music.band import Band

from testdata.musicians import *

if __name__ == '__main__':

    theBeatles = Band('The Beatles', *[johnLennon, paulMcCartney, georgeHarrison, ringoStarr],
                      start=date(1957, 7, 6), end=date(1970, 4, 10))
    theRollingStones = Band('The Rolling Stones', *[mickJagger, keithRichards, ronWood, charlieWatts],
                            start=date(1962, 7, 12))
    pinkFloyd = Band('Pink Floyd', *[sydBarrett, davidGilmour, rogerWaters, nickMason, rickWright])

    theBeatles_json = dumps(theBeatles, indent=4)
    print(theBeatles_json)
    print(theBeatles == loads(theBeatles_json))
    print()

    bands_json = dumps([theBeatles, theRollingStones, pinkFloyd], indent=4)
    print(bands_json)
    print([theBeatles, theRollingStones, pinkFloyd] == loads(bands_json))



