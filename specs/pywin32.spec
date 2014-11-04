Name:		pywin32-py2.7
Version:	219
Release:	1
Summary:	RPM wrapper for %{name}
License:	Python
Source:		http://switch.dl.sourceforge.net/project/pywin32/pywin32/Build%20219/pywin32-219.win32-py2.7.exe
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
