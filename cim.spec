%define	name		cim
%define	version		3.37
%define rel     	1
%define release 	%mkrel %rel
%define	libname_orig	libcim
%define	major		3
%define	libname		%mklibname %{name} %{major}
%define	libname_devel	%mklibname %{name} %{major} -d

Summary:	Simula to C translator. Mother of all OO-languages
Name:		%{name}
Version:	%{version}
Release:	%{release}
Url:		ftp://ftp.ifi.uio.no/pub/cim/
#http://www.ifi.uio.no/~cim/cim.html
Source0:	ftp://ftp.ifi.uio.no/pub/cim/%{name}-%{version}.tar.bz2
License:	GPL
Group:		Development/Other
Requires:	%{libname} = %{version}


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
Provides: %{libname_orig}-devel

%description -n %{libname_devel}
This package contains the headers that programmers will need to develop
applications which will use cim.

%prep
%setup -q

%build
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
%configure	--enable-dump=yes
(cd src; make libdir=%{_libdir} includedir=%{_includedir})
%make all

%install
%makeinstall mandir=$RPM_BUILD_ROOT%{_mandir} infodir=$RPM_BUILD_ROOT%{_infodir}

cd $RPM_BUILD_ROOT%{_libdir};chmod +x libcim.so.3.0.0

%clean 
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig

%post -n %{libname_devel}
%_install_info %{name}.info

%postun -n %{libname} -p /sbin/ldconfig

%postun -n %{libname_devel}
%_remove_install_info %{name}.info

%files
%defattr(-, root, root)
%doc NEWS
%{_bindir}/*

%files -n %{libname}
%defattr(-, root, root)
%{_libdir}/*.so.*

%files -n %{libname_devel}
%defattr(-, root, root)
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/cim.h
%{_mandir}/*/*
%{_infodir}/*
%doc README doc/SIMULA-HISTORY AUTHORS COPYING TODO

