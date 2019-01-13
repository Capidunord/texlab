$pdf_mode = 5;
$xelatex = 'xelatex -no-pdf %O -shell-escape -synctex=1 %S';
$recorder = 1;
add_cus_dep('pytxcode', 'tex', 0, 'pythontex');
sub pythontex { return system("pythontex \"$_[0]\""); }