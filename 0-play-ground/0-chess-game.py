import pygame
import time
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT =  800,  800
DIMENSION =  8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS =  15  # for animation
IMAGES = {}

# Initialize a dictionary of images
def loadImages():
    pieces = ['wp', 'bp', 'wR', 'bR', 'wN', 'bN', 'wB', 'bB', 'wQ', 'bQ', 'wK', 'bK']
    for piece in pieces:
        IMAGES[piece] = pygame.image.load('images/' + piece + '.png')

# Returns a list of all valid moves for a given piece
def getAllPossibleMoves(piece, board):
    moves = []
    if piece.type == 'p':
        if piece.team == 'w':
            moves = getWhitePawnMoves(piece, board)
        else:
            moves = getBlackPawnMoves(piece, board)
    elif piece.type == 'R':
        moves = getRookMoves(piece, board)
    elif piece.type == 'N':
        moves = getKnightMoves(piece, board)
    elif piece.type == 'B':
        moves = getBishopMoves(piece, board)
    elif piece.type == 'Q':
        moves = getQueenMoves(piece, board)
    elif piece.type == 'K':
        moves = getKingMoves(piece, board)
    return moves

# Determine all possible squares a knight can move to
def getKnightMoves(piece, board):
    moves = []
    # Add all possible knight moves
    for r in range(1,  3):
        for c in range(1,  3):
            if r + piece.row <  8 and c + piece.col <  8:
                if (board[r + piece.row][c + piece.col] == '  ' or
                        board[r + piece.row][c + piece.col][0] != piece.team):
                    moves.append((r + piece.row, c + piece.col))
    return moves

# Determine all possible squares a bishop can move to
def getBishopMoves(piece, board):
    moves = []
    # Add all possible bishop moves
    for i in range(1,  8):
        if piece.row + i <  8 and piece.col + i <  8:
            if board[piece.row + i][piece.col + i] == '  ':
                moves.append((piece.row + i, piece.col + i))
            elif board[piece.row + i][piece.col + i][0] != piece.team:
                moves.append((piece.row + i, piece.col + i))
                break
        if piece.row - i >=  0 and piece.col + i <  8:
            if board[piece.row - i][piece.col + i] == '  ':
                moves.append((piece.row - i, piece.col + i))
            elif board[piece.row - i][piece.col + i][0] != piece.team:
                moves.append((piece.row - i, piece.col + i))
                break
        if piece.row + i <  8 and piece.col - i >=  0:
            if board[piece.row + i][piece.col - i] == '  ':
                moves.append((piece.row + i, piece.col - i))
            elif board[piece.row + i][piece.col - i][0] != piece.team:
                moves.append((piece.row + i, piece.col - i))
                break
        if piece.row - i >=  0 and piece.col - i >=  0:
            if board[piece.row - i][piece.col - i] == '  ':
                moves.append((piece.row - i, piece.col - i))
            elif board[piece.row - i][piece.col - i][0] != piece.team:
                moves.append((piece.row - i, piece.col - i))
                break
    return moves

# Determine all possible squares a rook can move to
def getRookMoves(piece, board):
    moves = []
    # Add all possible rook moves
    for i in range(1,  8):
        if piece.row + i <  8:
            if board[piece.row + i][piece.col] == '  ':
                moves.append((piece.row + i, piece.col))
            elif board[piece.row + i][piece.col][0] != piece.team:
                moves.append((piece.row + i, piece.col))
                break
        if piece.row - i >=  0:
            if board[piece.row - i][piece.col] == '  ':
                moves.append((piece.row - i, piece.col))
            elif board[piece.row - i][piece.col][0] != piece.team:
                moves.append((piece.row - i, piece.col))
                break
        if piece.col + i <  8:
            if board[piece.row][piece.col + i] == '  ':
                moves.append((piece.row, piece.col + i))
            elif board[piece.row][piece.col + i][0] != piece.team:
                moves.append((piece.row, piece.col + i))
                break
        if piece.col - i >=  0:
            if board[piece.row][piece.col - i] == '  ':
                moves.append((piece.row, piece.col - i))
            elif board[piece.row][piece.col - i][0] != piece.team:
                moves.append((piece.row, piece.col - i))
                break
    return moves

# Determine all possible squares a queen can move to
def getQueenMoves(piece, board):
    moves = getRookMoves(piece, board)
    moves += getBishopMoves(piece, board)
    return moves

