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
        ##########################################################################
        #fuzzyfication
        ##########################################################################
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
        def pa_up_more_right(self,x):
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
        def pa_up_right(self,x):
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
        def pa_up(self,x):
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
        def pa_up_left(self,x):
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
        def pa_up_more_left(self,x):
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
        def pa_down_more_left(self,x):
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
        def pa_down_left(self,x):
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
        def pa_down(self,x):
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
        def pa_down_right(self,x):
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
        def pa_down_more_right(self,x):
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

        def pv_cw_fast(self,x):
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
        def pv_cw_slow(self,x):
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
        def pv_stop(self,x):
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
        def pv_ccw_slow(self,x):
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
        def pv_ccw_fast(self,x):
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
    # comment this section if need cp rules uncomment the section below        
        #calculate datas for cp
        # def cp_left_far(self,x):
        #     (x1,y1),(x2,y2),(x3,y3)=(-10,0),(-10, 1) (-5, 0);
        #     #if x is in the range of x1 and x2
        #     if(x<=x2):
        #         return self.equation_of_line(x1,y1,x2,y2,x)
        #     #if x is in the range of x2 and x3
        #     elif(x2<=x ):
        #         return self.equation_of_line(x3,y3,x2,y2,x)
        #     #or return zero
        #     else:
        #         return 0
        # #calculate left_near
        # def cp_left_near(self,x):
        #     (x1,y1),(x2,y2),(x3,y3)=(-10, 0), (-2.5, 1) ,(0, 0)
        #     #if x is in the range of x1 and x2
        #     if(x>=x1 and x<=x2):
        #         return self.equation_of_line(x1,y1,x2,y2,x)
        #     #if x is in the range of x2 and x3
        #     elif(x>x2 and x<=x3):
        #         return self.equation_of_line(x3,y3,x2,y2,x)
        #     #or return zero
        #     else:
        #         return 0                  
        # #calculate stop
        # def cp_stop(self,x):
        #     (x1,y1),(x2,y2),(x3,y3)=(-2.5, 0), (0, 1) ,(2.5, 0)
        #     #if x is in the range of x1 and x2
        #     if(x>=x1 and x<=x2):
        #         return self.equation_of_line(x1,y1,x2,y2,x)
        #     #if x is in the range of x2 and x3
        #     elif(x>x2 and x<=x3):
        #         return self.equation_of_line(x3,y3,x2,y2,x)
        #     #or return zero
        #     else:
        #         return 0        
        # #calculate right_near
        # def cp_right_near(self,x):
        #     (x1,y1),(x2,y2),(x3,y3)=(0, 0), (2.5, 1) ,(10, 0)
        #     #if x is in the range of x1 and x2
        #     if(x>=x1 and x<=x2):
        #         return self.equation_of_line(x1,y1,x2,y2,x)
        #     #if x is in the range of x2 and x3
        #     elif(x>x2 and x<=x3):
        #         return self.equation_of_line(x3,y3,x2,y2,x)
        #     #or return zero
        #     else:
        #         return 0
        # #calculate right_far
        # def cp_right_far(self,x):
        #     (x1,y1),(x2,y2),(x3,y3)=(5, 0) ,(10, 1),(10,0)
        #     #if x is in the range of x1 and x2
        #     if(x>=x1 and x<=x2):
        #         return self.equation_of_line(x1,y1,x2,y2,x)
        #     #if x is in the range of x2 and x3
        #     elif(x2<=x):
        #         return self.equation_of_line(x3,y3,x2,y2,x)
        #     #or return zero
        #     else:
        #         return 0 
       #####################################################################################################
       # calculate datas for cv
       #calculate left_fast
        def cv_left_fast(self,x):
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
        def cv_left_slow(self,x):
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
        def cv_stop(self,x):
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
        def cv_right_slow(self,x):
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
        def cv_right_fast(self,x):
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
        #caculate forcee data
        def force_left_fast(self,x,lim):
            (x1,y1),(x2,y2),(x3,y3)=(-100, 0), (-80, 1) ,(-60, 0)

            #if x is in the range of x1 and x2
            if(x1<x<=x2):
                y= self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x2<x<=x3):
                y= self.equation_of_line(x3,y3,x2,y2,x)
            else:
                y=0         
            #if limit is not reached
            if(y<lim):
                return y  
            #or return lim
            return  lim        
        #calculate force_left_slow
        def force_left_slow(self,x,lim):
            (x1,y1),(x2,y2),(x3,y3)=(-80, 0) ,(-60, 1), (0, 0)

            #if x is in the range of x1 and x2
            if(x1<x<=x2):
                y= self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x2<x<=x3):
                y= self.equation_of_line(x3,y3,x2,y2,x)
            else:
                y=0         
            #if limit is not reached
            if(y<lim):
                return  y
            #or return lim
            return lim
        #calculate force_stop
        def force_stop(self,x,lim):
            (x1,y1),(x2,y2),(x3,y3)=(-60, 0) ,(0, 1) ,(60, 0)

            #if x is in the range of x1 and x2
            if(x1<x<=x2):
                y= self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x2<x<=x3):
                y= self.equation_of_line(x3,y3,x2,y2,x)
            else:
                y=0         
            #if limit is not reached
            if(y<lim):
                return  y
            #or return lim
            return lim
        #calculate force_right_slow
        def force_right_slow(self,x,lim):
            (x1,y1),(x2,y2),(x3,y3)=(0, 0), (60, 1), (80, 0)

            #if x is in the range of x1 and x2
            if(x1<x<=x2):
                y= self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x2<x<=x3):
                y= self.equation_of_line(x3,y3,x2,y2,x)
            else:
                y=0         
            #if limit is not reached
            if(y<lim):
                return  y
            #or return lim
            return lim
        #calculate force_right_fast
        def force_right_fast(self,x,lim):
            (x1,y1),(x2,y2),(x3,y3)=(60, 0) (80, 1) (100, 0)

            #if x is in the range of x1 and x2
            if(x1<x<=x2):
                y= self.equation_of_line(x1,y1,x2,y2,x)
            #if x is in the range of x2 and x3
            elif(x2<x<=x3):
                y= self.equation_of_line(x3,y3,x2,y2,x)
            else:
                y=0         
            #if limit is not reached
            if(y<lim):
                return  y
            #or return lim
            return lim
        
        ##########################################################################
        #inference
        ##########################################################################
        #define dictionary for member ship
        #find same rules in  memeber.txt file
        #caculate rules for all force terms
        #calculate member shib for force 
        def mem_force(self,pa,pv,cp,cv):
            
            stop=max((max(min(self.pa_up(pa),self.pv_stop(pv)),min(self.pa_up_right(pa),self.pv_ccw_slow(pv)),min(self.pa_up_left(pa),self.pv_cw_slow(pv)))),min(self.pa_down_more_right(pa),self.pv_cw_slow(pv)),min(self.pa_down_more_left(pa),self.pv_ccw_slow(pv)),min(self.pa_down(pa),self.pv_ccw_fast(pv)),min(self.pa_up(pa),self.pv_stop(pv)),min(self.pa_down(pa),self.pv_cw_fast(pv)),min(self.pa_down_left(pa),self.pv_cw_fast(pv)),min(self.pa_down_right(pa),self.pv_cw_fast(pv)),min(self.pa_down_more_right(pa),self.pv_cw_fast(pv)),min(self.pa_down_more_right(pa),self.pv_ccw_fast(pv)),min(self.pa_down_more_left(pa),self.pv_cw_fast(pv)),min(self.pa_down_more_left(pa),self.pv_ccw_fast(pv)),min(self.cv_stop(cv),self.pv_stop(pv)))

            right_fast=max(min(self.pa_up_more_right(pa),self.pv_ccw_slow(pv)),min(self.pa_up_more_right(pa),self.pv_cw_slow(pv)),min(self.pa_up_more_right(pa),self.pv_cw_fast(pv)),min(self.pa_down_more_right(pa),self.pv_ccw_slow(pv)),min(
                self.pa_down_right(pa),self.pv_ccw_slow(pv)),min(self.pa_down_right(pa),self.pv_cw_slow(pv)),
                min(self.pa_up_right(pa),self.pv_cw_slow(pv)),min(self.pa_up_right(pa),self.pv_stop(pv)),min(self.pa_up_right(pa),self.pv_cw_fast(pv)),min(self.pa_up_left(pa),self.pv_cw_fast(pv)),min(self.pa_down(pa),self.pv_stop(pv)),min(self.pa_up(pa),self.pv_cw_fast(pv)),min(self.cv_stop(cv),self.pa_up(pa),self.pv_cw_fast(pv)),min(self.cv_right_fast(cv),self.pv_cw_slow(pv)),min(self.cv_left_slow(cv),self.pv_ccw_fast(pv)))
            left_fast=max(min(self.pa_up_more_left(pa),self.pv_ccw_slow(pv)),min(self.pa_up_more_left(pa),self.pv_cw_slow(pv)),min(self.pa_up_more_left(pa),self.pv_ccw_fast(pv)),min(self.pa_down_more_left(pa),self.pv_cw_slow(pv)),min(
                self.pa_down_left(pa),self.pv_cw_slow(pv)),min(self.pa_down_left(pa),self.pv_ccw_slow(pv)),
                min(self.pa_up_left(pa),self.pv_ccw_slow(pv)),min(self.pa_up_left(pa),self.pv_stop(pv)),min(self.pa_up_left(pa),self.pv_ccw_fast(pv)),min(self.pa_up_right(pa),self.pv_ccw_fast(pv)),min(self.pa_up(pa),self.pv_stop(pv)),min(self.cv_left_fast(cv),self.pv_ccw_slow(pv)),min(self.cv_stop(cv),self.pa_up(pa),self.pv_ccw_fast(pv)))   

            
            
            