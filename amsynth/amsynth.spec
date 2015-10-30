# Global variables for github repository
%global commit0 d394e832b24ec80ac4e2fc6ec9cbbc5508196bb1
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: Software Synthesizer
Name: amsynth
Version: 1.5.1
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL:            https://github.com/nixxcode/amsynth
Source0:        https://github.com/nixxcode/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: alsa-lib-devel
BuildRequires: gtkmm24-devel
BuildRequires: desktop-file-utils
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsndfile-devel
BuildRequires: dssi-devel
BuildRequires: liblo-devel
BuildRequires: lash-devel
BuildRequires: lv2-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool

%description
amSynth is a software synthesizer, taking inspiration from the
original synths and latest digital ones, while keeping an intuitive
interface.

%package -n lv2-amsynth
Summary:        amsynth lv2 plugin
Group:          Applications/Multimedia

%description -n lv2-amsynth
Amsynth LV2 plugin

%package -n dssi-amsynth
Summary:        amsynth DSSI plugin
Group:          Applications/Multimedia

%description -n dssi-amsynth
Amsynth DSSI plugin

%prep
%setup -qn %{name}-%{commit0}

%build
autoreconf --force --install
%configure
%{__make} %{_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install

# desktop file categories
BASE="X-PlanetCCRMA X-Fedora Application AudioVideo"
XTRA="X-Synthesis X-MIDI X-Jack"
%{__mkdir} -p %{buildroot}%{_datadir}/applications

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/amsynth
%{_datadir}/amsynth/*
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/amsynth.png

%files -n dssi-amsynth
%{_libdir}/dssi/*

%files -n lv2-amsynth
%{_libdir}/lv2/*

%changelog
* Thu Jun 04 2015 Yann Collette <ycollette dot nospam at free.fr> 1.5.1-1
- updated to 1.5.1
- added a DSSI package
- added a LV2 package

* Mon Aug 06 2012 Martin Tarenskeen <m.tarenskeen at zonnet.nl> 1.3.1-1
- updated to 1.3.1
- removed old patches (now fixed upstream)
- small patch to include unistd.h in Config.cc
- dssi version included

* Tue Jan  2 2007 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.2.0-1
- updated to 1.2.0, fixed install target for skeleton files (they
  install in /usr/share instead of /usr/share/amsynth)

* Fri Nov 24 2006 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.1.0-0.4.cvs
- spec file tweaks, use separate desktop file

* Thu Aug 24 2006 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.1.0-0.3.cvs
- wrong group (typo: Application instead of Applications, thanks to jos
  for the tip)

* Fri Jul 14 2006 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.1.0-0.2.cvs
- added explicit gtkmm24 requires for gtkmm24, keeping the previous version
  allows amsynth to install but it does not run

* Mon Jun 19 2006 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.1.0-0.2.cvs
- added Planet CCRMA categories to desktop file

* Wed Jan 25 2006 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.1.0-0.1.cvs
- updated to 1.1.0, uses gtkmm2
- needs a cvs snapshot and a patch for the gtkmm include and signal.h include

* Fri Feb 18 2005 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.0.0-3
- do not install main executable suid root

* Fri Dec 24 2004 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.0.0-2
- use rpm optimization flags

* Mon Dec 20 2004 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 
- spec file cleanup

* Sat May  8 2004 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 
- added proper buildrequires

* Tue Mar  2 2004 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.0.0-1
- bumped epoch to 1 to transition from 1.0rc4 to 1.0.0 (darn...)

* Sun Feb 29 2004 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.0.0-1
- updated to 1.0.0

* Wed Nov 12 2003 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.0rc4-1
- added release tags, spec file tweaks
- added patch1 with defines for using old alsa API

* Sat Jul 26 2003 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.0rc4-1
- updated t0 1.0rc4

* Wed Apr  2 2003 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.0rc2-2
- rebuild for jack 0.66.3, added explicit requires for it

* Mon Jan 27 2003 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.0rc2-1
- added patch to make it compile on 7.3

* Sun Jan 26 2003 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.0rc2-1
- Initial build.
