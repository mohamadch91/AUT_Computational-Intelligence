# -*- coding: utf-8 -*-

# python imports
from math import degrees

from numpy import np

class FuzzyController:

    def __init__(self, fcl_path):
        self.system = fuzzy_system()


    def _make_input(self, world):
        return dict(
            cp = world.x,
            cv = world.v,
            pa = degrees(world.theta),
            pv = degrees(world.omega)
        )


    def _make_output(self):
        return dict(
            force = 0.
        )


    def decide(self, world):
        output = self._make_output()
        self.system.calculate(self._make_input(world), output)
        return output['force']
class fuzzy_system:
        def __int__(self):
            pass
        #calculate equation of line
        #calculate distance between line and point
        #calculate line slope
        def equation_of_line(self,x1,y1,x2,y2,x):
            m = (y2-y1)/(x2-x1)
            b = y1 - m*x1
            y = m*x + b
            if(x1==x2):
                y=(float)(max(y1,y2))
            return y    
        #define function to calculate rules from complex.fcl
        #pa means angle of pendulum
        # pv means angular velocity of pendulum
        # cp means position of cart
        # cv means velocity of cart
        def pa_up_more_right(x):
            (x1,y1),(x2,y2),(x3,y3)=(0, 0) ,(30, 1), (60, 0)
            #where is x
            #if x is in the range of x1 and x2
            if(x>=x1 and x<=x2):
                return self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x>x2 and x<=x3):
                return self.equation_of_line(x3,y3,x2,y2,x)
            #or return zero
            else:
                return 0
        #calculate up right        
        def pa_up_right(x):
            (x1,y1),(x2,y2),(x3,y3)= (30, 0), (60, 1) ,(90, 0)
            #where is x
            #if x is in the range of x1 and x2
            if(x>=x1 and x<=x2):
                return self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x>x2 and x<=x3):
                return self.equation_of_line(x3,y3,x2,y2,x)
            #or return zero
            else:
                return 0                    
        #calculate up
        def pa_up(x):
            (x1,y1),(x2,y2),(x3,y3)= (60, 0) ,(90, 1) ,(120, 0)
            #where is x
            # if x is in the range of x1 and x2
            if(x>=x1 and x<=x2):
                return self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x>x2 and x<=x3):
                return self.equation_of_line(x3,y3,x2,y2,x)
            #or return zero
            else:
                return 0
        #calculate up left
        def pa_up_left(x):
            (x1,y1),(x2,y2),(x3,y3)= (90, 0), (120, 1) ,(150, 0)
            #where is x
            #if x is in the range of x1 and x2
            if(x>=x1 and x<=x2):
                return self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x>x2 and x<=x3):
                return self.equation_of_line(x3,y3,x2,y2,x)
            #or return zero
            else:
                return 0    
        #calculate up more left
        def pa_up_more_left(x):
            (x1,y1),(x2,y2),(x3,y3)= (120, 0) ,(150, 1), (180, 0)
            #where is x
            #if x is in the range of x1 and x2
            if(x>=x1 and x<=x2):
                return self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x>x2 and x<=x3):
                return self.equation_of_line(x3,y3,x2,y2,x)
            #or return zero
            else:
                return 0
        #calculate down more left
        def pa_down_more_left(x):
            (x1,y1),(x2,y2),(x3,y3)= (180, 0) ,(210, 1) ,(240, 0)
            #if x is in the range of x1 and x2
            if(x>=x1 and x<=x2):
                return self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x>x2 and x<=x3):
                return self.equation_of_line(x3,y3,x2,y2,x)
            #or return zero
            else:
                return 0    
        #calculate down left
        def pa_down_left(x):
            (x1,y1),(x2,y2),(x3,y3)= (210, 0), (240, 1) ,(270, 0)
            #if x is in the range of x1 and x2
            if(x>=x1 and x<=x2):
                return self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x>x2 and x<=x3):
                return self.equation_of_line(x3,y3,x2,y2,x)
            #or return zero
            else:
                return 0    
        #calculate down 
        def pa_down(x):
            (x1,y1),(x2,y2),(x3,y3)= (240, 0) ,(270, 1) ,(300, 0)
            #if x is in the range of x1 and x2
            if(x>=x1 and x<=x2):
                return self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x>x2 and x<=x3):
                return self.equation_of_line(x3,y3,x2,y2,x)
            #or return zero
            else:
                return 0
        #calculate down right
        def pa_down_right(x):
            (x1,y1),(x2,y2),(x3,y3)= (270, 0), (300, 1), (330, 0)
            #if x is in the range of x1 and x2
            if(x>=x1 and x<=x2):
                return self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x>x2 and x<=x3):
                return self.equation_of_line(x3,y3,x2,y2,x)
            #or return zero
            else:
                return 0
        #calculate down more right
        def pa_down_more_right(x):
            (x1,y1),(x2,y2),(x3,y3)= (300, 0) ,(330, 1), (360, 0)
            #if x is in the range of x1 and x2
            if(x>=x1 and x<=x2):
                return self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x>x2 and x<=x3):
                return self.equation_of_line(x3,y3,x2,y2,x)
            #or return zero
            else:
                return 0
        #calculate datas for pv
        ##################################################################################################################

        def pv_cw_fast(x):
            (x1,y1),(x2,y2),(x3,y3)= (-200, 0), (-200, 1), (-100, 0)
            #if x is in the range of x1 and x2
            if( x<=x2):
                return self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x>x2 and x<=x3):
                return self.equation_of_line(x3,y3,x2,y2,x)
            #or return zero
            else:
                return 0
        #calculate cw slow
        def pv_cw_slow(x):
            (x1,y1),(x2,y2),(x3,y3)= (-200, 0), (-100, 1), (0, 0)
            #if x is in the range of x1 and x2
            if(x>=x1 and x<=x2):
                return self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x>x2 and x<=x3):
                return self.equation_of_line(x3,y3,x2,y2,x)
            #or return zero
            else:
                return 0
        #calculate stop
        def pv_stop(x):
            (x1,y1),(x2,y2),(x3,y3)=(-100, 0), (0, 1), (100, 0)
            #if x is in the range of x1 and x2
            if(x>=x1 and x<=x2):
                return self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x>x2 and x<=x3):
                return self.equation_of_line(x3,y3,x2,y2,x)
            #or return zero
            else:
                return 0
        #caculate ccw slow
        def pa_ccw_slow(x):
            (x1,y1),(x2,y2),(x3,y3)=(0, 0), (100, 1) ,(200, 0)
            #if x is in the range of x1 and x2
            if(x>=x1 and x<=x2):
                return self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x>x2 and x<=x3):
                return self.equation_of_line(x3,y3,x2,y2,x)
            #or return zero
            else:
                return 0        
        #calculate ccw fast
        def pa_ccw_fast(x):
            (x1,y1),(x2,y2),(x3,y3)=(100, 0), (200, 1), (200, 0)
            #if x is in the range of x1 and x2
            if(x>=x1 and x<=x2):
                return self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x2<=x ):
                return self.equation_of_line(x3,y3,x2,y2,x)
            #or return zero
            else:
                return 0
    ##########################################################################################################            
        #calculate datas for cp
        def cp_left_far(x):
            (x1,y1),(x2,y2),(x3,y3)=(-10,0),(-10, 1) (-5, 0);
            #if x is in the range of x1 and x2
            if(x<=x2):
                return self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x2<=x ):
                return self.equation_of_line(x3,y3,x2,y2,x)
            #or return zero
            else:
                return 0
        #calculate left_near
        def cp_left_near(x):
            (x1,y1),(x2,y2),(x3,y3)=(-10, 0), (-2.5, 1) ,(0, 0)
            #if x is in the range of x1 and x2
            if(x>=x1 and x<=x2):
                return self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x>x2 and x<=x3):
                return self.equation_of_line(x3,y3,x2,y2,x)
            #or return zero
            else:
                return 0                  
        #calculate stop
        def cp_stop(x):
            (x1,y1),(x2,y2),(x3,y3)=(-2.5, 0), (0, 1) ,(2.5, 0)
            #if x is in the range of x1 and x2
            if(x>=x1 and x<=x2):
                return self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x>x2 and x<=x3):
                return self.equation_of_line(x3,y3,x2,y2,x)
            #or return zero
            else:
                return 0        
        #calculate right_near
        def cp_right_near(x):
            (x1,y1),(x2,y2),(x3,y3)=(0, 0), (2.5, 1) ,(10, 0)
            #if x is in the range of x1 and x2
            if(x>=x1 and x<=x2):
                return self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x>x2 and x<=x3):
                return self.equation_of_line(x3,y3,x2,y2,x)
            #or return zero
            else:
                return 0
        #calculate right_far
        def cp_right_far(x):
            (x1,y1),(x2,y2),(x3,y3)=(5, 0) ,(10, 1),(10,0)
            #if x is in the range of x1 and x2
            if(x>=x1 and x<=x2):
                return self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x2<=x):
                return self.equation_of_line(x3,y3,x2,y2,x)
            #or return zero
            else:
                return 0 
       #####################################################################################################
       # calculate datas for cv
       #calculate left_fast
        def cv_left_fast(x):
            (x1,y1),(x2,y2),(x3,y3)=(-5,0),(-5, 1), (-2.5, 0);
           #if x is in the range of x1 and x2      
            if(x<=x2):
                return self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x2<=x ):
                return self.equation_of_line(x3,y3,x2,y2,x)
            #or return zero
            else:
                return 0
        #calculate left_slow
        def cv_left_slow(x):
            (x1,y1),(x2,y2),(x3,y3)=(-5, 0), (-1, 1), (0, 0)
            #if x is in the range of x1 and x2
            if(x>=x1 and x<=x2):
                return self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x>x2 and x<=x3):
                return self.equation_of_line(x3,y3,x2,y2,x)
            #or return zero
            else:
                return 0              
        #calculate stop
        def cv_stop(x):
            (x1,y1),(x2,y2),(x3,y3)=(-1, 0), (0, 1), (1, 0)
            #if x is in the range of x1 and x2
            if(x>=x1 and x<=x2):
                return self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x>x2 and x<=x3):
                return self.equation_of_line(x3,y3,x2,y2,x)
            #or return zero
            else:
                return 0
        #calculate right_slow
        def cv_right_slow(x):
            (x1,y1),(x2,y2),(x3,y3)=(0, 0), (1, 1), (5, 0)
            #if x is in the range of x1 and x2
            if(x>=x1 and x<=x2):
                return self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x>x2 and x<=x3):
                return self.equation_of_line(x3,y3,x2,y2,x)
            #or return zero
            else:
                return 0
        #calculate right_fast
        def cv_right_fast(x):
            (x1,y1),(x2,y2),(x3,y3)=(2.5, 0), (5, 1), (5, 0)
            #if x is in the range of x1 and x2
            if(x>=x1 and x<=x2):
                return self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x2<=x):
                return self.equation_of_line(x3,y3,x2,y2,x)
            #or return zero
            else:
                return 0
        #####################################################################################################
        #caculate fore data
        