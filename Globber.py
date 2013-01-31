#!/usr/bin/env python
import sys


def _matchStar(glob, s):
    if len(glob) == 1:
        return ["", ""]
    index = s.find(glob[1])
    if index is not -1:
        return [glob[1:], s[index:]]
    return False


def _matchQuestionMark(glob, s):
    if s is not "":
        return [glob[1:], s[1:]]
    return False


def _matchNotSet(glob, s):
    not_set = glob.split("]")[0][2:]
    end = glob.find("]") + 1
    glob = glob[end:]
    if s[0] not in not_set:
        return [glob, s[1:]]
    return False


def _matchSet(glob, s):
    if glob[1] is "^":
        return _matchNotSet(glob, s)
    mset = glob.split("]")[0][1:]
    if s[0] in mset:
        return [glob, s[1:]]
    return False


def _matchChar(glob, s):
    char, glob = glob[0], glob[1:]
    if s[0] is char:
        return [glob, s[1:]]
    return False


matchMap = {
    "*": _matchStar,
    "?": _matchQuestionMark,
    "[": _matchSet
}


def match(glob, s):
    while len(s):
        if len(glob) is 0:
            return False
        m = matchMap.get(glob[0], _matchChar)(glob, s)
        if m is False:
            return False
        glob, s = m[0], m[1]
    return True

if __name__ == '__main__':
    if len(sys.argv) is not 3:
        print "usage Globber.py glob string"
    else:
        print match(sys.argv[1], sys.argv[2])
