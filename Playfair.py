s = []
for i in range(26):
    p = []
    for i in range(26):
        p.append('..')
    s.append(p)

u = "TR XY CB MH AF CM UV YE OH PT CS AF CS ST EQ CS IN TY IM ST NA AF CS CE MR BH XA AV AF RM IU CQ PU HL MR LC CE TO TF NH MA KU XA HK OT AW AN AO TX TF FU EI SC WN AF HM EB FU MC VA UG TO TR EB MH YL FI FU UV TY AN EH BS EI QY OQ MO UV SF AM EA FT EP YH YS XN SK EI FU SC"

v = "BE WA RY OF TH EN EX TC HA MB ER TH ER EI SV ER YL IT TL EI OY TH ER ES PE AK OU TX TH EP AS SW OR DO PE NS ES AM ET OG OT HR OU GH MA YX YO UH AV ET HE ST RE NG TH FO RT HE NE XT CH AM BE RT OF IN DT HE EX IT YO UF IR ST WI LX LN EX ED TO UT TE RM AG IC WO RD ST HE RE"

a = u.split(' ')
b = v.split(' ')

#for i in range(len(a)):
#    print(a[i], b[i])
    #print(ord(a[i][0]) - ord('A'), ord(a[i][1]) - ord('A'))
    #s[ord(a[i][0]) - ord('A')][ord(a[i][1]) - ord('A')] = b[i][0] + b[i][1]
    #s[ord(a[i][1]) - ord('A')][ord(a[i][0]) - ord('A')] = b[i][1] + b[i][0]
    #s[ord(b[i][0]) - ord('A')][ord(b[i][1]) - ord('A')] = a[i][0] + a[i][1]
    #s[ord(b[i][1]) - ord('A')][ord(b[i][0]) - ord('A')] = a[i][1] + a[i][0]
    
#for i in s:
#    print(i)

#for i in range(26):
#    t = ""
#    for j in range(26):
#        if(s[i][j][0] != '.'):
#            t = t + s[i][j][0]
#    print(t)

