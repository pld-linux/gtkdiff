Summary:	A diff front-end program using GTK+(GNOME)
Summary(pl.UTF-8):	Nakładka na program diff pod GTK+(GNOME)
Name:		gtkdiff
Version:	1.8.0
Release:	8
License:	GPL
Group:		X11/Applications
Source0:	http://home.catv.ne.jp/pp/ginoue/software/gtkdiff/%{name}-%{version}.tar.gz
# Source0-md5:	536979ae70650680518a0b79d14e9366
Patch0:		%{name}-desktop.patch
URL:		http://home.catv.ne.jp/pp/ginoue/software/gtkdiff/index-e.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtkdiff is a diff front-end program using GTK+(GNOME). Its features
are following:
- It has two view modes, one-pane and two-panes.
- Supports directory diff.
- Easy navigation across differences.

%description -l pl.UTF-8
gtkdiff jest Nakładką na program diff używającą GTK+ i GNOME.
Niektóre jego cechy to:
- dwa tryby oglądania - jedno- i dwupanelowy
- obsługa diff dla katalogów
- łatwa nawigacja pomiędzy różnicami.

%prep
%setup -q
%patch0 -p1

%build
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
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
	Utilitiesdir=%{_desktopdir}

install gtkdiffrc $RPM_BUILD_ROOT%{_datadir}/%{name}/

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gtkdiff
%{_desktopdir}/gtkdiff.desktop
%{_mandir}/man1/*
