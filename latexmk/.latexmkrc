$pdf_mode = 5;
$xelatex = 'xelatex -shell-escape -interaction=nonstopmode -file-line-error -synctex=1 %O %S';
$recorder = 1;
add_cus_dep('pytxcode', 'tex', 0, 'pythontex');
sub pythontex { return system("pythontex \"$_[0]\""); }