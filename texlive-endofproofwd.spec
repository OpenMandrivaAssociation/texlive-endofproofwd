Name:		texlive-endofproofwd
Version:	55643
Release:	2
Summary:	An "end of proof" sign
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/endofproofwd
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endofproofwd.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endofproofwd.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides an additional "end of proof" sign. The
command's name is \wasserdicht.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/endofproofwd
%doc %{_texmfdistdir}/doc/latex/endofproofwd

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
