import pandas
import re
import os
import shutil
import subprocess
import hashlib

__all__ = (
    "pyinstaller_change_py_to_exe",
    "install_python_exe_file",
    "test_packet_install_",
    "pyinstaller_change_py_to_exe",
)
# from newdw import *
pandas.set_option("display.max_rows", 10000)
pandas.set_option("display.max_columns", 300)
pandas.set_option("display.width", 1500)
pythons_exe_install_path = "D:\pythons_install"

bak_packet_table_path = r"D:\machine4\packet_bak\packet_down_load_table.csv"
order = "python.exe"
order_list = pandas.read_csv(bak_packet_table_path, header=0, encoding="gbk")
order_list = order_list.sort_values(by=["packet_name", "packet_version"])
order_list.drop_duplicates(["packet_file_name"], inplace=True)
order_list = order_list.set_index("packet_name")
installe_pythonexe = order_list.loc["python", :]

will_install = installe_pythonexe.loc[:, "packet_file_name"].values
py_file = set()

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

def get_project_py_file_list(project_path_, project_name=None, py_file=set()):
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


def install_python_exe_file(file_name, file_path=pythons_exe_install_path):
    file_name = file_name.strip()
    try:
        suffix = re.search("(.+)amd64.exe$", file_name).groups()[0]
        install_path = os.path.join(file_path, suffix)
        if not os.path.exists(install_path):
            os.makedirs(install_path)
    except Exception:
        suffix = None

    if suffix is not None:
        packet_local_file_path_no_file_name = installe_pythonexe.loc[:, "packet_path"][installe_pythonexe.loc[:, "packet_file_name"] == file_name].values[0]
        packet_local_file_path = os.path.join(packet_local_file_path_no_file_name, file_name)
        print(install_path)
        print(packet_local_file_path)
        target_copy_file_path = os.path.join(install_path, file_name)
        if not os.path.exists(target_copy_file_path):
            shutil.copy(packet_local_file_path, install_path)
        # raise Exception
        # ff = subprocess.Popen(target_copy_file_path, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding="gbk", cwd=install_path)

#          order = "pip install " + packet_path

def test_packet_install_(packet_name, packet_version, python_version):
    """
    test the packet can or not install in the specify version python.exe
    :param packet_name:
    :param packet_version:
    :param python_version:
    :return:
    """
    packet_name = packet_name.strip()
    packet_version = packet_version.strip()
    newlist = order_list.loc[packet_name, ["packet_version", "packet_path", "packet_file_name"]]
    newlist = newlist.loc[:,  ["packet_path", "packet_file_name"]][newlist.loc[:, "packet_version"] == packet_version]


    will_install_test_packet_back_path = os.path.join(newlist.loc[:, "packet_path"].values[0], newlist.loc[:,"packet_file_name"].values[0])
    print("i m {} i will be test".format(will_install_test_packet_back_path))
    add_path = "python" + "-" + python_version + "-"
    work_path = os.path.join(pythons_exe_install_path, add_path)
    python_version_path = os.path.join(pythons_exe_install_path, add_path, "python.exe")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    if os.path.exists(python_version_path):
        ff = subprocess.Popen("python", shell= True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=work_path, encoding="gbk")
        order_install = "pip install  " + will_install_test_packet_back_path
        print("yyyyyyyyyyyyyyyyyyyyyyyyyyyy")
        ff.stdin.write(order_install)
        pp = ff.stdout.readlines()
        for p in pp:
            print(p)

def get_current_file_find_it_program_version(file_name_path):
    project_path = os.path.dirname(file_name_path)
    py_files_list = get_project_py_file_list(project_path)
    print(py_files_list)

def pyinstaller_change_py_to_exe(file_name_path, pyinstallerexe_path="D:\Python39\Scripts"):
    order = "pyinstaller -Fw " + file_name_path
    print(order)
    ff = subprocess.Popen(order, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=pyinstallerexe_path)
    kk, err =ff.communicate()
    # print(err)
    erlist = err.decode("utf-8")
    # print(erlist)
    erlist = erlist.split("\n")
    print(erlist)
    while True:
        if len(erlist[-1]) == 0:
            del erlist[-1]
        else:
            break

    print(erlist[-1])
    if "completed successfully." in erlist[-1]:
        print("install is ok")

    file_basname = os.path.basename(file_name_path)
    exe_file_name_pr = re.search("(.+)\.py$", file_basname).groups()[0]

    exe_creat_path = os.path.join(pyinstallerexe_path, "dist")
    new_exe_file_name = exe_file_name_pr + ".exe"
    exe_soure = os.path.join(exe_creat_path, new_exe_file_name)
    exe_move_path = os.path.dirname(file_name_path)
    shutil.copy(exe_soure, exe_move_path)
    os.remove(exe_soure)



if __name__ == "__main__":
    # test_packet_install_("pyinstaller", "4.3", "3.7.9")
    #
    # for every in will_install:
    #     # print(every)
    #     install_python_exe_file(every)
    print('begin')
    # pyinstaller_change_py_to_exe(r"D:\machine\机器端\test4.py")
    # pyinstaller_change_py_to_exe(r"D:\kill_virus\kill_program.py")

    # get_current_file_find_it_program_version(r"D:\kill_virus\kill_program.py")
    pyinstaller_change_py_to_exe(r"D:\kill_virus\kill_program.py")