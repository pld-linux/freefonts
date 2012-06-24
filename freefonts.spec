Summary:     Collection of Free ATM Fonts
Summary(pl): Kolekcja Darmowych Font�w ATM
Name:        freefonts
Version:     0.10
Release:     12
Copyright:   free
Group:       X11/Utilities
Group(pl):   X11/Narz�dzia
Source:      ftp://sunsite.unc.edu/pub/Linux/X11/fonts/%{name}-%{version}.tar.gz
Requires:    type1inst >= 0.6.1
Prereq:      type1inst
BuildArchitectures: noarch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
This is a collection of 79 freely available fonts. All of them were found in
the CICA archives for Windows. Some of them are missing special characters,
some only contain capitals, some contain special alphabets. Be careful and
check!

%description -l pl
To jest kolekcja 79 darmowych font�w. Wszystkie z nich zosta�y znalezione w
archiwach CICA dla Windows. Niekt�rym z nich brakuje znak�w specjalnych,
inne zawieraj� wy��cznie wielkie litery, a inne zn�w zawieraj� tylko znaki
specjalne.

%prep
%setup -q -n freefont

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/share/fonts/Type1
install *.pfb $RPM_BUILD_ROOT/usr/share/fonts/Type1

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd /usr/share/fonts/Type1
type1inst -nogs -quiet

%postun
cd /usr/share/fonts/Type1
type1inst -nogs -quiet

%files
%defattr(644,root,root,755)
%doc README *.license
/usr/share/fonts/Type1/*.pfb
