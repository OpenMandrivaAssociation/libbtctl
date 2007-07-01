%define name	libbtctl
%define version 0.8.2
%define release %mkrel 2

%define major	4
%define libname %mklibname btctl %{major}

Name: 	 	%{name}
Summary: 	GNOME bluetooth control library
Version: 	%{version}
Release: 	%{release}

Source0:	http://ftp.gnome.org/pub/GNOME/sources/libbtctl/%{name}-%{version}.tar.bz2
#gw fix for new libopenobex detection
Patch0:		libbtctl-0.6.0-new-openobex.patch
Patch1:		libbtctl-0.6.0-libdir.patch
Patch2:		libbtctl-0.4.1-pydir.patch
Patch3:		libbtctl-0.8.0-crash.patch
Patch4:		libbtctl-0.6.0-print.patch
URL:		http://usefulinc.com/software/gnome-bluetooth/
License:	GPL
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	autoconf2.5 >= 2.54
BuildRequires:	libgnomeui2-devel libGConf2-devel
BuildRequires:	bluez-devel gtk-doc perl-XML-Parser
BuildRequires:	intltool python-devel
BuildRequires:	pygtk2.0-devel
BuildRequires:	openobex-devel >= 1.1

%description
Current features include:
    * Bonobo component to manage the discovery of nearby Bluetooth devices
    * Component will create serial (RFCOMM) connections for clients to devices
    * libbtcl, a GObject wrapper for Bluetooth functionality

Features planned in the near future include:
    * Control-center prefs application to give users overall control over
      devices

%package -n %libname
Group:		System/Libraries
Summary: 	GNOME bluetooth control library
Requires:	bluez-utils
Provides:   %name = %version-%release

%description -n %libname
Current features include:
    * Bonobo component to manage the discovery of nearby Bluetooth devices
    * Component will create serial (RFCOMM) connections for clients to devices
    * libbtcl, a GObject wrapper for Bluetooth functionality

Features planned in the near future include:
    * Control-center prefs application to give users overall control over
      devices

%package -n %libname-devel
Group:		Development/C
Summary:	Static libraries and header files from %name
Provides:	%name-devel = %version-%{release}
Requires:	%libname = %version

%description -n %libname-devel
Static libraries and header files from %name

%package -n python-%name
Group: Development/Python
Summary: Bluetooth Python bindings
Conflicts: %name < 0.5.0-2mdk
%description -n python-%name
This is the python wrapper for %name.

%prep
%setup -q
%patch0 -p1 -b .openobex
%patch1 -p1 -b .libdir
%patch2 -p1 -b .pydir
%patch3 -p1 -b .crash
%patch4 -p1 -b .print
aclocal
autoconf
automake

%build
%configure2_5x --enable-shared --disable-mono
# parallel build fails
make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %name
%if %_lib != lib
mkdir -p %buildroot%{py_platsitedir}/
mv %buildroot%{py_puresitedir}/* %buildroot%{py_platsitedir}/
%endif
rm -f %buildroot%{py_platsitedir}/*a

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %libname -f %name.lang
%defattr(-,root,root)
%{_libdir}/libbtctl.so.%{major}*

%files -n python-%name
%defattr(-,root,root)
%{py_platsitedir}/btctl.so


%files -n %{libname}-devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%doc %{_datadir}/gtk-doc/html/%name
%{_includedir}/%name
%{_libdir}/*.so
%attr(644,root,root) %{_libdir}/*.la
%{_libdir}/*.a

%{_libdir}/pkgconfig/%name.pc


