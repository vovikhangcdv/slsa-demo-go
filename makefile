clean:
	rm -rf bin tmp

build:
	go build -o bin/main main.go

%:
	@: