import pygame
import random 

SCALE = 600
Grid = SCALE/12
pygame.init()
WIDTH = SCALE
HEIGHT = SCALE
screen = pygame.display.set_mode([WIDTH,HEIGHT])

character_img = pygame.image.load("player.png")
CHARACTER_SIZE = (Grid,Grid)
character_img = pygame.transform.scale(character_img, CHARACTER_SIZE)

background = pygame.image.load("grass.png")
GRASS_SIZE = (Grid,Grid)
background = pygame.transform.scale(background, GRASS_SIZE)

holeOver = pygame.image.load("hole.png")
HOLE_SIZE = (Grid,Grid)
holeOver = pygame.transform.scale(holeOver, HOLE_SIZE)

chest = pygame.image.load("chest.png")
CHEST_SIZE = (Grid,Grid)
chest = pygame.transform.scale(chest, CHEST_SIZE)

water = pygame.image.load("water.png")
WATER_SIZE = (Grid,Grid)
water = pygame.transform.scale(water, WATER_SIZE)

tree = pygame.image.load("tree.png")
TREE_SIZE = (Grid,Grid*2)
tree = pygame.transform.scale(tree, TREE_SIZE)

Log = pygame.image.load("log.png")
LOG_SIZE = (Grid*3,Grid)
Log = pygame.transform.scale(Log, LOG_SIZE)

mushroom = pygame.image.load("mushroom.png")
MUSHROOM_SIZE = (Grid,Grid)
mushroom = pygame.transform.scale(mushroom, MUSHROOM_SIZE)

mushroom2 = pygame.image.load("mushroom2.png")
MUSHROOM2_SIZE = (Grid,Grid)
mushroom2 = pygame.transform.scale(mushroom2, MUSHROOM2_SIZE)

hWalk = pygame.image.load("horizontalWalk.png")
HWALK_SIZE = (Grid*3,Grid)
hWalk = pygame.transform.scale(hWalk, HWALK_SIZE)

vWalk = pygame.image.load("horizontalWalk.png")
VWALK_SIZE = (Grid*3,Grid)
vWalk = pygame.transform.scale(vWalk, VWALK_SIZE)

vWalk = pygame.transform.rotate(vWalk,90)

flowers = pygame.image.load("flowers.png")
FLOWERS_SIZE = (Grid,Grid)
flowers = pygame.transform.scale(flowers, FLOWERS_SIZE)

pflowers = pygame.image.load("pinkflowers.png")
PFLOWERS_SIZE = (Grid,Grid)
pflowers = pygame.transform.scale(pflowers, PFLOWERS_SIZE)

fox = pygame.image.load("fox.png")
FOX_SIZE = (Grid*2,Grid)
fox = pygame.transform.scale(fox, FOX_SIZE)

bunnyjump = pygame.image.load("bunnyjump.png")
BUNJ_SIZE = (Grid,Grid)
bunnyjump = pygame.transform.scale(bunnyjump, BUNJ_SIZE)

bunny = pygame.image.load("bunny.png")
BUN_SIZE = (Grid,Grid)
bunny = pygame.transform.scale(bunny, BUN_SIZE)

gameState = "inGame"
MULTIPLIER = Grid

#Initialize movement keys#
up = False
right = False
down = False
left = False
space = False
mousePressed = False

grass = [[0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0]]

pos = [0,0]

right = False
left = False
down = False
up = False

treasureLocX = random.randint(0, len(grass) - 1)
treasureLocY = random.randint(0, len(grass[0]) - 1)
#grass[treasureLocX][treasureLocY] = 2

grass[6][5] = 5
grass[7][5] = 5
grass[8][5] = 5
grass[6][6] = 5
grass[7][6] = 5
grass[8][6] = 5
grass[6][7] = 5
grass[7][7] = 5
grass[8][7] = 5

grass[2][3] = 6
grass[10][1] = 6

grass[7][9] = 7

grass[3][1] = 8
grass[5][10] = 8

grass[3][2] = 9
grass[4][1] = 9

grass[6][4] = 10
grass[6][8] = 10

grass[5][5] = 11
grass[9][5] = 11

#sp500
sp500 = []
spPrice = []
spSym = []

#stock yield
stockY = []
dividendPer = []
dividendSym = []
getDivPer = []

grass[1][6] = 14

grass[7][3] = 15

grass[4][2] = 16

grass[2][4] = 17
grass[2][6] = 17
grass[10][2] = 17
grass[7][4] = 17
grass[8][4] = 17
grass[9][5] = 17
grass[9][6] = 17
grass[9][7] = 17
grass[8][9] = 17
grass[9][9] = 17
grass[8][8] = 17
grass[7][8] = 17
grass[5][5] = 17
grass[5][6] = 17
grass[5][7] = 17


