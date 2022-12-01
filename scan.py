import json
import sys

import objectpath
import os
from sql import scanaction

if __name__ == '__main__':
    f = os.path.join(os.path.dirname(sys.executable), 'result.txt')
    tree_obj = objectpath.Tree(json.load(open(f, 'r', encoding="utf8")))
    iterator = tree_obj.execute('$..Text')
    result = ''
    for auto in iterator:
        result += auto

    badgeNum = int(result)
    boothf = os.path.join(os.path.dirname(sys.executable), 'settings.json')
    booth_obj = objectpath.Tree(json.load(open(boothf, 'r', encoding="utf8")))
    booth_iterator = booth_obj.execute('$..BoothId')
    booth = 0
    for auto in booth_iterator:
        booth = auto
    scanaction(badgeNum, booth)
