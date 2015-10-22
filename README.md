oVirt Windows Guest Tools toolchain
===================================

This is a collection of scripts/files to help build ovirt-guest-tools-iso.

Semi-Makefile format to explain the dependencies follows.

- These are just wrappers around existing binaries downloaded from the net:

nsis-simple-service-plugin:

py2exe-py2.7:

python-windows:

pywin32-py2.7:

spice-qxl:

vcredist-x86:

- This one extracts the iso file provided by virtio-win and wraps the result in an rpm:

virtio-win-drivers:

- This one takes the results of building ovirt-wgt-installer, creates an iso, and wraps
it in an rpm, and is the final deliverable, to be used by regular users:

ovirt-guest-tools-iso: ovirt-wgt-installer-iso

- The following are maintained in their own projects, but depend on things from here:

ovirt-guest-agent-windows: py2exe-py2.7 python-windows pywin32-py2.7
	In ovirt-guest-agent

ovirt-wgt-installer-iso: mingw32-nsis mingw32-spice-vdagent mingw64-spice-vdagent ovirt-guest-agent-windows vcredist-x86 virtio-win-drivers spice-qxl nsis-simple-service-plugin
	In ovirt-wgt (aka spice-nsis)

They are used by various jenkins jobs. Generally speaking, when changes
are merged to here, jenkins automatically rebuilds the affected RPMs,
but not the ones depending on them - so you should then rebuild one or more
of those depending on what you changed - ovirt-guest-agent-windows,
ovirt-wgt-installer-iso and ovirt-guest-tools-iso.
