# -- gdbundle_BEGIN
# Update GDB's Python paths with the `sys.path` values of the local Python installation,
#  whether that is brew'ed Python, a virtualenv, Conda env, or another system Python.
python

import os,subprocess,sys
# Execute a Python using the user's shell and pull out the sys.path (for site-packages)
paths = subprocess.check_output('python3 -c "import os,sys;print(os.linesep.join(sys.path).strip())"',shell=True).decode("utf-8").split()
# Extend the current GDB instance's Python paths
sys.path.extend(paths)

# Init and load plugins
import gdbundle
gdbundle.init(additional=['gdb_dashboard'])

end
# -- gdbundle_END
