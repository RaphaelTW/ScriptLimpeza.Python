import tkinter as tk
from tkinter import ttk
import subprocess
import threading

class CleanupApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cleanup App")
        
        self.progress_var = tk.DoubleVar()
        self.progress = ttk.Progressbar(self.root, variable=self.progress_var, maximum=100)
        self.progress.pack(pady=10)
        
        self.start_button = tk.Button(self.root, text="Iniciar Limpeza", command=self.start_cleanup)
        self.start_button.pack(pady=5)
        
    def start_cleanup(self):
        self.start_button.config(state=tk.DISABLED)
        self.cleanup_thread = threading.Thread(target=self.run_cleanup)
        self.cleanup_thread.start()
        self.root.after(100, self.check_thread)
        
    def run_cleanup(self):
        cleanup_commands = [
            # ... (comandos de limpeza do Windows aqui)
            "REM ******************** VIVALDI ********************",
            'taskkill /F /IM "vivaldi.exe"',
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\Default\\Cache\\data*.',
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\Default\\Cache\\f*.',
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\Default\\Cache\\index.',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\Default\\"Service Worker"\\Database\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\Default\\"Service Worker"\\CacheStorage\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\Default\\"Service Worker"\\ScriptCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\Default\\GPUCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\GrShaderCache\\GPUCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\ShaderCache\\GPUCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\Default\\Storage\\ext\\',
            
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\"Profile 1"\\Cache\\data*.',
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\"Profile 1"\\Cache\\f*.',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\"Profile 1"\\"Service Worker"\\Database\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\"Profile 1"\\"Service Worker"\\CacheStorage\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\"Profile 1"\\"Service Worker"\\ScriptCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\"Profile 1"\\GPUCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\"Profile 1"\\Storage\\ext\\',
            
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\"Profile 2"\\Cache\\data*.',
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\"Profile 2"\\Cache\\f*.',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\"Profile 2"\\"Service Worker"\\Database\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\"Profile 2"\\"Service Worker"\\CacheStorage\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\"Profile 2"\\"Service Worker"\\ScriptCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\"Profile 2"\\GPUCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\"Profile 2"\\Storage\\ext\\',


            # ... (comandos de limpeza do Edge aqui)
            "REM ******************** EDGE ********************",
            "taskkill /F /IM \"msedge.exe\"",
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Edge\\"User Data"\\Default\\Cache\\data*.',
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Edge\\"User Data"\\Default\\Cache\\f*.',
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Edge\\"User Data"\\Default\\Cache\\index.',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Edge\\"User Data"\\Default\\"Service Worker"\\Database\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Edge\\"User Data"\\Default\\"Service Worker"\\CacheStorage\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Edge\\"User Data"\\Default\\"Service Worker"\\ScriptCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Edge\\"User Data"\\Default\\GPUCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Edge\\"User Data"\\GrShaderCache\\GPUCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Edge\\"User Data"\\ShaderCache\\GPUCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Edge\\"User Data"\\Default\\Storage\\ext\\',

            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Edge\\"User Data"\\"Profile 1"\\Cache\\data*.',
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Edge\\"User Data"\\"Profile 1"\\Cache\\f*.',
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Edge\\"User Data"\\"Profile 1"\\Cache\\index.',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Edge\\"User Data"\\"Profile 1"\\"Service Worker"\\Database\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Edge\\"User Data"\\"Profile 1"\\"Service Worker"\\CacheStorage\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Edge\\"User Data"\\"Profile 1"\\"Service Worker"\\ScriptCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Edge\\"User Data"\\"Profile 1"\\GPUCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Edge\\"User Data"\\"Profile 1"\\Storage\\ext\\',

            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Edge\\"User Data"\\"Profile 2"\\Cache\\data*.',
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Edge\\"User Data"\\"Profile 2"\\Cache\\f*.',
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Edge\\"User Data"\\"Profile 2"\\Cache\\index.',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Edge\\"User Data"\\"Profile 2"\\"Service Worker"\\Database\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Edge\\"User Data"\\"Profile 2"\\"Service Worker"\\CacheStorage\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Edge\\"User Data"\\"Profile 2"\\"Service Worker"\\ScriptCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Edge\\"User Data"\\"Profile 2"\\GPUCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Edge\\"User Data"\\"Profile 2"\\Storage\\ext\\',


            # ... (comandos de limpeza do Firefox aqui)
            "# ******************** FIREFOX ********************",
            "taskkill /F /IM \"firefox.exe\"",
            'REM define qual é a pasta Profile do usuário e apaga os arquivos temporários dali',
            'set parentfolder=C:\\Users\\%USERNAME%\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\',
            'for /f "tokens=*" %%a in (\'dir /b "%parentfolder%" ^| findstr ".*\\.default-release"\') do set folder=%%a',
            'del C:\\Users\\%USERNAME%\\AppData\\local\\Mozilla\\Firefox\\Profiles\\%folder%\\cache2\\entries\\*.',
            'del C:\\Users\\%USERNAME%\\AppData\\local\\Mozilla\\Firefox\\Profiles\\%folder%\\startupCache\\*.bin',
            'del C:\\Users\\%USERNAME%\\AppData\\local\\Mozilla\\Firefox\\Profiles\\%folder%\\startupCache\\*.lz*',
            'del C:\\Users\\%USERNAME%\\AppData\\local\\Mozilla\\Firefox\\Profiles\\%folder%\\cache2\\index*.*',
            'del C:\\Users\\%USERNAME%\\AppData\\local\\Mozilla\\Firefox\\Profiles\\%folder%\\startupCache\\*.little',
            'del C:\\Users\\%USERNAME%\\AppData\\local\\Mozilla\\Firefox\\Profiles\\%folder%\\cache2\\*.log /s /q',


            # ... (outros comandos de limpeza do Vivaldi aqui)
            "REM ******************** VIVALDI ********************",
            'taskkill /F /IM "vivaldi.exe"',
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\Default\\Cache\\data*.',
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\Default\\Cache\\f*.',
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\Default\\Cache\\index.',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\Default\\"Service Worker"\\Database\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\Default\\"Service Worker"\\CacheStorage\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\Default\\"Service Worker"\\ScriptCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\Default\\GPUCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\GrShaderCache\\GPUCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\ShaderCache\\GPUCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\Default\\Storage\\ext\\',
            
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\"Profile 1"\\Cache\\data*.',
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\"Profile 1"\\Cache\\f*.',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\"Profile 1"\\"Service Worker"\\Database\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\"Profile 1"\\"Service Worker"\\CacheStorage\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\"Profile 1"\\"Service Worker"\\ScriptCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\"Profile 1"\\GPUCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\"Profile 1"\\Storage\\ext\\',
            
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\"Profile 2"\\Cache\\data*.',
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\"Profile 2"\\Cache\\f*.',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\"Profile 2"\\"Service Worker"\\Database\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\"Profile 2"\\"Service Worker"\\CacheStorage\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\"Profile 2"\\"Service Worker"\\ScriptCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\"Profile 2"\\GPUCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\"User Data"\\"Profile 2"\\Storage\\ext\\',
    

            # ... (comandos de limpeza do Brave aqui)
            "REM ******************** BRAVE ********************",
            'taskkill /F /IM "brave.exe"',
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\"User Data"\\Default\\Cache\\data*.',
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\"User Data"\\Default\\Cache\\f*.',
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\"User Data"\\Default\\Cache\\index.',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\"User Data"\\Default\\"Service Worker"\\Database\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\"User Data"\\Default\\"Service Worker"\\CacheStorage\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\"User Data"\\Default\\"Service Worker"\\ScriptCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\"User Data"\\Default\\GPUCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\"User Data"\\GrShaderCache\\GPUCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\"User Data"\\ShaderCache\\GPUCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\"User Data"\\Default\\Storage\\ext\\',
        
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\"User Data"\\"Profile 1"\\Cache\\data*.',
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\"User Data"\\"Profile 1"\\Cache\\f*.',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\"User Data"\\"Profile 1"\\"Service Worker"\\Database\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\"User Data"\\"Profile 1"\\"Service Worker"\\CacheStorage\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\"User Data"\\"Profile 1"\\"Service Worker"\\ScriptCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\"User Data"\\"Profile 1"\\GPUCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\"User Data"\\"Profile 1"\\Storage\\ext\\',
        
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\"User Data"\\"Profile 2"\\Cache\\data*.',
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\"User Data"\\"Profile 2"\\Cache\\f*.',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\"User Data"\\"Profile 2"\\"Service Worker"\\Database\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\"User Data"\\"Profile 2"\\"Service Worker"\\CacheStorage\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\"User Data"\\"Profile 2"\\"Service Worker"\\ScriptCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\"User Data"\\"Profile 2"\\GPUCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\"User Data"\\"Profile 2"\\Storage\\ext\\',
 

            # ... (comandos de limpeza do Chrome aqui)
            "REM ******************** CHROME ********************",
            'taskkill /F /IM "chrome.exe"',
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\"User Data"\\Default\\Cache\\data*.',
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\"User Data"\\Default\\Cache\\f*.',
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\"User Data"\\Default\\Cache\\index.',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\"User Data"\\Default\\"Service Worker"\\Database\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\"User Data"\\Default\\"Service Worker"\\CacheStorage\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\"User Data"\\Default\\"Service Worker"\\ScriptCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\"User Data"\\Default\\GPUCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\"User Data"\\GrShaderCache\\GPUCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\"User Data"\\ShaderCache\\GPUCache\\',
        'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\"User Data"\\Default\\Storage\\ext\\',
        
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\"User Data"\\"Profile 1"\\Cache\\data*.',
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\"User Data"\\"Profile 1"\\Cache\\f*.',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\"User Data"\\"Profile 1"\\"Service Worker"\\Database\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\"User Data"\\"Profile 1"\\"Service Worker"\\CacheStorage\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\"User Data"\\"Profile 1"\\"Service Worker"\\ScriptCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\"User Data"\\"Profile 1"\\GPUCache\\',
        'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\"User Data"\\"Profile 1"\\Storage\\ext\\',
        
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\"User Data"\\"Profile 2"\\Cache\\data*.',
            'del C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\"User Data"\\"Profile 2"\\Cache\\f*.',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\"User Data"\\"Profile 2"\\"Service Worker"\\Database\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\"User Data"\\"Profile 2"\\"Service Worker"\\CacheStorage\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\"User Data"\\"Profile 2"\\"Service Worker"\\ScriptCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\"User Data"\\"Profile 2"\\GPUCache\\',
            'rmdir /q /s C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\"User Data"\\"Profile 2"\\Storage\\ext\\',
            
            "exit"

        ],

        for command in cleanup_commands:
            subprocess.call(command, shell=True)
        
    def check_thread(self):
        if self.cleanup_thread.is_alive():
            self.root.after(100, self.check_thread)
        else:
            self.start_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = CleanupApp(root)
    root.mainloop()
