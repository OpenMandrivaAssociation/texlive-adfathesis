# revision 26048
# category Package
# catalog-ctan /macros/latex/contrib/adfathesis
# catalog-date 2011-11-23 23:58:18 +0100
# catalog-license pd
# catalog-version 2.42
Name:		texlive-adfathesis
Version:	2.42
Release:	8
Summary:	Australian Defence Force Academy thesis format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/adfathesis
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adfathesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adfathesis.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adfathesis.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle includes a BibTeX style file.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/adfathesis/adfathesis.bst
%{_texmfdistdir}/tex/latex/adfathesis/adfathesis.cls
%doc %{_texmfdistdir}/doc/latex/adfathesis/README
%doc %{_texmfdistdir}/doc/latex/adfathesis/adfathesis.pdf
%doc %{_texmfdistdir}/doc/latex/adfathesis/template.tex
#- source
%doc %{_texmfdistdir}/source/latex/adfathesis/adfathesis.dtx
%doc %{_texmfdistdir}/source/latex/adfathesis/adfathesis.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.42-2
+ Revision: 813364
- Update to latest release.
- Import texlive-adfathesis
- Import texlive-adfathesis

