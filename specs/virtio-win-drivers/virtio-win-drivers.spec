Name:		virtio-win-drivers
Version:	0.1
Release:	81.1
Summary:	RPM wrapper for %{name}
License:	GPLv2
Source:		virtio-win-0.1-81.tgz
URL:		https://github.com/YanVugenfirer/kvm-guest-drivers-windows/
BuildArch:	noarch
Packager:	Lev Veyde <lveyde@redhat.com>

%description
A package wrapping %{name} to provide dependency features.

%prep
%setup -n virtio-win -q
pwd

%build

%install
# Path where the artifact will be installed on the host on rpm -i
DST=%{buildroot}%{_datadir}/artifacts/%{name}/
mkdir -p $DST
cp -av %{_builddir}/virtio-win/* $DST

%files
%{_datadir}/artifacts/%{name}

%changelog
* Wed Oct 08 2014 Lev Veyde <lveyde@redhat.com> 0.1-81.1
- Initial version
