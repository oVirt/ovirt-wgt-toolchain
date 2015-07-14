%global		_basename py2exe
%global		_pyver py2.7

Name:		%{_basename}-%{_pyver}
Version:	0.6.9
Release:	1
Summary:	RPM wrapper for %{name}
License:	MIT
Source:		http://sourceforge.net/projects/%{_basename}/files/%{_basename}/%{version}/%{_basename}-%{version}.win32-%{_pyver}.exe
URL:		http://www.py2exe.org/
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
* Wed Oct 08 2014 Lev Veyde <lveyde@redhat.com> 0.6.9-1
- Initial version
