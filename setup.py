from cx_Freeze import setup, Executable

base = None    

executables = [Executable("youtube-downloader.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "youtube-downloader",
    options = options,
    version = "0.0.1",
    description = 'Download youtube videos',
    executables = executables
)
