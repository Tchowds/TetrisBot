from board import Board, Direction, Rotation, Action, Shape
from random import Random
from math import sqrt


class Player:
    def choose_action(self, board):
        raise NotImplementedError


class RandomPlayer(Player):
    def __init__(self, seed=None):
        self.random = Random(seed)
        self.current_row = 23

    def blocks_under(self, board, highest):
        for x,y in board.cells:
            highest[x][1] += 1

        score = 0
        for a, b in highest:
            score += 24-b
        
        print(score)
        return (-score)

    def score_position(self, board):
        miny = 24

        for x,y in board.cells:
            if y < miny:
                miny = y
        return miny

        

    def check_current_row(self, board):
        for x,y in board.cells:
            if y < self.current_row:
                self.current_row = y 


    def score_v2(self,board):
        score = 0
        highest_blocks = [[0,24],[1,24],[2,24],[3,24],[4,24],[5,24],[6,24],[7,24],[8,24],[9,24]]
        #print("---------------------")
        #print(board.cells)
        for x,y in board.cells:
            # for i in range(0,10):
            #     if x == highest_blocks[i][0] and y < highest_blocks[i][1]:
            #         highest_blocks[i][1] = y
            score += y
        #score += self.blocks_under(board, highest_blocks)
        return score

    




    def lines_complete(self,board):
        sub_score = 0
        board_cells = []
        for i in range(0,24):
            board_cells.append(0)
        for x,y in board.cells:
            for i in range(0,24):
                if y == i:
                    board_cells[i] += 1
        for cell in board_cells:
            if cell > 9:
                sub_score += 1
        print(sub_score)
        return (sub_score * 5) * (sub_score * 5)


    def aggregate_height(self,board, highest):
        sub_score = 0
        for cell in highest:
            sub_score += cell[1]
        #print(sub_score)
        return sub_score
    
    def bumpiness(self,board,highest):
        sub_score = 0
        for i in range(0,9):
            difference = highest[i][1] - highest[i+1][1]
            sub_score += -sqrt((difference * difference))
        return 0.2 * sub_score

    #def holes(self,board):
        
    





    def score_version_3(self,board):
        score = 0
        highest_blocks = [[0,24],[1,24],[2,24],[3,24],[4,24],[5,24],[6,24],[7,24],[8,24],[9,24]]
        for x,y in board.cells:
            for i in range(0,10):
                if x == highest_blocks[i][0] and y < highest_blocks[i][1]:
                    highest_blocks[i][1] = y
        #return self.aggregate_height(board, highest_blocks)
        return self.aggregate_height(board, highest_blocks) + self.bumpiness(board, highest_blocks)
    
        

    
    
    
    
    
    
    
    #Highe score = 11663 seed = 42
    #High score = 12788 seed = 52
    #score = 11769 seed = 60
    #11441 seed = 70
    #11703  seed = 80
    #14758 seed = 90
    #12137 seed = 100
    #12173 seed = 110
    #11877 seed = 120
    #15006 seed = 130
    #10484 seed = 140 LOST
    #12066 SEED = 150
    #9969 SEED = 160 LOST

    # To check how many lines have been eliminated
    #Count the difference in blocks on the field
    #If length of blocks = 0
    
    def version1(self,board):
        xpos = board.falling.left
        bestscore = 0
        bestmoves = []

        
        for i in range(0,4):
            #print("rotat")
            for x in range(0,10):
                sandbox = board.clone()
                xpos = sandbox.falling.left
                moves = []
                landed = False
                rot_count = i

                while rot_count>0:
                    sandbox.rotate(Rotation.Clockwise)
                    moves.append(Rotation.Clockwise)
                    rot_count -= 1
                    if sandbox.falling is not None:
                        xpos = sandbox.falling.left
                    else:
                        landed = True
                        break
                while xpos>x and landed == False:
                    sandbox.move(Direction.Left)
                    moves.append(Direction.Left)
                    if sandbox.falling is not None:
                        xpos = sandbox.falling.left
                    else:
                        landed = True
                        break     
                while xpos < x and landed == False:
                    sandbox.move(Direction.Right)
                    moves.append(Direction.Right)
                    if sandbox.falling is not None:
                        xpos = sandbox.falling.right
                    else:
                        landed = True
                        break                   
                if landed == False:

                    moves.append(Direction.Drop) 
                    sandbox.move(Direction.Drop)
            
                
                #score = self.score_position(sandbox)
                #score = self.score_v2(sandbox)
                score = self.score_version_3(sandbox)

                if score > bestscore:
                    bestscore = score 
                    bestmoves = moves
                    #print(sandbox.cells)

        #print("BestScore:", bestscore)
        return 1, bestmoves



    #Bottom row has y coordinate of 23, top row has y coordinate of 0
    #Most right column has x coordinate of 9, most left column has x coordinate of 0
    def choose_action(self, board):
        highest_layer = 1
        
        highest_layer, bestmoves = self.version1(board)
        return bestmoves
 
 
SelectedPlayer = RandomPlayer

