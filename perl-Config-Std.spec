%define upstream_name    Config-Std
%define upstream_version 0.007

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary:    Load and save configuration files in a standard format 
License:    GPL or Artistic
Group:      Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:      perl(Module::Build)
BuildRequires:      perl(Class::Std)
Requires:           perl(Class::Std)
BuildArch:          noarch
BuildRoot:          %{_tmppath}/%{name}-%{version}

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
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Config/Std*
%{_mandir}/*/*
