import os
import subprocess
import numpy
import pandas
import sys
import re
pandas.set_option("display.max_rows", None)
pandas.set_option("display.width", None)
pandas.set_option("display.max_columns", None)
version = "butler" + "1.0"


author = "boss"
pythonexe_bak_path = r"E:\machine4\pythonexe"
# install_pathon_fill_name = r"python-3.6.2rc1-amd64.exe"
install_pathon_path = "F:\\PY36\\"
project_interface_file = r"E:\machine4\machine_sever\main.py"
project_path = "E:\machine4\machine_sever"
project_version_back_file = "E:\machine4\project_version.csv"
project_name = "machine_sever"
# x = subprocess.Popen("dir/W", stdout=subprocess.PIPE, shell=True )
# print(x.communicate()[0].decode("gbk"))
# z = subprocess.Popen(" os.chdir", stdout=subprocess.PIPE, shell=True)
# print(z.communicate()[0].decode("gbk"))
curt_path = os.path.dirname(__file__)
os.chdir("F:\PY36")
# x = subprocess.Popen("dir/W", stdout=subprocess.PIPE, shell=True )
# print(x.communicate()[0].decode("gbk"))
# y = subprocess.Popen("pip install -U pip", stdout=subprocess.PIPE, shell=True )
# print(y.communicate()[0].decode("gbk"))
# print("ffffff")
y = subprocess.Popen("pip list", stdout=subprocess.PIPE, shell=True )
# print(y.communicate()[0].decode("gbk"))
order_list = [
                "pip list",
                "pip install virtualenv",
                "virtualenv venv",  # the last "venv" is the virtualenv install path
                "virtualenv -p /usr/bin/python2.7 venv　　",  # virtualenv used python2.7




]
yy = y.communicate()[0].decode("gbk")

# print(len(yy))
kk = yy.split()
# print(kk)
ff = numpy.array(kk)
ff = ff.reshape((-1, 2))


ffd = pandas.DataFrame(ff)
pip_addr = [
    "https://pypi.python.org/simple",
    "https://pypi.douban.com/simple/",
    "https://mirrors.aliyun.com/pypi/simple",
    "https://pypi.tuna.tsinghua.edu.cn/simple",
    "https://pypi.mirrors.ustc.edu.cn/simple",
]


ffd = ffd.iloc[2:, :]
# ffd.reset_index()
ffd = ffd.set_index(0)
# print(ffd.loc["asgiref", :])

version_base_index = ['project_name', 'project_path', 'project_version', 'project_run_computer_sys',
                      'version_stable_statues', 'back_project_file_path', 'project_code_file_name',
                      'project_code_file_path','project_code_modify_time','project_code_file_file_size',
                      'install_pathon_version', 'install_pathon_path', 'install_pathon_back_path',
                      'virtual_env', 'packet_name', 'packet_version', 'packet_locall_path']

version_data = pandas.DataFrame([], columns=version_base_index)





def path_format_change(path):
    import sys
    sys_version = sys.platform
    if sys_version.startswith("win"):
        path = path.replace("\\", "/")
        return path
    elif sys_version.startswith("linux"):
        path = path.replace("/", "\\")
        return path
    else:
        print(sys_version)
        return None


def get_packet_version(pipexe_path=None):
    import numpy
    import pandas
    pipexe_path = os.path.join(pipexe_path, "/pip.exe") if pipexe_path else "pip list"
    pipexe_path = path_format_change(pipexe_path)
    packet_list = subprocess.Popen(pipexe_path, shell=True, stdout=subprocess.PIPE)
    packet_list_d = packet_list.communicate()

    packet_list_d = packet_list_d[0].decode("gbk")

    packet_list_d = packet_list_d.split()

    packet_list = numpy.array(packet_list_d)

    packet_list = packet_list.reshape((-1, 2))

    packet_list = pandas.DataFrame(packet_list, columns=['Package', 'Version'])

    packet_list = packet_list.drop([0, 1])
    packet_list = packet_list.reset_index(drop=True)
    # print(packet_list)
    # packet_list.index = ["packet_name", "packet_version"]
    return packet_list
