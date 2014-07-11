%define _disable_ld_no_undefined 1

%define	major	3
%define	libname	%mklibname %{name} %{major}
%define	devname	%mklibname %{name} -d

Summary:	Simula to C translator. Mother of all OO-languages
Name:		cim
Version:	3.37
Release:	16
License:	GPLv2
Group:		Development/Other
Url:		ftp://ftp.ifi.uio.no/pub/cim/
Source0:	ftp://ftp.ifi.uio.no/pub/cim/%{name}-%{version}.tar.bz2
Patch0:		cim-3.37-fix-str-fmt.patch
Patch1:		cim_fix_progname.patch

%description
Cim compiles Simula code to C and uses a C compiler like gcc to
compile it further to machine-code. Simula was the first language
with object-oriented features. The Simula language has features for
quasi-parallel execution and a framework for doing simulations.

%package -n %{libname}
Summary:	Gnu Cim libraries packages
Group:		System/Libraries

%description -n %{libname}
This package contains the libraries needed to run programs dynamically 
linked with cim (the Gnu Simula Compiler)

%package -n %{devname}
Summary:	Headers for developing programs that will use cim
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel

%description -n %{devname}
This package contains the headers that programmers will need to develop
applications which will use cim.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--enable-dump=yes \
	--disable-static

%make 

%install
%makeinstall 

rm -f %{buildroot}%{_libdir}/*.a

%files
%doc NEWS
%{_bindir}/*
%{_mandir}/man1/cim.1*

%files -n %{libname}
%{_libdir}/libcim.so.%{major}*

%files -n %{devname}
%doc README doc/SIMULA-HISTORY AUTHORS COPYING TODO
%{_libdir}/*.so
%{_includedir}/cim.h
%{_infodir}/*

