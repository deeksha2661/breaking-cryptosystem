s1 = "wsam ie pjo ysgtm eyipbya .P axg niphay y, mey syw ahgm ewhrg tw hmysyam wh meyiepjo ys .Ag jygtmeyk pmys ie pjo ysavw kkoyjgsy whmy sy amwh rmephmewagh y!Me yigu ynay utg smew ajya apr ywap awjfkya no a mwmnmw ghiwfeyswhve wieuwr wm aepby oyyhae wtmy uox8 fkpiya. Me y fpaavgs uwa mxSrN03u wd dvwmegnmmey dngmya. Mew awameyt"

eng = {'e':12.7, 't':9.1, 'a':8.2, 'o':7.5, 'i':7.0, 'n':6.7, 's':6.3, 'h':6.1, 'r':6.0, 'd':4.3, 'l':4.0, 'u':2.8, 'c':2.8, 'm':2.4, 'w':2.4, 'f':2.2, 'y':2.0, 'g':2.0, 'p':1.9, 'b':1.5, 'v':1.0, 'k':0.8, 'x':0.2, 'j':0.2, 'q':0.1, 'z':0.1}

s1 = s1.lower()
s2 = ""
for c in s1:
    if c != ' ':
        s2 = s2 + c
print(s2)
l = len(s2)
print(l)
d = {}
for c in s2:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1
d = dict(sorted(d.items(), key = lambda item : -item[1]))
e = dict([(c, round(d[c]*100/l, 1)) for c in d])
print(e)
print(eng)
m = {}
for c in "abcdefghijklmnopqrstuvwxyz.,!803 ":
    m[c] = c

m['y'] = 'E' #frequency analysis
m['m'] = 'T' #frequency analysis
m['e'] = 'H' #to form the word'the' 
m['w'] = 'I' #to form the word 'this'
m['a'] = 'S' #to form the word 'this'
m['s'] = 'R' #to form the word 'there'
m['h'] = 'N' #to form the word 'interest'
m['p'] = 'A' #to form the word 'than'
m['g'] = 'O' #to form the word 'one'
m['r'] = 'G' #to form the word 'thing'
m['j'] = 'M' #to form the word 'message'
m['t'] = 'F' #to form the word 'for'
m['i'] = 'C' #to form the word 'chamber'
m['o'] = 'B' #to form the word 'chamber'
m['b'] = 'V' #to form the word 'caves'
m['k'] = 'L' #to form the word 'later'
m['v'] = 'W' #to form the word 'which'
m['x'] = 'Y' #to form the word 'you'
m['n'] = 'U' #to form the word 'you'
m['f'] = 'P' #to form the word 'password'
m['u'] = 'D' #to form the word 'password'
m['d'] = 'Q' #to form the word 'quotes'
m['8'] = '4' #8-x = x => x = 4
m['0'] = '6' #shift of 4
m['3'] = '9' #shift of 4

s3 = ""
for c in s2:
    s3 = s3 + m[c]
print(s3)