class NOPROJECT(Exception):
    def __str__(self):
        return "project not exit"

class install_manager:
    def __init__(self, install_path=None, project_name=None):
        self.sever_cilent_version_map = {}
        self._install_detect_(install_path, project_name)


    def _install_detect_(self, install_path, project_name):
        if (install_path is None) or (project_name is None):
            raise NOPROJECT
            print(NOPROJECT)
        else:
            if os.path.exists(project_version_back_file):

                data = pandas.read_csv(project_version_back_file,)

    def install_packet(self, order):
        install_r = subprocess.Popen(order, shell=True, stdout=subprocess.PIPE)
        print(install_r)

class version_manager:
    # project_path, project_name, project_interface_file, install_pathon_path, version
    def __init__(self, project_name, project_path, project_interface_file=None, python_exe_path=None, version=None, version_back_file=None):
        self.python_exe_path = os.path.join(python_exe_path, "pip.exe list") if python_exe_path else "pip list"
        print(self.python_exe_path)
        self.python_exe_path = path_format_change(python_exe_path)
        self.project_name = project_name
        self.project_path = project_path
        print(self.project_path, "fffffffffffffffffff")
        self.project_interface_file = project_interface_file if project_interface_file else os.path.join(project_path, "main.py")
        self.has_version_data = self.get_saved_data(version_back_file, self.project_name)


        if version is None:
            if self.version is None:
                self.version = self.project_name + "1.0"
        else:
            self.version = version


    def creat_new_version_back_file(self, back_file_path, back_file_name="version_bak.csv"):
        empty_table = version_data
        file_path = os.path.join(back_file_path, back_file_name)
        empty_table.to_csv(file_path, index=False)

    def get_saved_data(self, version_back_file, project_name):
        if (version_back_file is None) or (project_name is None):
            raise NOPROJECT
        else:
            if os.path.exists(project_version_back_file):
                data = pandas.read_csv(project_version_back_file, index_col=False)
            else:
                data = version_data
                data.to_csv(project_version_back_file, index=False)

            self.has_version_data = data

            self.has_version_data.drop_duplicates()
            self.has_version_data.tail()

            print(self.has_version_data.index)
            # print(self.has_version_data.loc[:, "version"])
            version_set = self.has_version_data.loc[:, ["project_name",  "project_version", 'project_run_computer_sys']][self.has_version_data.loc[:, "project_name"] == self.project_name]
            print("kkkkkkkkkkkkkkk88888888888888888888888")

            # print(self.has_version_data.loc[:, "project_version"])
            # version_set = pandas.DataFrame(version_set)
            version_set.drop_duplicates(subset=["project_name",  "project_version", 'project_run_computer_sys'], inplace=True)
            print(version_set)
            if version_set.empty:
                print(version_set)
                self.version = None

                print("im get self.version")
            else:
                if len(version_set) > 1:
                    last_version = version_set.values[-1]
                else:
                    last_version = version_set.values[0]
                print("last version is {}".format(last_version))
                if len(last_version) > 0 :
                    print(last_version, "fffffffffffmmmmmmmmmmm")
                    number = re.search("\.*(\d+)$", last_version[1]).groups()[0]
                    n = len(number)
                    print(n, number)
                    last_version = list(last_version[1])
                    del last_version[-n:]
                    newnumber = str(int(number) + 1)
                    last_version.append(newnumber)
                    self.version = "".join(last_version)


    def get_packet_version(self):
        pipexe_path = path_format_change(self.python_exe_path)
        packet_list = subprocess.Popen(pipexe_path, shell=True, stdout=subprocess.PIPE)
        packet_list_d = packet_list.communicate()
        packet_list_d = packet_list_d[0].decode("gbk")
        packet_list_d = packet_list_d.split()
        packet_list = numpy.array(packet_list_d)
        packet_list = packet_list.reshape((-1, 2))
        packet_list = pandas.DataFrame(packet_list, columns=['Package', 'Version'])
        packet_list = packet_list.drop([0, 1])
        packet_list = packet_list.reset_index(drop=True)
        return packet_list

    def path_format_change(self, path):
        import sys
        sys_version = sys.platform
        if sys_version.startswith("win"):
            path = path.replace("\\", "/")
            return path
        elif sys_version.startswith("linux"):
            path = path.replace("/", "\\")
            return path
        else:
            print(sys_version)
            return None

    def version_detect(self):
        # project_interface_file = project_interface_file if project_interface_file else os.path.join(self.project_path, "main.py")
        project_path2 = path_format_change(self.project_path)

        print(self.project_name, self.project_interface_file, self.project_path, os.getcwd())
        print(os.path.abspath(os.curdir))
        sys.path.append(os.path.abspath(os.curdir))
        current_path = (os.path.dirname(__file__))
        os.chdir(os.path.dirname(self.project_interface_file))

        result = subprocess.Popen("python " + self.project_interface_file, shell=True)
        main_py = self.project_interface_file.split("\\")[-1]



        os.chdir(current_path)
        project_run_computer_sys = sys.platform
        pipexe_path_ = self.path_format_change(self.python_exe_path)
        pipexe_path = pipexe_path_ + "pip list"
        # print(pipexe_path, self.python_exe_path, "xxxxxxxxxxxxxxxxxxxxxx")
        # packet_list = subprocess.Popen(pipexe_path, stdout=subprocess.PIPE, shell=True, cwd=pipexe_path_)
        packet_list = subprocess.Popen("pip list", stdout=subprocess.PIPE, shell=True, cwd=pipexe_path_)
        packet_list.wait(5)
        data, data_in = packet_list.communicate()
        print(data, type(data), "pppppppppppppppppppppppppp")
        data = data.decode()
        data_l = data.split()
        print(len(data_l))
        packet_list = numpy.array(data_l)
        packet_list = packet_list.reshape((-1, 2))

        packet_list = pandas.DataFrame(packet_list, columns=["packet_name", "packet_version"])
        packet_list = packet_list.drop([0, 1])
        packet_list2 = pandas.DataFrame([], columns=version_base_index)
        packet_list2.loc[:, "packet_name"] = packet_list.loc[:, "packet_name"]
        packet_list2.loc[:, "packet_version"] = packet_list.loc[:, "packet_version"]
        packet_list2.loc[:, "project_name"] = self.project_name
        # print(packet_list2.loc[:, "project_name"], "fpfpfpfpfpffppffp")
        packet_list2.loc[:, "project_path"] = project_path2
        packet_list2.loc[:, "project_version"] = self.version
        packet_list2.loc[:, "project_run_computer_sys"] = project_run_computer_sys
        packet_list2.loc[:, "back_project_file_path"] = False
        packet_list2.loc[:, "install_pathon_version"] = sys.version.split()[0]
        packet_list2.loc[:, "install_pathon_back_path"] = pythonexe_bak_path
        packet_list2.loc[:, "install_pathon_fill_name"] = r"python-" + sys.version.split()[0] + r"-amd64.exe"
        packet_list2.loc[:, "install_pathon_path"] = install_pathon_path

        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx2")
        all_file = self.statistic_project_file()
        all_file2 = pandas.DataFrame([], columns=version_base_index)
        all_file = pandas.concat([all_file2, all_file])
        print(all_file)
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx3")
        all_file.loc[:, "project_name"] = self.project_name
        all_file.loc[:, "project_path"] = project_path2
        all_file.loc[:, "project_version"] = self.version
        all_file.loc[:, "project_run_computer_sys"] = project_run_computer_sys
        all_file.loc[:, "back_project_file_path"] = False
        all_file.loc[:, "install_pathon_version"] = sys.version.split()[0]
        all_file.loc[:, "install_pathon_back_path"] = pythonexe_bak_path
        all_file.loc[:, "install_pathon_fill_name"] = r"python-" + sys.version.split()[0] + r"-amd64.exe"
        all_file.loc[:, "install_pathon_path"] = install_pathon_path


        re_data = pandas.concat([packet_list2, all_file], ignore_index=True)

        print(re_data)
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx4")
        re_data.to_csv(project_version_back_file, mode="a", header=False, index=False)
        return re_data

    def statistic_project_file(self):
        columns = ["project_code_file_name", "project_code_file_path", "project_code_modify_time", "project_code_file_file_size"]
        print(self.project_path, "kkkkkkkkkkkkkkkkkkkkkkk")
        all_file = os.walk(self.project_path)
        data = []
        for every in all_file:

            for every_file in every[-1]:
                full_path = os.path.join(every[0], every_file)

                full_path = path_format_change(full_path)

                modify_time = os.path.getmtime(full_path)
                file_size = os.path.getsize(full_path)

                data.append([every_file, every[0], modify_time, file_size])
        data = pandas.DataFrame(data, columns=columns)
        return data
