# Global variables for github repository
%global commit0 46beb4891ac6f223b33b298b96764535d8f80e18
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    midimsg-lv2
Version: 0.0.5.%{shortcommit0}
Release: 2%{?dist}
Summary: A collection of basic LV2 plugins to translate midi messages to usable values
License: GPLv2+
URL:     https://github.com/blablack/midimsg-lv2

Source0: https://github.com/blablack/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: python2

%description
A collection of basic LV2 plugins to translate midi messages to usable values

%prep
%autosetup -n %{name}-%{commit0}

# For Fedora 29
%if 0%{?fedora} >= 29
  for Files in `grep -lr "/usr/bin/env.*python"`; do sed -ie "s/env python/python2/g" $Files; done
%endif

%build

%set_build_flags

./waf configure --destdir=%{buildroot} --libdir=%{_libdir}
./waf

%install 
./waf -j1 install --destdir=%{buildroot}

%files
%doc README.md THANKS
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Mon Oct 19 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.5-2
- fix debug build

* Wed Nov 13 2019 Yann Collette <ycollette.nospam@free.fr> - 0.0.5-1
- update 0.0.5-1

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.0.4-1
- update for Fedora 29

* Mon Oct 23 2017 Yann Collette <ycollette.nospam@free.fr> - 0.0.4-1
- update to 0.0.4-1

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial build
