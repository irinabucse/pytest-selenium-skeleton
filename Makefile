all:
	source env/bin/activate
run:
	@echo "Running tests"
	pytest ./src/Tests/test_abc.py --alluredir=./results

generate:
	@echo "Generating allure reports..."
	allure generate ./results --clean

clean:
	@echo "Cleaning up..."
	rm -rf ./results/*

start_ui:
	@echo "Starting ui..."
	$(shell ./bin/start_server.sh)
