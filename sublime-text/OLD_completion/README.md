# Plugins à installer

Installer LaTeXTools et LateX-cwl.

# Complétions

 - Aller dans "Préférences - Browse Packages"
 - Dans l'explorateur qui s'ouvre, créer un dossier "User/cwl"
 - Y copier le fichier "custom.cwl"
 - Dans les réglages de LaTeXTools, ajouter :
```
"cwl_list": [
        "tex.cwl",
        "latex-209.cwl",
        "latex-document.cwl",
        "latex-l2tabu.cwl",
        "latex-mathsymbols.cwl",
        "custom.cwl",
    ]
```
 - Dans le dossier "User", copier le fichier "latex-custom-snippets.sublime-completions".