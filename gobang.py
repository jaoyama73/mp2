import argparse
import math
import string
import numpy as np
import time
from collections import Counter
import random
d = dict(enumerate(string.ascii_lowercase,1))

#   _oo__
three2D_1 = ['D','D',' ',' ',' ']
three2L_1 = ['L','L',' ',' ',' ']
#   __oo_
three2D_2 = [' ',' ','D','D',' ']
three2L_2 = [' ',' ','L','L',' ']
#   _o__o
three2D_3 = [' ','D',' ',' ','D']
three2L_3 = [' ','L',' ',' ','L']
#   o__o_
three2D_4 = ['D',' ',' ','D',' ']
three2L_4 = ['L',' ',' ','L',' ']
#   _o_o_
three2D_5 = [' ','D',' ','D',' ']
three2L_5 = [' ','L',' ','L',' ']

#   _ooo_
three3D_1 = [' ','D','D','D',' ']
three3L_1 = [' ','L','L','L',' ']
#   _o_oo
three3D_2 = [' ','D',' ','D','D']
three3L_2 = [' ','L',' ','L','L']
#   oo_o_
three3D_3 = ['D','D',' ','D',' ']
three3L_3 = ['L','L',' ','L',' ']
#   ooo__
three3D_4 = ['D','D','D',' ',' ']
three3L_4 = ['L','L','L',' ',' ']
#   __ooo
three3D_5 = [' ',' ','D','D','D']
three3L_5 = [' ',' ','L','L','L']
#   o_o_o
three3D_6 = ['D',' ','D',' ','D']
three3L_6 = ['L',' ','L',' ','L']
#   oo__o
three3D_7 = ['D','D',' ',' ','D']
three3L_7 = ['L','L',' ',' ','L']
#   o__oo
three3D_8 = ['D',' ',' ','D','D']
three3L_8 = ['L',' ',' ','L','L']
#   _oooo
three4D_1 = ['D','D','D','D',' ']
three4L_1 = ['L','L','L','L',' ']
#   oooo_
three4D_2 = [' ','D','D','D','D']
three4L_2 = [' ','L','L','L','L']
#   oo_oo
three4D_5 = ['D','D',' ','D','D']
three4L_5 = ['L','L',' ','L','L']
#   ooo_o
three4D_3 = ['D','D','D',' ','D']
three4L_3 = ['L','L','L',' ','L']
#   o_ooo
three4D_4 = ['D',' ','D','D','D']
three4L_4 = ['L',' ','L','L','L']
#   _oooo_
extremeD = [' ','D','D','D','D',' ']
extremeL = [' ','L','L','L','L',' ']

da2 = [three2D_1,three2D_2,three2D_5]#,three2D_4,three2D_5]
da3 = [three3D_1,three3D_2,three3D_3]#,three3D_4,three3D_5]
da4 = [three4D_1,three4D_4,three4D_3]#,three4D_4]#,three4D_5]
li2 = [three2L_1,three2L_2,three2L_5]#,three2L_4,three2L_5]
li3 = [three3L_1,three3L_2,three3L_3]#,three3L_4,three3L_5]
li4 = [three4L_1,three4L_4,three4L_3]#,three4L_4]#,three4L_5]
Dwin = ['D','D','D','D','D']
Lwin = ['L','L','L','L','L']