while True:
    if grass[treasureLocX][treasureLocY] != 0: 
        treasureLocX = random.randint(0, len(grass) - 1)
        treasureLocY = random.randint(0, len(grass[0]) - 1)
    else:
        grass[treasureLocX][treasureLocY] = 2
        break
    
foundChest = "You have found the chest!"
twoTiles = "You are very close to the chest!"
constant = 60

def drawGrass():
    #Creates the 2D list for the grass using nested loops
    global grass

    for i in range(12):
        for j in range(12):
            # 0 = regular grass, 1 = stepped over, 2 = treasure, 3 = treasure stepped over
            if grass[i][j] == 0 or grass[i][j] == 2:
                screen.blit(background,(i*MULTIPLIER,j*MULTIPLIER))
            if i == pos[0] and j == pos[1]:
                grass[i][j] = 1
            if grass[i][j] == 1 or grass[i][j] == 3:
                screen.blit(holeOver, (i*MULTIPLIER,j*MULTIPLIER))
            if grass[i][j] == 5:
                screen.blit(background,(i*MULTIPLIER,j*MULTIPLIER))
                screen.blit(water, (i*MULTIPLIER,j*MULTIPLIER))
            if grass[2][3] == 6:
                screen.blit(background,(2*MULTIPLIER,3*MULTIPLIER))
                screen.blit(background,(2*MULTIPLIER,4*MULTIPLIER))
                screen.blit(tree, (2*MULTIPLIER,3*MULTIPLIER))  
            if grass[10][1] == 6:
                screen.blit(background,(10*MULTIPLIER,1*MULTIPLIER))
                screen.blit(background,(10*MULTIPLIER,2*MULTIPLIER))
                screen.blit(tree, (10*MULTIPLIER,1*MULTIPLIER)) 
            if grass[7][9] == 7:
                screen.blit(background,(7*MULTIPLIER,9*MULTIPLIER))
                screen.blit(background,(8*MULTIPLIER,9*MULTIPLIER))
                screen.blit(background,(9*MULTIPLIER,9*MULTIPLIER))
                screen.blit(Log, (7*MULTIPLIER,9*MULTIPLIER)) 
            if grass[i][j] == 8:
                screen.blit(background,(5*MULTIPLIER,10*MULTIPLIER))
                screen.blit(mushroom, (5*MULTIPLIER,10*MULTIPLIER))      
                screen.blit(background,(3*MULTIPLIER,1*MULTIPLIER))
                screen.blit(mushroom, (3*MULTIPLIER,1*MULTIPLIER)) 
            if grass[i][j] == 9:
                screen.blit(background,(3*MULTIPLIER,2*MULTIPLIER))
                screen.blit(mushroom2, (3*MULTIPLIER,2*MULTIPLIER))      
                screen.blit(background,(4*MULTIPLIER,1*MULTIPLIER))
                screen.blit(mushroom2, (4*MULTIPLIER,1*MULTIPLIER)) 
            if grass[6][4] == 10:
                screen.blit(background,(6*MULTIPLIER,4*MULTIPLIER))
                screen.blit(background,(7*MULTIPLIER,4*MULTIPLIER))
                screen.blit(background,(8*MULTIPLIER,4*MULTIPLIER))
                screen.blit(hWalk, (6*MULTIPLIER,4*MULTIPLIER)) 
            if grass[6][8] == 10:
                screen.blit(background,(6*MULTIPLIER,8*MULTIPLIER))
                screen.blit(background,(7*MULTIPLIER,8*MULTIPLIER))
                screen.blit(background,(8*MULTIPLIER,8*MULTIPLIER))
                screen.blit(hWalk, (6*MULTIPLIER,8*MULTIPLIER))  
            if grass[5][5] == 17:
                screen.blit(background,(5*MULTIPLIER,5*MULTIPLIER))
                screen.blit(background,(5*MULTIPLIER,6*MULTIPLIER))
                screen.blit(background,(5*MULTIPLIER,7*MULTIPLIER))
                screen.blit(vWalk, (5*MULTIPLIER,5*MULTIPLIER)) 
            if grass[9][5] == 17:
                screen.blit(background,(9*MULTIPLIER,5*MULTIPLIER))
                screen.blit(background,(9*MULTIPLIER,6*MULTIPLIER))
                screen.blit(background,(9*MULTIPLIER,7*MULTIPLIER))
                screen.blit(vWalk, (9*MULTIPLIER,5*MULTIPLIER)) 
            if grass[i][j] == 12:
                screen.blit(background,(1*MULTIPLIER,9*MULTIPLIER))
                screen.blit(flowers, (1*MULTIPLIER,9*MULTIPLIER)) 
                screen.blit(background,(1*MULTIPLIER,10*MULTIPLIER))
                screen.blit(flowers, (1*MULTIPLIER,10*MULTIPLIER))    
                screen.blit(background,(2*MULTIPLIER,9*MULTIPLIER))
                screen.blit(flowers, (2*MULTIPLIER,9*MULTIPLIER)) 
                screen.blit(background,(2*MULTIPLIER,10*MULTIPLIER))
                screen.blit(flowers, (2*MULTIPLIER,10*MULTIPLIER)) 
                screen.blit(background,(9*MULTIPLIER,1*MULTIPLIER))
                screen.blit(flowers, (9*MULTIPLIER,1*MULTIPLIER)) 
                screen.blit(background,(9*MULTIPLIER,2*MULTIPLIER))
                screen.blit(flowers, (9*MULTIPLIER,2*MULTIPLIER)) 
                screen.blit(background,(10*MULTIPLIER,3*MULTIPLIER))
                screen.blit(flowers, (10*MULTIPLIER,3*MULTIPLIER))
                screen.blit(background,(0*MULTIPLIER,9*MULTIPLIER))
                screen.blit(flowers, (0*MULTIPLIER,9*MULTIPLIER)) 
                screen.blit(background,(0*MULTIPLIER,10*MULTIPLIER))
                screen.blit(flowers, (0*MULTIPLIER,10*MULTIPLIER))
            if grass[i][j] == 13:
                screen.blit(background,(10*MULTIPLIER,8*MULTIPLIER))
                screen.blit(pflowers, (10*MULTIPLIER,8*MULTIPLIER)) 
                screen.blit(background,(10*MULTIPLIER,9*MULTIPLIER))
                screen.blit(pflowers, (10*MULTIPLIER,9*MULTIPLIER)) 
                screen.blit(background,(9*MULTIPLIER,8*MULTIPLIER))
                screen.blit(pflowers, (9*MULTIPLIER,8*MULTIPLIER)) 
            if grass[1][6] == 14:
                screen.blit(background,(1*MULTIPLIER,6*MULTIPLIER))
                screen.blit(background,(2*MULTIPLIER,6*MULTIPLIER))
                screen.blit(fox, (1*MULTIPLIER,6*MULTIPLIER))
            if grass[7][3] == 15:
                screen.blit(background,(7*MULTIPLIER,3*MULTIPLIER))
                screen.blit(bunnyjump, (7*MULTIPLIER,3*MULTIPLIER))
            if grass[4][2] == 16:
                screen.blit(background,(4*MULTIPLIER,2*MULTIPLIER))
                screen.blit(bunny, (4*MULTIPLIER,2*MULTIPLIER))

