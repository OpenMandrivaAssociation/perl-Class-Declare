%define upstream_name    Class-Declare
%define upstream_version 0.20
Name:		perl-%{upstream_name}
Version:	0.20
Release:	1

Summary:	Class-Declare module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://github.com/denormal/perl-Class-Declare
Source0:	https://cpan.metacpan.org/authors/id/I/IB/IBB/Class-Declare-0.20.tar.gz

BuildRequires:	make
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
%setup -q -n %{upstream_name}-%{version}

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