class game:
    board = np.array([],dtype=object)
    #available = []
    #availableCopy = []
    occupied = []
    placeable = []
    boardSize = 11
    player = 'L'

    def __init__(self,boardSize = 11, player = 'L'):
        self.boardSize = boardSize
        self.player = player
        parser = argparse.ArgumentParser(description='Game Setup Options')
        parser.add_argument('-n',help='Set Board Size')
        parser.add_argument('-l',help='Switch to Light Color Player',action='store_true')
        args = parser.parse_args()
        if args.n:
            if(int(args.n)<3 or int(args.n)>26):
                print('invalid size')
                exit(0)
            else:
                self.boardSize = int(args.n)
        if args.l:
            self.player = 'D'
        self.board = np.zeros([self.boardSize,self.boardSize],dtype=int)
        self.board = np.where(self.board==0,' ',self.board)
        #for idx,x in np.ndenumerate(self.board):
        #    idx = [idx[0],idx[1]]
            #self.available.append(idx)
        #self.availableCopy = self.available
        
    def bestMove(self):
        bestScore = -math.inf
        score = 0
        Move = [-1,-1]
        self.placeable = self.getCandidates(self.occupied)
        #print(len(self.placeable))
        if(len(self.placeable)!=0):
            #print("placeable: ",self.placeable)
            for pos in self.placeable:
                i = pos[0]
                j = pos[1]
                #print(pos)
                if(self.board[i][j]==' '):
                    #print(i,j,"empty")
                    self.board[i][j]=self.player
                    if(self.player == 'D'):
                        score = self.minimaxFirst(self.board,2,-math.inf,math.inf,False)
                    else:
                        score = self.minimaxSecond(self.board,2,-math.inf,math.inf,False)
                    #print(score,"points",i,j)
                    if(score>bestScore):
                        bestScore=score
                        Move = [i,j]
                    self.board[i][j]=' '
        
        if(Move!=[-1,-1]):
            self.board[Move[0]][Move[1]]=self.player
            print("Move played:",str(d[Move[0]+1])+str(Move[1]+1))
            #self.available.remove(Move)
            self.occupied.append(Move)
            self.placeable = self.getCandidates(self.occupied)
            #self.availableCopy = self.available
        
        else:
            #print("-1,-1")
            x,y = random.randint(0,self.boardSize-1),random.randint(0,self.boardSize-1)
            self.board[x][y]=self.player
            print("Move played:",str(d[x+1])+str(y+1))
            self.occupied.append([x,y])
            self.placeable = self.getCandidates(self.occupied)
            
        print(self.board)
        
        print("placeable",self.placeable)
        print("occupied",self.occupied)
        #print(self.diag(Move[0],Move[1]))
        if(self.player == 'D'):
            self.player='L'
        else:
            self.player='D'
        self.evaluate(self.board)
    
    #-l
    def minimaxFirst(self,board,depth,alpha,beta,isMax):
        if(depth == 0):
            score = self.evaluate(self.player)
            return score
        
        
        if(isMax):
            bestScore = -math.inf
            if(len(self.placeable)!=0):
                for pos in self.placeable:
                    #print(self.board)
                    #print('place',self.placeable)
                    #print(pos,self.board[pos[0]][pos[1]])
                    if(self.board[pos[0]][pos[1]]==' '):
                        self.board[pos[0]][pos[1]] = 'D'
                        self.occupied.append([pos[0],pos[1]])
                        score= self.minimaxFirst(self.board,depth-1,alpha,beta,False)
                        self.board[pos[0]][pos[1]]= ' '
                        self.occupied.pop()
                        bestScore = max(score,bestScore)
                        alpha = max(alpha,bestScore)
                        if(beta<=alpha):
                            break     
            return bestScore
        else:
            bestScore = math.inf
            if(len(self.placeable)!=0):
                for pos in self.placeable:
                    #print('place',self.placeable)
                    #print(pos,self.board[pos[0]][pos[1]])
                    if(self.board[pos[0]][pos[1]]==' '):
                        self.board[pos[0]][pos[1]] = 'L'
                        self.occupied.append([pos[0],pos[1]])
                        score = self.minimaxFirst(self.board,depth-1,alpha,beta,True)
                        self.board[pos[0]][pos[1]]= ' '
                        self.occupied.pop()
                        #print("min score",score)
                        bestScore = min(score,bestScore)
                        #print(bestScore)
                        beta = min(beta,bestScore)
                        if(beta<=alpha):
                            break              
            return bestScore

    def minimaxSecond(self,board,depth,alpha,beta,isMax):
        if(depth == 0):
            score = self.evaluate(self.player)
            return score
       
        
        if(isMax):
            bestScore = -math.inf
            if(len(self.placeable)!=0):
                for pos in self.placeable:
                    #print("pos in minimax",pos)
                    i = pos[0]
                    j = pos[1]
                    if(self.board[i][j]==' '):
                        self.board[i][j] = 'L'
                        #self.occupied.append([pos[0],pos[1]])
                        score= self.minimaxSecond(self.board,depth-1,alpha,beta,False)
                        self.board[i][j]= ' '
                        #self.occupied.pop()
                        bestScore = max(score,bestScore)
                        alpha = max(alpha,bestScore)
                        if(beta<=alpha):
                            break     
            return bestScore
        else:
            bestScore = math.inf
            if(len(self.placeable)!=0):
                for pos in self.placeable:
                    i = pos[0]
                    j = pos[1]
                    if(self.board[i][j]==' '):
                        self.board[i][j] = 'D'
                        #self.occupied.append([pos[0],pos[1]])
                        score = self.minimaxSecond(self.board,depth-1,alpha,beta,True)
                        self.board[i][j]= ' '
                        #self.occupied.pop()
                        bestScore = min(score,bestScore)
                        beta = min(beta,bestScore)
                        if(beta<=alpha):
                            break              
            return bestScore
    
    def checkWinner(self):
        #print("in check winner")
        winner = ''
        win = True
        if(self.player == 'D'):
            oppo = 'L'
        else:
            oppo = 'D'
        ai_win = np.array([self.player,self.player,self.player,self.player,self.player])
        human_win = np.array([oppo,oppo,oppo,oppo,oppo])
        for row in self.board:
            checkai = self.findSubarray(row,ai_win)
            if(win in checkai):
                winner = self.player
            checkhuman = self.findSubarray(row,human_win)
            if(win in checkhuman):
                winner = oppo
        for row in self.board.T:
            checkai = self.findSubarray(row,ai_win)
            if(win in checkai):
                winner = self.player
            checkhuman = self.findSubarray(row,human_win)
            if(win in checkhuman):
                winner = oppo
        diag1 = np.array(self.getDiagonal(self.board))
        for i in diag1:
            i = np.array(i)
            check_ai = self.findSubarray(i,ai_win)
            check_human = self.findSubarray(i,human_win)
            if(win in check_ai):
                winner = self.player
            if(win in check_human):
                winner = oppo
        #print("check winner finished")
        empty = ' '
        if (empty not in self.board and winner ==''):
            return 'tie'
        else:
            return winner  

    def evaluate(self,player):
        d2,d3,d4,l2,l3,l4,d5,l5 = 0,0,0,0,0,0,0,0
        SCORE = 0
        diag = self.getDiagonal(self.board)
        diag1=[]
        for i in diag:
            for j in range(len(i)-4):
                diag1.append(i[j:j+5])
        
        for i in range(self.boardSize):
            for j in range(self.boardSize-4):
                x = self.board[i][j:j+5].tolist()
                if(x in da2):
                    d2+=1
                if(x in da3):
                    d3+=1
                if(x in da4):
                    d4+=1
                if(x in li2):
                    l2+=1
                if(x in li3):
                    l3+=1
                if(x in li4):
                    l4+=1
                if(x == Dwin):
                    if(self.player =='D'):
                        return 10000000
                    else:
                        return -10000000
                if(x ==Lwin):
                    if(self.player =='L'):
                        return 10000000
                    else:
                        return -10000000
                
                y = self.board.T[i][j:j+5].tolist()
                if(y in da2):
                    d2+=1
                if(y in da3):
                    d3+=1
                if(y in da4):
                    d4+=1
                if(y in li2):
                    l2+=1
                if(y in li3):
                    l3+=1
                if(y in li4):
                    l4+=1
                if(y == Dwin):
                    if(self.player =='D'):
                        return 10000000
                    else:
                        return -10000000
                if(y ==Lwin):
                    if(self.player =='L'):
                        return 10000000
                    else:
                        return -10000000
                '''
                diag1,diag2 = self.diag(i,j)
                if(diag1 in da2):
                    d2+=1
                if(diag1 in da3):
                    d3+=1
                if(diag1 in da4):
                    d4+=1
                if(diag1 in li2):
                    l2+=1
                if(diag1 in li3):
                    l3+=1
                if(diag1 in li4):
                    l4+=1
                if(diag1 == Dwin):
                    if(self.player =='D'):
                        return 10000000000
                    else:
                        return -10000000000
                if(diag1 ==Lwin):
                    if(self.player =='L'):
                        return 10000000000
                    else:
                        return -10000000000
                if(diag2 in da2):
                    d2+=1
                if(diag2 in da3):
                    d3+=1
                if(diag2 in da4):
                    d4+=1
                if(diag2 in li2):
                    l2+=1
                if(diag2 in li3):
                    l3+=1
                if(diag2 in li4):
                    l4+=1
                if(diag2 == Dwin):
                    if(self.player =='D'):
                        return 10000000000
                    else:
                        return -10000000000
                if(diag2 ==Lwin):
                    if(self.player =='L'):
                        return 10000000000
                    else:
                        return -10000000000
                
                '''
        
        for i in range(len(diag1)):        
            z = diag1[i]
            if(z in da2):
                d2+=1
            if(z in da3):
                d3+=1
            if(z in da4):
                d4+=1
            if(z in li2):
                l2+=1
            if(z in li3):
                l3+=1
            if(z in li4):
                l4+=1
            if(z == Dwin):
                if(self.player =='D'):
                    return 10000000
                else:
                    return -10000000
            if(z ==Lwin):
                if(self.player =='L'):
                    return 10000000
                else:
                    return -10000000
        print(d2,d3,d4,l2,l3,l4)
        if(self.player == 'D'):    
            SCORE = d2*40+d3*1800+d4*100000-l2*800-l3*50000-l4*2000000
        else:
            SCORE = l2*40+l3*1800+l4*100000-d2*800-d3*30000-d4*2000000
        return SCORE

    def findHelperD(self,array,tolist):
        d2 = 0
        d3 = 0
        d4 = 0
        l2 = 0
        l3 = 0
        l4 = 0
        medium = 0
        extreme = 0
        for row in array:
            if(tolist == True):
                r = self.stripArray(row.tolist())
            else:
                r = self.stripArray(row)
            
            if(three4D_1 in r):
                d4+=1
                ind = r.index(three4D_1)
                #del r[ind:min(ind+5,len(r))]
            if(three4D_2 in r):
                d4+=1
                ind = r.index(three4D_2)
                #del r[ind:min(ind+5,len(r))]
            
            if(three4D_3 in r):
                d4 +=1
                ind = r.index(three4D_3)
                #del r[ind:min(ind+5,len(r))]
            
            if(three4D_4 in r):
                d4 +=1
                ind = r.index(three4D_4)
                #del r[ind:min(ind+5,len(r))]
            
            if(three3D_1 in r):
                medium +=1
                d3+=1
                ind = r.index(three3D_1)
                #del r[ind:min(ind+5,len(r))]
            
            if(three3D_2 in r):
                d3+=1
                ind = r.index(three3D_2)
                #del r[ind:min(ind+5,len(r))]
            if(three3D_3 in r):
                ind = r.index(three3D_3)
                #del r[ind:min(ind+5,len(r))]
             
            if(three3D_4 in r):
                d3+=1
                ind = r.index(three3D_4)
                #del r[ind:min(ind+5,len(r))]
            if(three3D_5 in r):
                d3+=1
                ind = r.index(three3D_5)
                #del r[ind:min(ind+5,len(r))]  
            
            if(three3D_6 in r):
                d3+=1
                ind = r.index(three3D_6)
                #del r[ind:min(ind+5,len(r))]  
            if(three3D_7 in r):
                d3+=1
                ind = r.index(three3D_7)
                #del r[ind:min(ind+5,len(r))]
            if(three3D_8 in r):
                d3+=1
                ind = r.index(three3D_8)
                #del r[ind:min(ind+5,len(r))]
            
            if(three2D_1 in r):
                d2+=1
                ind = r.index(three2D_1)
               # del r[ind:min(ind+5,len(r))]
            if(three2D_2 in r):
                d2+=1
                ind = r.index(three2D_2)
                #del r[ind:min(ind+5,len(r))]
            
            if(three2D_3 in r):
                d2+=1
                ind = r.index(three2D_3)
                #del r[ind:min(ind+5,len(r))]
            if(three2D_4 in r):
                d2+=1
                ind = r.index(three2D_4)
                #del r[ind:min(ind+5,len(r))]
            
            if(three2D_5 in r):
                d2+=1
                ind = r.index(three2D_5)
                #del r[ind:min(ind+5,len(r))]
            
            if(extremeD in r):
                extreme +=1
                ind = r.index(extremeD)
                del r[ind:min(ind+5,len(r))]
            

            if(three4L_1 in r):
                l4+=1
                ind = r.index(three4L_1)
                #del r[ind:min(ind+5,len(r))]
      
            if(three4L_2 in r):
                l4+=1
                ind = r.index(three4L_2)
                #del r[ind:min(ind+5,len(r))]
            
            if(three4L_3 in r):
                l4 +=1
                ind = r.index(three4L_3)
                #del r[ind:min(ind+5,len(r))]
            
            if(three4L_4 in r):
                l4 +=1
                ind = r.index(three4L_4)
                #del r[ind:min(ind+5,len(r))]
            
            if(three3L_1 in r):
                medium +=1
                l3+=1
                ind = r.index(three3L_1)
                #del r[ind:min(ind+5,len(r))]
               
            if(three3L_2 in r):
                l3+=1
                ind = r.index(three3L_2)
                #del r[ind:min(ind+5,len(r))]
            if(three3L_3 in r):
                l3+=1
                ind = r.index(three3L_3)
                #del r[ind:min(ind+5,len(r))]
            
            if(three3L_4 in r):
                l3+=1
                ind = r.index(three3L_4)
                #del r[ind:min(ind+5,len(r))]
            if(three3L_5 in r):
                l3+=1
                ind = r.index(three3L_5)
                #del r[ind:min(ind+5,len(r))]  
             
            if(three3L_6 in r):
                l3+=1
                ind = r.index(three3L_6)
                #del r[ind:min(ind+5,len(r))]  
            if(three3L_7 in r):
                l3+=1
                ind = r.index(three3L_7)
                #del r[ind:min(ind+5,len(r))]
            if(three3L_8 in r):
                l3+=1
                ind = r.index(three3L_8)
                #del r[ind:min(ind+5,len(r))]
            
            if(three2L_1 in r):
                l2+=1
                ind = r.index(three2L_1)
                #del r[ind:min(ind+5,len(r))]
            if(three2L_2 in r):
                l2+=1
                ind = r.index(three2L_2)
                #del r[ind:min(ind+5,len(r))]
            
            if(three2L_3 in r):
                l2+=1
                ind = r.index(three2L_3)
                #del r[ind:min(ind+5,len(r))]
            if(three2L_4 in r):
                l2+=1
                ind = r.index(three2L_4)
                #del r[ind:min(ind+5,len(r))]
            
            if(three2L_5 in r):
                l2+=1
                ind = r.index(three2L_5)
                #del r[ind:min(ind+5,len(r))]
            '''
            if(extremeL.tolist() in r):
                extreme +=1
                ind = r.index(extremeL.tolist())
                del r[ind:min(ind+5,len(r))]
            '''
        return d2,d3,d4,l2,l3,l4#,extreme,medium
    
    def findHelperL(self,array,tolist):
        d2 = 0
        d3 = 0
        d4 = 0
        l2 = 0
        l3 = 0
        l4 = 0
        for row in array:
            if(tolist == True):
                r = self.stripArray(row.tolist())
            else:
                r = self.stripArray(row)
            if(three4L_1.tolist() in r):
                l4+=1
                ind = r.index(three4L_1.tolist())
                del r[ind:min(ind+5,len(r))]
      
            if(three4L_2.tolist() in r):
                l4+=1
                ind = r.index(three4L_2.tolist())
                del r[ind:min(ind+5,len(r))]
            '''
            if(three4L_3.tolist() in r):
                l4 +=1
                ind = r.index(three4L_3.tolist())
                del r[ind:min(ind+5,len(r))]
            '''
            if(three4L_4.tolist() in r):
                l4 +=1
                ind = r.index(three4L_4.tolist())
                del r[ind:min(ind+5,len(r))]
            
            if(three3L_1.tolist() in r):
                
                l3+=1
                ind = r.index(three3L_1.tolist())
                del r[ind:min(ind+5,len(r))]
               
            if(three3L_2.tolist() in r):
                l3+=1
                ind = r.index(three3L_2.tolist())
                del r[ind:min(ind+5,len(r))]
            if(three3L_3.tolist() in r):
                l3+=1
                ind = r.index(three3L_3.tolist())
                del r[ind:min(ind+5,len(r))]
            
            if(three3L_4.tolist() in r):
                l3+=1
                ind = r.index(three3L_4.tolist())
                del r[ind:min(ind+5,len(r))]
            if(three3L_5.tolist() in r):
                l3+=1
                ind = r.index(three3L_5.tolist())
                del r[ind:min(ind+5,len(r))]  
            '''  
            if(three3L_6.tolist() in r):
                l3+=1
                ind = r.index(three3L_6.tolist())
                del r[ind:min(ind+5,len(r))]  
            if(three3L_7.tolist() in r):
                l3+=1
                ind = r.index(three3L_7.tolist())
                del r[ind:min(ind+5,len(r))]
            if(three3L_8.tolist() in r):
                l3+=1
                ind = r.index(three3L_8.tolist())
                del r[ind:min(ind+5,len(r))]
            '''
            if(three2L_1.tolist() in r):
                l2+=1
                ind = r.index(three2L_1.tolist())
                del r[ind:min(ind+5,len(r))]
            
           
            if(three2L_3.tolist() in r):
                l2+=1
                ind = r.index(three2L_3.tolist())
                del r[ind:min(ind+5,len(r))]
            
            
            if(three2L_5.tolist() in r):
                l2+=1
                ind = r.index(three2L_5.tolist())
                del r[ind:min(ind+5,len(r))]
            '''
            if(extremeL.tolist() in r):
                extreme +=1
                ind = r.index(extremeL.tolist())
                del r[ind:min(ind+5,len(r))]
            '''
        return l2,l3,l4
    '''
    def getPosLines(self,arr,j):
        res = []
        x = self.rolling_window(arr,5).tolist()
        res= x[slice(max(0,j-4),min(j,len(arr)-5)+1)]
        return res

    def getIndexLines(self,i,j):
        horizontal = self.getPosLines(self.board[i],j)
        vertical = self.getPosLines(self.board.T[j],i)
        majorDiag = np.diagonal(self.board,offset=(j-i))
        minorDiag = np.diagonal(np.rot90(self.board),offset=-self.boardSize+(j+i)+1)
        #print(majorDiag)
        minor, major = [],[]
        if(len(majorDiag)>=5):
            major = self.getPosLines(majorDiag,min(i,j))
        if(len(minorDiag)>=5):
            minor = self.getPosLines(minorDiag,min(i,j))
        #print('minor',minor)
        total = horizontal+vertical+minor+major
        return total

    def evalX(self,i,j):
        SCORE = 0
        lines = self.getIndexLines(i,j)
        print(lines)
        d2 = lines.count(three2D_1)+lines.count(three2D_2)+lines.count(three2D_3)+lines.count(three2D_4)+lines.count(three2D_5)
        d3 = lines.count(three3D_1)+lines.count(three3D_2)+lines.count(three3D_3)+lines.count(three3D_7)
        d4 = lines.count(three4D_1)+lines.count(three4D_2)+lines.count(three4D_3)
        l2 = lines.count(three2L_2)
        l3 = lines.count(three3L_1)+lines.count(three3L_2)+lines.count(three3L_3)+lines.count(three3L_7)
        l4 = lines.count(three4L_1)+lines.count(three4L_2)+lines.count(three4L_3)
        if(self.player == 'D'):    
            SCORE = d2*40+d3*1800+d4*50000-l2*500-l3*30000-l4*1000000
        else:
            SCORE = l2*40+l3*1800+l4*50000-d2*500-d3*30000-d4*1000000
        print(d2,d3,d4,l2,l3,l4)
        return SCORE
    '''
    
    def diag(self,i,j):
        diag1,diag2 = [],[]
        if(j+5<=self.boardSize and i+5<=self.boardSize):
            temp = []
            temp.append(self.board[i,j])
            temp.append(self.board[i+1,j+1])
            temp.append(self.board[i+2,j+2])
            temp.append(self.board[i+3,j+3])
            temp.append(self.board[i+4,j+4])
            diag1.append(temp)
        if(j-4>=0 and i+5<=self.boardSize):
            temp = []
            temp.append(self.board[i,j])
            temp.append(self.board[i+1,j-1])
            temp.append(self.board[i+2,j-2])
            temp.append(self.board[i+3,j-3])
            temp.append(self.board[i+4,j-4])
            diag2.append(temp)

        #print(diag)
        return diag1,diag2
    
    # HELPER FUNCTION
    def stripArray(self,array):
        a = []
        for i in range(len(array)-4):
            a.append(array[i:i+5])
        return a
    def findSubarray(self,axis,subarray):
        x = np.all(self.rolling_window(axis,len(subarray))==subarray,axis=1)
        return x
    def rolling_window(self,a, size):
        shape = a.shape[:-1] + (a.shape[-1] - size + 1, size)
        strides = a.strides + (a. strides[-1],)
        return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)
    def getDiagonal(self,array):
        diags = [array[::-1,:].diagonal(i) for i in range(-array.shape[0]+1,array.shape[1])]
        diags.extend(array.diagonal(i) for i in range(array.shape[1]-1,-array.shape[0],-1))
        diag = [n.tolist() for n in diags if len(n)>=5]
        return diag
    def getCandidates(self,array):
        candidates = []
        res = []
        final = []
        for occupied in array:
            x = occupied[0]
            y = occupied[1]
            for i in range(x,x+3):
                for j in range(y,y+3):
                    candidates.append([i-1,j-1])
        res = [i for n, i in enumerate(candidates) if (i not in candidates[:n])]
        for i in res:
            if(i[0]>=0 and i[1]>=0 and i[0]<=self.boardSize-1 and i[0]<=self.boardSize-1 and i[1]<=self.boardSize-1):
                if(i not in array):
                    final.append(i)
        return final


