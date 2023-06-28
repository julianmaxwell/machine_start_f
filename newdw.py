"""
pip_down_packet()  it update the D:\machine4\packet_bak\packet_down_load_table.csv table
install_local_packet(packet_file_name, file_lock = file_lock) packet_version is the packet file_name
get_project_py_file_to_csv()
this file use up three function work

"""


import sys
import hashlib
import subprocess
import os
import time
import re
# import regex as re
import shutil
from multiprocessing import Lock as plock
import pandas
import numpy
import platform
import datetime
from functools import partial
from concurrent.futures import ProcessPoolExecutor

pandas.set_option("display.max_rows", 10000)
pandas.set_option("display.max_columns", 300)
pandas.set_option("display.width", 1500)

project_packet_version_map_table = r"D:\machine4\project_version.csv"
oldproject_packet_version_map_table = pandas.read_csv(project_packet_version_map_table, header=0)

__all__ = ("update_version_manager_collect_and_backup_py_file",
           "get_installed_packet_version",
           "translate_to_md5",
           "translate_py_file_content_to_md5",
           "pip_down_packet",
           "install_local_packet",
           "uninstall_packet",
           "get_project_py_file_list",
           "manual_down_packet_register_backup",



           "project_file_table",
           "bak_packet_table",
           "project_packet_version_map_table",
           "projects_version_back_path",
           "packet_locall_path",
           "packet_download_source_url",

           )

project_packet_version_colomns = ['project_name', 'project_path', 'project_version', 'project_run_computer_sys',
'version_stable_statues', 'back_project_file_path', 'project_code_file_name', 'project_code_file_path',
'project_code_back_path', 'project_code_modify_time', 'project_code_file_file_size', 'install_pathon_version',
'install_pathon_path', 'install_pathon_back_path', 'virtual_env', 'packet_name', 'packet_version',
'packet_locall_path', 'python_version', 'projec_path_md5', 'project_version_md5_add_time', 'register_time', 'file_md5']
oldproject_packet_version_map_table.columns = project_packet_version_colomns
project_packet_version_colomns = oldproject_packet_version_map_table.columns
projects_version_back_path = "I:\projects_version_save"
packet_download_source_url = r"-i https://pypi.douban.com/simple/ "
# packet_download_source_url = r"-i http://mirrors.aliyun.com/pypi/simple"

packet_locall_path = r"D:\machine4\packet_bak"
sucess_feature = r"Successfully downloaded"
bak_packet_table = r"D:\machine4\packet_bak\packet_down_load_table.csv"
project_file_table = r"D:\machine4\project_file.csv"
project_file_column = [
    "project_name",
    "project_path",
    "file_name",
    "file_path",
    "file_creat_time",
    "file_modify_time",
    "file_last_vist_time",
    "file_statue",

]



file_lock = plock()


def get_installed_packet_version():
    packet_list = subprocess.Popen("pip list", shell=True, stdout=subprocess.PIPE, cwd=r"D:\Python39\Scripts")
    packet_list_d = packet_list.communicate()

    packet_list_d = packet_list_d[0].decode("gbk")
    packet_list_d = packet_list_d.split()

    packet_list = numpy.array(packet_list_d)

    packet_list = packet_list.reshape((-1, 2))
    packet_list = pandas.DataFrame(packet_list, columns=['Package', 'Version'])
    packet_list = packet_list.drop([0, 1])
    packet_list = packet_list.reset_index(drop=True)

    return packet_list




def translate_to_md5(dir_name):
    dir_md5 = hashlib.md5()
    dir_md5.update(dir_name.encode(encoding="utf-8"))
    md5_code = dir_md5.hexdigest()
    return md5_code

def translate_py_file_content_to_md5(file_path):
    if os.path.isfile(file_path):
        with open(file_path) as ff:
            data = ff.read()
            md5_code = translate_to_md5(data)
            return md5_code
    else:
        md5_code = translate_to_md5(file_path)
        return md5_code

