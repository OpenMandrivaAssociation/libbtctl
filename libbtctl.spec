%define major 6
%define libname %mklibname btctl %{major}
%define develname %mklibname btctl -d

Name: 	 	libbtctl
Summary: 	GNOME bluetooth control library
Version: 	0.11.1
Release: 	6
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libbtctl/%{name}-%{version}.tar.bz2
Patch:		libbtctl-0.11.1-format-strings.patch
Patch2:		libbtctl-0.4.1-pydir.patch
Patch3:		libbtctl-0.8.0-crash.patch
Patch4:		libbtctl_fix_broken_check.patch
URL:		http://usefulinc.com/software/gnome-bluetooth/
License:	GPLv2+
Group:		System/Libraries

BuildRequires:	libgnomeui2-devel
BuildRequires:	libGConf2-devel
BuildRequires:	bluez-devel
BuildRequires:	gtk-doc
BuildRequires:	perl-XML-Parser
BuildRequires:	intltool
BuildRequires:	python-devel
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

%description -n python-%{name}
This is the python wrapper for %name.

%prep
%setup -q
%apply_patches

%build
autoreconf -fi
%configure2_5x \
	--disable-static \
	--enable-shared \
	--disable-mono
# parallel build fails
make
										
%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
%find_lang %{name}

%files -n %{libname} -f %{name}.lang
%{_libdir}/libbtctl.so.%{major}*

%files -n python-%{name}
%{py_platsitedir}/btctl.so

%files -n %{develname}
%doc AUTHORS ChangeLog README
%doc %{_datadir}/gtk-doc/html/%{name}
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

