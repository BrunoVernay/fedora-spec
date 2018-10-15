# Global variables for github repository
%global commit0 3cb4233f1690cb4d338bbfbb860e9ba505b67dba
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           radium
Version:        3.3.2
Release:        1%{?dist}
Summary:        A tracker / sequencer

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/kmatheussen/radium
Source0:        https://github.com/kmatheussen/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: qt4-devel
BuildRequires: libXaw-devel
BuildRequires: python2-devel
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsamplerate-devel
BuildRequires: liblrdf-devel
BuildRequires: libsndfile-devel
BuildRequires: ladspa-devel
BuildRequires: glib2-devel
BuildRequires: ladspa-calf-plugins
BuildRequires: binutils-devel
BuildRequires: libtool-ltdl
BuildRequires: libtool
BuildRequires: tk
BuildRequires: libogg-devel
BuildRequires: libvorbis-devel
BuildRequires: speex-devel
BuildRequires: fftw-devel
BuildRequires: guile
BuildRequires: libxkbfile-devel
BuildRequires: xorg-x11-util-macros
BuildRequires: cmake

%description
A tracker / sequencer

%prep
%setup -qn %{name}-%{commit0}

%build

make packages
BUILDTYPE=RELEASE ./build_linux.sh -j2

%install 

%__install -m 755 -d %{buildroot}%{_datadir}/%{name}/samples/
%__install -m 644 *.rad %{buildroot}/%{_datadir}/%{name}/samples/

%__install -m 755 -d %{buildroot}%{_datadir}/%{name}/doc/
%__install -m 644 README %{buildroot}/%{_datadir}/%{name}/doc/
%__install -m 644 COPYING %{buildroot}/%{_datadir}/%{name}/doc/

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 755 bin/radium %{buildroot}/%{_bindir}/

%__install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/
%__install -m 644 bin/radium_256x256x32.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/

%post 
update-desktop-database -q
touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :

%postun
update-desktop-database -q
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :
  gtk-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :
fi

%posttrans 
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%{_bindir}/
%{_datadir}/

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 3.3.2
- update for Fedora 29

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 3.3.2
- Initial build
