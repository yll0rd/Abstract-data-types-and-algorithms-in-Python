class Time:
    def __init__(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.n_secs = (int(hours)*60*60) + (int(minutes)*60) + int(seconds)
    
    def hour(self):
        return self.hours

    def get_minutes(self):
        return self.minutes

    def get_seconds(self):
        return self.seconds
    
    def numSeconds(self, otherTime):
        if self.n_secs >= otherTime.n_secs: return self.n_secs - otherTime.n_secs
        else: return otherTime.n_secs - self.n_secs

    def isAM(self):
        if self.hours in range(12): return True
        else: return False

    def isPM(self):
        if self.hours in range(12,25): return True
        else: return False

    def __str__(self):
        return "%02d:%02d:%02d" % (self.hours, self.minutes, self.seconds)