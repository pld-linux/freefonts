Summary:   Collection of Free ATM Fonts
Name:      freefonts
Version:   0.10
Release:   10
Copyright: free
BuildArchitectures: noarch
Group:     X11/fonts
Source:    ftp://sunsite.unc.edu/pub/Linux/X11/fonts/%{name}-%{version}.tar.gz
Requires:  type1inst >= 0.6.1
Prereq:    type1inst
BuildRoot: /tmp/%{name}-%{version}-root

%description
This is a collection of 79 freely available fonts. All of them were found in
the CICA archives for Windows. Some of them are missing special characters,
some only contain capitals, some contain special alphabets. Be careful and
check!

%prep
%setup -q -n freefont

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/lib/X11/fonts/Type1
install *.pfb $RPM_BUILD_ROOT/usr/X11R6/lib/X11/fonts/Type1

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd /usr/X11R6/lib/X11/fonts/Type1
type1inst -nogs -quiet

%postun
cd /usr/X11R6/lib/X11/fonts/Type1
type1inst -nogs -quiet

%files
%defattr(644, root, root, 755)
%doc README *.license
/usr/X11R6/lib/X11/fonts/Type1/*.pfb

%changelog
* Thu Jul 23 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.10-10]
- added "Requires: type1inst >= 0.6.1",
- fixed %defattr.

* Wed May  6 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
- %%{version} macro instead %%{PACKAGE_VERSION},
- added -q %setup parameter,
- added using %%{name} macro in Buildroot and Source field.

* Fri Apr 17 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
- Buildroot changed to /tmp/freefonts-%%{PACKAGE_VERSION}-root,
- added %%{PACKAGE_VERSION} to Source url,
- replaced "mkdir -p" with "install -d" in %install,
- simplification in %files,
- added beter font (un)registration in font.scale by using for this
  type1inst perl script (changed %post, %postun),
- added %defattr macro in %files (allows building package from
  non-root account); %defattr requires rpm >= 2.4.99.

* Tue Dec 9 1997 Peter Soos <sp@osb.hu>
Moved to noarch architecture
