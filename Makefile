test:
	clear
	python -m unittest

dev_test:
	fswatch -o tests fastqc_parser | xargs -n1 -I{} make test

blast:
	bin/blastFastQC --debug --input tests/data/fastqc_data.txt --output ~/test_blastFastQC.csv
