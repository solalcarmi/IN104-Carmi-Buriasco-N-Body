from ..utils.vector import Vector, Vector2
from .constants import G
from ..solvers import RK4
from simulator import Simulator, World, Body


def gravitational_force(pos1, mass1, pos2, mass2):
    """ Return the force applied to a body in pos1 with mass1
        by a body in pos2 with mass2
    """
    F = -G*mass1*mass2*(pos1-pos2)/(((pos1-pos2).norm())**3)
    

    return F

class IEngine:
    def __init__(self, world):
        self.world = world

    def derivatives(self, t0, y0):
        """ This is the method that will be fed to the solver
            it does not use it's first argument t0,
            its second argument y0 is a vector containing the positions 
            and velocities of the bodies, it is laid out as follow
                [x1, y1, x2, y2, ..., xn, yn, vx1, vy1, vx2, vy2, ..., vxn, vyn]
            where xi, yi are the positions and vxi, vyi are the velocities.

            Return the derivative of the state, it is laid out as follow
                [vx1, vy1, vx2, vy2, ..., vxn, vyn, ax1, ay1, ax2, ay2, ..., axn, ayn]
            where vxi, vyi are the velocities and axi, ayi are the accelerations.
        """
        

    def make_solver_state(self) :
        """ Returns the state given to the solver, it is the vector y in
                y' = f(t, y)
            In our case, it is the vector containing the 
            positions and speeds of all our bodies:
                [x1, y1, x2, y2, ..., xn, yn, vx1, vy1, vx2, vy2, ..., vxn, vyn]
            where xi, yi are the positions and vxi, vyi are the velocities.
        """
        raise NotImplementedError


class DummyEngine(IEngine):
    def __init__(self, world):
        super().__init__(world)
        self.world = world
    

    def derivatives(self, t0, y0):
        N = len(self.world)
        deriv = Vector(4*N)
        for i in range(N) :
            deriv[2*i] = y0[(N+i)*2]
            deriv[2*i+1] = y0[(N+i)*2+1]
            acc_i = Vector2(0,0)
            pos_i = Vector2(y0[2*i],y0[2*i+1])
            for j in range(N) :
                if i != j :
                    i_pos = self.world.get(i).position
                    j_pos = self.world.get(j).position
                    if (i_pos.get_x() != j_pos.get_x()) or (i_pos.get_y() != j_pos.get_y()) :
                        acc_i += gravitational_force(pos_i, 1, Vector2(y0[2*j],y0[2*j+1]), self.world.get(j).mass)
                j+=1
            deriv[2*(N+i)] = acc_i.get_x()
            deriv[2*(N+i)+1] = acc_i.get_y()
            i+=1

        return deriv

    def make_solver_state(self):
        """ Returns the state given to the solver, it is the vector y in
                y' = f(t, y)
            In our case, it is the vector containing the 
            positions and speeds of all our bodies:
                [x1, y1, x2, y2, ..., xn, yn, vx1, vy1, vx2, vy2, ..., vxn, vyn]
            where xi, yi are the positions and vxi, vyi are the velocities.
        """
        n = len(self.world)
        y0 = Vector(4*n)
        t0 = 0
        tmax = 10
        dt = 0.01
        i = 0
        
        for body in self.world.bodies():
            y0[i] = body.position.get_x()
            y0[i+1] = body.position.get_y()
            
            y0[i+2*n] = body.velocity.get_x()
            y0[i+1+2*n] = body.velocity.get_y()
            
            i += 2

        return y0
       
        
