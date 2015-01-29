Name:		python-windows
Version:	2.7.8
Release:	1
Summary:	RPM wrapper for %{name}
License:	Python
Source:		https://www.python.org/ftp/python/2.7.8/python-2.7.8.msi
URL:		https://www.python.org/
BuildArch:	noarch
Packager:	Lev Veyde <lveyde@redhat.com>

%description
A package wrapping %{name} to provide dependency features.

%prep
install -d %{_builddir}/%{name}
cp -v %{SOURCE0} %{_builddir}/%{name}

%install
DST=%{buildroot}%{_datadir}/artifacts/%{name}/
mkdir -p $DST
cp -v %{_builddir}/%{name}/* $DST

%files
%{_datadir}/artifacts/%{name}

%changelog
* Wed Oct 08 2014 Lev Veyde <lveyde@redhat.com> 2.7.8-1
- Initial version
