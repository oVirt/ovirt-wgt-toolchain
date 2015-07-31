Name:		virtio-win-drivers
Version:	0.1
Release:	109.1%{?dist}
Summary:	RPM wrapper for %{name}
License:	GPLv2
#Stable
#Source:		https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/stable-virtio/virtio-win.iso
#Latest:
Source:	https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/latest-virtio/virtio-win.iso
URL:		https://github.com/YanVugenfirer/kvm-guest-drivers-windows/
BuildArch:	noarch
BuildRequires:	p7zip
BuildRequires:	p7zip-plugins
Packager:	Lev Veyde <lveyde@redhat.com>

%description
A package wrapping %{name} to provide dependency features.

%prep

%build

%install
# Path where the artifact will be installed on the host on rpm -i
DST=%{buildroot}%{_datadir}/artifacts/%{name}/
mkdir -p "${DST}"
7z -o"${DST}" x "%{SOURCE0}"
# current iso has the files read-only for the owner
chmod -R u+w $DST


%files
%{_datadir}/artifacts/%{name}

%changelog
* Mon Aug 17 2015 Sandro Bonazzola <sbonazzo@redhat.com> - 0.1-109.1
* Wed Oct 08 2014 Lev Veyde <lveyde@redhat.com> - 0.1-81.1
- Initial version
