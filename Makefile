# Makefile
# some handy commands

help:
	@echo "make sync    : readme, count and sync GitHub repo"
	@echo "make github  : sync + testcases"
	@echo "make test    : github + run tests (for GitHub repo source tree)"
	@echo "make cloc    : count lines of code"

sync:
	@./hr_github.sh

github:
	@./hr_github.sh -t

test:
	@./hr_github.sh -a

build:
	@mkdir -p build && cd build && cmake -DHACKERRANK_FP:BOOL=OFF -DCMAKE_BUILD_TYPE=Debug .. && make -j2

clean:
	rm -rf build

cloc:
	@cloc --exclude-dir=.vscode --vcs git
