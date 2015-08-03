Name:		ovirt-wgt-installer
Version:	3.6.0
Release:	0.1_master%{?dist}
Summary:	oVirt Windows Guest Tools Installer
License:	GPLv2 and GPLv2+ and ASL 2.0 and Zlib and MIT and Python and Platform SDK Redistributable EULA and Microsoft DDK Redistributable EULA
Source:		http://resources.ovirt.org/pub/ovirt-3.5-snapshot/src/ovirt-wgt-%{version}.tgz
URL:		http://www.ovirt.org/Features/oVirt_Windows_Guest_Tools
BuildArch:	noarch
Packager:	Lev Veyde <lveyde@redhat.com>

BuildRequires:	mingw32-nsis >= 2.46
BuildRequires:	mingw32-spice-vdagent >= 0.7.2
BuildRequires:	mingw64-spice-vdagent >= 0.7.2
BuildRequires:	ovirt-guest-agent-windows
BuildRequires:	vcredist-x86
BuildRequires:	virtio-win-drivers
BuildRequires:	spice-qxl

%description
oVirt Windows Guest Tools installer.
The installer includes VirtIO-Win drivers, Spice QXL drivers, as well as oVirt and Spice Guest Agents.

%prep
%setup -n ovirt-wgt -q

%build
mkdir -p bin/vdagent_x86 bin/vdagent_x64
mkdir -p drivers/virtio drivers/qxl

cp /usr/i686-w64-mingw32/sys-root/mingw/bin/vdagent.exe bin/vdagent_x86/
cp /usr/i686-w64-mingw32/sys-root/mingw/bin/vdservice.exe bin/vdagent_x86/
cp /usr/x86_64-w64-mingw32/sys-root/mingw/bin/vdagent.exe bin/vdagent_x64/
cp /usr/x86_64-w64-mingw32/sys-root/mingw/bin/vdservice.exe bin/vdagent_x64/

OVIRTGA=ovirt-guest-agent-windows
cp %{_datadir}/artifacts/$OVIRTGA/OVirtGuestService.exe bin/
cp %{_datadir}/artifacts/$OVIRTGA/default.ini bin/
cp %{_datadir}/artifacts/$OVIRTGA/default-logger.ini bin/
cp %{_datadir}/artifacts/$OVIRTGA/ovirt-guest-agent.ini bin/
cp %{_datadir}/artifacts/vcredist-x86/vcredist_x86.exe bin/

cp -a %{_datadir}/artifacts/virtio-win-drivers/* drivers/virtio/
cp -a %{_datadir}/artifacts/spice-qxl/* drivers/qxl/

makensis -DOVIRT -DEXE_VERSION -D'DISPLAYED_VERSION=%{version}-%{release}' win-guest-tools.nsis

%install
DST=%{buildroot}%{_datadir}/artifacts/%{name}/
mkdir -p $DST
cp %{_builddir}/ovirt-wgt/ovirt-guest-tools-setup.exe $DST
DST=%{buildroot}%{_datadir}/artifacts/%{name}-iso/
mkdir -p $DST
cp %{_builddir}/ovirt-wgt/ovirt-guest-tools-setup.exe $DST
cp -a %{_builddir}/ovirt-wgt/bin $DST
cp -a %{_builddir}/ovirt-wgt/drivers $DST

%files
%{_datadir}/artifacts/%{name}/ovirt-guest-tools-setup.exe

%package iso
Summary: RPM wrapper for %{name}

%description iso
A package wrapping %{name} to provide dependency features.

%files iso
%{_datadir}/artifacts/%{name}-iso

%changelog
* Mon Nov 24 2014 Lev Veyde <lveyde@redhat.com> 0.9.1-2
- Updated oVirt Guest Agent

* Wed Oct 08 2014 Lev Veyde <lveyde@redhat.com> 0.9.1-1
- Initial version
