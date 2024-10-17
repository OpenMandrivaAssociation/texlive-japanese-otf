Name:		texlive-japanese-otf
Epoch:		1
Version:	64072
Release:	2
Summary:	Advanced font selection for platex and its friends
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/japanese/japanese-otf
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/japanese-otf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/japanese-otf.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/japanese-otf.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex

%description
The package contains pLaTeX support files and virtual fonts for
supporting a wide variety of fonts in LaTeX using the pTeX
engine.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/ofm/public/japanese-otf
%{_texmfdistdir}/fonts/tfm/public/japanese-otf
%{_texmfdistdir}/fonts/vf/public/japanese-otf
%{_texmfdistdir}/tex/platex/japanese-otf
%_texmf_updmap_d/japanese-otf
%doc %{_texmfdistdir}/doc/fonts/japanese-otf
#- source
%doc %{_texmfdistdir}/source/fonts/japanese-otf

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/japanese-otf <<EOF
KanjiMap otf-@kanjiEmbed@.map
KanjiMap otf-cktx.map
EOF