class back_packet_manager:
    def __init__(self):
        self.packet_path = None
        self.stable_vesion = None

    def detect_packet_new_version(self):
        pass

    def find_need_version_packet(self):
        pass

    def download_packet(self, packet_name, path_="E:\machine4\packet_back"):
        """
        numpy-1.19.5-cp36-cp36m-win_amd64
        pip install <包名> -d <目录>
        :param packet_name:
        :return:
        """


        order = "pip download  " + packet_name + " -d " + path_ + " -i " + "https://pypi.douban.com/simple/"
        print(order)
        data = subprocess.Popen(order, shell=True, stdout=subprocess.PIPE)
        data = data.communicate()
        print(data)

    def parse_packet_name(self, packet_name):
        pass

class butler:
    def __init__(self):
        self.install_manager = install_manager()
        self.version_manager = version_manager()
        self.back_packet_manager = back_packet_manager()

    def run_project(self, project_path):
        pass

    def set_project_version_name(self, project_name, author_version,):
        pass

    def path_format_change(self, path):
        import sys
        sys_version = sys.platform
        if sys_version.startswith("Window"):
            path = path.replace("\\", "/")
            return path
        elif sys_version.startswith("linux"):
            path = path.replace("/", "\\")
            return path
        else:
            pass
            return None

