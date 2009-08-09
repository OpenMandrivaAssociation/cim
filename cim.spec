%define _disable_ld_no_undefined 1

%define	name		cim
%define	version		3.37
%define rel     	4
%define release 	%mkrel %rel
%define	libname_orig	libcim
%define	major		3
%define	libname		%mklibname %{name} %{major}
%define	libname_devel	%mklibname %{name} -d

Summary:	Simula to C translator. Mother of all OO-languages
Name:		%{name}
Version:	%{version}
Release:	%{release}
Url:		ftp://ftp.ifi.uio.no/pub/cim/
#http://www.ifi.uio.no/~cim/cim.html
Source0:	ftp://ftp.ifi.uio.no/pub/cim/%{name}-%{version}.tar.bz2
Patch0:		cim-3.37-fix-str-fmt.patch
License:	GPL
Group:		Development/Other
Requires:	%{libname} = %{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Cim compiles Simula code to C and uses a C compiler like gcc to
compile it further to machine-code. Simula was the first language
with object-oriented features. The Simula language has features for
quasi-parallel execution and a framework for doing simulations.

%package -n %{libname}
Summary: Gnu Cim libraries packages  
Group: Development/Other 

%description -n %{libname}
This package contains the libraries needed to run programs dynamically 
linked with cim (the Gnu Simula Compiler)  

%package -n %{libname_devel}
Summary: Headers for developing programs that will use cim
Group: Development/Other
Requires: %{libname} = %{version}
Provides: %{name}-devel
Provides: %{libname_orig}-devel
Obsoletes: %{libname}-devel

%description -n %{libname_devel}
This package contains the headers that programmers will need to develop
applications which will use cim.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x	--enable-dump=yes
(cd src; make libdir=%{_libdir} includedir=%{_includedir})
%make all

%install
rm -fr %buildroot
%makeinstall mandir=$RPM_BUILD_ROOT%{_mandir} infodir=$RPM_BUILD_ROOT%{_infodir}

cd $RPM_BUILD_ROOT%{_libdir};chmod +x libcim.so.%{major}.0.0

%clean 
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%post -n %{libname_devel}
%_install_info %{name}.info

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%postun -n %{libname_devel}
%_remove_install_info %{name}.info

%files
%defattr(-, root, root)
%doc NEWS
%{_bindir}/*

%files -n %{libname}
%defattr(-, root, root)
%{_libdir}/*.so.%{major}*

%files -n %{libname_devel}
%defattr(-, root, root)
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/cim.h
%{_mandir}/*/*
%{_infodir}/*
%doc README doc/SIMULA-HISTORY AUTHORS COPYING TODO
