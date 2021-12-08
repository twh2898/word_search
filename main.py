#!/usr/bin/env python3

from collections import defaultdict

with open('field.txt', 'r') as f:
    field = [[c.upper() for c in line.strip()] for line in f]

with open('words.txt', 'r') as f:
    words = [line.strip().upper() for line in f]

letters = defaultdict(list)
for r, row in enumerate(field):
    for c, col in enumerate(row):
        letters[col].append((r, c))


def valid(r, c):
    return r >= 0 and c >= 0 and r < len(field) and c < len(field[0])


def take_n(r, c):
    while valid(r, c):
        yield field[r][c]
        r -= 1


def take_s(r, c):
    while valid(r, c):
        yield field[r][c]
        r += 1


def take_w(r, c):
    while valid(r, c):
        yield field[r][c]
        c -= 1


def take_e(r, c):
    while valid(r, c):
        yield field[r][c]
        c += 1


def take_nw(r, c):
    while valid(r, c):
        yield field[r][c]
        r -= 1
        c -= 1


def take_ne(r, c):
    while valid(r, c):
        yield field[r][c]
        r -= 1
        c += 1


def take_sw(r, c):
    while valid(r, c):
        yield field[r][c]
        r += 1
        c -= 1


def take_se(r, c):
    while valid(r, c):
        yield field[r][c]
        r += 1
        c += 1


_search = {
    'n': take_n,
    'ne': take_ne,
    'e': take_e,
    'se': take_se,
    's': take_s,
    'sw': take_sw,
    'w': take_w,
    'nw': take_nw,
}


def search_word(start, word):
    def test(take_fn):
        r, c = start
        gen = take_fn(r, c)
        for letter in word:
            try:
                gen_next = next(gen)
            except StopIteration:
                return False
            if letter != gen_next:
                return False
        return True

    res = []
    for take in _search:
        fn = _search[take]
        if test(fn):
            res.append(take)

    return res


if __name__ == '__main__':
    for word in words:
        starts = letters[word[0]]
        for start in starts:
            res = search_word(start, word)
            if any(res):
                print(word, start, res)
