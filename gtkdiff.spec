Summary:	a diff front-end program using GTK+(GNOME)
Name:		gtkdiff
Version:	1.6.0
Release:	2
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://www.ainet.or.jp/~inoue/software/gtkdiff/%{name}-%{version}.tar.gz
URL:		http://www.ainet.or.jp/~inoue/software/gtkdiff/index-e.html
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
gtkdiff is a diff front-end program using GTK+(GNOME). Its features
are following:
- It has two view modes, one-pane and two-panes.
- Supports directory diff.
- Easy navigation across differences.

%prep
%setup -q

%build
gettextize --copy --force
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Utilitiesdir=%{_applnkdir}/Utilities

install gtkdiffrc $RPM_BUILD_ROOT%{_datadir}/%{name}/

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gtkdiff
%{_applnkdir}/Utilities/gtkdiff.desktop
%{_mandir}/man1/*
