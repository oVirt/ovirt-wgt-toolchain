Name:		virtio-win-drivers
Version:	0.1
Release:	110.2%{?dist}
Summary:	RPM wrapper for %{name}
License:	GPLv2
#Stable
#Source:		https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/stable-virtio/virtio-win.iso
#Latest:
Source:	https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/latest-virtio/virtio-win.iso
URL:		https://fedoraproject.org/wiki/Windows_Virtio_Drivers
BuildArch:	noarch
BuildRequires:	p7zip
BuildRequires:	p7zip-plugins
Packager:	Lev Veyde <lveyde@redhat.com>

%description
A package wrapping %{name} to provide dependency features.
virtio-win drivers are already packaged upstream twice - in an RPM and
in an ISO - which use different tree structures for the drivers.
This package wraps in an RPM the drivers from the ISO file, keeping its
tree structure.

%prep

%build

%install
# Path where the artifact will be installed on the host on rpm -i
DST=%{buildroot}%{_datadir}/%{name}/
mkdir -p "${DST}"
7z -o"${DST}" x "%{SOURCE0}"
# current iso has the files read-only for the owner
# And current (109.1) iso also has all files readable only for owner!
chmod -R u=rwX,g=rX,o=rX $DST

%files
%{_datadir}/%{name}

%changelog
* Tue Oct 19 2015 Yedidyah Bar David <didi@redhat.com> - 0.1-110.2
- dropped "artifacts" from all paths

* Mon Aug 17 2015 Sandro Bonazzola <sbonazzo@redhat.com> - 0.1-109.1
* Wed Oct 08 2014 Lev Veyde <lveyde@redhat.com> - 0.1-81.1
- Initial version
