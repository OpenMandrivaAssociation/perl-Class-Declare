%define upstream_name    Class-Declare
%define upstream_version 0.17

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Class-Declare module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::Exception)
BuildArch:	noarch

%description
Class::Declare allows class authors to specify public, private and
protected attributes and methods for their classes, giving them control
over how their modules may be accessed. The standard object oriented
programming concepts of *public*, *private* and *protected* have been
implemented for both class and instance (or object) attributes and
methods.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Class/Declare.pm
%{perl_vendorlib}/Class/Declare
%{_mandir}/*/*

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.170.0-2mdv2011.0
+ Revision: 680818
- mass rebuild

* Mon Aug 23 2010 Jérôme Quelin <jquelin@mandriva.org> 0.170.0-1mdv2011.0
+ Revision: 572182
- update to 0.17
- bump mkrel
- update to 0.13

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.0
+ Revision: 403011
- rebuild using %%perl_convert_version

* Tue Jul 08 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdv2009.0
+ Revision: 232708
- update to new version 0.12

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.08-1mdv2008.1
+ Revision: 136683
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2008.0
+ Revision: 46614
- update to new version 0.08


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 0.05-1mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.05-1mdk
- initial Mandriva package

