Name:		ovirt-guest-tools-iso
Version:	3.5
Release:	7
Summary:	oVirt Windows Guest Tools
License:	GPLv2 and GPLv2+ and ASL 2.0 and Zlib and MIT and Python and Platform SDK Redistributable EULA and Microsoft DDK Redistributable EULA
Source0:	COPYING.csv
Source1:	LICENSES
Source2:	.genisoimagerc
URL:		http://www.ovirt.org/Features/oVirt_Windows_Guest_Tools
BuildArch:	noarch
Packager:	Lev Veyde <lveyde@redhat.com>

BuildRequires:	genisoimage
BuildRequires:	ovirt-wgt-installer-iso

Obsoletes:	ovirt-guest-tools

%description
Windows Guest tools ISO for oVirt Virtualization Manager.

%build
cp %{SOURCE0} %{_builddir}/
cp %{SOURCE2} %{_builddir}/

%install
install -d %{buildroot}%{_datadir}/%{name}/ISO
cp %{SOURCE1} %{buildroot}%{_datadir}/%{name}/ISO
cp -a %{_datadir}/artifacts/ovirt-wgt-installer-iso/* %{buildroot}%{_datadir}/%{name}/ISO
mkisofs -J -r -lsv -V oVirt-Tools-%{version}-%{release} -p "oVirt - KVM Virtualization Manager Project (www.ovirt.org)" -publisher "oVirt - KVM Virtualization Manager Project (www.ovirt.org)" -o %{buildroot}%{_datadir}/%{name}/oVirt-toolsSetup_%{version}_%{release}.iso %{buildroot}%{_datadir}/%{name}/ISO
ln -s %{_datadir}/%{name}/oVirt-toolsSetup_%{version}_%{release}.iso %{buildroot}/%{_datadir}/%{name}/ovirt-tools-setup.iso
rm -rf %{buildroot}%{_datadir}/%{name}/ISO

%files
%{_datadir}/%{name}
%doc COPYING.csv

%changelog
* Mon Nov 24 2014 Lev Veyde <lveyde@redhat.com> 3.5-7
- Updated oVirt Guest Agent (1.0.10.3)

* Wed Oct 22 2014 Lev Veyde <lveyde@redhat.com> 3.5-6
- Volume label was changed to include oVirt prefix
- ISO metada was added

* Wed Oct 08 2014 Lev Veyde <lveyde@redhat.com> 3.5-5
- Initial RPM based version of oVirt Guest Tools
- Includes latest oVirt Guest Agent 1.0.10.2
- Includes Spice Agent 0.7.2
- Includes Spice QXL 0.1-21
- Includes VirtIO-Win 0.1-81
