# To do: Implement Minimax algorithm for AI
class Board():
    def __init__(self, dimension):
        self.listOfCells = [ ];
        self.boardString = '';
        self.dim = dimension;
        for y in range(1, dimension + 1):
            for x in range(1, dimension + 1):
                c = Cell(x, y);
                self.listOfCells.append(c);
                
    def showBoard(self):
        self.boardString = '\n';
        for i in range(1, self.dim + 1):
            self.boardString += '   ' + str(i) + ' ';
        self.boardString += '\n1';
        for q in range(len(self.listOfCells)):
            if((q != 0) and (q % self.dim == 0)):
               self.boardString += ('\n' + str((q + self.dim) / self.dim));
            self.boardString += str(self.listOfCells[q].status);
            
        print self.boardString;

    def checkConditions(self, listOfCells, cross, dimensions):
        # Check winning conditions
        
        # Check rows
        xCountR = oCountR = xCountC = oCountC = 0;
        for i in range(len(self.listOfCells)):
            
            if(i % dimensions == 0):
                xCountR = oCountR = 0;

            if(listOfCells[i].status == "['X']"):
                xCountR += 1;
            elif(listOfCells[i].status == "['O']"):
                oCountR += 1;

            if(xCountR == dimensions):
                return 2;
            elif(oCountR == dimensions):
                return 3;

        # Check columns        
        for x in range(dimensions):
            for y in range(dimensions):                 
                # Translate x,y into int pos in array
                pos = ( (x - 1) + ((y - 2) * dimensions));
                        
                if(listOfCells[pos].status == "['X']"):
                        xCountC += 1;
                elif(listOfCells[pos].status == "['O']"):
                        oCountC += 1;
                if(xCountC == dimensions):
                    return 2;
                elif(oCountC == dimensions):
                    return 3;
                        
            xCountC = oCountC = 0;


        # Check diagonals UL -> DR
        xCountD = oCountD = 0;
        for i in range(dimensions):
            # Translate x,y into int pos in array
            pos = ( i * (1 + dimensions) );

            if(listOfCells[pos].status == "['X']"):
                    xCountC += 1;
            elif(listOfCells[pos].status == "['O']"):
                    oCountC += 1;
            # print(self.listOfCells[pos].status);
            if(xCountC == dimensions):
                return 2;
            elif(oCountC == dimensions):
                return 3;

        # Check diagonals DL -> UR
        xCountD = oCountD = 0;
        for i in range(dimensions):
            # Translate x,y into int pos in array
            pos = i + dimensions * (dimensions - i - 1);
            # print xCountD
            if(listOfCells[pos].status == "['X']"):
                    xCountD += 1;
                    # print xCountD
            elif(listOfCells[pos].status == "['O']"):
                    oCountD += 1;

            # print(self.listOfCells[pos].status);
            
            if(xCountD == dimensions):
                return 2;
            elif(oCountD == dimensions):
                return 3;


    def updateBoard(self, xy, cross):
        myXstr = '';
        myXint = 0;
        myYstr = '';
        myYint = 0;
        firstPart = True;
        for a in xy:
            if(a == ','):
                firstPart = False;
            if(firstPart):
                myXstr += a;
            else:
                myYstr += a;

        myYint = int(myYstr.translate(None, ", "));
        myXint = int(myXstr);

        # Place new thing
        for i in range(len(self.listOfCells)):
            if( (self.listOfCells[i].xp == myXint) and (self.listOfCells[i].yp == myYint)):
                # Check if cell is empty
                if(self.listOfCells[i].status != [' ']):
                    return 1;
                else:
                    # Place mark
                    if(cross):
                        self.listOfCells[i].status = "['X']";
                    else:
                        self.listOfCells[i].status = "['O']";

        self.showBoard();

        return self.checkConditions(self.listOfCells, cross, self.dim);
        
class Cell(Board):
    def __init__(self, xpos, ypos):
        self.xp = xpos;
        self.yp = ypos;
        self.status = [' '];
        
def playTicTacToe():
    running = True;

    size = int(raw_input("Enter size of the board: "));
    
    b = Board(size);

    b.showBoard();

    cross = True;

    steps = 0;
    
    while running:

        if(steps == size * size):
            print("It's a draw! Restarting..");
            playTicTacToe();
        
        inpurt = list(raw_input("Input x,y -> "));

        result = b.updateBoard(inpurt, cross);

        if(result == 1):
            print("Error: Position already taken.");
        elif(result == 2):
            print("X's win! Restarting..");
            playTicTacToe();
        elif(result == 3):
            print("O's win! Restarting..");
            playTicTacToe();
        else:
            if(cross):
                cross = False;
            else:
                cross = True;

        steps += 1;

playTicTacToe();

def getRandomNumber():
    return 4;  # Yup

