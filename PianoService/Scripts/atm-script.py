#!C:\projects\GreatPianoService\PianoService\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'automium==0.2.6','console_scripts','atm'
__requires__ = 'automium==0.2.6'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('automium==0.2.6', 'console_scripts', 'atm')()
    )
