test: all
	python3 test/acceptance/test_echoserver.py

all: bin/echoserver

bin/echoserver: build/echoserver.o
	gcc -o bin/echoserver -Wall -Werror echoserver.o

build/echoserver.o: src/echoserver.c
	gcc -c -Wall -Werror src/echoserver.c -o build/echoserver.o