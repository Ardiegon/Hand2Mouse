import math

def calculate_center(hand):
    ids = [0,5,9,13,17]
    avg_x = sum(hand[x][0] for x in ids)/len(ids)
    avg_y = sum(hand[x][1] for x in ids)/len(ids)
    return avg_x, avg_y


def calculate_squared_distance(hand, ids):
    distance_x_sq = (hand[ids[0]][0] - hand[ids[1]][0])**2
    distance_y_sq = (hand[ids[0]][0] - hand[ids[1]][0])**2
    return distance_x_sq + distance_y_sq

def calculate_turned_back(hand):
    distance_x = hand[4][0] - hand[17][0]
    return distance_x < -40

def filter_noise_movement(mov, func = "none"):
    if func =="x3rd":
        return (1/10000)*(mov**3)
    elif func =="atanintegral":
        if mov > 0:
            return mov*math.atan(mov) - (math.log((mov**2)+1))/2
        else:
            return -(mov*math.atan(mov) - (math.log((mov**2)+1))/2)
    elif func == "none":
        return mov
