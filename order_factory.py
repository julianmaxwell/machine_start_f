import pandas

import order_abc
import inspect
import asyncio
order_class_list = []


class order_meta(type):

    def __init__(self, class_name, inherit, attr):
        type.__init__(self, class_name, inherit, attr)
        order_class_list.append(self)
        print(inspect.currentframe().f_code.co_names)

class simulate_single(order_abc.EveryMachineRunOrder, metaclass=order_meta):
    async def run(self):
        self.delta_time = 0.01
        sleep_ = asyncio.sleep
        Equepment_tigger_tooch_f_coordinate = self.interface_operator_obj.machine_obj.main_beam.Equepment_tigger_tooch_f
        Equepment_pressure_warter_data = self.interface_operator_obj.machine_obj.main_beam.Equepment_pressure_warter
        result1 = self.interface_operator_obj.machine_obj.drill_box.Equepment_drill_box_digit_piont.grap_hand_stop()

        while True:
            if Equepment_tigger_tooch_f_coordinate.simulation:
                data = await self.read_data()
                Equepment_tigger_tooch_f_coordinate.coordinate = data  # here get the data.
                await sleep_(self.delta_time)

    def read_exe(self, ars):

        data = pandas.read_csv(r"D:\machine\机器端\nnnnnn.csv")
        data = data.loc[:, ["delta_time", "current_push_pull_gear", "beam_coordinate", "hand_coordinate", "beam_coordinate", "messure_push_pull", "messure_drill", "messure_water"]]
        if ars == "beam_coordinate":
            return data.loc[:, "delta_time", "beam_coordinate", "messure_push_pull"]
        if ars == "hand_coordinate":
            return data.loc[:, "delta_time", "hand_coordinate", "messure_push_pull"]

    def __read__(self):
        pass

    async def read_data(self, loop):
        """
        gear [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        pressure  slow 0-35, 0-35  quick 0-20 0-20
        here can simulation all of the statue
        """

        while True:
            data = loop.call_later(0.02, self.__read__, "data")

            pass



