#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/e_dbus e_dbus; \
#cd e_dbus; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#v_maj=$(cat configure.ac | grep 'm4_define(\[v_maj\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_min=$(cat configure.ac | grep 'm4_define(\[v_min\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_mic=$(cat configure.ac | grep 'm4_define(\[v_mic\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#PKG_VERSION=$v_maj.$v_min.$v_mic.$SVNREV; \
#cd ..; \
#tar -Jcf e_dbus-$PKG_VERSION.tar.xz e_dbus/ --exclude .svn --exclude .*ignore


%define snapshot 0

%if %snapshot
%define	svndate	20120103
%define	svnrev	66792
%endif

%define	major		1
%define	libname		%mklibname %{name} %{major}
%define	develname	%mklibname %{name} -d

Summary:	E17 basic convenience wrappers around dbus
Name:		e_dbus
%if %snapshot
Version:	1.1.99.%{svnrev}
Release:	0.%{svndate}.1
%else
Version:	1.7.3
Release:	1
%endif
License:	BSD
Group:		System/Servers
URL:		http://www.enlightenment.org/
%if %snapshot
Source0:	%{name}-%{version}.tar.xz
%else
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.gz
%endif

BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(ecore) >= 1.7.0
BuildRequires:	pkgconfig(eina) >= 1.7.0

%description
This is the start of some basic convenience wrappers around dbus to
ease integrating dbus with EFL based applications.
When using e_dbus, direct use of the low level dbus api is still
heavily required for processing messages.

%package -n %{libname}
Summary:	Libraries for the %{name} package
Group:		System/Libraries
Obsoletes:	%{mklibname e_dbus 1} <= 0.01

%description -n %{libname}
Libraries for %{name}.

%package -n %{develname}
Summary:	Headers and development libraries from %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
%{name} development headers and libraries.

%prep
%if %{snapshot}
%setup -qn %{name}
%else
%setup -q
%endif

%build
%if %{snapshot}
NOCONFIGURE=yes ./autogen.sh
%endif

%configure \
	--disable-static \
	--enable-econnman0_7x \
	--enable-ebluez

%make

%install
%makeinstall_std

%files
%doc AUTHORS README
%{_bindir}/*
%{_datadir}/%{name}/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_includedir}/%{name}*



%changelog
* Wed Jun 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.0-1
+ Revision: 807158
- version update 1.2.0

* Thu Jan 05 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.1.99.66792-0.20120103.1
+ Revision: 757935
- fix to files list
- new version/snapshot 1.1.99.66792
- merge spec with UnityLinux
- cleaned up spec
- disabled static build

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 1.0.1-1
+ Revision: 681653
- update to new version 1.0.1

* Sat Jan 29 2011 Funda Wang <fwang@mandriva.org> 1.0.0-1
+ Revision: 633925
- 1.0.0 final

* Sat Dec 18 2010 Funda Wang <fwang@mandriva.org> 1.0.0-0.beta3.1mdv2011.0
+ Revision: 622798
- 1.0 beta3

* Tue Nov 16 2010 Funda Wang <fwang@mandriva.org> 1.0.0-0.beta2.1mdv2011.0
+ Revision: 597951
- 1.0.0 beta2

* Wed Oct 13 2010 Funda Wang <fwang@mandriva.org> 1.0.0-0.beta.1mdv2011.0
+ Revision: 585331
- 1.0.0 beta

* Fri Jul 16 2010 Funda Wang <fwang@mandriva.org> 0.5.0.49898-1mdv2011.0
+ Revision: 553946
- new version 0.5.0.49898

* Sun Dec 13 2009 Funda Wang <fwang@mandriva.org> 0.5.0.063-1mdv2010.1
+ Revision: 478153
- new version 0.5.0.063

* Fri Aug 07 2009 Funda Wang <fwang@mandriva.org> 0.5.0.062-1mdv2010.0
+ Revision: 411123
- new version 0.5.0.062

* Wed Jul 08 2009 Funda Wang <fwang@mandriva.org> 0.5.0.061-2mdv2010.0
+ Revision: 393496
- rebuild

* Mon Jul 06 2009 Funda Wang <fwang@mandriva.org> 0.5.0.061-1mdv2010.0
+ Revision: 392855
- new version 0.5.0.061

* Mon Jul 06 2009 Funda Wang <fwang@mandriva.org> 0.5.0.060-2mdv2010.0
+ Revision: 392831
- rebuild for new ecore

* Sat May 02 2009 Funda Wang <fwang@mandriva.org> 0.5.0.060-1mdv2010.0
+ Revision: 370691
- New version 0.5.0.060

* Mon Mar 02 2009 Antoine Ginies <aginies@mandriva.com> 0.5.0.050-2mdv2009.1
+ Revision: 346964
- SVN SNAPSHOT 20090227, release 0.5.0.050

* Sun Oct 12 2008 Funda Wang <fwang@mandriva.org> 0.5.0.050-1mdv2009.1
+ Revision: 292633
- New version 0.5.0.050

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jun 01 2008 Funda Wang <fwang@mandriva.org> 0.5.0.043-1mdv2009.0
+ Revision: 213988
- fix filelist
- New version 0.5.0.043

* Fri Feb 15 2008 Antoine Ginies <aginies@mandriva.com> 0.1.0.042-2mdv2008.1
+ Revision: 168997
- bump release, restore buildrequires specific version

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Sat Feb 02 2008 Austin Acton <austin@mandriva.org> 0.1.0.042-1mdv2008.1
+ Revision: 161521
- new vesrion
- tidy spec
- fix URL

* Fri Dec 21 2007 Adam Williamson <awilliamson@mandriva.org> 0.1.0.003-0.20071220.1mdv2008.1
+ Revision: 136141
- sync sources
- new library policy
- update to current CVS to fix build with changed core API
- sane buildrequires
- clean spec

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jun 04 2007 Antoine Ginies <aginies@mandriva.com> 0.01-2mdv2008.0
+ Revision: 35111
- fix Major, prevent major bug to happen again

* Fri May 25 2007 Antoine Ginies <aginies@mandriva.com> 0.01-1mdv2008.0
+ Revision: 31174
- add some buildrequires
- first release of e_dbus
- Import e_dbus

