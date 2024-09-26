from pyautogui import typewrite, press, hotkey, keyDown, keyUp, hold
import time
import fire


"""
This file contains a VS Code Class that uses autogui to automate some tasks in VS Code.
"""
class VSCode(object):

    print('dung')


    def __init__(self, path, command:str, file=None):
        self.HOT_KEY_MAP = {
            "mash": ["ctrl","shift","alt","command"],
        }
        self.path = path
        
        if not path:
            print("Error: Please provide a path to the git repository.", file=sys.stderr)
            sys.exit(1)
        
        if command == "open terminal":
            self.open_terminal()
        
    def _focus_vs_code(self):
        hotkey('cmd', 'tab')
        
        time.sleep()
        hotkey('cmd', '`')
        time.sleep(1)
        
    def open_terminal(self):
        
        # self._focus_vs_code()
        time.sleep(5)
        for key in self.HOT_KEY_MAP["mash"]:
            keyDown(key)
        
        
        cd_cmd = f"cd {self.path}"
        
        typewrite(cd_cmd)
        
        time.sleep(.2)    


if __name__ == '__main__':
    fire.Fire(VSCode)