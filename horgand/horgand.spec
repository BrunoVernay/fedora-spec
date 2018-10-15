# Global variables for github repository
%global commit0 0f4ef66ad46d3a1e542ea160487b1a3fe3b76031
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: Software Synthesizer
Name: horgand
Version: 1.15.0
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL:            https://github.com/ycollet/horgand
Source0:        https://github.com/ycollet/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: alsa-lib-devel
BuildRequires: alsa-utils
BuildRequires: fltk-devel
BuildRequires: desktop-file-utils
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsndfile-devel
BuildRequires: libxcb-devel
BuildRequires: libXpm-devel
BuildRequires: zlib-devel
BuildRequires: freetype-devel
BuildRequires: fontconfig-devel

%description
Horgand is a organ ... generates sound like a FM sinthesizer in real time,
good reason for use a fast computer, there are many others programs who emulate a organ and sure
their sound is better, but i program what i need, and just for fun.

%prep
%setup -qn %{name}-%{commit0}

%build

./autogen.sh
%configure --libdir=%{_libdir}

%{__make} DESTDIR=%{buildroot} %{_smp_mflags} CFLAGS="-fPIC %{__global_cflags}" CXXFLAGS="-fPIC %{__global_cflags}"

%install

%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} %{_smp_mflags} install

# desktop file categories
BASE="X-Fedora Application AudioVideo"
XTRA="X-Synthesis X-MIDI X-Jack"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/%{name}
%{_datadir}/man/*
%{_datadir}/horgand/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette dot nospam at free.fr> 1.15.0-1
- update for Fedora 29
* Thu May 12 2016 Yann Collette <ycollette dot nospam at free.fr> 1.15.0-1
- Initial release of spec fil to 1.15.0
