class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out
        # variables not allowed :( 
        # pass

        # insertion sort?
        # while the left neighbor> right neighbor, swap, so the smallest values stays to the left

        # we are at 0, we want to start at second element so lets move right
        # if Im not holding anything(light is off)-->im holding None AND can move to the right: go right
        while self.can_move_right() and self.light_is_on() is False:
            # move right
            self.move_right()
            # pick up our item (swap with None)
            self.swap_item() 
            self.set_light_on() # Holding item
            # in place of our item there is NONE 

            # while we can move left AND our item is smaller than the left neighbor: swap

            # if we are holding an item and can go left
            while self.can_move_left() and self.light_is_on() is True:
                # move left 
                self.move_left()
                # and check if our item is smaller than the left neighbor
                if self.compare_item() == -1:
                    # swap them: put our item down and hold the bigger one
                    self.swap_item() # since we're not holding None, the light stays on

                    # now were holding the bigger item
                    # go back right where None is,
                    self.move_right()
                    # put item down and hold None 
                    self.swap_item()
                    self.set_light_off()
                    # then come back (left) with None
                    self.move_left()

                    #pick the bigger item back up again --> put None down
                    self.swap_item()
                    self.set_light_on() # now we're holding the bigger item and can continue on
                    
                # otherwise, our item is bigger that its left neighbor:
                # we want to go back to our place(right) and put our item down
                else:
                    self.move_right()
                    # drop item 
                    self.swap_item() # -> pick None back up
                    self.set_light_off() # not holding any item --> Im holding None

            # If I am all the way to the left(cant move left anymore), drop my item
            if self.can_move_left() is False:
                # drop item
                self.swap_item() # pick up None
                self.set_light_off() # holding NONE
 

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]
    # l = [2,4,5,3,1,0]
    # l = [2,1]
    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)



    # ```🍝 Spaghetti code 🍝```

        # selection sort:
        # put biggest number at the end (swap with whatever is at the end currently) 
        # once we have the biggest number, we can compare the last values
        # loop through the list 
            # looping might mean moving left and right?
            # find our max value
        ##----> we are at zero, 
        ## pick up the item and turn on the light (thats our current "max" value)
        # check if we can move right
        # while we can move right
            # compare each item
            # if the new item is bigger, swap them, and pick up the new item instea
        # pick it up, turn on the robot ligh
        # swap it with the last index
        # turn off light
        # recurse on list without the last value?
        

### maybe bubble sort? Recursion?
        # compare 2 values at a time and swap if the left value > right value
        # recursion? 

        # base case?
        # if we can't move right
            
        # # start at 0 --> already there!
        # # pick up the item 
        # self.swap_item()
        # # turn on ligt 
        # self.set_light_on()
        # # move to the right, now we're at position 1
        # self.move_right()


        # # check if we can move right
        # # while we can move right, we can perform certain steps:
        # while self.can_move_right() and self.light_is_on():
        #     # compare the items:
        #     # if our item > item on the floor, swap
        #     if self.compare_item() == 1:
        #         # swap
        #         self.swap_item()
        #         # turn the light off
        #         self.set_light_off()
        #         # pick up the new item and wait
        #         self.swap_item()
        #         self.set_light_on()
        #     # if our item < item on the floor
        #     if self.compare_item() == -1:
        #         # go back left, 
        #         self.move_left()
        #         # drop item
        #         self.swap_item()
        #         # turn light off
        #         self.set_light_off()
        #         # go right
        #         self.move_right()
        #         # pick up item
        #         self.swap_item()

        #     # move to the right and repeat
            # self.move_right()

        # self.swap_item()
        # now we're holding our second biggest number and are at the very end of list
        # # check if can move left
        # while self.can_move_left():
        # # move all the way to the beginning
        #     self.move_left()

        # # start over
        
    