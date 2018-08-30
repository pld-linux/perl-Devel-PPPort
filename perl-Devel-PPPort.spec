#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	PPPort
Summary:	Devel::PPPort - Perl/Pollution/Portability
Summary(pl.UTF-8):	Devel:::PPPort - Perl/Zanieczyszczenie/Przenośność
Name:		perl-Devel-PPPort
Version:	3.36
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Devel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e713c0b047949d1e1db5499af9f10b63
URL:		http://search.cpan.org/dist/Devel-PPPort/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl's API has changed over time, gaining new features, new functions,
increasing its flexibility, and reducing the impact on the C namespace
environment (reduced pollution). The header file written by this
module, typically ppport.h, attempts to bring some of the newer Perl
API features to older versions of Perl, so that you can worry less
about keeping track of old releases, but users can still reap the
benefit.

Devel::PPPort contains a single function, called WriteFile. Its
only purpose is to write the ppport.h C header file. This file
contains a series of macros and, if explicitly requested, functions
that allow XS modules to be built using older versions of Perl.
Currently, Perl versions from 5.003 to 5.10.0 are supported.

This module is used by h2xs to write the file ppport.h.

%description -l pl.UTF-8
Perlowe API zmieniało się w czasie, zyskując nowe możliwości, nowe
funkcje, zwiększając elastyczność i zmniejszając wpływ na środowisko
przestrzeni nazw C (mniejsze zanieczyszczenie). Plik nagłówkowy
zapisywany przez ten moduł, zwykle ppport.h, próbuje udostępnić
niektóre z nowych możliwości API Perla w starszych wersjach Perla, aby
mniej trzeba było martwić się o śledzenie starszych wersji.

Devel::PPPort zawiera jedną funkcję - WriteFile. Jej jedynym celem
jest zapis pliku nagłówkowego C ppport.h. Plik ten zawiera ciąg makr
i, jeśli tego zażądano, funkcje pozwalające na budowanie modułów XS
przy użyciu starszych wersji Perla. Aktualnie obsługiwane są wersje
Perla od 5.003 do 5.10.0.

Ten moduł jest używany przez h2xs do zapisu pliku ppport.h.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%{perl_vendorarch}/Devel/PPPort.pm
%dir %{perl_vendorarch}/auto/Devel/PPPort
%attr(755,root,root) %{perl_vendorarch}/auto/Devel/PPPort/PPPort.so
%{_mandir}/man3/Devel::PPPort.3pm*