# print(sys.version)
# print(os.path.dirname(__file__))
# fm = os.path.dirname(__file__)
# fm = os.path.dirname(fm)
# # fm = fm.replace("/", "\\")
# fm = path_format_change(fm)
# m = os.listdir(os.path.dirname(os.path.dirname(__file__)))
# print("fffffffffffffffffffffffff")
# print(os.path.isdir(r"E:\360MoveData"))
# print(fm)
# for dd in m:
#     path = os.path.join(fm, dd)
#     path = path_format_change(path)
#     print(path, os.path.isfile(path))
#     print(os.path.isdir(path))
# ddf = "G:\baiduyun2\cdd2\BAZX-210.mp4"
# ddff = ddf.split("\\")
#################################################################
# cdr = os.getcwd()
# newdr = project_path
# os.chdir(newdr)
#
# sys.path.insert(0, os.getcwd())
#
# print("fffffffffffffffffffffffffffffffffffff")
# version_back_file = "E:\machine4\\bak\\" + project_name + ".bak"
# version = None
# project_name = "console_station"
# fo = version_manager(project_name, project_path,  project_interface_file, install_pathon_path, version, version_back_file=project_version_back_file)
# pf = fo.version_detect()
# print(pf)
#################################################################

fpp = back_packet_manager()
fpp.download_packet("numpy 1.19.5")
get_packet_version()