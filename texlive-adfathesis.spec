Name:		texlive-adfathesis
Version:	26048
Release:	2
Summary:	Australian Defence Force Academy thesis format
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/adfathesis
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adfathesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adfathesis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adfathesis.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
