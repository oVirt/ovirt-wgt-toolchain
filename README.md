oVirt Windows Guest Tools toolchain
===================================

> IMPORTANT: This project has been dropped from oVirt.
>
> Keeping the following section only for reference.



This is a collection of scripts/specfiles to help build dependencies
of ovirt-guest-tools-iso as rpm wrappers around external blobs.

Semi-Makefile format to explain the dependencies follows.

ovirt-guest-agent-windows: py2exe-py2.7 python-windows pywin32-py2.7
	In ovirt-guest-agent

ovirt-guest-tools-iso: mingw32-nsis mingw32-spice-vdagent mingw64-spice-vdagent ovirt-guest-agent-windows vcredist-x86 nsis-simple-service-plugin
	In ovirt-wgt (aka spice-nsis)

They are used by various jenkins jobs. Generally speaking, when changes
are merged to here, jenkins automatically rebuilds the affected RPMs,
but not the ones depending on them - so you should then rebuild one or more
of those depending on what you changed - ovirt-guest-agent-windows,
ovirt-wgt-installer-iso and ovirt-guest-tools-iso.
