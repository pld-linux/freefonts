Summary:     Collection of Free ATM Fonts
Summary(pl): Kolekcja Darmowych Fontów ATM
Name:        freefonts
Version:     0.10
Release:     12
Copyright:   free
Group:       X11/Utilities
Group(pl):   X11/Narzêdzia
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
To jest kolekcja 79 darmowych fontów. Wszystkie z nich zosta³y znalezione w
archiwach CICA dla Windows. Niektórym z nich brakuje znaków specjalnych,
inne zawieraj± wy³±cznie wielkie litery, a inne znów zawieraj± tylko znaki
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
