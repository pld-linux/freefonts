Summary:	Collection of Free ATM Fonts
Summary(pl):	Kolekcja Darmowych Fontów ATM
Name:		freefonts
Version:	0.10
Release:	12
License:	free
Group:		X11/Fonts
Group(de):	X11/Fonts
Group(pl):	X11/Fonty
Source0:	ftp://sunsite.unc.edu/pub/Linux/X11/fonts/%{name}-%{version}.tar.gz
Source1:	%{name}.Fontmap
Prereq:		textutils
Prereq:		sed
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

%description -l pl
To jest kolekcja 78 darmowych fontów. Wszystkie z nich zosta³y
znalezione w archiwach CICA dla Windows. Niektórym z nich brakuje
znaków specjalnych, inne zawieraj± wy³±cznie wielkie litery, a inne
znów zawieraj± tylko znaki specjalne.

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

gzip -9nf README *.license

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{_t1fontsdir}
rm -f fonts.scale.bak Fontmap.bak
cat fonts.scale.* | sort -u > fonts.scale.tmp
cat fonts.scale.tmp | wc -l | sed -e 's/ //g' > fonts.scale
cat fonts.scale.tmp >> fonts.scale
rm -f fonts.scale.tmp
ln -sf fonts.scale fonts.dir
cat Fontmap.* > Fontmap

%postun
cd %{_t1fontsdir}
rm -f fonts.scale.bak Fontmap.bak
cat fonts.scale.* 2>/dev/null | sort -u > fonts.scale.tmp
cat fonts.scale.tmp | wc -l | sed -e 's/ //g' > fonts.scale
cat fonts.scale.tmp >> fonts.scale
rm -f fonts.scale.tmp
ln -sf fonts.scale fonts.dir
cat Fontmap.* > Fontmap 2>/dev/null

%files
%defattr(644,root,root,755)
%doc {README,*.license}.gz
%{_t1fontsdir}/*.pfb
%{_t1afmdir}/*.afm
%{_t1pfmdir}/*.pfm
