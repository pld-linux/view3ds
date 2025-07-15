Summary:	A simple realtime 3DS file previewer
Summary(pl.UTF-8):	Prosta przeglądarka plików 3DS działająca w czasie rzeczywistym
Name:		view3ds
Version:	1.0.0
Release:	1
License:	LGPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/lib3ds/%{name}-%{version}.tar.gz
# Source0-md5:	d2b297379865111654537dd141e0e79a
Patch0:		%{name}-update.patch
URL:		http://lib3ds.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	automake >= 1.4
BuildRequires:	lib3ds-devel >= 1.1.0
BuildRequires:	qt-devel >= 2.2.0
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
A simple realtime 3DS file previewer based on the lib3ds library.

%description -l pl.UTF-8
Prosta przeglądarka plików 3DS działająca w czasie rzeczywistym,
oparta na bibliotece 3ds

%prep
%setup -q
%patch -P0 -p1

%build
# extract CONFIGURE_{X11,OPENGL,QT} macros
tail -n +627 aclocal.m4 > acinclude.m4
# ...but ac/am/lt cannot be rebuilt - Makefile.in is hacked for moc :/
cp -f /usr/share/automake/config.* .
CPP="%{__cxx} -E"; export CPP
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
