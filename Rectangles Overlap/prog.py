# Check whether two rectangles overlap

def doOverlap(rect1, rect2):
    if rect1['x1'] > rect2['x2'] or rect1['x2'] < rect2['x1']:
        return False
    
    if rect1['y1'] < rect2['y2'] or rect1['y2'] > rect2['y1']:
        return False
    
    return True

def getPoint(line):
    rect = {'x1': 0, 'y1': 0, 'x2': 0, 'y2': 0}
    rect['x1'] = line[0]
    rect['y1'] = line[1]
    rect['x2'] = line[2]
    rect['y2'] = line[3]

    return rect

if __name__ == '__main__':
    line1 = list(map(int, input().strip().split()))
    line2 = list(map(int, input().strip().split()))

    rect1 = getPoint(line1)
    rect2 = getPoint(line2)
    
    if doOverlap(rect1, rect2):
        print('They do overlap!')
    else:
        print('They don\'t overlap!')
