#A basic Sudoku solver, created by PK22
#Uses logic to get as close to a solution as possible, then uses trial and error to complete the puzzle.
#Capable of solving almost any Sudoku (based on the fact that it can consistently solve a 17-clue puzzle in a fraction of a second).

#Importing modules
import random #Used to select a random square when performing trial and error.
import time   #Used to determine the program's total runtime.
import copy   #Used when saving a copy of the grid.
starttime = time.time()
try:
    f = open('infile.txt', 'r')
    f.close()
except:
    print('You need to put your puzzle in infile.txt, otherwise the program cannot find it!')
#Creating the grid as a list of dictionaries.
#ID represents the square's index in the list.
#Value represents the square's number. If it is not filled in, it is represented by 0.
#Row represents what row a square is in (0 is the top row, 8 is the bottom row).
#Column represents what column a square is in (0 is the left column, 8 is the right column).
#Square represents what 3x3 square a square is in (0 being top left, 2 being top right, 4 being middle, 8 being bottom right).
#Possibilities is a list of all possible values a square could be. 
squares = [{'ID':0,'Value':0,'Row':0,'Column':0,'Square3x3':0,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':1,'Value':0,'Row':0,'Column':1,'Square3x3':0,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':2,'Value':0,'Row':0,'Column':2,'Square3x3':0,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':3,'Value':0,'Row':0,'Column':3,'Square3x3':1,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':4,'Value':0,'Row':0,'Column':4,'Square3x3':1,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':5,'Value':0,'Row':0,'Column':5,'Square3x3':1,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':6,'Value':0,'Row':0,'Column':6,'Square3x3':2,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':7,'Value':0,'Row':0,'Column':7,'Square3x3':2,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':8,'Value':0,'Row':0,'Column':8,'Square3x3':2,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':9,'Value':0,'Row':1,'Column':0,'Square3x3':0,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':10,'Value':0,'Row':1,'Column':1,'Square3x3':0,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':11,'Value':0,'Row':1,'Column':2,'Square3x3':0,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':12,'Value':0,'Row':1,'Column':3,'Square3x3':1,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':13,'Value':0,'Row':1,'Column':4,'Square3x3':1,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':14,'Value':0,'Row':1,'Column':5,'Square3x3':1,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':15,'Value':0,'Row':1,'Column':6,'Square3x3':2,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':16,'Value':0,'Row':1,'Column':7,'Square3x3':2,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':17,'Value':0,'Row':1,'Column':8,'Square3x3':2,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':18,'Value':0,'Row':2,'Column':0,'Square3x3':0,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':19,'Value':0,'Row':2,'Column':1,'Square3x3':0,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':20,'Value':0,'Row':2,'Column':2,'Square3x3':0,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':21,'Value':0,'Row':2,'Column':3,'Square3x3':1,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':22,'Value':0,'Row':2,'Column':4,'Square3x3':1,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':23,'Value':0,'Row':2,'Column':5,'Square3x3':1,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':24,'Value':0,'Row':2,'Column':6,'Square3x3':2,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':25,'Value':0,'Row':2,'Column':7,'Square3x3':2,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':26,'Value':0,'Row':2,'Column':8,'Square3x3':2,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':27,'Value':0,'Row':3,'Column':0,'Square3x3':3,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':28,'Value':0,'Row':3,'Column':1,'Square3x3':3,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':29,'Value':0,'Row':3,'Column':2,'Square3x3':3,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':30,'Value':0,'Row':3,'Column':3,'Square3x3':4,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':31,'Value':0,'Row':3,'Column':4,'Square3x3':4,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':32,'Value':0,'Row':3,'Column':5,'Square3x3':4,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':33,'Value':0,'Row':3,'Column':6,'Square3x3':5,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':34,'Value':0,'Row':3,'Column':7,'Square3x3':5,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':35,'Value':0,'Row':3,'Column':8,'Square3x3':5,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':36,'Value':0,'Row':4,'Column':0,'Square3x3':3,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':37,'Value':0,'Row':4,'Column':1,'Square3x3':3,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':38,'Value':0,'Row':4,'Column':2,'Square3x3':3,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':39,'Value':0,'Row':4,'Column':3,'Square3x3':4,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':40,'Value':0,'Row':4,'Column':4,'Square3x3':4,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':41,'Value':0,'Row':4,'Column':5,'Square3x3':4,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':42,'Value':0,'Row':4,'Column':6,'Square3x3':5,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':43,'Value':0,'Row':4,'Column':7,'Square3x3':5,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':44,'Value':0,'Row':4,'Column':8,'Square3x3':5,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':45,'Value':0,'Row':5,'Column':0,'Square3x3':3,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':46,'Value':0,'Row':5,'Column':1,'Square3x3':3,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':47,'Value':0,'Row':5,'Column':2,'Square3x3':3,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':48,'Value':0,'Row':5,'Column':3,'Square3x3':4,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':49,'Value':0,'Row':5,'Column':4,'Square3x3':4,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':50,'Value':0,'Row':5,'Column':5,'Square3x3':4,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':51,'Value':0,'Row':5,'Column':6,'Square3x3':5,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':52,'Value':0,'Row':5,'Column':7,'Square3x3':5,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':53,'Value':0,'Row':5,'Column':8,'Square3x3':5,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':54,'Value':0,'Row':6,'Column':0,'Square3x3':6,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':55,'Value':0,'Row':6,'Column':1,'Square3x3':6,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':56,'Value':0,'Row':6,'Column':2,'Square3x3':6,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':57,'Value':0,'Row':6,'Column':3,'Square3x3':7,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':58,'Value':0,'Row':6,'Column':4,'Square3x3':7,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':59,'Value':0,'Row':6,'Column':5,'Square3x3':7,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':60,'Value':0,'Row':6,'Column':6,'Square3x3':8,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':61,'Value':0,'Row':6,'Column':7,'Square3x3':8,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':62,'Value':0,'Row':6,'Column':8,'Square3x3':8,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':63,'Value':0,'Row':7,'Column':0,'Square3x3':6,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':64,'Value':0,'Row':7,'Column':1,'Square3x3':6,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':65,'Value':0,'Row':7,'Column':2,'Square3x3':6,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':66,'Value':0,'Row':7,'Column':3,'Square3x3':7,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':67,'Value':0,'Row':7,'Column':4,'Square3x3':7,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':68,'Value':0,'Row':7,'Column':5,'Square3x3':7,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':69,'Value':0,'Row':7,'Column':6,'Square3x3':8,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':70,'Value':0,'Row':7,'Column':7,'Square3x3':8,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':71,'Value':0,'Row':7,'Column':8,'Square3x3':8,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':72,'Value':0,'Row':8,'Column':0,'Square3x3':6,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':73,'Value':0,'Row':8,'Column':1,'Square3x3':6,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':74,'Value':0,'Row':8,'Column':2,'Square3x3':6,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':75,'Value':0,'Row':8,'Column':3,'Square3x3':7,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':76,'Value':0,'Row':8,'Column':4,'Square3x3':7,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':77,'Value':0,'Row':8,'Column':5,'Square3x3':7,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':78,'Value':0,'Row':8,'Column':6,'Square3x3':8,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':79,'Value':0,'Row':8,'Column':7,'Square3x3':8,'Possibilities':[1,2,3,4,5,6,7,8,9]}, {'ID':80,'Value':0,'Row':8,'Column':8,'Square3x3':8,'Possibilities':[1,2,3,4,5,6,7,8,9]}]
def printgrid():
    #A function to print the 9x9 sudoku grid as nine rows of numbers.
    grid = ''
    for x in range(9):
        for y in range(9):
            grid = grid + str(squares[9*x+y]['Value'])
        grid = grid + '\n'
    print(grid)
def getblankcount():
    #This counts the number of zeroes, which represent blank spaces.
    #If it returns 0, then the grid is complete.
    zerocount = 0
    for x in squares:
        if x['Value'] == 0:
            zerocount = zerocount + 1
    return zerocount

def readfile():
    #The sudoku grid is stored in infile.txt, this function reads the grid and updates it with the given information.
    global squares
    f = open('infile.txt', 'r')
    grid = f.read().replace('\n', '').replace(' ', '')
    f.close()
    for x in range(81):
        if grid[x] != '0':
            squares[x]['Value'] = int(grid[x])
            squares[x]['Possibilities'] = [int(grid[x])]
    print('File read!')

#Functions to return the IDs/indexes of all squares in a given row, column, or 3x3 square.
def getrow(num):
    return [num*9, num*9+1, num*9+2, num*9+3, num*9+4, num*9+5, num*9+6, num*9+7, num*9+8]
def getcolumn(num):
    return [num, num+9, num+18, num+27, num+36, num+45, num+54, num+63, num+72]
def getsquare(num):
    square1 = 27 * (num//3) + 3 * (num%3)
    return [square1, square1+1, square1+2, square1+9, square1+10, square1+11, square1+18, square1+19, square1+20]
readfile()
if getblankcount() > 64:
    print('This puzzle is unsolvable - at least 17 clues are required.')
    print('Your puzzle only features '+str(81-getblankcount())+' clues.')
    time.sleep(10)
    exit()
printgrid()
def updategrid():
    #This is a function which fills in the values of all squares with only one possibility.
    global squares
    for x in squares:
        if x['Value'] == 0 and len(x['Possibilities']) == 1:
            squares[x['ID']]['Value'] = x['Possibilities'][0]
    
def firstlevellogic():
    #One of the main logical processors. It removes the values of squares in the same row, column, or 3x3 square from a square's possibilities.
    #Since this is simply application of the basic rules of Sudoku, it is only 'first level'.
    global squares
    for x in squares:
        if x['Value'] == 0:
            samerow = getrow(x['Row'])
            samecolumn = getcolumn(x['Column'])
            samesquare = getsquare(x['Square3x3'])
            for y in samerow:
                if squares[y]['Value'] in x['Possibilities']:
                    newpossibilities = x['Possibilities'].copy()
                    newpossibilities.remove(squares[y]['Value'])
                    squares[squares.index(x)]['Possibilities'] = newpossibilities
            for y in samecolumn:
                if squares[y]['Value'] in x['Possibilities']:
                    newpossibilities = x['Possibilities'].copy()
                    newpossibilities.remove(squares[y]['Value'])
                    squares[squares.index(x)]['Possibilities'] = newpossibilities
            for y in samesquare:
                if squares[y]['Value'] in x['Possibilities']:
                    newpossibilities = x['Possibilities'].copy()
                    newpossibilities.remove(squares[y]['Value'])
                    squares[squares.index(x)]['Possibilities'] = newpossibilities
def secondlevellogic():
    #A slightly more advanced logical processor. It takes advantage of the fact that each number appears once in each row, column, and 3x3 square.
    #For each row, column, and 3x3 square, it creates a list of the possible positions (as ID numbers) for each number.
    global squares
    numbernames = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    for r in range(9):
        rowids = getrow(r)
        possiblepositions = {'One':[],'Two':[],'Three':[],'Four':[],'Five':[],'Six':[],'Seven':[],'Eight':[],'Nine':[]}
        for x in rowids:
            workingsquare = squares[x]
            for y in workingsquare['Possibilities']:
                possiblepositions[numbernames[y]] = possiblepositions[numbernames[y]] + [x]
        for x in possiblepositions:
            if len(possiblepositions[x]) == 1:
                if squares[possiblepositions[x][0]]['Value'] == 0:
                    squares[possiblepositions[x][0]]['Value'] = numbernames.index(x)
                    squares[possiblepositions[x][0]]['Possibilities'] = [numbernames.index(x)]
    for r in range(9):
        rowids = getcolumn(r)
        possiblepositions = {'One':[],'Two':[],'Three':[],'Four':[],'Five':[],'Six':[],'Seven':[],'Eight':[],'Nine':[]}
        for x in rowids:
            workingsquare = squares[x]
            for y in workingsquare['Possibilities']:
                possiblepositions[numbernames[y]] = possiblepositions[numbernames[y]] + [x]
        for x in possiblepositions:
            if len(possiblepositions[x]) == 1:
                if squares[possiblepositions[x][0]]['Value'] == 0:
                    squares[possiblepositions[x][0]]['Value'] = numbernames.index(x)
                    squares[possiblepositions[x][0]]['Possibilities'] = [numbernames.index(x)]
    for r in range(9):
        rowids = getsquare(r)
        possiblepositions = {'One':[],'Two':[],'Three':[],'Four':[],'Five':[],'Six':[],'Seven':[],'Eight':[],'Nine':[]}
        for x in rowids:
            workingsquare = squares[x]
            for y in workingsquare['Possibilities']:
                possiblepositions[numbernames[y]] = possiblepositions[numbernames[y]] + [x]
        for x in possiblepositions:
            if len(possiblepositions[x]) == 1:
                if squares[possiblepositions[x][0]]['Value'] == 0:
                    squares[possiblepositions[x][0]]['Value'] = numbernames.index(x)
                    squares[possiblepositions[x][0]]['Possibilities'] = [numbernames.index(x)]
def contradictionexists():
    #Since trial and error is necessary in some cases, we need to determine if a grid is currently solvable.
    contradictory = False
    for x in squares:
        if len(x['Possibilities']) == 0:
            #If there are no possible values that can complete a square, we know we have gone wrong.
            contradictory = True
            break
    if not contradictory:
        #Checking to see if a number appears more than once in a row, column, or 3x3 square.
        for r in range(9):
            rowids = getrow(r)
            columnids = getcolumn(r)
            squareids = getsquare(r)
            rowcontents = []
            columncontents = []
            squarecontents = []
            for x in rowids:
                rowcontents.append(squares[x]['Value'])
            for x in columnids:
                columncontents.append(squares[x]['Value'])
            for x in squareids:
                squarecontents.append(squares[x]['Value'])
            for x in range(1, 10):
                if rowcontents.count(x) > 1 or columncontents.count(x) > 1 or squarecontents.count(x) > 1:
                    contradictory = True
                    break
    return contradictory
iterations = 0
savedgrid = copy.deepcopy(squares)
previousblankcount = 100
saved = False
#The main loop is below:
while (getblankcount() != 0 or contradictionexists()):
    #Keep track of progress:
    previousblankcount = getblankcount()
    iterations = iterations + 1
    #Run logical processing:
    firstlevellogic()
    updategrid()
    secondlevellogic()
    #Check for any contradictions in the grid, and load the last save if any are found:
    if contradictionexists():
        squares = copy.deepcopy(savedgrid)
    #This if statement controls trial and error, which is necessary for the hardest of puzzles:
    if previousblankcount == getblankcount():
        #If there has been no change after an iteration, there will be no change with subsequent iterations.
        #Thus, we need to use trial and error.
        if not saved:
            #A saved copy of the grid is created once at the start of the program and once when trial and error are deemed necessary.
            #The saved copy is guaranteed to have no contradictions (provided the puzzle is solvable).
            saved = True
            savedgrid = copy.deepcopy(squares)
        chosen = False
        chosensquare = random.choice(squares)
        while (not chosen) or (chosensquare['Value'] != 0):
            chosen = True
            #This selects a random square which has not yet been assigned a value.
            chosensquare = random.choice(squares)
        #We then choose a random number from the square's possible values, and assign it that.
        chosenvalue = random.choice(chosensquare['Possibilities'])
        squares[chosensquare['ID']]['Value'] = chosenvalue
        squares[chosensquare['ID']]['Possibilities'] = [chosenvalue]
            
        
timetaken = round(time.time() - starttime, 4)
print('Succeeded in '+str(iterations)+' iterations and '+str(timetaken)+' seconds.')
if saved:
    print('Trial and error had to be used.')
else:
    print('Solved without trial and error!')
printgrid()
