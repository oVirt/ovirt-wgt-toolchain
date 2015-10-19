Name:		python-windows
Version:	2.7.8
Release:	2%{?dist}
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
DST=%{buildroot}%{_datadir}/%{name}/
mkdir -p $DST
cp -v %{_builddir}/%{name}/* $DST

%files
%{_datadir}/%{name}

%changelog
* Tue Oct 20 2015 Yedidyah Bar David <didi@redhat.com> 2.7.8-2
- dropped "artifacts" from all paths

* Wed Oct 08 2014 Lev Veyde <lveyde@redhat.com> 2.7.8-1
- Initial version