def pip_down_packet(packet_name, packet_vesion=None, file_lock = file_lock):
    if r"D:\Python39\Scripts" not in sys.path:
        sys.path.insert(0, r"D:\Python39\Scripts")
    path_ = os.path.join(packet_locall_path, packet_name)
    if packet_vesion is not None:
        path_ = os.path.join(path_, packet_vesion)
    # print(path_)
    if packet_vesion is None:
        order = "pip download -d {} {} {}".format(path_, packet_download_source_url, packet_name)
    else:
        order = "pip download -d {}  {} {}=={} ".format(path_, packet_download_source_url, packet_name, packet_vesion)
    print(order)
    try:
        if os.path.exists(path_):
            print("{} has exists".format(path_))
        else:
            os.makedirs(path_)
            print("{} has creat".format(path_))
    except Exception as ee:
        print(ee)

    single_ = subprocess.Popen(order, shell=True, stdout=subprocess.PIPE, cwd=r"D:\Python39\Scripts")
    try:

        order_return_back, errr = single_.communicate()
        order_utf = order_return_back.decode("gbk")
        print(order_utf)
        # print(errr.decode("gbk"))



    except Exception as e:
        print(e)

    order_utf_split = order_utf.split("\n")

    order_utf_split = list(order_utf_split)
    sucess_index = None
    for xd in order_utf_split:
        if sucess_feature in xd:
            sucess_index = order_utf_split.index(xd)
            break

    result_split = order_utf_split[sucess_index]
    version_data_index = None
    for dd in order_utf_split:
        if packet_name in dd:
            version_data_index = order_utf_split.index(dd) + 1
            print(version_data_index)
            break

    version_parse_data = order_utf_split[version_data_index]
    result_split = version_parse_data.split("/")
    print(result_split)
    result_version = result_split[-1]
    result_version = re.search("(.+)\s\(", result_version)
    result_version = result_version.groups()[0]
    print("file_version", result_version)

    if sucess_index is None:
        shutil.rmtree(path_)
    else:
        new_path_ = os.path.dirname(path_)
        result_version_dir = re.sub(r"\.", "", result_version)
        new_path_ = new_path_ + "\\" + result_version_dir
        os.renames(path_, new_path_.strip())
        columns = ["packet_name", "pip_list_version", "packet_version", "packet_path", "download_time", "sourse_url"]
        pip_version1 = result_version.split("-")
        packet_name2, pip_version, *_ = pip_version1
        print("ffffffffffffffffffffffffffffffffffffffffffffff")
        print(pip_version1)
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaakkkkkkk")
        try:
            current_recorder = pandas.DataFrame([[
                packet_name,
                pip_version,
                result_version,
                new_path_,
                time.time(),
                packet_download_source_url
            ]], columns=columns)
            current_recorder.replace("\n", '', inplace=True, regex=True)
        except Exception as fff:
            print(fff)
        with file_lock:
            current_recorder.to_csv(bak_packet_table, header=False, index=False, mode="a")


def install_local_packet(packet_file_name=None, file_lock = file_lock):
    """

    :param packet_version: is the will install packet file name like: psutil-5.8.0-cp39-cp39-win_amd64.whl
    :param file_lock:
    :param model: "install",  "uninstall"
    :return:
    """
    packet_file_name = packet_file_name.strip()

    with file_lock:
        version_data = pandas.read_csv(bak_packet_table, header=0)
    # version_data.columns = ["packet_name", "packet_version", "packet_file_name", "packet_path", "download_time", "sourse_url"]
    version_data.reset_index(inplace=True, drop=True)
    version_data.set_index(["packet_file_name"], inplace=True)
    packet_path = version_data.loc[packet_file_name, "packet_path"]
    print(packet_path)
    packet_path = packet_path.strip()
    packet_name = version_data.loc[packet_file_name, "packet_name"]
    packet_name = packet_name.strip()
    print(packet_path)
    packet_path = os.path.join(packet_path, packet_file_name)
    if os.path.exists(packet_path):
        order = "pip install " + packet_path
        ff = subprocess.Popen(order, shell=True, stdout=subprocess.PIPE, cwd=r"D:\Python39\Scripts")
        out_trace, err, = ff.communicate()
        out_trace_ = out_trace.decode("gbk")
        print(out_trace_)
        result = get_installed_packet_version()
        if packet_name in result.loc[:, ["Package"]].values:
            print("packet {} is install ok ".format(packet_path))
            return True
        else:
            print("packet_ {} not exist".format(packet_path))
            return False
    else:
        print("packet_ {} not exist".format(packet_path))
        return False

