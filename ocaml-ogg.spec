Name:     ocaml-ogg

Version:  0.5.1
Release:  1
Summary:  OCaml bindings for libogg
License:  GPLv2+
URL:      https://github.com/savonet/ocaml-ogg
Source0:  https://github.com/savonet/ocaml-ogg/releases/download/%{version}/ocaml-ogg-%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-bytes
BuildRequires: libogg-devel
Requires:      libogg

%prep
%setup -q 

%build
./configure \
   --prefix=%{_prefix} \
   -disable-ldconf
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
install -d $OCAMLFIND_DESTDIR/stublibs
make install

%files
/usr/lib64/ocaml/ogg/META
/usr/lib64/ocaml/ogg/ogg.a
/usr/lib64/ocaml/ogg/ogg.cma
/usr/lib64/ocaml/ogg/ogg.cmi
/usr/lib64/ocaml/ogg/ogg.cmx
/usr/lib64/ocaml/ogg/ogg.cmxa
/usr/lib64/ocaml/ogg/ogg.mli
/usr/lib64/ocaml/ogg/ocaml-ogg.h
/usr/lib64/ocaml/ogg/ogg_demuxer.cmx
/usr/lib64/ocaml/ogg/ogg_demuxer.cmi
/usr/lib64/ocaml/ogg/ogg_demuxer.mli
/usr/lib64/ocaml/ogg/libogg_stubs.a
/usr/lib64/ocaml/stublibs/dllogg_stubs.so
/usr/lib64/ocaml/stublibs/dllogg_stubs.so.owner

%description
OCAML bindings for libogg


%changelog
* Sat Apr 15 2017 Lucas Bickel <hairmare@rabe.ch>
- Bump version

* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch>
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-ogg.spec
