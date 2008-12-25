%define name	libbtctl
%define version 0.10.0
%define release %mkrel 4

%define major 4
%define libname %mklibname btctl %{major}
%define develname %mklibname btctl -d

Name: 	 	%{name}
Summary: 	GNOME bluetooth control library
Version: 	%{version}
Release: 	%{release}
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libbtctl/%{name}-%{version}.tar.bz2
Patch2:		libbtctl-0.4.1-pydir.patch
Patch3:		libbtctl-0.8.0-crash.patch
# From upstream SVN: port to Bluez 4 - AdamW 2008/10
Patch4:		libbtctl-0.10.0-bluez4.patch
URL:		http://usefulinc.com/software/gnome-bluetooth/
License:	GPLv2+
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

%package -n %{libname}
Group:		System/Libraries
Summary:	GNOME bluetooth control library
Requires:	bluez
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
Current features include:
    * Bonobo component to manage the discovery of nearby Bluetooth devices
    * Component will create serial (RFCOMM) connections for clients to devices
    * libbtcl, a GObject wrapper for Bluetooth functionality

Features planned in the near future include:
    * Control-center prefs application to give users overall control over
      devices

%package -n %{develname}
Group:		Development/C
Summary:	Static libraries and header files from %{name}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%mklibname btctl 4 -d
Provides:	%mklibname btctl 4 -d

%description -n %{develname}
Static libraries and header files from %name

%package -n python-%{name}
Group:		Development/Python
Summary:	Bluetooth Python bindings
Conflicts:	%{name} < 0.5.0-2mdk

%description -n python-%{name}
This is the python wrapper for %name.

%prep
%setup -q
%patch2 -p1 -b .pydir
%patch3 -p1 -b .crash
%patch4 -p1 -b .bluez4
aclocal
autoconf
automake

%build
%configure2_5x --enable-shared --disable-mono
# parallel build fails
make
										
%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}
rm -f %{buildroot}%{py_platsitedir}/*a

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname} -f %{name}.lang
%defattr(-,root,root)
%{_libdir}/libbtctl.so.%{major}*

%files -n python-%{name}
%defattr(-,root,root)
%{py_platsitedir}/btctl.so

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%doc %{_datadir}/gtk-doc/html/%{name}
%{_includedir}/%{name}
%{_libdir}/*.so
%attr(644,root,root) %{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/pkgconfig/%{name}.pc
