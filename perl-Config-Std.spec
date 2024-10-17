%define upstream_name    Config-Std
%define upstream_version 0.901

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3
Summary:    Load and save configuration files in a standard format 
License:    GPL or Artistic
Group:      Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Config/Config-Std-%{upstream_version}.tar.gz
BuildRequires:      perl(Module::Build)
BuildRequires:      perl(Class::Std)
Requires:           perl(Class::Std)
BuildArch:          noarch

%description
Load and save configuration files in a standard format 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
# only when building from CVS (version 1.51-3mdk)
#CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
#make docs -i
# only when building from CVS (version 1.51-3mdk)
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%clean 

%install
./Build install destdir=%{buildroot}

%files
%doc Changes README
%{perl_vendorlib}/Config/Std*
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.7.0-2mdv2011.0
+ Revision: 680844
- mass rebuild

* Mon Dec 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.0-1mdv2011.0
+ Revision: 474569
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - Import perl-Config-Std



* Tue May 22 2007 Shlomi Fish <shlomif@iglu.org.il> v0.0.4-1mdv2007.1
- Initial release.


