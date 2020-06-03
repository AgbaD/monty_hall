#! /usr/bin/python
# Author:   @BlankGodd

from random import choice

wins = 0
loss = 0

for i in range(11):
    for j in range(21):
        print()
    print('Test ',i+1)
    print()
    reals = {'a':'car','b':'goat','c' :'goat'}

    doors = ['a','b','c']
    door_guessed = input('Enter which door to guess(a,b,c)\n')
    print('Door guessed is ',door_guessed)
    doors.remove(door_guessed)

    m = ''
    if 'b' in doors and 'c' in doors:
        m = choice(doors)
        doors.remove(m)
        doors.append(door_guessed)
    else:
        if 'b' in doors:
            m = 'b'
            doors.remove(m)
            doors.append(door_guessed)
        else:
            m = 'c'
            doors.remove(m)
            doors.append(door_guessed)

    print('Behind door '+m+' is a goat')
    print('Would you like to swap to the other door?')
    cho = input('Y/n: ').lower()
    door = ''
    if cho == 'y':
        doors.remove(door_guessed)
        door = doors[0]
        if door == 'a':
            wins += 1
        else:
            loss += 1 
    else:
        door = door_guessed
    
    print('You have a ',reals[door], 'behind your door')
        if door == 'a':
            wins += 1
        else:
            loss += 1

print('P(W) = {}/{}'.format(wins,wins+loss))
print('P(L) = {}/{}'.format(loss,wins+loss))


