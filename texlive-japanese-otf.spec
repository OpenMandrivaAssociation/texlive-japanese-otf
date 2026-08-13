%global tl_name japanese-otf
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Advanced font selection for platex and its friends
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/jptex/latex/japanese-otf
License:	bsd3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/japanese-otf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/japanese-otf.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/japanese-otf.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The package contains pLaTeX support files and virtual fonts for
supporting a wide variety of fonts in LaTeX using the pTeX engine.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from japanese-otf:
KanjiMap otf-@jaEmbed@.map
KanjiMap otf-ko-@koEmbed@.map
KanjiMap otf-sc-@scEmbed@.map
KanjiMap otf-tc-@tcEmbed@.map
KanjiMap otf-up-@jaEmbed@.map
TL_DROPIN_EOF
