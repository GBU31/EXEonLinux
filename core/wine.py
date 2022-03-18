from  subprocess import check_output
import os

class Wine:
    def is_installed(self):
        try:
            proc = check_output('dpkg -s wine'.split())
            return True
        except:
            return False

    def install(self): 
         os.system('snap info wine-platform-3-stable')
        
    def run_exe(self, path, **kwargs):
        print(f'-> {path}')
        os.system(f'wine {path}')

    def __repr__(self):
        if self.is_installed():
            return 'wine is installed'
    
        return 'wine is not installed'
