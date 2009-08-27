#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MouseX
%define	pnam	Types-Path-Class
Summary:	MouseX::Types::Path::Class - A Path::Class type library for Mouse
Summary(pl.UTF-8):	MouseX::Types::Path::Class - biblioteka typu Path::Class dla Mouse
Name:		perl-MouseX-Types-Path-Class
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/MA/MASAKI/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d6283288e9ba7cbfece79a04b8b3dc22
URL:		http://search.cpan.org/dist/MouseX-Types-Path-Class/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(MouseX::Types) >= 0.01
BuildRequires:	perl-Mouse
BuildRequires:	perl-Path-Class
BuildRequires:	perl-Any-Moose >= 0.05
BuildRequires:	perl-Test-UseAllModules
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MouseX::Types::Path::Class - A Path::Class type library for Mouse

%description -l pl.UTF-8
MouseX::Types::Path::Class - biblioteka typu Path::Class dla Mouse

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MouseX/Types/Path/*.pm
%{_mandir}/man3/*
