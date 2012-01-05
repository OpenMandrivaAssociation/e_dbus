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


%define snapshot 1

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
Version:	1.1.0
Release:	1
%endif
License:	BSD
Group:		System/Servers
URL:		http://www.enlightenment.org/
%if %snapshot
Source0:	%{name}-%{version}.tar.xz
%else
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
%endif

BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(ecore) >= 1.0.0
BuildRequires:	pkgconfig(eina) >= 1.0.0

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
%if %snapshot
%setup -qn %{name}
%else
%setup -q
%endif

%build

%if %snapshot
NOCONFIGURE=yes ./autogen.sh
%endif

%configure \
	--disable-static

%make

%install
rm -rf %{buildroot}
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

