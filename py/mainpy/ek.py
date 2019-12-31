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
deck2 = ['defuse', 'nope']
clear = '\n' * 39
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

for x in range(1, 4):
    deck2.append(random.choice(cards))
    cards.remove(deck2[x])

cards.append('exploding kitten')

def catcards(deck, deck2, used, nope):
    if used in ['rainbow ralphing cat', 'tacocat', 'beard cat', 'hairy potato cat', 'cattermelon']:
            cats = ' '.join(deck).count(used)
            
            if cats > 1:
                query = '2'
                
                if cats > 2:
                    query = input('[enter 2 or 3] play double or triple %ss? '%used)

                if query == '3' and not nope:
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

                elif not nope:
                    for x in range(0, 2):
                        deck.remove(used)
                        cards.append(used)
                        
                    taken = random.choice(deck2)
                    print('you took a %s' %taken)
                    deck.append(taken)
                    deck2.remove(taken)

def skipattack(deck, deck2, used, nope):
    if used in ['skip', 'attack'] and not nope:
            draw = False
            deck.remove(used)
            cards.append(used)
            
            if used == 'attack':
                attacx = True
                print('you skipped your turn and the other player will draw two cards!')
                
            else:
                print('you skipped your turn!')

def seethefuture(deck, deck2, used, nope):
    if used == 'see the future' and not nope:
            print('the next three cards are: %s' %' | '.join(com))
            deck.remove(used)
            cards.append(used)

def favor(deck, deck2, used, nope):
    if used == 'favor' and not nope:
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

def shuffle(deck, deck2, used, nope):
    if used == 'shuffle' and not nope:
        deck.remove(used)
        cards.append(used)
        com.clear()
        print('you shuffled the deck')
            
        for x in range(0, 3):
            z = random.choice(cards)
            com.append(z)
            cards.remove(z)

def noped(query, used):
    global deck2
    
    print('pass the computer to the other player')
    time.sleep(2)
    
    print(clear)
    print('your deck is: ', ' | '.join(deck2))
    nopeq = input('[enter y/n] do you want to nope %s %s? ' %(query, used))
    
    if nopeq == 'y':
        if ' '.join(deck2).count('nope') > 0:
            print('the %s got noped!' %used)
            deck2.remove('nope')
            cards.append('nope')
            turn = 0
            return True

        else:
            print('you don\'t have a nope!')
            return False

    if nopeq == 'n':
        print('you did not nope the %s' %used)
        return False

# turns in game
def gameturn(deck, deck2):
    global game
    global turn

    query = 'a'
    attack = False
    attax = False
    used = 'none'
    index = 100
    draw = True
    nope = False
    usable = False

    print(clear)
    print('your deck is: ', ' | '.join(deck))

    while usable == False:
        index = input('[enter number 1-%s or none] index of card: ' %len(deck))

        if index != 'none':
            index = int(index)

            if len(deck) >= index:
                used = deck[index - 1]
                if used in ['skip', 'attack', 'see the future', 'favor', 'shuffle']:
                    usable = True

                if used in ['rainbow ralphing cat', 'tacocat', 'beard cat', 'hairy potato cat', 'cattermelon']:
                    cats = ' '.join(deck).count(used)
            
                    if cats > 1:
                        query = '2'
                        usable = True
                
                    if cats > 2:
                        query = input('[enter 2 or 3] play double or triple %ss? '%used)

        if index == 'none':
            usable = True

        if used != 'none' and usable:
            nope = noped(query, used)
            
            print('pass the computer to the other player')
            time.sleep(2)
            print(clear)

        catcards(deck, deck2, used, nope)
        skipattack(deck, deck2, used, nope)
        seethefuture(deck, deck2, used, nope)
        favor(deck, deck2, used, nope)
        shuffle(deck, deck2, used, nope)

        if nope:
            print('your card got noped!')
            
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

    if attax:
        attack = True
        attax = False
        
    if 'exploding kitten' in deck:
        print('you picked up an exploding kitten!')

        if 'defuse' in deck:
            print('you defused the exploding kitten!')

        else:
            print('you don\'t have a defuse!')
            game = 'over'
        
    print('\nyour deck is: ', ' | '.join(deck))
    time.sleep(2.5)
    print(clear)

    print('pass the computer to the other player')
    time.sleep(5)

# game starts
while True:
    if game == 'over':
        break
    gameturn(deck, deck2)
    if game == 'over':
        break
    gameturn(deck2, deck)
