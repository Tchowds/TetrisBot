       
        '''
        xpos = board.falling.left
        bestscore = 0
        bestmoves = []
        for x in range(0,10):
            sandbox = board.clone()
            xpos = sandbox.falling.left
            moves = []
            landed = False
            while xpos>x:
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
                    xpos = sandbox.falling.left 
                else:
                    landed = True
                    break                   
            if landed == False:

            #print(sandbox.falling.left) 
                moves.append(Direction.Drop) 
                sandbox.move(Direction.Drop)

            score = self.score_position(sandbox)

            if score > bestscore:
                bestscore = score 
                bestmoves = moves

        return bestmoves
        #assert(False)
        '''
            
        '''
        if self.random.random() > 0.97:
            # 3% chance we'll discard or drop a bomb
            return self.random.choice([
                Action.Discard,
                Action.Bomb,
            ])
        else:
            # 97% chance we'll make a normal move
            return self.random.choice([
                Direction.Left,
                Direction.Right,
                Direction.Down,
                Rotation.Anticlockwise,
                Rotation.Clockwise,
            ]);;
        '''

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

    
    
    
    
    
    
    
    
    def score_position(self, board):
        miny = 24
        for x,y in board.cells:
            if y < miny:
                miny = y 
        return miny

    def based_on_height(self,board):
        
        xpos = board.falling.left
        bestscore = 0
        bestmoves = []
        for x in range(0,10):
            sandbox = board.clone()
            xpos = sandbox.falling.left
            moves = []
            landed = False
            while xpos>x:
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
                    xpos = sandbox.falling.left 
                else:
                    landed = True
                    break                   
            if landed == False:

            #print(sandbox.falling.left) 
                moves.append(Direction.Drop) 
                sandbox.move(Direction.Drop)

            score = self.score_position(sandbox)

            if score > bestscore:
                bestscore = score 
                bestmoves = moves

        return bestmoves




