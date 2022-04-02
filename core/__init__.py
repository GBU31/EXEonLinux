from .wine import Wine

w = Wine()
print(w)
if not w.is_installed():
    w.install()
