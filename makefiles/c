CXX = gcc
CXXFLAGS = -Wall

OBJS = 

.PHONY: clean

all: main

main: main.c $(OBJS)
	$(CXX) $(CXXFLAGS) -o $@ $^

run:
	./main

clean:
	rm -f $(OBJS) main
