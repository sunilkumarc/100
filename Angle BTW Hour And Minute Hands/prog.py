# Given an input of the form HH:MM, find the angle between hour and minute hands
# of a clock

def findAngle(hours, minutes):
    hourHandAt = hours%12
    minuteHandAt = int(minutes/5)
    
    angleOfHourHand = hourHandAt * 30 + (minutes*0.5)
    angleOfMinuteHand = minutes * 6

    return abs(angleOfMinuteHand - angleOfHourHand)

def isInvalid(hours, minutes):
    if hours < 0 or hours > 23:
        return True
    
    if minutes < 0 or minutes > 59:
        return True
    
    return False

if __name__ == '__main__':
    hours, minutes = map(int, input().strip().split(':'))
    
    if hours == None or minutes == None or isInvalid(hours, minutes):
        print('Invalid input. Exiting...')
    else:
        res = findAngle(hours, minutes)
        print(res)