def uninstall_packet(packet_name):
    packet_name = packet_name.strip()
    installed_packet = get_installed_packet_version()
    installed_packet = installed_packet.loc[:, "Package"].values
    if packet_name in installed_packet:
        print("i will uninstall {}".format(packet_name))
        order_ = installed_packet
        ff = subprocess.Popen(order_, shell=True, stdout=subprocess.PIPE, cwd=r"D:\Python39\Scripts")
        out_trace, err, = ff.communicate()
        out_trace_ = out_trace.decode("gbk")
        print(out_trace_)
        installed_packet2 = get_installed_packet_version()
        installed_packet2 = installed_packet2.loc[:, "Package"].values
        if packet_name not in installed_packet2:
            print("uninstall {} ok".format(packet_name))
        else:
            print("uninstall {} failed try it agin".format(packet_name))

py_file = set()


def get_project_py_file_list(project_path_, project_name=None, py_file=py_file):
    if project_name is not None:
        project_path_new = os.path.join(project_path_, project_name)

    else:
        project_path_new = project_path_
    for root, dir_names, files_name in os.walk(project_path_new, topdown=True):

            for xr in files_name:
                try:
                    xr2 = re.search(".*\.(.*)$", xr, re.IGNORECASE)
                    if xr2:
                        type_ = xr2.groups()[0]
                        if type_.lower() == "py":
                            py_file_path = os.path.join(root, xr)
                            file_md5 = translate_py_file_content_to_md5(py_file_path)
                            py_file.add((xr, py_file_path, file_md5))
                except Exception as e:
                        pass
    py_file = list(py_file)
    return py_file

def get_project_py_file_to_csv(project_path_, project_name=None, py_file=py_file):
    old_data = get_project_py_file_list(project_path_, project_name=project_name, py_file=py_file)

    print(old_data)

    temprory_data = pandas.DataFrame([], columns=project_file_column,)
    try:
        project_file_data = pandas.read_csv(project_file_table, index_col=None)
        project_file_data.columns = project_file_column
    except Exception as e:
        temprory_data.to_csv(index=False, columns=project_file_column, header=True)
        project_file_data = pandas.DataFrame([], columns=project_file_column,)

    if project_name is None:
        project_name_path_1 = project_path_.strip("\\")
        project_name_path_2 = project_name_path_1.split("\\")
        project_path__ = project_name_path_2[-1]
        project_name = project_path__

    for filename, file_path, file_md5 in old_data:
        file_creat_time = os.path.getctime(file_path)
        file_modify_time = os.path.getmtime(file_path)
        file_last_vist_time = os.path.getatime(file_path)
        add_data = {
            "project_name": project_name,
            "project_path": project_path_,
            "file_name": filename,
            "file_path": file_path,
            "file_creat_time": file_creat_time,
            "file_modify_time": file_modify_time,
            "file_last_vist_time": file_last_vist_time,
            "file_statue": True,
        }

        temprory_data = temprory_data.append(add_data, ignore_index=True)

    temprory_data.drop_duplicates(["file_path"], inplace=True)

    new_ = pandas.concat([project_file_data, temprory_data], axis=0)
    # print("concat len is {}".format(len(new_)))
    new__ = new_.drop_duplicates(["project_path", "file_path", "file_creat_time",  "file_modify_time"], keep="first")
    add_data2 = new__.iloc[len(project_file_data):, :]
    if len(add_data2) > 0:
        print("{} data add".format(len(add_data2)))
        add_data2.to_csv(project_file_table, index=False, header=False, mode="a", encoding="gbk")
    print("project file check check ok")

def time_forward_str(s):
    loc_time = time.localtime(s)
    str_time = time.strftime("%Y-%m-%d %H:%M:%S", loc_time)
    return str_time



