"""
Once a model is learned, use this to play it.
"""
import drivingStep
import numpy as np
from nn import neural_net
import threading

# Agent driving controller with RL model (arg)
# action extraction
# parallel processing 

class AgentDriving(threading.Thread):

	# 1 : play / 0 : stop 
    playingFlag = 1
    NUM_SENSORS = 3
    

    def play(self,model):
        car_distance = 0
        game_state = drivingStep.GameState()
        action_flag = 0;

	    # Do nothing to get initial.
        _, state = game_state.frame_step((2))

	    # Move.
        while True:
            car_distance += 1
		
	        # Choose action.
            action = (np.argmax(model.predict(state, batch_size=1)))

            
	    # flag 0 : stop
            if self.playingFlag == 0:
                action = 3
                _, state = game_state.frame_step(action)
                return
 
	        # Take action.
            _, state = game_state.frame_step(action)

            if action_flag != action: 
                action_flag = action
                print("=============")
                print(state)
                print(action)

    def stop(self):
        self.playingFlag = 0

    def run(self):
        saved_model = 'saved-models/164-150-100-50000-50000.h5'
        model = neural_net(self.NUM_SENSORS, [164, 150], saved_model)
        self.play(model)
