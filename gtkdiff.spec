Name:		gtkdiff
Summary:	a diff front-end program using GTK+(GNOME).
Version:	1.5.1
Release:	1
License:	GPL
URL:		http://www.ainet.or.jp/~inoue/software/gtkdiff/index-e.html
Group:		X11/Utilities
Group(pl):	X11/Narzêdzia
Source0:	http://www.ainet.or.jp/~inoue/software/gtkdiff/%{name}-%{version}.tar.gz
Patch0:		gtkdiff-DESTDIR.patch
Patch1:		gtkdiff-applnkdir.patch
Requires:	gtk+ >= 1.2.0, gnome-libs >= 1.0.0
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
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1

%build
LDFLAGS="-s"
export LDFLAGS
%configure 
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
install -m 0644 gtkdiffrc $RPM_BUILD_ROOT%{_datadir}/%{name}/
gzip -9nf AUTHORS ChangeLog NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,TODO}.gz
%attr(755,root,root) %{_bindir}/*

%dir %{_datadir}/gtkdiff
%config %{_datadir}/gtkdiff/*
%{_datadir}/locale/*/*/*
%{_applnkdir}/Utilities/gtkdiff.desktop
%{_mandir}/man1/*
