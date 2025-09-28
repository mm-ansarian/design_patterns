'''
In this module, we show you a very simple example of implementing the Mediator Design Pattern.
For this purpose, we are simulating a smart home system that works based on temperature, time period of the day and the activity that the owner is doing...

The Mediator pattern suggests that you should cease all direct communication between the components which you want to make independent of each other. 

You can read more about this Design Pattern from this url: https://www.geeksforgeeks.org/system-design/mediator-design-pattern/
'''



import time
import sys


# This class is the center of the smart home. It calls device actions.
class SmartHomeHub:
    def __init__(self, smart_door: object, smart_ac: object, smart_lights: object, smart_curtains: object, ai_assistant: object) -> None:
        # Store the device objects passed from outside. The hub will use them.
        self.door = smart_door        
        self.ac = smart_ac        
        self.lights = smart_lights     
        self.curtains = smart_curtains        
        self.ai_assistant = ai_assistant

    # Adjust AC based on a short label for temperature.
    def temperature(self, current_temp: str='o') -> None:
        # If user says it is cold, lower AC intensity or turn it off.
        if current_temp in ('c', 'cold'):
            if self.ac.intensity == 'high':
                self.ac.set_low()
            else:
                self.ac.turn_off()
        # If user says it is warm, raise AC intensity or turn it on then set low.
        elif current_temp in ('w', 'warm'):
            if self.ac.intensity == 'low':
                self.ac.set_high()
            else:
                self.ac.turn_on()
                self.ac.set_low()
            
    # Morning routine: lights low and curtains open.
    def morning(self) -> None:
        self.lights.turn_on()
        self.lights.set_low()
        self.curtains.open()

    # Night routine: lights high and curtains closed.
    def night(self) -> None:
        self.lights.turn_on()
        self.lights.set_high()
        self.curtains.close()

    # Leave-home routine: lock door, turn off AC and lights, close curtains, say goodbye.
    def leave_home(self) -> None:
        self.door.lock()
        self.ac.turn_off()
        self.lights.turn_off()
        self.curtains.close()
        self.ai_assistant.say('Have a good time. See you later!')


# This class simulates a smart door with two states: locked or unlocked.
class SmartDoor:
    def __init__(self, mode: str='locked') -> None:
        # mode holds the door state. Default is 'locked'.
        self.mode = mode

    # Unlock the door if it is locked. Then print the state.
    def unlock(self) -> None:
        if self.mode == 'locked':
            self.mode = 'unlocked'
        print(f'\nDoor: {self.mode}')

    # Lock the door if it is unlocked. Then print the state.
    def lock(self) -> None:
        if self.mode == 'unlocked':
            self.mode = 'locked'
        print(f'\nDoor: {self.mode}')


# This class simulates a simple air conditioner.
class SmartAC:
    def __init__(self, mode: str='off', intensity: bool|str=None) -> None:
        # mode can be 'on' or 'off'. intensity can be True/False or 'low'/'high'.
        self.mode = mode
        self.intensity = intensity

    # Turn the AC on. If it was off and had no intensity, set a default True value.
    def turn_on(self) -> None:
        if self.mode == 'off' and not self.intensity:
            self.mode = 'on'
            self.intensity = True
        print(f'\nAC: turned {self.mode}')

    # Turn the AC off. If it was on and had an intensity, clear it.
    def turn_off(self) -> None:
        if self.mode == 'on' and self.intensity:
            self.mode = 'off'
            self.intensity = False
        print(f'\nAC: turned {self.mode}')

    # Set AC to low intensity when it is on. Then print the intensity.
    def set_low(self) -> None:
        if self.mode == 'on':
            self.intensity = 'low'
        print(f'\nAC intensity: {self.intensity}')

    # Set AC to high intensity when it is on. Then print the intensity.
    def set_high(self) -> None:
        if self.mode == 'on':
            self.intensity = 'high'
        print(f'\nAC intensity: {self.intensity}')


