#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	PPPort
Summary:	Devel::PPPort - Perl/Pollution/Portability
#Summary(pl.UTF-8):	
Name:		perl-Devel-PPPort
Version:	3.11_01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/MH/MHX/Devel-PPPort-3.11_01.tar.gz
# Source0-md5:	d446bc2e6346d213dffa67d6d3ac2965
URL:		http://search.cpan.org/dist/Devel-PPPort/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl's API has changed over time, gaining new features, new functions,
increasing its flexibility, and reducing the impact on the C namespace
environment (reduced pollution). The header file written by this module,
typically ppport.h, attempts to bring some of the newer Perl API
features to older versions of Perl, so that you can worry less about
keeping track of old releases, but users can still reap the benefit.

Devel::PPPort contains a single function, called WriteFile. Its
only purpose is to write the ppport.h C header file. This file
contains a series of macros and, if explicitly requested, functions that
allow XS modules to be built using older versions of Perl. Currently,
Perl versions from 5.003 to 5.9.4 are supported.

This module is used by h2xs to write the file ppport.h.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorarch}/Devel/*.pm
%dir %{perl_vendorarch}/auto/Devel/PPPort
%{perl_vendorarch}/auto/Devel/PPPort/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Devel/PPPort/*.so
%{_mandir}/man3/*
