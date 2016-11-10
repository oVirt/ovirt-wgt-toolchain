Name:		nsis-simple-service-plugin
Version:	1.30
Release:	1%{?dist}
Summary:	RPM wrapper for %{name}
License:	MPLv1.1 or LGPLv2+
Source:		http://nsis.sourceforge.net/mediawiki/images/c/c9/NSIS_Simple_Service_Plugin_1.30.zip
URL:		http://nsis.sourceforge.net/NSIS_Simple_Service_Plugin
BuildArch:	noarch
Packager:	Yedidyah Bar David <didi@redhat.com>

%description
A package wrapping %{name} to provide dependency features.

%prep
%setup -c -n %{name}

%install
DST=%{buildroot}%{_datadir}/nsis/Plugins
mkdir -p $DST
cp -v %{_builddir}/%{name}/SimpleSC.dll $DST

%files
%{_datadir}/nsis/Plugins/SimpleSC.dll

%changelog
* Thu Jul 30 2015 Yedidyah Bar David <didi@redhat.com> 1.30-1
- Initial release
