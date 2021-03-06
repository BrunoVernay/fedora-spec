Summary: A crossplatform music editor for creating Commodore 64 music. Uses reSID library by Dag Lem and supports alternatively HardSID & CatWeasel devices.
Name:    goatracker
Version: 2.76
Release: 2%{?dist}
License: GPL
URL:     https://sourceforge.net/projects/goattracker2/

Source0: https://sourceforge.net/projects/goattracker2/files/GoatTracker 2 Stereo/%{version}/GoatTracker_%{version}_Stereo.zip

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: SDL-devel

%description
A crossplatform music editor for creating Commodore 64 music.
Uses reSID library by Dag Lem and supports alternatively
HardSID & CatWeasel devices.

%prep
%autosetup -n gt2stereo

sed -i -e "/CFLAGS/c\CFLAGS=%{build_cflags} -Ibme -Iasm" trunk/src/makefile.common
sed -i -e "/CXXFLAGS/c\CXXFLAGS=%{build_cflags} -Ibme -Iasm" trunk/src/makefile.common
sed -i -e "s/strip/true/g" trunk/src/makefile.common

%build

%set_build_flags

cd trunk/src
make clean
%make_build

%install

cd trunk

install -m 755 -d %{buildroot}/%{_bindir}/
cp -a linux/* %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/pixmaps
install -m 644 -p src/goattrk2.bmp %{buildroot}%{_datadir}/pixmaps/

install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/goatracker.desktop << EOF
[Desktop Entry]
Name=goatracker
Comment=A tracker synthetizer.
Exec=/usr/bin/gt2stereo
Type=Application
Terminal=0
Icon=/usr/share/pixmaps/goattrk2.bmp
Categories=AudioVideo;
EOF

install -m 755 -d %{buildroot}%{_datadir}/%{name}/examples
cp -r examples/* %{buildroot}%{_datadir}/%{name}/examples/

install -m 755 -d %{buildroot}%{_datadir}/%{name}/doc
cp -a goat_tracker_commands.pdf %{buildroot}%{_datadir}/%{name}/doc/

desktop-file-install --vendor '' \
        --add-category=Audio \
        --add-category=Midi \
        --add-category=Sequencer \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/goatracker.desktop

%files
%doc trunk/authors trunk/readme_resid.txt trunk/readme_sdl.txt trunk/readme.txt
%license trunk/copying
%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%changelog
* Tue Oct 20 2020 Yann Collette <ycollette dot nospam at free.fr> 2.76-2
- fix debug build

* Wed Jun 17 2020 Yann Collette <ycollette dot nospam at free.fr> 2.76-1
- update to 2.76

* Thu Jan 3 2019 Yann Collette <ycollette dot nospam at free.fr> 2.75-1
- Initial release of spec file
