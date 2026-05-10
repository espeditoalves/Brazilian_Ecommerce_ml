.PHONY: test docs clean pre-commit

test:
	poetry run pytest tests/ -v

docs:
	@echo "Gerando documentação com pdoc3..."
	poetry run pdoc --html src -o docs --force
	@echo "Documentação gerada na pasta docs/."

docs-serve:
	@echo "Iniciando servidor de documentação local..."
	poetry run pdoc src --http localhost:8080

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache

pre-commit:
	poetry run pre-commit run --all-files
