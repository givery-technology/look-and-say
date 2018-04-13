import sys
from operator import itemgetter

def main(filename):
    segments = []
    with open(filename, 'r') as fp:
        fp.readline()
        segments = [[int(p) for p in s.strip().split(' ')] for s in fp.readlines()]
    segments.sort(key=itemgetter(0))
    ret = []
    for seg in segments:
        for r in ret:
            if (seg[0] <= r[1]) and (seg[1] >= r[1]):
                r[1] = seg[1]
                break
            elif (seg[0] <= r[0]) and (seg[1] >= r[0]):
                r[0] = seg[0]
                break
        else:
            ret.append(list(seg))
    print max(map(lambda r: r[1] - r[0], ret))

main(sys.argv[1])
