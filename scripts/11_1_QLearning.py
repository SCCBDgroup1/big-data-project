"""
Based on Machine Learning Tutorial in Python | Edureka
https://youtu.be/LzaWrmKL1Z4

    1 = +
    "   "
2 = 3   5 
    "   "
0 = 4 = +
"""

import numpy as np

# R matrix
R = np.matrix([[-1,-1,-1,-1,0,1],
               [-1,-1,-1,0,-1,100],
               [-1,-1,-1,0,-1,-1],
               [-1,0,0,-1,0,-1],
               [0,-1,-1,0,-1,100],
               [-1,0,-1,-1,0,100],               
               ])

# Q matrix
Q = np.matrix(np.zeros([6, 6]))

# Gamma (Learning parameter)
gamma = 0.8



# Actions in the state
def available_actions(state):
    current_state_row = R[state,]
    av_act = np.where(current_state_row >=0) [1]
    return av_act

# The available actions
def sample_next_action(available_actions_range):
    next_action = int(np.random.choice(available_actions_range, 1))
    return next_action

# Update Q values
def update(current_state, action, gamma):
    max_index = np.where(Q[action,] == np.max(Q[action,])) [1]
    if max_index.shape[0] > 1:
        max_index = int(np.random.choice(max_index, size=1))
    else:
        max_index = int(max_index)
    max_value = Q[action, max_index]
    
    #Q value
    Q[current_state, action] = R[current_state, action] + gamma * max_value
    

###############
# Initial state
initial_state = 1
available_act = available_actions(initial_state)
action = sample_next_action(available_act)
update(initial_state, action, gamma)


#####################
# Explores (training)

for i in range(10000):
    current_state = np.random.randint(0, int(Q.shape[0]))
    available_act = available_actions(current_state)
    action = sample_next_action(available_act)
    update(current_state, action, gamma)
    
print("Q matrix")
print(Q / np.max(Q) * 100)


#########
# Testing

current_state = 2
steps = [current_state]

while current_state != 5:
    next_step_index = np.where(Q[current_state,] == np.max(Q[current_state,]))[1]
    if next_step_index.shape[0] > 1:
        next_step_index = int(np.random.choice(next_step_index, size=1))
    else:
        next_step_index = int(next_step_index)
        
    steps.append(next_step_index)
    current_state = next_step_index
    
print("Selected path:")
print(steps)



