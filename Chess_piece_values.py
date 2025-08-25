#Complete the function that accepts two arguments, an 8x8 array representing a chess board and a string
#String can be "white" or "black"



#values.get(s[2:])

values = {
    "queen": 9,
    "rook": 5,
    "bishop": 3,
    "knight": 3,
    "pawn": 1,
    }

def chess_piece_values(chess_board, chess_string):
    white_total=0
    black_total=0
    
    for chess_row in chess_board:
        for item in chess_row:
            if "w-" in item:
                white_total += values.get(item[2:], 0)
            elif "b-" in item:
                black_total += values.get(item[2:], 0)

        

    if chess_string == "white":
        return white_total
    else:
        return black_total
    
print(chess_piece_values([ [" ", " ", " ", " ", " ", " ", " ", " "],
  [" ", " ", "b-queen", " ", " ", " ", " ", "w-queen"],
  [" ", "b-king", " ", " ", "w-rook", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " ", " "],
  ["w-king", " ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " ", " "] ], 
  "black"))        



#return total value of white pieces
#return total value of black pieces





