Name:		vcredist-x86
Version:	2008.sp1
Release:	1%{?dist}
Summary:	RPM wrapper for %{name}
License:	Platform SDK Redistributable EULA
Source:		http://download.microsoft.com/download/d/d/9/dd9a82d0-52ef-40db-8dab-795376989c03/vcredist_x86.exe
URL:		http://www.microsoft.com/en-us/download/details.aspx?id=5582
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
* Mon Oct 13 2014 Lev Veyde <lveyde@redhat.com> 2008.sp1-1
- Initial version
