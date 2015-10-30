# Global variables for github repository
%global commit0 f8b18cff1d3bd24fbf666abb27ecc08785b67617
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           Cadence
Version:        master
Release:        1%{?dist}
Summary:        A JACK control center

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/falkTX/Cadence
Source0:        https://github.com/falkTX/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: python3-qt4-devel
BuildRequires: qt-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: pulseaudio-module-jack
BuildRequires: python3-dbus
BuildRequires: a2jmidid
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: jack-audio-connection-kit-dbus
BuildRequires: jack_capture

%description
A JACK control center

%prep
%setup -qn %{name}-%{commit0}

%build
make PREFIX=/usr DESTDIR=%{buildroot} %{?_smp_mflags}

%install 
make PREFIX=/usr DESTDIR=%{buildroot} %{?_smp_mflags} install

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
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/cadence/*
%{_datadir}/icons/*
%{_sysconfdir}/*

%changelog
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - master
- Initial build
