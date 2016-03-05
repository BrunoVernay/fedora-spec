# Global variables for github repository
%global commit0 922601d76b5959949253695267dbc83609077aeb
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

Name:           zam-plugins
Version:        3.5
Release:        1%{?dist}
Summary:        Zam LV2 set of plugins

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/zamaudio/zam-plugins
Source0:        https://github.com/zamaudio/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel

%description
Zam LV2 set of plugins

%package -n ladspa-zam
Summary:        Zam LADSPA plugin
Group:          Applications/Multimedia

%description -n ladspa-zam
Zam LADSPA plugin

%package -n vst-zam
Summary:        Zam VST plugin
Group:          Applications/Multimedia

%description -n vst-zam
Zam VST plugin

%prep
%setup -qn %{name}-%{commit0}

%build
make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} HAVE_DGL=1 %{?_smp_mflags}

%install 
make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} HAVE_DGL=1 %{?_smp_mflags} install

%files
%{_libdir}/lv2/*

%files -n ladspa-zam
%{_libdir}/ladspa/* 

%files -n vst-zam
%{_libdir}/vst/* 

%changelog
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 3.5
- Initial build
