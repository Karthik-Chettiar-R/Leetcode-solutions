class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        MinuteHand=float(minutes)/5.0
        HourHand=hour+float(minutes)/60.0
        angle=min(12-abs(MinuteHand-HourHand),abs(MinuteHand-HourHand))
        ang=30*angle
        return ang
        
    

        