def checkCollision():
    if treasureLocX == pos[0] and treasureLocY == pos[1]:
        screen.blit(chest, (treasureLocX*MULTIPLIER, treasureLocY*MULTIPLIER))
        grass[treasureLocX][treasureLocY] = 3
        font = pygame.font.SysFont("agencyfb", int(Grid/1.5), bold=True, italic=False)
        chestMessage = font.render(str(foundChest), True, (0,0,0))
        screen.blit(chestMessage, [10,10])
    if treasureLocX + 1 == pos[0] and treasureLocY == pos[1] or treasureLocX + 2 == pos[0] and treasureLocY == pos[1] or treasureLocX - 2 == pos[0] and treasureLocY == pos[1] or treasureLocX - 1 == pos[0] and treasureLocY == pos[1] or treasureLocX + 1 == pos[0] and treasureLocY + 1 == pos[1] or treasureLocX - 1 == pos[0] and treasureLocY + 1 == pos[1]:
        font = pygame.font.SysFont("agencyfb", int(Grid/1.5), bold=True, italic=False)
        closeToChest = font.render(str(twoTiles), True, (0,0,0))
        screen.blit(closeToChest, [10,10])
    if treasureLocY + 1 == pos[1] and treasureLocX == pos[0] or treasureLocY + 2 == pos[1] and treasureLocX == pos[0] or treasureLocY - 2 == pos[1] and treasureLocX == pos[0] or treasureLocY - 1 == pos[1] and treasureLocX == pos[0] or treasureLocY - 1 == pos[1] and treasureLocX - 1 == pos[0] or treasureLocY - 1 == pos[1] and treasureLocX + 1 == pos[0]:
        font = pygame.font.SysFont("agencyfb", int(Grid/1.5), bold=True, italic=False)
        closeToChest = font.render(str(twoTiles), True, (0,0,0))
        screen.blit(closeToChest, [10,10])

