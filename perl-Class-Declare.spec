%define real_name Class-Declare

Summary:	Class-Declare module for perl 
Name:		perl-%{real_name}
Version:	0.05
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel, perl-Test-Exception
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Class::Declare allows class authors to specify public, private and
protected attributes and methods for their classes, giving them control
over how their modules may be accessed. The standard object oriented
programming concepts of *public*, *private* and *protected* have been
implemented for both class and instance (or object) attributes and
methods.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Class/Declare.pm
%{perl_vendorlib}/Class/Declare
%{_mandir}/*/*


