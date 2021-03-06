# Global variables for github repository
%global commit0 50cc35124c17d2c42b8b097b558eaa07eab438b7
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: B.Harvestr is an experimental granular synthesizer LV2 plugin
Name:    lv2-BHarvestr
Version: 0.1.0
Release: 3%{?dist}
License: GPL
URL:     https://github.com/sjaehn/BHarvestr

Source0: https://github.com/sjaehn/BHarvestr/archive/%{commit0}.tar.gz#/BHarvestr-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: cairo-devel
BuildRequires: libsndfile-devel

%description
B.Harvestr is an experimental granular synthesizer LV2 plugin.

Warning: B.Harvestr is in an early stage of development.
Not for production use! No guarantees! Some essential features are not (fully) implemented yet.
Major changes in the plugin definition need to be expected.
Therefore, future versions of this plugin may be completely incompatible to this version.

%prep
%autosetup -n BHarvestr-%{commit0}

%build

%make_build PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -std=c++11 -fvisibility=hidden -fPIC"

%install

%make_install PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -std=c++11 -fvisibility=hidden -fPIC"

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Mon Mar 15 2021 Yann Collette <ycollette dot nospam at free.fr> 0.1.0-3
- updata to 0.1.0-3 - last master version

* Fri Jun 26 2020 Yann Collette <ycollette dot nospam at free.fr> 0.1.0-2
- updata to 0.1.0-2 - last master version

* Wed May 13 2020 Yann Collette <ycollette dot nospam at free.fr> 0.1.0-1
- initial release of the spec file
