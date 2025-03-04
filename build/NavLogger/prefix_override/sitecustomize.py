import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/james/Documents/dev/Snapshot_Coords/install/NavLogger'