def movement():
    global right, left, up, down
    global pos

    if right:
        pos[0] += 1
        right = False
        if pos[0]+1 == 3:
            if pos[1] == 3 or pos[1] == 4:
                pos[0] -= 1
        if pos[0]+1 == 4:
            if pos[1] == 1 or pos[1] == 2:
                pos[0] -= 1
        if pos[0]+1 == 2:
            if pos[1] == 6:
                pos[0] -= 1
        if pos[0]+1 == 7:
            if pos[1] == 4 or pos[1] == 8:
                pos[0] -= 1
        if pos[0] + 1 == 6:
            if pos[1] == 5 or pos[1] == 6 or pos[1] == 7 or pos[1] == 10:
                pos[0] -= 1
        if pos[0]+1 == 8:
            if pos[1] == 9 or pos[1] == 3:
                pos[0] -= 1
        if pos[0]+1 == 10:
            if pos[1] == 1 or pos[1] == 2:
                pos[0] -= 1
        if pos[0]+1 == 11:
            if pos[1] == 3:
                pos[0] -= 1
    elif left:
        pos[0] -= 1
        left = False
        if pos[0] - 1 == 8:
            if pos[1] == 5 or pos[1] == 6 or pos[1] == 7:
                pos[0] += 1
        if pos[0] - 1 == 1:
            if pos[1] == 3 or pos[1] == 4 or pos[1] == 6 or pos[1] == 9 or pos[1] == 10:
                pos[0] += 1
        if pos[0] - 1 == 3:
            if pos[1] == 1 or pos[1] == 2:
                pos[0] += 1
        if pos[0] - 1 == 4:
            if pos[1] == 10:
                pos[0] += 1
        if pos[0] - 1 == 9:
            if pos[1] == 1 or pos[1] == 2 or pos[1] == 3 or pos[1] == 8 or pos[1] == 9:
                pos[0] += 1
        if pos[0] - 1 == 7:
            if pos[1] == 4:
                pos[0] += 1
        if pos[0] - 1 == 6:
            if pos[1] == 3:
                pos[0] += 1
    elif up:
        pos[1] -= 1
        up = False 
        if pos[1] - 1 == 6:
            if pos[0] == 5:
                pos[1] += 1
        if pos[1] - 1 == 3:
            if pos[0] == 2:
                pos[1] += 1
        if pos[1] - 1 == 1:
            if pos[0] == 3 or pos[0] == 4 or pos[0] == 9:
                pos[1] += 1
        if pos[1] - 1 == 2:
            if pos[0] == 10:
                pos[1] += 1
        if pos[1] - 1 == 5:
            if pos[0] == 1 or pos[0] == 2:
                pos[1] += 1
        if pos[1] - 1 == 7:
            if pos[0] == 6:
                pos[1] += 1
        if pos[1] - 1 == 8:
            if pos[0] == 7 or pos[0] == 8 or pos[0] == 9 or pos[0] == 10:
                pos[1] += 1
        if pos[1] - 1 == 9:
            if pos[0] == 0 or pos[0] == 1 or pos[0] == 2 or pos[0] == 5:
                pos[1] += 1
    elif down:
        pos[1] += 1
        down = False
        if pos[1] + 1 == 5:
            if pos[0] == 6 or pos[0] == 7 or pos[0] == 8:
                pos[1] -= 1
        if pos[1] + 1 == 4:
            if pos[0] == 2 or pos[0] == 7:
                pos[1] -= 1
        if pos[1] + 1 == 2:
            if pos[0] == 3 or pos[0] == 4 or pos[0] == 9 or pos[0] == 10:
                pos[1] -= 1
        if pos[1] + 1 == 6:
            if pos[0] == 5 or pos[0] == 9:
                pos[1] -= 1
        if pos[1] + 1 == 9:
            if pos[0] == 10:
                pos[1] -= 1
        if pos[1] + 1 == 7:
            if pos[0] == 1 or pos[0] == 2:
                pos[1] -= 1
        if pos[1] + 1 == 10:
            if pos[0] == 0 or pos[0] == 1 or pos[0] == 2:
                pos[1] -= 1
        if pos[1] + 1 == 11:
            if pos[0] == 5:
                pos[1] -= 1
print("The position the chest:", treasureLocX, treasureLocY)

#Game loop
while True:
    # ===================== HANDLE EVENTS (DO NOT EDIT) ===================== #
    done = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True
            break
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_RIGHT:     
                right = True
            if event.key == pygame.K_LEFT: 
                left = True
            if event.key == pygame.K_DOWN:     
                down = True

    if done == True:
        break

    # ============================== MOVE STUFF ============================= #
    if gameState == "inGame":
        if pos[0] > 11:
            pos[0] = 11
        if pos[0] < 0:
            pos[0] = 0
        if pos[1] > 11:
            pos[1] = 11
        if pos[1] < 0:
            pos[1] = 0
        movement()
        
    screen.fill ((56,140,70))
    drawGrass()
    screen.blit(character_img, (pos[0]*MULTIPLIER,pos[1]*MULTIPLIER))
    checkCollision()
   
    # ====================== PYGAME STUFF (DO NOT EDIT) ===================== #
    pygame.display.update()
    pygame.display.flip()
    pygame.time.delay(20)
pygame.quit()