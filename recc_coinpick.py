ways= 0
winner= ""
# wins= {'Alice':0, 'bob':0}
def play(n, p1, p2):
    if n==0:
        global ways
        ways+=1
        global winner
        winner= p2
        # wins[p2]+=1
        # return
    elif n<0:
        pass
    elif n%3==2:
        p1, p2 = p2, p1
        play(n - 2, p1, p2)
    elif n%3==1 and n>=4:
        p1, p2 = p2, p1
        play(n - 4, p1, p2)
        play(n - 1, p1, p2)
    else:
        p1,p2= p2,p1
        play(n - 1, p1, p2)

        play(n - 2, p1, p2)
        play(n - 4, p1, p2)

def main():
    play(30, 'alice', 'bob')
    # print(wins)
    print(ways)
    print(winner)
main()