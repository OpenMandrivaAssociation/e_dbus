%define major		1
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Summary: 	E17 basic convenience wrappers around dbus
Name: 		e_dbus
Version: 	1.0.0
Release: 	%mkrel -c beta 1
Source:		http://download.enlightenment.org/releases/%{name}-%{version}.beta.tar.bz2
Patch0:		e_dbus-1.0.0.beta-link.patch
License: 	BSD
Group: 		System/Servers
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: 		http://www.enlightenment.org/
BuildRequires:	dbus-devel
BuildRequires:	ecore-devel >= 1.0.0

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
%setup -qn %{name}-%{version}.beta

%build
autoreconf -fi
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS README
%{_bindir}/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/*
