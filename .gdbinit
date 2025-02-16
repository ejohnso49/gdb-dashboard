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
gdbundle.init()

end
# -- gdbundle_END

python

import gdb_dashboard

# XXX traceback line numbers in this Python block must be increased by 1
end

# Better GDB defaults ----------------------------------------------------------

set history save
set verbose off
set print pretty on
set print array off
set print array-indexes on
set python print-stack full

# Start ------------------------------------------------------------------------

python gdb_dashboard.Dashboard.start()

# Fixes ------------------------------------------------------------------------

# workaround for the GDB readline issue, see #325
python import sys; sys.modules['readline'] = None

# File variables ---------------------------------------------------------------

# vim: filetype=python
# Local Variables:
# mode: python
# End:
