test:
	clear
	python -m unittest

dev_test:
	fswatch -o tests fastqc_parser | xargs -n1 -I{} make test
