from .wine import Wine
import os

w = Wine()
print(w)
if not w.is_installed():
    w.install()
    
    
