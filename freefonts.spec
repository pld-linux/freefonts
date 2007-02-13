Summary:	Collection of Free ATM Fonts
Summary(pl.UTF-8):	Kolekcja Darmowych Fontów ATM
Name:		freefonts
Version:	0.10
Release:	14
License:	Free
Group:		Fonts
Source0:	ftp://sunsite.unc.edu/pub/Linux/X11/fonts/%{name}-%{version}.tar.gz
# Source0-md5:	a547b5b861d6eb138394bb83748d4eee
Source1:	%{name}.Fontmap
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/Type1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_t1fontsdir	%{_fontsdir}/Type1
%define		_t1afmdir	%{_t1fontsdir}/afm
%define		_t1pfmdir	%{_t1fontsdir}/pfm

%description
This is a collection of 78 freely available fonts. All of them were
found in the CICA archives for Windows. Some of them are missing
special characters, some only contain capitals, some contain special
alphabets. Be careful and check!

%description -l pl.UTF-8
To jest kolekcja 78 darmowych fontów. Wszystkie z nich zostały
znalezione w archiwach CICA dla Windows. Niektórym z nich brakuje
znaków specjalnych, inne zawierają wyłącznie wielkie litery, a inne
znów zawierają tylko znaki specjalne.

%prep
%setup -q -n freefont

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_t1fontsdir},%{_t1afmdir},%{_t1pfmdir}}
mkdir ans
tar xzf ans.tgz -C ans
install ans/*.afm $RPM_BUILD_ROOT%{_t1afmdir}
install ans/*.pfm $RPM_BUILD_ROOT%{_t1pfmdir}
install *.pfb $RPM_BUILD_ROOT%{_t1fontsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_t1fontsdir}/Fontmap.%{name}
tail -n +2 fonts.dir > $RPM_BUILD_ROOT%{_t1fontsdir}/fonts.scale.%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst Type1

%postun
fontpostinst Type1

%files
%defattr(644,root,root,755)
%doc README *.license
%{_t1fontsdir}/fonts.scale.%{name}
%{_t1fontsdir}/Fontmap.%{name}
%{_t1fontsdir}/*.pfb
%{_t1afmdir}/*.afm
%{_t1pfmdir}/*.pfm
