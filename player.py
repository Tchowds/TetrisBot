from board import Board, Direction, Rotation, Action, Shape
from random import Random
from math import sqrt


class Player:
    def choose_action(self, board):
        raise NotImplementedError


class RandomPlayer(Player):
    def __init__(self, seed=None):
        self.random = Random(seed)


    def lines_complete(self,board, cells):
        if cells-len(board.cells) >= 36:
            return 4
        elif cells -len(board.cells) >= 26:
            return 3
        elif cells -len(board.cells) >= 16:
            return -2
        elif cells -len(board.cells) >= 6:
            return -1
        else:
            return 0


    def aggregate_height(self,board, highest):
        sub_score = 0
        for cell in highest:
            sub_score += cell[1]
        return sub_score
    
    def aggregate_height_v2(self,board, highest):
        sub_score = 0
        for cell in highest:
            sub_score += 24 -  cell[1]
        return sub_score
        
    
    def bumpiness(self,board,highest):
        sub_score = 0
        for i in range(0,9):
            difference = highest[i][1] - highest[i+1][1]
            sub_score += sqrt((difference * difference))
        return  sub_score

    def holes(self,board, highest):
        sub_score = 0
        for x,y in board.cells:
            highest[x][1] += 1
        for a,b in highest:
            sub_score += 24 - b
        return sub_score 

    #seed = 130 hscore = 31411

    def score_version_3(self,board,cells):
        highest_blocks = [[0,24],[1,24],[2,24],[3,24],[4,24],[5,24],[6,24],[7,24],[8,24],[9,24]]
        for x,y in board.cells:
            for i in range(0,10):
                if x == highest_blocks[i][0] and y < highest_blocks[i][1]:
                    highest_blocks[i][1] = y
        #
        return (1.2 * self.aggregate_height(board, highest_blocks)) - (0.2 * self.bumpiness(board, highest_blocks)) + (12.3 * self.lines_complete(board, cells)) - (0.3 * self.holes(board, highest_blocks))
        #return (-0.5 * self.aggregate_height_v2(board, highest_blocks)) - (0.2 * self.bumpiness(board, highest_blocks)) + (4.95 * self.lines_complete(board, cells)) - (0.2 * self.holes(board, highest_blocks))

            
    def version1(self,board):
        xpos = board.falling.left
        bestscore = -999999
        bestmoves = []
        sandbox = board.clone()
        prev_cells = len(sandbox.cells)
        for i in range(0,4):

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
            

                score = self.score_version_3(sandbox, prev_cells)


                if score > bestscore:
                    bestscore = score 
                    bestmoves = moves

        #print("BestScore:", bestscore)
        return bestmoves



    def choose_action(self, board):

        
        bestmoves = self.version1(board)
        return bestmoves
 
 
SelectedPlayer = RandomPlayer

