$pdf_mode = 5;
$xelatex = 'xelatex -no-pdf %O -shell-escape %S';
$recorder = 1;
add_cus_dep('pytxcode', 'tex', 0, 'pythontex');
sub pythontex { return system("pythontex \"$_[0]\""); }