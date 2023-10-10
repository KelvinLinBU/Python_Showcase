#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Bowling_Game():
    """class for the bowling game"""
    
    def __init__(self):
        """constructor for the bowling game"""
        self.score = 0
        
    def startgame(self):
        """the method that starts the game"""
        total_score = 0
        bonus_counter = 0
        for frames in range(1,11):
            score_for_frame = 0
            roll1 = int(input('1st roll of frame ' + str(frames)+ '. How do you roll?: '))
            if roll1 > 10:
                print('You cannot roll higher than a 10! Try again!')
                return
            elif roll1 < 0: 
                print('You cannot roll lower than a 0! Try again!')
                return
            elif roll1 == 10:
                print('Congrats! You rolled a strike!')
                total_score += 10
                print('Your score for frame ' + str(frames) + ' is 10')
                if bonus_counter > 0:
                    total_score += 20
                    bonus_counter -= 1
                bonus_counter += 2
                print('Your total score is ' + str(total_score))
                if frames == 10:
                    bonus_counter = 2
            else:
                roll2 = int(input('2nd roll of frame ' + str(frames)+ '. How do you roll?: '))
                if roll1 + roll2 > 10:
                    print('You cannot roll higher than a 10! Try again!')
                    return
                elif roll2 < 0: 
                    print('You cannot roll lower than a 0! Try again!')
                    return
                elif roll1 + roll2 == 10:
                    print('Congrats! You rolled a spare!')
                    if bonus_counter > 0:
                        total_score += 10
                        bonus_counter -= 1
                    bonus_counter += 1
                    total_score += 10
                    
                    print('Your total score is ' + str(total_score))
                    if frames == 10:
                        bonus_counter = 1
                else:
                    score_for_frame = roll1 + roll2
                    print('Your score for frame ' + str(frames) + ' is ' + str(score_for_frame))
                    if bonus_counter > 0:
                        total_score += roll1
                        bonus_counter -= 1
                    if bonus_counter > 0:
                        total_score += roll2
                        bonus_counter -= 1
                    total_score += score_for_frame
                    print('Your total score is ' + str(total_score))
        while bonus_counter > 0:
           bonus_roll = int(input('How do you roll on your bonus roll? '))
           if bonus_roll > 10:
               print('You cannot roll higher than a 10! Try again!')
               return
           elif bonus_roll < 0: 
               print('You cannot roll lower than a 0! Try again!')
               return
           else:
               total_score += bonus_roll
               bonus_counter -= 1
        print('Your total score is ' + str(total_score) + '. Good Game!')
        return total_score