# Determine all possible squares a king can move to
def getKingMoves(piece, board):
    moves = []
    for i in range(-1,  2):
        for j in range(-1,  2):
            if i ==  0 and j ==  0:
                continue
            if piece.row + i <  8 and piece.col + j <  8:
                if board[piece.row + i][piece.col + j] == '  ':
                    moves.append((piece.row + i, piece.col + j))
                elif board[piece.row + i][piece.col + j][0] != piece.team:
                    moves.append((piece.row + i, piece.col + j))
    return moves

# Determine all possible squares a pawn can move to
def getWhitePawnMoves(piece, board):
    moves = []
    if board[piece.row -  1][piece.col] == '  ':
        moves.append((piece.row -  1, piece.col))
    if piece.row ==  6:
        if board[piece.row -  1][piece.col] == '  ' and board[piece.row -  2][piece.col] == '  ':
            moves.append((piece.row -  2, piece.col))
    if piece.col -  1 >=  0:
        if board[piece.row -  1][piece.col -  1][0] != piece.team:
            moves.append((piece.row -  1, piece.col -  1))
    if piece.col +  1 <  8:
        if board[piece.row -  1][piece.col +  1][0] != piece.team:
            moves.append((piece.row -  1, piece.col +  1))
    return moves

# Determine all possible squares a pawn can move to
def getBlackPawnMoves(piece, board):
    moves = []
    if board[piece.row +  1][piece.col] == '  ':
        moves.append((piece.row +  1, piece.col))
    if piece.row ==  1:
        if board[piece.row +  1][piece.col] == '  ' and board[piece.row +  2][piece.col] == '  ':
            moves.append((piece.row +  2, piece.col))
    if piece.col -  1 >=  0:
        if board[piece.row +  1][piece.col -  1][0] != piece.team:
            moves.append((piece.row +  1, piece.col -  1))
    if piece.col +  1 <  8:
        if board[piece.row +  1][piece.col +  1][0] != piece.team:
            moves.append((piece.row +  1, piece.col +  1))
    return moves

# Highlight all possible moves for a piece
# Highlight all possible moves for a piece
def highlightMoves(board, moves, screen):
    for move in moves:
        row, col = move
        pygame.draw.rect(screen, (255,   255,   0), (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

# Draw the board and pieces on the screen
def drawBoard(screen, board):
    screen.fill((135,  206,  250))
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = GRAY if (row + col) %  2 ==  0 else LIGHT_GRAY
            pygame.draw.rect(screen, color, (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            if board[row][col] != '  ':
                screen.blit(IMAGES[board[row][col]], (col * SQ_SIZE, row * SQ_SIZE))

# Main game loop
def main():
    global GRAY, LIGHT_GRAY, WIDTH, HEIGHT, SQ_SIZE, MAX_FPS, IMAGES

    GRAY = (169,  169,  169)
    LIGHT_GRAY = (211,  211,  211)

    loadImages()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Chess')

    board = getStartBoard()

    playerClicks = []
    gameOver = False
    validMove = False

    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if not playerClicks:
                    playerClicks.append((row, col))
                else:
                    piece = board[playerClicks[0][0]][playerClicks[0][1]]
                    moves = getAllPossibleMoves(piece, board)
                    if (row, col) in moves:
                        board[playerClicks[0][0]][playerClicks[0][1]] = '  '
                        board[row][col] = piece
                        playerClicks = []
                        validMove = True
                    else:
                        playerClicks = []
                        validMove = False

        if validMove:
            validMove = False
            time.sleep(0.5)

        drawBoard(screen, board)
        highlightMoves(board, getAllPossibleMoves(board[playerClicks[0][0]][playerClicks[0][1]], board), screen)
        pygame.display.flip()
        clock.tick(MAX_FPS)

# Initialize the board
def getStartBoard():
    board = []
    for i in range(DIMENSION):
        row = []
        for j in range(DIMENSION):
            if i <  2:
                row.append('bp' if j %  2 ==  0 else 'bn')
            elif i >  6:
                row.append('wp' if j %  2 ==  0 else 'wn')
            else:
                row.append('  ')
        board.append(row)
    board[0][0] = 'bR'
    board[0][7] = 'bR'
    board[0][1] = 'bN'
    board[0][6] = 'bN'
    board[0][2] = 'bB'
    board[0][5] = 'bB'
    board[0][3] = 'bQ'
    board[0][4] = 'bK'
    board[7][0] = 'wR'
    board[7][7] = 'wR'
    board[7][1] = 'wN'
    board[7][6] = 'wN'
    board[7][2] = 'wB'
    board[7][5] = 'wB'
    board[7][3] = 'wQ'
    board[7][4] = 'wK'
    return board

if __name__ == '__main__':
    main()