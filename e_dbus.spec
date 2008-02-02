%define major		0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Summary: 	E17 basic convenience wrappers around dbus
Name: 		e_dbus
Version: 	0.1.0.042
Release: 	%mkrel 1
Source:		%{name}-%{version}.tar.bz2
License: 	BSD
Group: 		System/Servers
URL: 		http://www.enlightenment.org/
BuildRequires:	dbus-devel
BuildRequires:	ecore-devel

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
Requires:	%{libname} = %{version}
Requires:	%{name} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
%{name} development headers and libraries.

%prep
rm -rf %{buildroot}
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS README
%{_bindir}/%{name}*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/*.h

