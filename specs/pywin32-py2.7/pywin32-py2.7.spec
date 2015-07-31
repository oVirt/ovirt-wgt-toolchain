%global		_basename pywin32
%global		_pyver py2.7

Name:		%{_basename}-%{_pyver}
Version:	219
Release:	1%{?dist}
Summary:	RPM wrapper for %{name}
License:	Python
Source:		http://sourceforge.net/projects/%{_basename}/files/%{_basename}/Build%20%{version}/%{_basename}-%{version}.win32-%{_pyver}.exe
URL:		http://sourceforge.net/projects/pywin32/
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
* Wed Oct 08 2014 Lev Veyde <lveyde@redhat.com> 219-1
- Initial release
