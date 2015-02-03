Name:		spice-qxl
Version:	0.1
Release:	21.1
Summary:	RPM wrapper for %{name}
License:	GPLv2+
Source0:	http://www.spice-space.org/download/windows/qxl/qxl-0.1-21/qxl_xp_x86.zip
Source1:	http://www.spice-space.org/download/windows/qxl/qxl-0.1-21/qxl_w7_x86.zip
Source2:	http://www.spice-space.org/download/windows/qxl/qxl-0.1-21/qxl_w7_x64.zip
Source3:	http://www.spice-space.org/download/windows/qxl/qxl-0.1-21/qxl_8k2R2_x64.zip
URL:		http://www.spice-space.org/
BuildArch:	noarch
Packager:	Lev Veyde <lveyde@redhat.com>

%description
A package wrapping %{name} to provide dependency features.

%prep
%setup -c -n %{name} -q
%setup -D -T -b 1 -c -n %{name} -q
%setup -D -T -b 2 -c -n %{name} -q
%setup -D -T -b 3 -c -n %{name} -q

%build
mv %{_builddir}/%{name}/xp %{_builddir}/%{name}/winxp
mv %{_builddir}/%{name}/w7 %{_builddir}/%{name}/win7
mv %{_builddir}/%{name}/2k8R2 %{_builddir}/%{name}/win2k8r2

%install
DST=%{buildroot}%{_datadir}/artifacts/%{name}/
mkdir -p $DST
cp -av %{_builddir}/%{name}/* $DST

%files
%{_datadir}/artifacts/%{name}

%changelog
* Wed Oct 08 2014 Lev Veyde <lveyde@redhat.com> 0.1-21.1
- Initial version
