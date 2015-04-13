#!/usr/bin/env python

bag = [(800, .1), (600, .2), (400, .3), (300, .4), ]

gain = { }

for item1 in bag:
    for item2 in bag:
        sp = item1[0]+item2[0]
        prob = item1[1]*item2[1]
        try:
            gain[sp] += prob
        except KeyError:
            gain[sp] = prob
        pass
    pass

aggreg = 0
for key in reversed(sorted(gain.iterkeys())):
    aggreg += gain[key]
    print "%4d: %2.0f%% %3.0f%%" % (key, 100*gain[key], 100*aggreg)
