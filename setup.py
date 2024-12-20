import os.path
import venv
import subprocess
import shutil

def setup() -> None:
    path = os.path.abspath(os.path.dirname(__file__))
    venv_path = os.path.join(path, ".venv")
    pip_path = os.path.join(venv_path, "Scripts", "pip.exe")
    requirements_path = os.path.join(path, "requirements.txt")
    pyinstaller_path = os.path.join(venv_path, "Scripts", "pyinstaller.exe")
    
    os.chdir(path)

    if not os.path.isdir(venv_path):
        venv.create(venv_path, with_pip=True)

    subprocess.run([pip_path, "install", "-r", requirements_path])
    pyinstaller_output = subprocess.Popen([
        pyinstaller_path,
        "--distpath",
        f"{path}",
        "--noconfirm",
        f"{os.path.join(path, "Private Game Helper.spec")}"]
    )
    pyinstaller_output.wait()
    os.system("color")
    if pyinstaller_output.returncode:
        input("\033[91mERROR: Could not compile the app. Press any key to exit...\033[0m")
        return
    
    updater_output = subprocess.Popen([
        pyinstaller_path,
        "--distpath",
        f"{path}",
        "--noconfirm",
        f"{os.path.join(path, "updater.spec")}"]
    )
    updater_output.wait()
    
    shutil.move(os.path.join(path, "updater.exe"), os.path.join(path, "Private Game Helper", "updater.exe"))
    
    if updater_output.returncode:
        input("\033[91mERROR: Could not compile the app. Press any key to exit...\033[0m")
        return

    input(f"\33[32mSUCCESS: App compiled to {os.path.join(path, "Private Game Helper")}. Press any key to exit...\033[0m")
    
if __name__ == "__main__":
    setup()