def main():
    g = game()
    player = g.player
    #If AI moves first
    if(player=='D'):
        g.bestMove()
        while(g.checkWinner()==''):
            var = input('input\n')
            if(g.board[string.ascii_letters.index(var[0])][int(var[1:])-1]==' '):
                g.board[string.ascii_letters.index(var[0])][int(var[1:])-1]='L'
                #g.available.remove([string.ascii_letters.index(var[0]),int(var[1:])-1])
                #g.availableCopy == g.available
                g.occupied.append([string.ascii_letters.index(var[0]),int(var[1:])-1])
                print("Move played:",var)
                g.player='D'
                if(g.checkWinner()!=''):
                    break
                else:
                    x = time.time()
                    g.bestMove()
                    print("--%--",time.time()-x)    
    else:
        while(g.checkWinner()==''):
            print(g.placeable)
            var = input('input\n')
            if(g.board[string.ascii_letters.index(var[0])][int(var[1:])-1]==' '):
                g.board[string.ascii_letters.index(var[0])][int(var[1:])-1]='D'
                #g.available.remove([string.ascii_letters.index(var[0]),int(var[1:])-1])
                #g.availableCopy == g.available
                g.occupied.append([string.ascii_letters.index(var[0]),int(var[1:])-1])
                print("Move played:",var)
                g.player='L'
                if(g.checkWinner()!=''):
                    break
                else:
                    g.bestMove()
    print(g.checkWinner())
if __name__=="__main__":
    main()
   
