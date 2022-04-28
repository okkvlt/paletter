from paletter_web.settings import ALLOWED_EXTENSIONS

def checkExtensions(f):
    for ext in ALLOWED_EXTENSIONS:
        if f.endswith(ext):
            return True
        
    return False