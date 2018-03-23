import subprocess

def exe_cmd(cmd):
    try:
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr = subprocess.PIPE, shell=True)
        #out, err = p.communicate(timeout=15)
        out, err = p.communicate()
        return out, err
    except Exception as e:
        return "", "Exception in subprocess " + str(e)


if __name__ == "__main__":
    o,e = exe_cmd("cp adfhjdf fajdf")
    print(o,e)