def project_temporary_process_py_file(project_name_, project_path):
    all_data = get_project_py_file_list(project_path, project_name_)
    print(all_data)
    print(project_name_)
    print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
    x1 = platform.system()
    x2 = platform.version()
    project_run_computer_sys = x1 + x2
    pd_add_new_file_statue = pandas.DataFrame([], columns=project_packet_version_colomns)
    tim_ = time.time()
    tim_ = time.localtime(tim_)
    str_time = time.strftime("%Y-$m-$d $H:$M:$S", tim_)
    projec_path_md5 = translate_py_file_content_to_md5(os.path.join(project_path, project_name_))
    for filename, file_path , file_md5 in all_data:
        project_code_modify_time = os.path.getmtime(file_path)
        project_code_modify_time = time.localtime(project_code_modify_time)
        project_code_modify_time = time.strftime("%Y-%m-%d %H:%M:%S", project_code_modify_time)

        project_code_file_file_size = os.path.getsize(file_path)
        pd_add_new_file_statue_dict = {'project_name': project_name_,
                                       'project_path': project_path,
                                       'project_version': None,
                                       'project_run_computer_sys': project_run_computer_sys,
                                       'version_stable_statues': "Test",
                                       'back_project_file_path': None,
                                       'project_code_file_name': filename,
                                       'project_code_file_path': file_path,
                                       'project_code_modify_time': project_code_modify_time,
                                       'project_code_file_file_size':project_code_file_file_size,
                                        'install_pathon_version': None,
                                       'install_pathon_path': None,
                                       'install_pathon_back_path': None,
                                       'virtual_env': None,
                                       'packet_name': None,
                                       'packet_version': None,
                                       'packet_locall_path': None,
                                       'projec_path_md5': projec_path_md5,
                                       'file_md5': file_md5,
                                       'register_time': str_time
                                        }
        pd_add_new_file_statue = pd_add_new_file_statue.append(pd_add_new_file_statue_dict, ignore_index=True)
    pd_add_new_file_statue.drop_duplicates(inplace=True)



    return pd_add_new_file_statue

def shutil_copy_order(data):
    project_name_ = data.loc["project_name"]
    print("KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK")
    print(project_name_)

    sourse = data.loc["project_code_file_path"]
    print(sourse)
    target = data.loc["back_project_file_path"]
    x = "D:\machine4\manager_port_sever"
    sp = x[2]
    xx = sourse.split(sp)
    sourse_next_index = xx.index(project_name_)
    sourse_next_ = xx[(sourse_next_index + 1):]
    target = os.path.join(target, *sourse_next_)
    if os.path.exists(target):
        pass
    else:
        target = os.path.dirname(target)
        if os.path.exists(target):
            pass
        else:
            os.makedirs(target)

        print(target)


    shutil.copy(sourse, target)
    return target


