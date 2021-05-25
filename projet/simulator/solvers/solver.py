class SolverError(Exception):
    pass


class ISolver:

    # NOTE: our systems do not depend on time,
    # so the input t0 will never be used by the
    # the derivatives function f
    # However, removing it will not simplify
    # our functions so we might as well keep it
    # and build a more general library that
    # we will be able to reuse some day

    def __init__(self, f, t0, y0, max_step_size=0.01):
        self.f = f
        self.t0 = t0
        self.y0 = y0
        self.max_step_size = max_step_size

    def integrate(self, t):
        """ Compute the solution of the system at t
            The input `t` given to this method should be increasing
            throughout the execution of the program.
            Return the new state at time t.
        """
        


class DummySolver(ISolver):
    def integrate(self, t):
        """ Compute the solution of the system at t
            The input `t` given to this method should be increasing
            throughout the execution of the program.
            Return the new state at time t.
        """
        t0 = self.t0
        if t-t0 <= self.max_step_size:
            self.y0 = self.y0 + (t-t0)*self.f(t0,self.y0) 
        
        else :
            n = (t-t0) / self.max_step_size
            dt = (t-t0)/int(n+1)
            
            while t0 < t :
                self.y0 = self.y0 + dt*self.f(t0,self.y0)
                t0 += dt
        
        return self.y0
 
class Leapfrog(ISolver):
    
    def integrate(self, t):
        t0 = self.t0
        n = (t-t0)/self.max_step_size
        dt = (t-t0)/int(n+1)
        
        
        while t0 < t :
        
            a = self.f(t,self.y0)
        
            for i in range (len(a)//2):
                self.y0[i] = dt * a[i] + 1/2 * dt**2 * a[len(a)//2 + i]
        
            a2 = self.f(t, self.y0)
        
            for i in range (len(a)//2):
                self.y0[i + len(a)//2] = 1/2 * dt * (a[len(a)//2 + i] + a2[len(a)//2 + i])
            
            t0 += dt
    
    
        return self.y0


class RK4(ISolver):
   
    def integrate(self, t):
        t0 = self.t0
        n = (t-t0)/self.max_step_size
        dt = (t-t0)/int(n+1)
        
        
        while t0 < t :
        
            y1 = len(self.y0)*[0]
            k1 = self.f(t0,self.y0)
            l2 = len(self.y0)*[0]
            l3 = len(self.y0)*[0]
            l4 = len(self.y0)*[0]

            for j in range(len(self.y0)):
                l2[j]=self.y0[j] + dt/2 * k1[j]


            k2 = self.f(self.t0,l2)
            
            for j in range(len(self.y0)):
                l3[j] = self.y0[j] + dt/2 * k2[j] 


            k3 = self.f(self.t0,l3)
            
            for j in range(len(self.y0)):
                l4[j] = self.y0[j] + dt * k3[j] 
            
            
            k4 = self.f(self.t0,l4) 
            
            
            for j in range(len(self.y0)):
                y1[j] = self.y0[j]+dt*(k1[j] + 2*k2[j] + 2*k3[j] + k4[j])
            
            
            
            self.y0=y1
            
            t0 += dt
            
            
              
        return (self.y0)
