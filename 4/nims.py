# Name:
# Section:
# nims.py


"""
In this game, two players sit in front of a pile of 100 stones. They
take turns, each removing between 1 and 5 stones (assuming there are
at least 5 stones left in the pile). The person who removes the last
stone(s) wins.
"""

def play_nims(pile, max_stones):
    '''
    An interactive two-person game; also known as Stones.
    @param pile: the number of stones in the pile to start
    @param max_stones: the maximum number of stones you can take on one turn
    '''

    X = int(raw_input('Pick a number.\n'))
    print 'Answer: ', X + 2


play_nims(11,5)

    ## Basic structure of program (feel free to alter as you please):

#    while [pile is not empty]:
#        print 'There are', pile, 'stones left.'
#        while [player 1's answer is not valid]:
#            [ask player 1]
#        [execute player 1's move]
#       
#        print 'There are', pile, 'stones left.'
#        while [player 2's answer is not valid]:
#            [ask player 2]
#        [execute player 2's move]
#
#    print "Game over"