# This class simulates smart lights with mode and intensity.
class SmartLights:
    def __init__(self, mode: str='off', intensity: bool|str=None) -> None:
        # mode is 'on' or 'off'. intensity may be boolean or 'low'/'high'.
        self.mode = mode
        self.intensity = intensity

    # Turn lights on. If they were off and had no intensity, set a default True value.
    def turn_on(self) -> None:
        if self.mode == 'off' and not self.intensity:
            self.mode = 'on'
            self.intensity = True
        print(f'\nLights: {self.mode}')

    # Turn lights off. If they were on and had an intensity, clear it.
    def turn_off(self) -> None:
        if self.mode == 'on' and self.intensity:
            self.mode = 'off'
            self.intensity = False
        print(f'\nLights: {self.mode}')

    # Set lights to low intensity when they are on. Then print intensity.
    def set_low(self) -> None:
        if self.mode == 'on' and (self.intensity == 'high' or self.intensity):
            self.intensity = 'low'
        print(f'\nLights intensity: {self.intensity}')

    # Set lights to high intensity when they are on. Then print intensity.
    def set_high(self) -> None:
        if self.mode == 'on' and (self.intensity == 'low' or self.intensity):
            self.intensity = 'high'
        print(f'\nLights intensity: {self.intensity}')


# This class simulates curtains with open/closed states.
class SmartCurtains:
    def __init__(self, mode: str='closed') -> None:
        # mode is 'open' or 'closed'. Default is 'closed'.
        self.mode = mode

    # Open the curtains if they are closed. Then print the state.
    def open(self) -> None:
        if self.mode == 'closed':
            self.mode = 'open'
        print(f'\nCurtains: {self.mode}')

    # Close the curtains if they are open. Then print the state.
    def close(self) -> None:
        if self.mode == 'open':
            self.mode = 'closed'
        print(f'\nCurtains: {self.mode}')


# A small wrapper for an AI assistant voice output.
class AIAssistant:
    # Say a short message. This prints the assistant speech.
    def say(self, speech: str) -> None:
        print(f'\n** AI Assistant: {speech} **')


# Main interactive loop. This code runs if the module is executed directly.
if __name__ == '__main__':

    # Create device objects with default states.
    smart_door_obj = SmartDoor()
    smart_ac_obj = SmartAC()
    smart_lights_obj = SmartLights()
    smart_curtains_obj = SmartCurtains()
    ai_assistant_obj = AIAssistant()

    # Create the hub and pass device objects to it.
    smart_home_obj = SmartHomeHub(smart_door=smart_door_obj, smart_ac=smart_ac_obj, smart_lights=smart_lights_obj, smart_curtains=smart_curtains_obj, ai_assistant=ai_assistant_obj)

    # Run a simple text loop to ask the user about actions.
    while True:
        print('\n\n\n\n\n')

        # Map user answers to functions. This makes input handling simple.
        activity_input_dict = {
            'y': smart_home_obj.leave_home,
            'yes': smart_home_obj.leave_home,
            'e': sys.exit,
            'exit': sys.exit,
        }
        time_period_input_dict = {
            'm': smart_home_obj.morning,
            'morning': smart_home_obj.morning,
            'n': smart_home_obj.night,
            'night': smart_home_obj.night,
            'e': sys.exit,
            'exit': sys.exit,
        }

        # Ask the user if they are leaving home.
        activity = input('\nAre you going to leave home(y/n)? ').strip().lower()

        # Find a function for this activity and run it if found.
        func = activity_input_dict.get(activity)
        if func:
            func()
        else:
            # If the answer is not yes/leave, check for no.
            if activity not in ('n', 'no'):
                print('\n!! It seems you have entered an invalid input as the answer of the questions !!')
                continue

        # If the user is not leaving, ask about time and temperature.
        if activity not in ('y', 'yes'):
            time_period = input('\nIs it morning or night(m/n)? ').strip().lower()
            temperature = input('\nWhat do you think of current temperature? Cold, Warm or ok(c/w/o)? ').strip().lower()

            func = time_period_input_dict.get(time_period)
            if func:
                # Only act if temperature input is one of allowed short labels.
                if temperature in ('c', 'cold', 'w', 'warm', 'o', 'ok'):
                    func()
                    smart_home_obj.temperature(temperature)
            else:
                print('\n!! It seems you have entered an invalid input as the answer of the questions !!')
                continue

        # Wait a little bit before the next loop. This gives time to read outputs.
        time.sleep(3)
