Summary:	a diff front-end program using GTK+(GNOME)
Summary(pl):	Frontend na program diff pod GTK+(GNOME)
Name:		gtkdiff
Version:	1.8.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://home.catv.ne.jp/pp/ginoue/software/gtkdiff/%{name}-%{version}.tar.gz
# Source0-md5:	536979ae70650680518a0b79d14e9366
URL:		http://home.catv.ne.jp/pp/ginoue/software/gtkdiff/index-e.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
gtkdiff is a diff front-end program using GTK+(GNOME). Its features
are following:
- It has two view modes, one-pane and two-panes.
- Supports directory diff.
- Easy navigation across differences.

%description -l pl
gtkdiff jest frontendem do programu diff u¿ywaj±cym GTK+ i GNOME.
Niektóre jego cechy to:
- dwa tryby ogl±dania - jedno- i dwupanelowy
- obs³uga diff dla katalogów
- ³atwa nawigacja pomiêdzy ró¿nicami.

%prep
%setup -q

%build
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
rm -f missing
%{__gettextize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Utilitiesdir=%{_applnkdir}/Utilities

install gtkdiffrc $RPM_BUILD_ROOT%{_datadir}/%{name}/

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gtkdiff
%{_applnkdir}/Utilities/gtkdiff.desktop
%{_mandir}/man1/*
