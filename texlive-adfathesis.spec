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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle includes a BibTeX style file.

