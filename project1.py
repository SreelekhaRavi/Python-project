tic_board=['-1-','-2-','-3-',
           '-4-','-5-','-6-',
           '-7-','-8-','-9-']

choices=['' , '']
res=[0]
cells=[1,2,3,4,5,6,7,8,9]


def print_tic_board():
       print(tic_board[0]+'|'+tic_board[1]+'|'+tic_board[2]+ '\n'
            +tic_board[3]+'|'+tic_board[4]+'|'+tic_board[5]+ '\n'
            +tic_board[6]+'|'+tic_board[7]+'|'+tic_board[8])

def chose():
    choice=''
    while choice!="x" and choice!="o":
        choice=str(input("Enter the choice:x o\n"))
    if choice=='x':
        choices[0]='x'
        choices[1]='o'
    else:
        choices[0]='o'
        choices[1]='x'
    print('Player 1:'+choices[0])
    print('Player 2:'+choices[1])

def res_check():
     if ((tic_board[0]==tic_board[1]==tic_board[2]) or (tic_board[0]==tic_board[3]==tic_board[6])
         or (tic_board[0]==tic_board[4]==tic_board[8]) or (tic_board[1]==tic_board[4]==tic_board[7])
         or (tic_board[2]==tic_board[5]==tic_board[8]) or (tic_board[2]==tic_board[4]==tic_board[6])
         or (tic_board[3]==tic_board[4]==tic_board[5]) or (tic_board[6]==tic_board[7]==tic_board[8])):
        res[0]=1
        print("Game Over!!! ")
              
def game():
    j=1
   
    while j<10:
        i=0
        while i not in cells:
                 i=int(input("Enter a number 1 to 9 to chose a cell or select an unchosed cell\n"))
       
        cells.remove(i)
        if j%2==0:
            if i>0 or i <10:
                 tic_board[i-1]=choices[1]
                 print_tic_board()
                 res_check()
                 if res[0]==1:
                    print('Player 2 wins!!')
                    break
        else:
            if i>0 or i <10:
                 tic_board[i-1]=choices[0]
                 print_tic_board()
                 res_check()
                 if res[0]==1:
                      print('Player 1 wins!!')
                      break
        j+=1
         

def main():
   
    print_tic_board()
    chose()
    game()
if __name__ == '__main__':
    main()