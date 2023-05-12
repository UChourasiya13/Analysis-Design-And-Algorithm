# define function to implement greedy activity selection algorithm
def activity_selection(start, finish):
    n = len(start)
    activities = [] # list to store selected activities
    i = 0 # index of the current activity
    
    # select the first activity
    activities.append(i)
    
    # iterate over the remaining activities
    for j in range(1, n):
        # if the start time of the current activity is greater than or equal to the finish time of the previous activity, select the current activity
        if start[j] >= finish[i]:
            activities.append(j)
            i = j # update the index of the current activity
    
    return activities

# example usage
start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
selected_activities = activity_selection(start, finish)
print(selected_activities) # output: [0, 1, 3, 4]
