import random
import time

cards = ['rainbow ralphing cat', 'rainbow ralphing cat', 'rainbow ralphing cat', 'rainbow ralphing cat', 
       'tacocat', 'tacocat', 'tacocat', 'tacocat', 
       'beard cat', 'beard cat', 'beard cat', 'beard cat', 
       'hairy potato cat', 'hairy potato cat', 'hairy potato cat', 'hairy potato cat', 
       'cattermelon', 'cattermelon', 'cattermelon', 'cattermelon', 
       'attack', 'attack', 'attack', 'attack', 
       'skip', 'skip', 'skip', 'skip', 
       'see the future', 'see the future', 'see the future', 'see the future', 'see the future', 
       'favor', 'favor', 'favor', 'favor', 
       'shuffle', 'shuffle', 'shuffle', 'shuffle', 
       'nope', 'nope', 'nope', 'nope']

deck = ['defuse']
deck2 = ['defuse']
clear = '\n' * 37
numwords = ['single', 'double', 'triple']
com = []
game = 'on'

# setup
for x in range(0, 3):
    z = random.choice(cards)
    com.append(z)
    cards.remove(z)

for x in range(1, 5):
    deck.append(random.choice(cards))
    cards.remove(deck[x])

for x in range(1, 5):
    deck2.append(random.choice(cards))
    cards.remove(deck2[x])

cards.append('exploding kitten')

# turns in game
def turn(deck, deck2):
    global game
    
    attack = False
    nope = False
    used = 'none'
    index = 100
    a = 1

    draw = True
    print(clear)
    print('your deck is: ', ' | '.join(deck))

    while a == 1:
        index = input('[enter number 1-%s or none] index of card: ' %len(deck))
        
        if index != 'none':
            index = int(index)
            used = deck[index - 1]

        if used in ['rainbow ralphing cat', 'tacocat', 'beard cat', 'hairy potato cat', 'cattermelon']:
            cats = ' '.join(deck).count(used)
            
            if cats > 1:
                a = 0
                
                if cats > 2:
                    index = input('[enter 2 or 3] play double or triple %ss? '%used)

                if index == '3':
                    for x in range(0, 3):
                        cards.append(used)
                        
                    taken = input('[enter any card] what card would you like to take? ')
                            
                    if taken in deck2:
                        print('you can made a pair of %ss' %used)
                        print('you took a %s!' %taken)
                        deck.append(taken)
                        deck2.remove(taken)

                        for x in range(0, 3):
                            deck.remove(used)
                            cards.append(used)

                    else:
                        print('the other player does not have a %s' %taken)

                else:
                    for x in range(0, 2):
                        deck.remove(used)
                        cards.append(used)
                        
                    taken = random.choice(deck2)
                    print('you took a %s' %taken)
                    deck.append(taken)
                    deck2.remove(taken)

        if used in ['skip', 'attack']:
            a = 0
            draw = False
            deck.remove(used)
            cards.append(used)
            
            if used == 'attack':
                # attacks yourself on this turn
                attack = True
                print('you skipped your turn and the other player will draw two cards!')
                
            else:
                print('you skipped your turn!')

        if used == 'see the future':
            a = 0
            print('the next three cards are: %s' %' | '.join(com))
            deck.remove(used)
            cards.append(used)

        if used == 'favor':
            a = 0
            deck.remove(used)
            cards.append(used)
            
            print(clear)
            print('pass the computer to the other player')
            time.sleep(5)

            index = 100
            print(clear)
            print('your deck is: ', ' | '.join(deck2))

            while index >= len(deck2):
                index = int(input('[enter 1-%s] what card will you favor? ' %len(deck2)))
                favor = deck2[index - 1]

            deck2.remove(favor)
            deck.append(favor)

            print(clear)
            print('pass the computer to the other player')
            time.sleep(5)

        if used == 'shuffle':
            a = 0
            deck.remove(used)
            cards.append(used)
            com.clear()
            print('you shuffled the deck')
            
            for x in range(0, 3):
                z = random.choice(cards)
                com.append(z)
                cards.remove(z)

        if used == 'none':
            a = 0
            
    if draw and not attack:
        deck.append(com[0])
        com.pop(0)

        z = random.choice(cards)
        com.append(z)
        cards.remove(z)

    if attack:
        for x in range(0, 2):
            deck.append(com[0])
            com.pop(0)

            z = random.choice(cards)
            com.append(z)
            cards.remove(z)
                
        attack = False
        # attacks yourself on this turn

    if 'exploding kitten' in deck:
        print('you picked up an exploding kitten!')

        if 'defuse' in deck:
            print('you defused the exploding kitten!')

        else:
            print('you don\'t have a defuse!')
            game = 'over'
        
    print('\nyour deck is: ', ' | '.join(deck))
    time.sleep(5)
    print(clear)

    print('pass the computer to the other player')
    time.sleep(5)

# game starts
while game != 'over':
    turn(deck, deck2)
    turn(deck2, deck)
