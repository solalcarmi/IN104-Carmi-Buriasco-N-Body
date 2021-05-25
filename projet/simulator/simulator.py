
class Simulator:
    def __init__(self, world, Engine, Solver):
        self.t = 0
        self.world = world

        self.engine = Engine(self.world)

        # Engine uses World to represent the state
        # of the world while Solver uses a
        # vector to represent the current state of
        # the ODE system.
        # The method Engine.make_solver_state computes
        # the vector of state variables (the positions
        # and velocities of the bodies) as a Vector

        y0 = self.engine.make_solver_state()

        self.solver = Solver(self.engine.derivatives, self.t, y0)

    def check_for_collisions(self):
        y = self.solver.y0
        to_delete = []
        for i in range(len(self.world)):
            for j in range(len(self.world)):
                b_i = self.world.get(i)
                b_j = self.world.get(j)
                if i != j and b_i.does_collide(b_j):
                    strongest_body = b_i
                    weakest_body = b_j
                    if b_i.mass <= b_j.mass:
                        to_delete.append(i)
                        strongest_body, weakest_body = b_j, b_i
                    else:
                        to_delete.append(j)
                    strongest_body.mass += weakest_body.mass
        to_delete.sort(reverse=True)
        N = len(self.world._bodies)
        i=0
        for deletable_body_index in to_delete:
            y.remove(y[deletable_body_index + 2 * N + 1])
            y.remove(y[deletable_body_index + 2 * N])
            y.remove(y[deletable_body_index + 1])
            y.remove(y[deletable_body_index])
            i+=1

    def step(self, h):
        import time
        profiler = time.time()
        y = self.solver.integrate(self.t + h)
        print("Time took to integrate", time.time() - profiler)

        for i in range(len(self.world)):
            b_i = self.world.get(i)

            b_i.position.set_x(y[2 * i])
            b_i.position.set_y(y[2 * i + 1])

            b_i.velocity.set_x(y[len(self.world) + 2 * i])
            b_i.velocity.set_y(y[len(self.world) + 2 * i + 1])
            i+=1
        self.t += h
