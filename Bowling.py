class Bowling_Game():
    """ This Class calculates the total score after all the frames are complete."""

    def __init__(self):
        """Creating empty list to store the number of pins dropped in each roll."""
        self.pins_dropped = []

    def roll(self, pins):
        """ Appending the list for dropped pins on every roll """
        self.pins_dropped.append(pins)

    def final_score(self):
        """ This function calculates the score after all the rolls are complete.
            Check each frame if there is a strike or spare
            if it is a strike the bonus for that frame is the value of the next two balls rolled (score = 10+bonus)
            if it is a spare the bonus for that frame is the value of the next ball rolled (score = 10+bonus)
            if it is neither there is no bonus and the score for that frame will be sum of the pins dropped in 2 rolls
            :return = score"""
        score = 0
        roll_index = 0
        for frame in range(10):
            if self._is_strike(roll_index):
                score += 10 + self.pins_dropped[roll_index+1] + self.pins_dropped[roll_index+2]
                roll_index += 1
            elif self._is_spare(roll_index):
                score += 10 + self.pins_dropped[roll_index+2]
                roll_index += 2
            else:
                score += self.pins_dropped[roll_index] + self.pins_dropped[roll_index+1]
                roll_index += 2
        return score

    def _is_spare(self, roll_index):
        """ This function checks for spare
            :return boolean,  true if it's a spare else false"""
        return self.pins_dropped[roll_index] + self.pins_dropped[roll_index+1] == 10

    def _is_strike(self, roll_index):
        """ This function checks for strike
            :return boolean,  true if it's a strike else false"""
        return self.pins_dropped[roll_index] == 10
