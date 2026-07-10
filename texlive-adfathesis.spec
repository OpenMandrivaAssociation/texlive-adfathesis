%global tl_name adfathesis
%global tl_revision 26048

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.42
Release:	%{tl_revision}.1
Summary:	Australian Defence Force Academy thesis format
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/adfathesis
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/adfathesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/adfathesis.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/adfathesis.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle includes a BibTeX style file.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/bibtex
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/bibtex/bst
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/bibtex/bst/adfathesis
%dir %{_datadir}/texmf-dist/doc/latex/adfathesis
%dir %{_datadir}/texmf-dist/source/latex/adfathesis
%dir %{_datadir}/texmf-dist/tex/latex/adfathesis
%{_datadir}/texmf-dist/bibtex/bst/adfathesis/adfathesis.bst
%doc %{_datadir}/texmf-dist/doc/latex/adfathesis/README
%doc %{_datadir}/texmf-dist/doc/latex/adfathesis/adfathesis.pdf
%doc %{_datadir}/texmf-dist/doc/latex/adfathesis/template.tex
%doc %{_datadir}/texmf-dist/source/latex/adfathesis/adfathesis.dtx
%doc %{_datadir}/texmf-dist/source/latex/adfathesis/adfathesis.ins
%{_datadir}/texmf-dist/tex/latex/adfathesis/adfathesis.cls
