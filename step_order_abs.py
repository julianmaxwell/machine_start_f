class step():

    def __init__(self, box_pole_obj, machin_obj, box_prepare_obj):
        self.box_pole_obj = box_pole_obj
        self.machin_obj = machin_obj
        self.box_prepare_obj = box_prepare_obj

        self.pause = False

        self.step = [
            self.step_1,
            self.step_1,
            self.step_1,
            self.step_1,
            self.step_1,
            self.step_1,
            self.step_1,
            self.step_1,




                     ]
        self.current_step = []

    def run_set(self):
        self.step[0] = [self.run_0, False, "wait_run"],
        self.step[1] = [self.run_1, False, "wait_run"],
        self.step[2] = [self.run_2, False, "wait_run"],
        self.step[3] = [self.run_3, False, "wait_run"],
        self.step[4] = [self.run_4, False, "wait_run"],
        self.step[5] = [self.run_5, False, "wait_run"],
        self.step[6] = [self.run_6, False, "wait_run"],
        self.step[7] = [self.run_7, False, "wait_run"],


    @contextlib.contextmanager
    def in_run(self,N):
        self.step[N][2] = "begin"
        self.current_step = step[N]
        yield self.step[N][0]()
        self.step[N][2] = "complete"

    def run(self):
        if (self.step[0][1],self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (False,False, False, False, False, False, False):
            with self.in_run(0) as T0:
                 if T0 == True:
                    self.step[0][1] = True
        if (self.step[0][1],self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True,False, False, False, False, False, False):
            with self.in_run(1) as T:
                 if T == True:
                    self.step[1][1] = True
        if (self.step[0][1],self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True,True, False, False, False, False, False):
            with self.in_run(2) as T:
                if T == True:
                    self.step[2][1] = True
        if (self.step[0][1],self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True,True, True, False, False, False, False):
            with self.in_run(3) as T:
                if T == True:
                    self.step[3][1] = True
        if (self.step[0][1],self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True,True, True, True, False, False, False):
            with self.in_run(4) as T:
                if T == True:
                    self.step[4][1] = True
        if (self.step[0][1],self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True,True, True, True, True, False, False):
            with self.in_run(5) as T:
                if T == True:
                    self.step[5][1] = True
        if (self.step[0][1],self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True,True, True, True, True, True, False):
            with self.in_run(6) as T:
                if T == True:
                    self.step[6][1] = True
        if (self.step[0][1],self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True,True, True, True, True, True, True):
            with self.in_run(7) as T:
                if T == True:
                    self.step[7][1] = True
                    return  True

    def run_pause_stop(self,current_step,current_function):
        if self.step.index(self.current_step) == 0:
            pass
        if self.step.index(self.current_step) == 1:
            pass
        if self.step.index(self.current_step) == 2:
            pass

    def run_backward(self):
        if self.step.index(self.current_step) == 0:
            pass
        if self.step.index(self.current_step) == 1:
            pass
        if self.step.index(self.current_step) == 2:
            pass


    def run_1(self):
        self.step[0] = [self.run_0, False, "wait_run"],
        self.step[1] = [self.run_1,False,"wait_run"],
        self.step[2] = [self.run_2, False, "wait_run"],
        self.step[3] = [self.run_3, False, "wait_run"],
        self.step[4] = [self.run_4, False, "wait_run"],
        self.step[5] = [self.run_5, False, "wait_run"],
        self.step[6] = [self.run_6, False, "wait_run"],
        self.step[7] = [self.run_7, False, "wait_run"],

    def run_2(self):
        self.step[0] = [self.run_0, False, "wait_run"],
        self.step[1] = [self.run_1, False, "wait_run"],
        self.step[2] = [self.run_2, False, "wait_run"],
        self.step[3] = [self.run_3, False, "wait_run"],
        self.step[4] = [self.run_4, False, "wait_run"],
        self.step[5] = [self.run_5, False, "wait_run"],
        self.step[6] = [self.run_6, False, "wait_run"],
        self.step[7] = [self.run_7, False, "wait_run"],

    def run_3(self):
        self.step[0] = [self.run_0, False, "wait_run"],
        self.step[1] = [self.run_1, False, "wait_run"],
        self.step[2] = [self.run_2, False, "wait_run"],
        self.step[3] = [self.run_3, False, "wait_run"],
        self.step[4] = [self.run_4, False, "wait_run"],
        self.step[5] = [self.run_5, False, "wait_run"],
        self.step[6] = [self.run_6, False, "wait_run"],
        self.step[7] = [self.run_7, False, "wait_run"],

    def run_4(self):
        self.step[0] = [self.run_0, False, "wait_run"],
        self.step[1] = [self.run_1, False, "wait_run"],
        self.step[2] = [self.run_2, False, "wait_run"],
        self.step[3] = [self.run_3, False, "wait_run"],
        self.step[4] = [self.run_4, False, "wait_run"],
        self.step[5] = [self.run_5, False, "wait_run"],
        self.step[6] = [self.run_6, False, "wait_run"],
        self.step[7] = [self.run_7, False, "wait_run"],

    def run_5(self):
        self.step[0] = [self.run_0, False, "wait_run"],
        self.step[1] = [self.run_1, False, "wait_run"],
        self.step[2] = [self.run_2, False, "wait_run"],
        self.step[3] = [self.run_3, False, "wait_run"],
        self.step[4] = [self.run_4, False, "wait_run"],
        self.step[5] = [self.run_5, False, "wait_run"],
        self.step[6] = [self.run_6, False, "wait_run"],
        self.step[7] = [self.run_7, False, "wait_run"],

    def run_6(self):
        self.step[0] = [self.run_0, False, "wait_run"],
        self.step[1] = [self.run_1, False, "wait_run"],
        self.step[2] = [self.run_2, False, "wait_run"],
        self.step[3] = [self.run_3, False, "wait_run"],
        self.step[4] = [self.run_4, False, "wait_run"],
        self.step[5] = [self.run_5, False, "wait_run"],
        self.step[6] = [self.run_6, False, "wait_run"],
        self.step[7] = [self.run_7, False, "wait_run"],

    def run_7(self):
        self.step[0] = [self.run_0, False, "wait_run"],
        self.step[1] = [self.run_1, False, "wait_run"],
        self.step[2] = [self.run_2, False, "wait_run"],
        self.step[3] = [self.run_3, False, "wait_run"],
        self.step[4] = [self.run_4, False, "wait_run"],
        self.step[5] = [self.run_5, False, "wait_run"],
        self.step[6] = [self.run_6, False, "wait_run"],
        self.step[7] = [self.run_7, False, "wait_run"],

    def run_0(self):
        self.step[0] = [self.run_0, False, "wait_run"],
        self.step[1] = [self.run_1, False, "wait_run"],
        self.step[2] = [self.run_2, False, "wait_run"],
        self.step[3] = [self.run_3, False, "wait_run"],
        self.step[4] = [self.run_4, False, "wait_run"],
        self.step[5] = [self.run_5, False, "wait_run"],
        self.step[6] = [self.run_6, False, "wait_run"],
        self.step[7] = [self.run_7, False, "wait_run"],

