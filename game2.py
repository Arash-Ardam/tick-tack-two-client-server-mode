class Game:

    def __init__(self, game_id, player1, player2):
        self.game_id = game_id
        self.player1 = player1
        self.player2 = player2
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turn = 1
        self.winner = 0

    def __str__(self):
        return f"Game({self.game_id}, {self.player1}, {self.player2})"

    def __repr__(self):
        return f"Game({self.game_id}, {self.player1}, {self.player2})"

    def hand(self, p1, p2):

        p1_recv = p1.connection.recv(1024).decode()
        p2_recv = p2.connection.recv(1024).decode()

        if p1_recv == 'N1':
            self.put('N1')
        if p1_recv == 'S1':
            self.put('S1')
        if p1_recv == 'W1':
            self.put('W1')
        if p1_recv == 'E1':
            self.put('E1')
        if p1_recv == 'NW1':
            self.put('NW1')
        if p1_recv == 'SW1':
            self.put('SW1')
        if p1_recv == 'NE1':
            self.put('NE1')
        if p1_recv == 'SE1':
            self.put('SE1')
        if p1_recv == 'C1':
            self.put('C1')
        if p1_recv == 'win1 ?':
            self.win('win1 ?')


        if p2_recv == 'N2':
            self.put('N2')
        if p2_recv == 'S2':
            self.put('S2')
        if p2_recv == 'W2':
            self.put('W2')
        if p2_recv == 'E2':
            self.put('E2')
        if p2_recv == 'NW2':
            self.put('NW2')
        if p2_recv == 'SW2':
            self.put('SW2')
        if p2_recv == 'NE2':
            self.put('NE2')
        if p2_recv == 'SE2':
            self.put('SE2')
        if p2_recv == 'C2':
            self.put('C2')
        if p2_recv == 'win2 ?':
            self.win('win2 ?')

    def put(self, bt):
      
        if bt == 'N1':
            self.board[0][1] = self.player1.button
            self.show(self.player1.connection)
        if bt == 'N2':
            self.board[0][1] = self.player2.button
            self.show(self.player2.connection)

        if bt == 'S1':
            self.board[2][1] = self.player1.button
            self.show(self.player1.connection)
        if bt == 'S2':
            self.board[2][1] = self.player2.button
            self.show(self.player2.connection)

        if bt == 'W1':
            self.board[1][0] = self.player1.button
            self.show(self.player1.connection)
        if bt == 'W2':
            self.board[1][0] = self.player2.button
            self.show(self.player2.connection)

        if bt == 'E1':
            self.board[1][2] = self.player1.button
            self.show(self.player1.connection)
        if bt == 'E2':
            self.board[1][2] = self.player2.button
            self.show(self.player2.connection)

        if bt == 'NW1':
            self.board[0][0] = self.player1.button
            self.show(self.player1.connection)
        if bt == 'NW2':
            self.board[0][0] = self.player2.button
            self.show(self.player2.connection)

        if bt == 'SW1':
            self.board[2][0] = self.player1.button
            self.show(self.player1.connection)
        if bt == 'SW2':
            self.board[2][0] = self.player2.button
            self.show(self.player2.connection)

        if bt == 'NE1':
            self.board[0][2] = self.player1.button
            self.show(self.player1.connection)
        if bt == 'NE2':
            self.board[0][2] = self.player2.button
            self.show(self.player2.connection)

        if bt == 'SE1':
            self.board[2][2] = self.player1.button
            self.show(self.player1.connection)
        if bt == 'SE2':
            self.board[2][2] = self.player2.button
            self.show(self.player2.connection)

        if bt == 'C1':
            self.board[1][1] = self.player1.button
            self.show(self.player1.connection)
        if bt == 'C2':
            self.board[1][1] = self.player2.button
            self.show(self.player2.connection)


    def show(self, conn):
        b1 = self.board[0][0]
        b2 = self.board[0][1]
        b3 = self.board[0][2]
        b4 = self.board[1][0]
        b5 = self.board[1][1]
        b6 = self.board[1][2]
        b7 = self.board[2][0]
        b8 = self.board[2][1]
        b9 = self.board[2][2]
        displaying = '\n {} | {} | {} \n ---------- \n {} | {} | {} \n ---------- \n {} | {} | {} \n'.format(b1, b2, b3, b4, b5, b6, b7, b8, b9)
        conn.send(displaying.encode())
        
    def win(self, msg):
        b1 = self.board[0][0]
        b2 = self.board[0][1]
        b3 = self.board[0][2]
        b4 = self.board[1][0]
        b5 = self.board[1][1]
        b6 = self.board[1][2]
        b7 = self.board[2][0]
        b8 = self.board[2][1]
        b9 = self.board[2][2]
        if msg == 'win1 ?':
            if (b1 == b2 == b3 and b1 == self.player1.button) or (b4 == b5 == b6 and b4 == self.player1.button) or (b7 == b8 == b9 and b7 == self.player1.button)\
                or (b1 == b5 == b9 and b1 == self.player1.button) or (b3 == b5 == b7 and b3 == self.player1.button) or (b1 == b4 == b7 and b1 == self.player1.button)\
                or (b2 == b5 == b8 and b2 == self.player1.button) or (b3 == b6 == b9 and b3 == self.player1.button):
                self.player1.connection.send('Win1 :) '.encode())
                
            else:
                self.player1.connection.send('game over1 :( '.encode())

        if msg == 'win2 ?':
            if (b1 == b2 == b3 and b1 == self.player2.button) or (b4 == b5 == b6 and b4 == self.player2.button) or (b7 == b8 == b9 and b7 == self.player2.button) \
                or (b1 == b5 == b9 and b1 == self.player2.button) or (b3 == b5 == b7 and b3 == self.player2.button) or (b1 == b4 == b7 and b1 == self.player2.button) \
                or (b2 == b5 == b8 and b2 == self.player2.button) or (b3 == b6 == b9 and b3 == self.player2.button):
                self.player2.connection.send('Win2 :) '.encode())
            else:
                self.player2.connection.send('game over2 :( '.encode())

            pass




            


        
        