def update_version_manager_collect_and_backup_py_file(project_name_, project_path, project_version=None, version_stable_statues="Test", back_order=False):
    """
    this function use the project_version.csv file to control the version. and backup the *.py file
    :param project_name_:
    :param project_version:
    :param project_path:
    :param version_stable_statues: "Test" or "stable"
    :return:
    """

    will_process_data = project_temporary_process_py_file(project_name_, project_path)

    will_process_data.loc[:, "version_stable_statues"] = version_stable_statues
    x1 = platform.system()
    x2 = platform.version()
    sys_version = x1 + x2
    projects_version_back_path_inner = projects_version_back_path
    md5_dir = os.path.join(project_path, project_name_)
    md5_dir_code = translate_to_md5(md5_dir)
    part1 = os.path.join(projects_version_back_path_inner, md5_dir_code, project_name_)
    old_version1 = pandas.read_csv(project_packet_version_map_table, header=0)
    old_version2 = old_version1.loc[:][old_version1.loc[:, "projec_path_md5"] == md5_dir_code]
    old_version2 = old_version2.loc[:][old_version1.loc[:, "project_run_computer_sys"] == sys_version]
    if len(old_version2) == 0:
        if project_version is not None:
            if version_stable_statues == "Test":
                version_name = project_name_ + sys_version + "Test" + project_version
            else:
                version_name = project_name_ + sys_version + project_version
            version_number = project_version
            will_process_data.loc[:, "project_version"] = version_number

        else:
            if version_stable_statues == "Test":
                version_name = project_name_ + sys_version + "Test" + "version1.0"
            else:
                version_name = project_name_ + sys_version + "version1.0"
            version_number = "version1.0"
        will_process_data.loc[:, "project_version"] = version_number
        porject_back_path = os.path.join(part1, sys_version, version_name)
        will_process_data.loc[:, "back_project_file_path"] = porject_back_path
    else:

        old_type_seriers = old_version2.tail(1)
        old_type = old_type_seriers.loc[:, "version_stable_statues"].values[0]
        old_version = old_type_seriers.loc[:, "project_version"].values[0]

        # last_version_number = str(int(re.search("\.(\d+)$", old_version).groups()[0]) + 1)
        last_version_number = re.search("\.(\d+)$", old_version)
        last_version_number = last_version_number.groups()[0]
        last_version_numberold = last_version_number
        last_version_number = int(last_version_number)
        last_version_number = last_version_number + 1
        last_version_number = str(last_version_number)
        if len(last_version_number) < len(last_version_numberold):
            last_version_number = last_version_number.rjust(len(last_version_numberold), "0")
        prelen = len(old_version) - len(last_version_numberold)
        pre_str = old_version[0: prelen]

        if version_stable_statues == "Test":
            if old_type == "Test":
                version_name =project_name_ + sys_version + pre_str + last_version_number
                porject_back_path = os.path.join(part1, sys_version, version_name)
                version_number = pre_str + last_version_number
            elif old_type == "stable":
                pre_str = pre_str + last_version_number + ".1"

                version_name = project_name_ + sys_version + "Test" + pre_str
                porject_back_path = os.path.join(part1, sys_version, version_name)
                version_number = pre_str
            will_process_data.loc[:, "project_version"] = version_number
            porject_back_path = os.path.join(part1, sys_version, version_name)
            will_process_data.loc[:, "back_project_file_path"] = porject_back_path
        elif version_stable_statues == "stable":
            if old_type == "Test":
                pre_str = pre_str[0: -1]
                version_name = project_name_ + sys_version + pre_str
                porject_back_path = os.path.join(part1, sys_version, version_name)
                version_number = pre_str
            elif old_type == "stable":
                version_name = project_name_ + sys_version + pre_str + last_version_number
                version_number = pre_str + last_version_number
                porject_back_path = os.path.join(part1, sys_version, version_name)
            will_process_data.loc[:, "project_version"] = version_number
            porject_back_path = os.path.join(part1, sys_version, version_name)
            will_process_data.loc[:, "back_project_file_path"] = porject_back_path
    project_version_md5_add_time1 = project_path + project_name_ + str(time.time())
    project_version_md5_add_time = translate_to_md5(project_version_md5_add_time1)
    will_process_data.loc[:, "project_version_md5_add_time"] = project_version_md5_add_time
    will_process_data.loc[:, "project_run_computer_sys"] = sys_version
    will_process_data.loc[:, "version_stable_statues"] = version_stable_statues
    will_process_data.loc[:, "register_time"] = pandas.to_datetime(datetime.datetime.now())
    try:
        last_project_version_md5_add_time = old_version2.loc[:, "project_version_md5_add_time"].values[-1]
    except Exception:
        last_project_version_md5_add_time = pandas.NaT

    if pandas.isna(last_project_version_md5_add_time):

        will_process_data.to_csv(project_packet_version_map_table, index=False, header=False, mode="a", encoding="gbk")
        will_process_data.apply(shutil_copy_order, axis=1)
    else:

        last_version_file_md5_set1 =old_version2.loc[:, "file_md5"][old_version2.loc[:, "project_version_md5_add_time"] == last_project_version_md5_add_time]

        last_version_file_md5_set2 = last_version_file_md5_set1.values

        last_version_file_md5_set = set(last_version_file_md5_set2)
        current_version_file_mdt_set = set(will_process_data.loc[:, "file_md5"])
        if last_version_file_md5_set != current_version_file_mdt_set:
            print("ppppppppppppppppppppppppppppppppppppp")
            print(will_process_data)
            will_process_data.to_csv(project_packet_version_map_table, index=False, header=False, mode="a", encoding="gbk")
            will_process_data.apply(shutil_copy_order, axis=1)



project_porject_name_map_path = pandas.read_csv("D:\machine4\project_name_path_map.csv",  encoding="gbk")
# print(project_porject_name_map_path)

