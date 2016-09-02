%global		_basename pywin32
%global		_pyver py2.7

Name:		%{_basename}-%{_pyver}
Version:	220
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
DST=%{buildroot}%{_datadir}/%{name}/
mkdir -p $DST
cp -v %{_builddir}/%{name}/* $DST

%files
%{_datadir}/%{name}

%changelog
* Fri Sep  2 2016 Sandro Bonazzola <sbonazzo@redhat.com> - 220-1
- rebased on upstream 220

* Tue Oct 20 2015 Yedidyah Bar David <didi@redhat.com> 219-2
- dropped "artifacts" from all paths

* Wed Oct 08 2014 Lev Veyde <lveyde@redhat.com> 219-1
- Initial release
