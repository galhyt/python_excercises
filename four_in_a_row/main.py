from board import Board

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    b = Board()
    b.insert(0, Board.Disks.red)
    print(b.is_a_winner())
    b.insert(0, Board.Disks.red)
    print(b.is_a_winner())
    b.insert(0, Board.Disks.red)
    print(b.is_a_winner())
    b.insert(0, Board.Disks.red)
    print(b.is_a_winner())
    print(b)

