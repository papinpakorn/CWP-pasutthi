#!/usr/bin/env python3

def checkmate(board):
    if not board or not isinstance(board, str):
        return

    lines = board.strip().split('\n')
    if not lines:
        return

    rows = len(lines)
    for line in lines:
        if len(line) != rows:
            return
        
    king_pos = None
    king_count = 0
    for r in range(rows):
        for c in range(rows):
            if lines[r][c] == 'K':
                king_pos = (r, c)
                king_count += 1

    if king_count != 1:
        return

    kr, kc = king_pos

    PIECES = ('P', 'R', 'B', 'Q', 'K')

    pawn_attackers = [(kr + 1, kc - 1), (kr + 1, kc + 1)]
    for r, c in pawn_attackers:
        if 0 <= r < rows and 0 <= c < rows:
            if lines[r][c] == 'P':
                print("Success")
                return

    straight_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    for dr, dc in straight_directions:
        r, c = kr + dr, kc + dc
        while 0 <= r < rows and 0 <= c < rows:
            piece = lines[r][c]
            if piece in PIECES:
                if piece in ('R', 'Q'):
                    print("Success")
                    return
                break 
            r += dr
            c += dc

    diagonal_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)] 
    for dr, dc in diagonal_directions:
        r, c = kr + dr, kc + dc
        while 0 <= r < rows and 0 <= c < rows:
            piece = lines[r][c]
            if piece in PIECES:
                if piece in ('B', 'Q'):
                    print("Success")
                    return
                break
            r += dr
            c += dc

    print("Fail")