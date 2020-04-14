$xelatex = 'lualatex -no-pdf %O -shell-escape -synctex=1 %S';
$recorder = 1;
add_cus_dep('pytxcode', 'tex', 0, 'pythontex');
sub pythontex { return system("pythontex \"$_[0]\""); }