Name:    sendmidi
Version: 1.0.15
Release: 3%{?dist}
Summary: A command line tool to send MIDI event
License: GPLv3
URL:     https://github.com/gbevin/SendMIDI

Source0: %{url}/archive/%{version}.tar.gz#/SendMIDI-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: libX11-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel

%description
SendMIDI is a multi-platform command-line tool makes it very easy to quickly
send MIDI messages to MIDI devices from your computer.

%prep
%autosetup -n SendMIDI-%{version}

%build

cd Builds/LinuxMakefile

%make_build STRIP=true CPPFLAGS="%{optflags}"

%install 

cd Builds/LinuxMakefile

install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 -p build/sendmidi %{buildroot}/%{_bindir}/

%files
%doc README.md
%license COPYING.md
%{_bindir}/*

%changelog
* Sat Jan 2 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.15-3
- update to 1.0.5

* Sun Oct 4 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.14-3
- fix debug + install

* Thu Jul 16 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.14-2
- fix permission

* Thu Jul 16 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.14-1
- Initial spec file
