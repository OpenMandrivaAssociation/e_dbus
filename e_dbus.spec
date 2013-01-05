%define	major	1
%define	libname	%mklibname %{name} %{major}
%define	devname	%mklibname %{name} -d

Summary:	E17 basic convenience wrappers around dbus
Name:		e_dbus
Version:	1.7.5
Release:	1
License:	BSD
Group:		System/Servers
URL:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.fr/releases/%{name}-%{version}.tar.bz2

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

%package -n %{devname}
Summary:	Headers and development libraries from %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
%{name} development headers and libraries.

%prep
%setup -q

%build
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

%files -n %{devname}
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_includedir}/%{name}*

