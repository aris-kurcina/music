import platform
import sys
import traceback

def isWindows():
    try:
        return "Windows" in platform.system()

    except Exception:
        traceback.print_exc()

        return "N/A"


def isMacOS():
    try:
        return "Darwin" in platform.system()

    except Exception:
        traceback.print_exc()

        return "N/A"

def isLinux():
    try:
        return "Linux" in platform.system()

    except Exception:
        traceback.print_exc()

        return "N/A"


def getDetails():
    try:
        return("""
        system: %s
        machine: %s
        platform: %s
        """ % (
            platform.system(),
            platform.machine(),
            platform.platform()
        ))

    except Exception:
        traceback.print_exc();

        return "N/A"


print ("details = ", getDetails())
print ("isMacOS = ", isMacOS())
print ("isWindows = ", isWindows())
print ("isLinux = ", isLinux())