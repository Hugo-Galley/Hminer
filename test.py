

import subprocess
def detect_GPU():
    try:
        result = subprocess.run(['wmic', 'path', 'win32_videocontroller', 'get', 'name'], capture_output=True,
                                text=True)

        if 'NVIDIA' in result.stdout.upper() or 'AMD' in result.stdout.upper() or result.stdout.upper():
            print(result)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False
print(detect_GPU())