from multiprocessing import Process
import psutil
import os
import signal
import time

ok_process = ['MasterPDF.exe', 'KwService.exe', 'WINWORD.EXE', 'PDFConvert.exe',
              '115chrome.exe', 'kwmusic.exe', 'StormPlayer.exe', 'WMIADAP.exe', 'System Idle Process', 'alphase.exe',
              'System', 'NVDisplay.Container.exe', 'smss.exe', 'svchost.exe', 'csrss.exe', 'wininit.exe', 'csrss.exe',
              'services.exe', 'winlogon.exe', 'lsass.exe', 'svchost.exe', 'lsm.exe', 'conhost.exe', 'svchost.exe',
              'svchost.exe', 'svchost.exe', 'audiodg.exe', 'svchost.exe', 'svchost.exe', 'fdhost.exe',
              'NVDisplay.Container.exe', 'svchost.exe', 'sqlwriter.exe', 'sqlbrowser.exe', 'spoolsv.exe',
              'taskhost.exe', 'MsDtsSrvr.exe', 'svchost.exe', 'pycharm64.exe', 'svchost.exe', 'msmdsrv.exe',
              'sqlservr.exe', 'sqlservr.exe', 'mysqld.exe', 'ReportingServicesService.exe', 'dwm.exe', 'svchost.exe',
              'fsnotifier64.exe', 'AlphaseX.exe', 'WmiPrvSE.exe', 'python.exe', 'RtkNGUI64.exe', 'fdlauncher.exe',
              'SearchIndexer.exe', 'SearchProtocolHost.exe', 'SearchFilterHost.exe', 'conhost.exe', 'conhost.exe',
              'explorer.exe', 'SGTool.exe', 'taskmgr.exe', 'mmc.exe', 'DAQM-4200演示.exe', 'QQ.exe', 'EXCEL.EXE',
              '无锡邦赫编码器测试V1.1.exe', 'DAQM-4206C演示V1.4.exe', 'perfmon.exe', 'cmd.exe', 'USR-TCP232-Test-V1.3.exe',
              'mspaint.exe', 'Ssms.exe', 'regedit.exe', 'rundll32.exe', 'iexplore.exe', '360zip.exe', 'SnippingTool.exe',
              "googleearth.exe", "acad.exe", "designer.exe", "notepad.exe",  "firefox.exe",  "geckodriver.exe",
       # next is used by win10
              "SgrmBroker.exe", "fontdrvhost.exe", "sihost.exe", "RuntimeBroker.exe", "StartMenuExperienceHost.exe",
              "ChsIME.exe",  "KuGou.exe",  "Taskmgr.exe",  "bf5_new.exe", "chrome.exe",  "wmplayer.exe",
              "SystemSettings.exe",   ##this file may used by trojan, here wires mouse or keyboard cant use, may it be killed 1
              "SystemSettingsBroker.exe",
              "ShellExperienceHost.exe",
              "WUDFHost.exe",  # bluefeesh driver
              "ApplicationFrameHost.exe",
              "OIS.EXE",

              "BaiduNetdiskRender.exe'",    # for baidu netdisk   will be closed if not used baidudisk
              "BaiduNetdiskHost.exe",    # for baidu netdisk  will be closed if not used baidudisk
              "dllhost.exe",    # for baidu netdisk  will be closed if not used baidudisk
              "BaiduNetdiskRender.exe",    # for baidu netdisk  will be closed if not used baidudisk
              "BaiduNetdisk.exe",    # for baidu netdisk  will be closed if not used baidudisk
              "YunDetectService.exe",    # for baidu netdisk  will be closed if not used baidudisk
              ]

def kill_process():
    killed_set = set()
    newee = True
    while True:
        pids = psutil.pids()
        for pid in pids:
            try:
                p = psutil.Process(pid)
            except Exception as newe:
                newee = False
                print(newe)
                break
            if p.name() in ("baidunetdisk.exe", "SGTool.exe", "baidunetdiskhost.ex", "MySQLInstallerConsole.exe",
                     'AlphaseX.exe',  'ZhuDongFangYu.exe', '360DayPop.exe', '360Newsld.exe', 'MultiTip.exe',
                            'SecurityProxy.exe',  '360DayPop.exe',
                            ):
                try:
                    print(p.name(), p.exe())
                except Exception as e:
                    print(e)
                print(p.name())
                try:
                    os.kill(pid, signal.SIGINT)
                except Exception as ee:
                    print("rogue {} at {} ".format(p.name(), p.exe()), ee)

            if p.name() not in ok_process:
                new_ = (p.name(), p.exe())
                if new_ not in killed_set:
                    killed_set.add(new_)
                    print("****************************")
                    print(new_)

                print("{} is been killed ,beautifule, file path is {}".format(p.name(), p.exe()))
                try:
                    os.kill(pid, signal.SIGINT)
                except Exception as ee:
                    print("rogue {} at {} ".format(p.name(), p.exe()), ee)
        if newee is False:
            newee = True
            continue

        time.sleep(10)

x = Process(target=kill_process())
x.start()
print(ok_process)
