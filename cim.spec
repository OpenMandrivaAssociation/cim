%define _disable_ld_no_undefined 1

%define	libname_orig	libcim
%define	major		3
%define	libname		%mklibname %{name} %{major}
%define	libname_devel	%mklibname %{name} -d

Summary:	Simula to C translator. Mother of all OO-languages
Name:		cim
Version:	3.37
Release:	10
License:	GPL
Group:		Development/Other
Url:		ftp://ftp.ifi.uio.no/pub/cim/
#http://www.ifi.uio.no/~cim/cim.html
Source0:	ftp://ftp.ifi.uio.no/pub/cim/%{name}-%{version}.tar.bz2
Patch0:		cim-3.37-fix-str-fmt.patch
Patch1:		cim_fix_progname.patch
Requires:	%{libname} = %{version}-%{release}

%description
Cim compiles Simula code to C and uses a C compiler like gcc to
compile it further to machine-code. Simula was the first language
with object-oriented features. The Simula language has features for
quasi-parallel execution and a framework for doing simulations.

%package -n %{libname}
Summary:	Gnu Cim libraries packages
Group:		Development/Other

%description -n %{libname}
This package contains the libraries needed to run programs dynamically 
linked with cim (the Gnu Simula Compiler)

%package -n %{libname_devel}
Summary:	Headers for developing programs that will use cim
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel
Provides:	%{libname_orig}-devel

%description -n %{libname_devel}
This package contains the headers that programmers will need to develop
applications which will use cim.

%prep
%setup -q
%patch0 -p0
%patch1 -p1

%build
%configure2_5x	--enable-dump=yes --disable-static
(cd src; make libdir=%{_libdir} includedir=%{_includedir})
%make all

%install
%makeinstall mandir=%{buildroot}%{_mandir} infodir=%{buildroot}%{_infodir}

cd %{buildroot}%{_libdir};chmod +x libcim.so.%{major}.0.0

%files
%doc NEWS
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{libname_devel}
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/cim.h
%{_mandir}/*/*
%{_infodir}/*
%doc README doc/SIMULA-HISTORY AUTHORS COPYING TODO

%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 3.37-8mdv2011.0
+ Revision: 663376
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 3.37-7mdv2011.0
+ Revision: 603831
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 3.37-6mdv2010.1
+ Revision: 522359
- rebuilt for 2010.1

* Thu Sep 24 2009 Olivier Blin <oblin@mandriva.com> 3.37-5mdv2010.0
+ Revision: 448225
- fix build (from Arnaud Patard)
  __progname is coming from libc so it has to be declared as extern
  This is fixing the build on mipsel where gcc doesn't like that

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 3.37-4mdv2010.0
+ Revision: 413236
- rebuild

* Tue Apr 07 2009 Funda Wang <fwang@mandriva.org> 3.37-3mdv2009.1
+ Revision: 364758
- fix str fmt

* Mon Aug 25 2008 Emmanuel Andry <eandry@mandriva.org> 3.37-3mdv2009.0
+ Revision: 276013
- apply devel policy
- check major

* Fri Jul 04 2008 Oden Eriksson <oeriksson@mandriva.com> 3.37-2mdv2009.0
+ Revision: 231852
- use _disable_ld_no_undefined to make it build

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 3.37-1mdv2008.1
+ Revision: 140693
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Apr 25 2007 Adam Williamson <awilliamson@mandriva.org> 3.37-1mdv2008.0
+ Revision: 18329
- 3.37 (rebuild for new era)
- drop patch (no longer needed)
- clean spec


* Fri May 12 2006 Stefan van der Eijk <stefan@eijk.nu> 3.36-10mdk
- rebuild for sparc

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 3.36-9mdk
- Rebuild

* Tue Aug 02 2005 Guillaume Bedot <littletux@mandriva.org> 3.36-8mdk
- changed buggy Patch0 (thanks to Gwenole Beauschene)
- use mkrel

* Sat Jul 30 2005 Guillaume Bedot <littletux@mandriva.org> 3.36-7mdk
- rebuild
- Patch0: allows to build with gcc4

* Thu Sep 18 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 3.36-6mdk
- fix deps

* Sat Jul 12 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 3.36-5mdk
- use %%mklibname
- fix url to source
- use %%configure and %%make macro

