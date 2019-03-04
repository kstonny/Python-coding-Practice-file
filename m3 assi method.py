def batscore(d):
    name=d.get('name')
    runs=d.get('runs')
    balls=d.get('balls')
    fours=d.get('4')
    six=d.get('6')
    batscore=int(runs/2)

batscore=int(runs/2)
if runs>=50:
    batscore=batsocre+5
if runs>=100:
    batscore=batscore=10

if run>0:
    sr=runs*100/balls
    if sr>=80 and sr<100:
        batscore=batscore+2
    if sr>100
        batscore=batscore+4

batscore=batscore+four
batscore=batscore=2*six

return{'name':name,'batscore':batscore}
def bowlscore(d):
    name=d.get('name')
    balls=d.get('overs')*6
    wkt=d.get('wkts')
    runs=d.get('runs')
    bowlscore=wkt*10

if wkt>=3:
    bowlscore=bowlscore+5
if wkt>=5:
    bowlscore=bowlscore+10

if balls>0:
    er=runs/balls
if er <= 2:
    bowlscore = bowlscore + 10
if er > 2 and er <= 3.5:
    bowlscore = bowlscore + 7
if er > 3.5 and er <= 4.5:
    bowlscore = bowlscore + 4

return {'name': name, 'bowlscore': bowlscore}
