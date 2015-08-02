# Global variables for github repository
%global commit0 53458838505efef91ed069d0a7d970b6b3588eba
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           DISTRHO-Ports
Version:        1.0.0
Release:        1%{?dist}
Summary:        A set of LV2 plugins

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/DISTRHO/DISTRHO-Ports
Source0:        https://github.com/DISTRHO/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1:        http://downloads.sourceforge.net/premake/premake-linux-3.7.tar.gz

BuildRequires: ladspa-devel
BuildRequires: liblo-devel
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: freetype-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
# For premake
%ifarch x86_64 amd64
BuildRequires: glibc(x86-32)
%endif

%description
A set of LV2 plugins

%prep
%setup -qn %{name}-%{commit0}

sed -i "s/PREFIX = \/usr\/local/PREFIX = \/usr/g" Makefile
sed -i "s/\/lib\//\/lib64\//g" Makefile

%build

tar xvfz %SOURCE1
export PATH=`pwd`:$PATH
./scripts/premake-update.sh linux
make DESTDIR=%{buildroot} lv2 %{?_smp_mflags}

%install 
make DESTDIR=%{buildroot} lv2 %{?_smp_mflags} install

rm -rf %{buildroot}/usr/src

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
%{_libdir}/lv2

%changelog
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 1.0.0beta
- Initial build
