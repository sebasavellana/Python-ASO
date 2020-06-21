import os, subprocess, sys, shutil

namedirs = ['Bash','Powershell','Python']

try:
    if sys.platform == 'win32':
        path = os.environ['TEMP'] + '\\ASO\\'
        for i in namedirs:
            os.makedirs(path + i)
            subprocess.run(['powershell.exe', 'New-Item', path + i +'\\helloworld'])
        subprocess.run(['powershell.exe', 'Get-ChildItem','-Recurse', path])
    elif sys.platform == 'linux':
        path = '/tmp/aso/'
        for i in namedirs:
            os.makedirs(path + i)
            subprocess.run(['touch',path + i + '/helloworld'])
        subprocess.run(['ls','-lR',path])
except FileExistsError:
    print("Directorios ya creados. Se procede a su eliminación")
    for i in namedirs:
        shutil.rmtree(path + i)