"""
this is the machine engine setting used only machine engine
"""

import pickle
import struct
import psutil
import wmi
import os
first_recev_data_buffer = 4
normal_buffer = 1024
lost_client_distroy_time = 60*10
project_packet_version_map_table = r"D:\machine4\project_version.csv"
task_make_module_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks_")
if not os.path.exists(task_make_module_path):
    os.makedirs(task_make_module_path)
# print("task_path :", task_make_module_path)
def get_bios_cpu_number():
    data = wmi.WMI()
    for cpu in data.Win32_Processor():
        cup_id = cpu.ProcessorId.strip()
        # cup_core_number = cpu.NumberOfCore
    for bios in data.Win32_BaseBoard():
        bios_id = bios.SerialNumber

    return cup_id, bios_id
cpu_core_number = psutil.cpu_count()
cup_id, bios_id = get_bios_cpu_number()
mchine_id = get_bios_cpu_number()
machine_id_str = str(cup_id) + "-" + str(bios_id)
bmachine_id = str(pickle.dumps(mchine_id))

bmachine_id_ = (len(bmachine_id), bmachine_id)
b_machine_id_len = struct.pack("i", len(bmachine_id))

# print(bmachine_id_)
"""
"from_manager_sever_ip": (("127.0.0.1", 62000), "thread", 2),
the 2 is the ip level. if is 1, it must used the que. it self.
                       if is 2, it used the  port_map_process_table[-1] minimum data que
"""
local_host = "127.0.0.1"


"""
 ["127.0.0.1", 62001, "to_manager_sever_ip", None], the data None is the timedelta.
"""
