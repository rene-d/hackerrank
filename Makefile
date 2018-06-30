# Makefile
# some handy commands

help:
	@echo "make github  : sync github repo"
	@echo "make test    : sync github, build and run the tests"
	@echo "make clean   : remove"
	@echo "make cloc"

sync:
	@./hr_github.sh

github:
	@./hr_github.sh -t

test:
	@./hr_github.sh -T

clean:
	rm -rf build

cloc:
	@cloc --exclude-dir=.vscode --vcs git
