Summary: Multi channel MIDI step sequencer LV2 plugin with a variable matrix
Name:    lv2-BSEQuencer
Version: 1.8.8
Release: 1%{?dist}
License: GPL
URL:     https://github.com/sjaehn/BSEQuencer

Source0: https://github.com/sjaehn/BSEQuencer/archive/%{version}.tar.gz#/BSEQuencer-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: cairo-devel

%description
Multi channel MIDI step sequencer LV2 plugin with a variable matrix

%prep
%autosetup -n BSEQuencer-%{version}

%build

%make_build PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -std=c++11 -fvisibility=hidden -fPIC"

%install

%make_install PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -std=c++11 -fvisibility=hidden -fPIC" install

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Mon Mar 15 2021 Yann Collette <ycollette dot nospam at free.fr> 1.8.8-1
- update to 1.8.8-1

* Sun Feb 7 2021 Yann Collette <ycollette dot nospam at free.fr> 1.8.6-1
- update to 1.8.6-1

* Sat Sep 19 2020 Yann Collette <ycollette dot nospam at free.fr> 1.8.4-1
- update to 1.8.4-1

* Tue Sep 15 2020 Yann Collette <ycollette dot nospam at free.fr> 1.8.2-1
- update to 1.8.2-1

* Tue Sep 15 2020 Yann Collette <ycollette dot nospam at free.fr> 1.8.0-1
- update to 1.8.0-1

* Mon Jul 6 2020 Yann Collette <ycollette dot nospam at free.fr> 1.6.0-1
- update to 1.6.0-1

* Mon May 18 2020 Yann Collette <ycollette dot nospam at free.fr> 1.4.2-1
- update to 1.4.2-1

* Thu May 7 2020 Yann Collette <ycollette dot nospam at free.fr> 1.4.0-1
- update to 1.4.0-1

* Sun Dec 29 2019 Yann Collette <ycollette dot nospam at free.fr> 1.2.0-1
- initial release 