def manual_down_packet_register_backup(path_="D:\machine4\will_registor_packet", backpath="D:\machine4\packet_bak"):
    """
    the packet must download by operator self, and use this function to register the packet file. and backup
    use "D:\machine4\packet_bak\packet_down_load_table.csv" manager it
    :param path_:
    :param backpath:
    :return:
    """


    regist_table = pandas.read_csv(bak_packet_table, header=0, encoding="gbk")
    # regist_table.columns = ["packet_name", "packet_version", "packet_file_name", "packet_path", "download_time", "sourse_url"]
    has_ad = regist_table.loc[:, "packet_name"].values
    new_table = pandas.DataFrame([], columns=regist_table.columns)
    new_add = {}

    for root, dir_names, files_name in  os.walk(path_):
        for ever_packet in files_name:

            ever_packet_path = os.path.join(root, ever_packet)
            print(ever_packet, type(ever_packet))
            new_path = os.path.join(backpath, ever_packet)
            version_ = re.search("-(.+)-", ever_packet).groups()[0]

            if not os.path.exists(new_path):
                os.makedirs(new_path)
            else:
                new_file_path = os.path.join(new_path, ever_packet)
                if os.path.exists(new_file_path):
                    os.remove(ever_packet_path)
                    if ever_packet_path not in has_ad:
                        new_add["packet_name"] = ever_packet
                        new_add["packet_version"] = version_
                        new_add["packet_file_name"] = ever_packet
                        new_add["packet_path"] = new_path
                        new_add["download_time"] = pandas.to_datetime(datetime.datetime.now())
                        new_add["sourse_url"] = "official website"
                        new_table = new_table.append(new_add, ignore_index=True)
                else:
                    shutil.copy(ever_packet_path, new_path)
                    new_add["packet_name"] = ever_packet
                    new_add["packet_version"] = None
                    new_add["packet_file_name"] = ever_packet
                    new_add["packet_path"] = new_path
                    new_add["download_time"] = pandas.to_datetime(datetime.datetime.now())
                    new_add["sourse_url"] = "official website"
                    new_table = new_table.append(new_add, ignore_index=True)
                    os.remove(ever_packet_path)
    new_table.to_csv(bak_packet_table, header=False, mode="a", encoding="gbk", index=False)

def version_back_process(p_name_pth_data):
    update_version_manager_collect_and_backup_py_file(p_name_pth_data.loc["project_name"], p_name_pth_data.loc["project_path"])

if __name__ == "__main__":
    # pool_process = ProcessPoolExecutor(5)
    # pool_process.submit(pip_down_packet, "eventlet")
    # pool_process.submit(pip_down_packet, "PyQt5-tools")

    # pool_process.submit(pip_down_packet, "Scrapy")
    # pool_process.submit(pip_down_packet, "pandas")
    # pp = pool_process.submit(pip_down_packet, "qtdisgner")
    # pp = pool_process.submit(pip_down_packet, "psutil")
    # pool_process.shutdown()


    install_local_packet("eventlet-0.31.0-py2.py3-none-any.whl")
    # install_local_packet("setuptools-57.0.0-py3-none-any.whl")
    # install_local_packet("D:\machine4\packet_bak\pyqt5_tools-515432-py3-none-anywhl")
    # install_local_packet("psutil-5.8.0-cp39-cp39-win_amd64.whl ")
    # install_local_packet("PyQt5_sip-12.9.0-cp39-cp39-win_amd64.whl")
    # install_local_packet("wheel-0.36.2-py2.py3-none-any.whl")
    # install_local_packet("pyinstaller-pyinstaller-v4.3-128-g5a3c858.zip", model="uninstall")
    # install_local_packet("pyinstaller-4.3-py3-none-any.whl")

    # install_local_packet("Scrapy-2.5.0-py2.py3-none-any.whl")

    #
    # project_path = "D:\machine\机器端"
    # get_project_py_file_to_csv(project_path)
    # a = 5
    # project_list = []
    # project_name = "manager_port_sever"


    # project_path = "D:\machine"
    # project_path = project_path[0:3]
    # print(project_path)
    # update_version_manager_collect_and_backup_py_file("机器端", project_path, )


    # map(update_version_collect_and_backup_py_file, project_list)

    # project_porject_name_map_path.apply(version_back_process, axis=1)
    # update_version_collect_and_backup_py_file("机器端", "D:\machine")
    # ff = get_installed_packet_version()
    # print(ff)
    # manual_down_packet_register_backup()   # 手动下载包登记

    # uninstall_packet("PyQt5")

    pass