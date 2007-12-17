%define	name	e_dbus
%define	version 0.01
%define release %mkrel 2

%define major 0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Summary: 	E17, some basic convenience wrappers around dbus
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		System/Servers
URL: 		http://get-e.org/
Source: 	%{name}-%{version}.tar.bz2
Buildrequires:	%{mklibname dbus-1_3}-devel, ecore-devel >= 0.9.9.038

%description
This is the start of some basic convenience wrappers around dbus to ease
integrating dbus with EFL based applications.
When using e_dbus, direct use of the low level dbus api is still
heavily required for processing messages.

%package -n %libname
Summary: Libraries for the %{name} package
Group: System/Libraries

%description -n %libname
Libraries for %{name}

%package -n %libnamedev
Summary: Headers and development libraries from %{name}
Group: Development/Other
Requires: %libname = %{version}
Requires: %name = %{version}
Provides: lib%{name}-devel = %{version}-%{release}
Provides: %name-devel = %{version}-%{release}

%description -n %libnamedev
%{name} development headers and libraries

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS README
%{_bindir}/%{name}*

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %libnamedev
%defattr(-,root,root)
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/*.h

