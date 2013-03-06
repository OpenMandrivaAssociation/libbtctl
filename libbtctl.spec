%define url_ver %(echo %{version} | cut -d. -f1,2)

%define major 6
%define libname %mklibname btctl %{major}
%define devname %mklibname btctl -d

Summary:	GNOME bluetooth control library
Name:		libbtctl
Version:	0.11.1
Release:	6
License:	GPLv2+
Group:		System/Libraries
Url:		http://usefulinc.com/software/gnome-bluetooth/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libbtctl/%{url_ver}/%{name}-%{version}.tar.bz2
Patch0:		libbtctl-0.11.1-format-strings.patch
Patch2:		libbtctl-0.4.1-pydir.patch
Patch3:		libbtctl-0.8.0-crash.patch
Patch4:		libbtctl_fix_broken_check.patch

BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig(bluez)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	pkgconfig(openobex) >= 1.1
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(python)

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

%package -n %{devname}
Group:		Development/C
Summary:	Development libraries and header files from %{name}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Development libraries and header files from %{name}

%package -n python-%{name}
Group:		Development/Python
Summary:	Bluetooth Python bindings

%description -n python-%{name}
This is the python wrapper for %{name}.

%prep
%setup -q
%apply_patches

sed -i -e 's|AM_PROG_CC_STDC|AC_PROG_CC|g' \
	configure*

%build
autoreconf -fi
%configure2_5x \
	--disable-static \
	--enable-shared \
	--disable-mono
# parallel build fails
make

%install
%makeinstall_std

%find_lang %{name}

%files -n %{libname} -f %{name}.lang
%{_libdir}/libbtctl.so.%{major}*

%files -n python-%{name}
%{py_platsitedir}/btctl.so

%files -n %{devname}
%doc AUTHORS ChangeLog README
%doc %{_datadir}/gtk-doc/html/%{name}
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

