import random

def tit_for_tat(opponent_previous_decision):
    return opponent_previous_decision

def joss(opponent_previous_decision):
    true = random.choices([True, False], weights=(10,90))
    print(true)
    if true[0] == False:
        return opponent_previous_decision
    else:
        return random.choices(['C', 'D'])

def game_master():
    number_of_rounds = 0
    player1_decisions = []
    player2_decisions = []
    player1_points = 0
    player2_points = 0
    while 0 < 200:
        if number_of_rounds == 200:
            break 
        if number_of_rounds == 0:
            player1 = tit_for_tat('C')
            player1_decisions.append('C')
            player2 = joss('C')
            player2_decisions.append('C')
            if player1 == 'C' and player2 == 'C':
                player1_points += 3
                player2_points += 3
            if player1 == 'D' and player2 == 'C':
                player1_points += 5
            if player1 == 'C' and player2 == 'D':
                player2_points += 5
            if player1 == 'D' and player2 == 'D':
                player1_points += 1
                player2_points += 1
            number_of_rounds += 1
        else:
            player1 = tit_for_tat(player2_decisions[-1])
            player2 = joss(player1_decisions[-1])
            player1_decisions.append(player1[0])
            player2_decisions.append(player2[0])
            if player1 == 'C' and player2 == 'C':
                player1_points += 3
                player2_points += 3
            if player1 == 'D' and player2 == 'C':
                player1_points += 5
            if player1 == 'C' and player2 == 'D':
                player2_points += 5
            if player1 == 'D' and player2 == 'D':
                player1_points += 1
                player2_points += 1
            number_of_rounds += 1 
            
    print(f"Player 1 Points: {player1_points} | Player 1 Decisions: {player1_decisions} | Player 2 Points: {player2_points} | Player 2 Decisions: {player2_decisions}")
    if player1_points > player2_points:
        return "Player 1 Wins"
    else:
        return "Player 2 Wins"
        
if __name__ == "__main__":
    n = 0
    winners = []
    while n < 10:
        if n == 10:
            break
        winner = game_master()
        winners.append(winner)
        n += 1
    
    print(winners)