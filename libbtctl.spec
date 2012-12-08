%define major 6
%define libname %mklibname btctl %{major}
%define develname %mklibname btctl -d

Name:		libbtctl
Summary:	GNOME bluetooth control library
Version:	0.11.1
Release:	6
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libbtctl/%{name}-%{version}.tar.bz2
Patch0:		libbtctl-0.11.1-format-strings.patch
Patch2:		libbtctl-0.4.1-pydir.patch
Patch3:		libbtctl-0.8.0-crash.patch
Patch4:		libbtctl_fix_broken_check.patch
URL:		http://usefulinc.com/software/gnome-bluetooth/
License:	GPLv2+
Group:		System/Libraries

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

%package -n %{develname}
Group:		Development/C
Summary:	Static libraries and header files from %{name}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

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



%changelog
* Thu Dec 08 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.11.1-6
+ Revision: 739101
- converted BRs to pkgconfig provides
- corrected patch numbering
- rebuild
- cleaned up spec
- disabled static build
- removed .la files
- removed mkrel, BuildRoot, clean section, defattr
- removed pre 200900 scriptlets
- employed apply_patches

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 0.11.1-5
+ Revision: 660222
- mass rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.11.1-4mdv2011.0
+ Revision: 520758
- rebuilt for 2010.1

* Sun Sep 27 2009 Olivier Blin <blino@mandriva.org> 0.11.1-3mdv2010.0
+ Revision: 449854
- fix broken lib64 vs lib check (from Arnaud Patard)

  + Christophe Fergeau <cfergeau@mandriva.com>
    - rebuild

* Fri Feb 20 2009 Götz Waschk <waschk@mandriva.org> 0.11.1-1mdv2009.1
+ Revision: 343197
- new version
- new major
- drop patch 4
- fix format string

* Thu Dec 25 2008 Adam Williamson <awilliamson@mandriva.org> 0.10.0-4mdv2009.1
+ Revision: 319124
- rebuild with python 2.6

* Wed Oct 15 2008 Adam Williamson <awilliamson@mandriva.org> 0.10.0-3mdv2009.1
+ Revision: 293805
- add bluez4.patch: from upstream SVN, port to BlueZ 4.x
- should require bluez, not bluez-utils, now bluez-utils doesn't exist

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.10.0-2mdv2009.0
+ Revision: 222517
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 04 2008 Götz Waschk <waschk@mandriva.org> 0.10.0-1mdv2008.1
+ Revision: 162387
- new version
- drop patch 4

* Thu Jan 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.0-3mdv2008.1
+ Revision: 153937
- rebuild due to wrong tag
- new license policy
- new devel library policy
- spec file clean

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 0.9.0-2mdv2008.1
+ Revision: 150476
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Jul 13 2007 Götz Waschk <waschk@mandriva.org> 0.9.0-1mdv2008.0
+ Revision: 51799
- new version
- drop patches 0,1
- fix installation

  + Emmanuel Andry <eandry@mandriva.org>
    - add fedora patches
    - buildrequires python-devel
    - rebuild for openobex


* Wed Nov 08 2006 Götz Waschk <waschk@mandriva.org> 0.8.2-1mdv2007.0
+ Revision: 78203
- new version

* Tue Oct 24 2006 Götz Waschk <waschk@mandriva.org> 0.8.1-1mdv2007.1
+ Revision: 71718
- new version
- new version
  new major
- Import libbtctl

* Tue Sep 19 2006 Götz Waschk <waschk@mandriva.org> 0.8.0-1mdv2007.0
- New version 0.8.0

* Sat Jun 17 2006 Austin Acton <austin@mandriva.org> 0.6.0-1mdv2007.0
- Rebuild

* Mon Mar 27 2006 Götz Waschk <waschk@mandriva.org> 0.6.0-3mdk
- rebuild for new openobex

* Fri Feb 10 2006 Götz Waschk <waschk@mandriva.org> 0.6.0-2mdk
- fix python installation
- Rebuild
- use mkrel

* Thu Nov 24 2005 Götz Waschk <waschk@mandriva.org> 0.6.0-1mdk
- New release 0.6.0

* Thu Aug 18 2005 Götz Waschk <waschk@mandriva.org> 0.5.0-2mdk
- split out the python binding

* Thu Aug 18 2005 Götz Waschk <waschk@mandriva.org> 0.5.0-1mdk
- major 2
- drop patch 0
- new version

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.4.1-7mdk
- Rebuild for new python

* Tue Oct 19 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.4.1-6mdk
- lib64 fixes

* Thu Sep 30 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.4.1-5mdk
- Rebuild for new libbluetooth location

* Tue Sep 14 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.4.1-4mdk
- add BuildRequires: perl-XML-Parser openobex-devel pygtk2.0-devel

* Thu Jul 29 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.4.1-3mdk
- Patch0 (CVS): fix wrong ABI in obex object, causing crash in gnome-obex-server

* Sun Jun 20 2004 Austin Acton <austin@mandrake.org> 0.4.1-2mdk
- move python .so to lib package (bad idea, but works)

* Sat Jun 19 2004 Austin Acton <austin@mandrake.org> 0.4.1-1mdk
- 0.4.1

* Wed Jun 16 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.4-2mdk
- fix libification

* Fri Jun 11 2004 Austin Acton <austin@mandrake.org> 0.4-1mdk
- 0.4, major 1
- fix buildrequires
- configure 2.5
- disable mono bindings
- add languages macro
- add python libraries (split later?)

