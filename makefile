.PHONY: start

start:
	docker build -t cmd-tool .
	docker run -t cmd-tool