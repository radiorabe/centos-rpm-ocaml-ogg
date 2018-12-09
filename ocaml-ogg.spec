%define debug_package %{nil}

Name:     ocaml-ogg
Version:  0.5.2
Release:  3
Summary:  OCaml bindings for libogg

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

License:  GPLv2+
URL:      https://github.com/savonet/ocaml-ogg
Source0:  https://github.com/savonet/ocaml-ogg/releases/download/%{version}/ocaml-ogg-%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: libogg-devel
Requires:      libogg


%description
OCAML bindings for libogg


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}

%build
./configure \
   --prefix=%{_prefix} \
   --disable-ldconf
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
install -d $OCAMLFIND_DESTDIR/stublibs
make install

%files
%doc README
%license COPYING
%{_libdir}/ocaml/%{libname}
%{_libdir}/ocaml/stublibs/dll%{libname}_stubs.so
%{_libdir}/ocaml/stublibs/dll%{libname}_stubs.so.owner
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/%{libname}/*.a
%exclude %{_libdir}/ocaml/%{libname}/*.cmxa
%exclude %{_libdir}/ocaml/%{libname}/*.cmx
%exclude %{_libdir}/ocaml/%{libname}/*.mli
%endif

%files devel
%license COPYING
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{libname}/*.a
%{_libdir}/ocaml/%{libname}/*.cmxa
%{_libdir}/ocaml/%{libname}/*.cmx
%{_libdir}/ocaml/%{libname}/*.mli
%endif

%changelog
* Sun Dec  9 2018 Lucas Bickel <hairmare@rabe.ch> - 0.5.2-3
- Cleanup and add seperate -devel subpackage

* Sun Nov 11 2018 Lucas Bickel <hairmare@rabe.ch> - 0.5.2-2
- Fix Fedora Rawhide build

* Sun Oct  8 2017 Lucas Bickel <hairmare@rabe.ch> - 0.5.2-1
- Bump version

* Sat Apr 15 2017 Lucas Bickel <hairmare@rabe.ch>
- Bump version

* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch>
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-ogg.spec
