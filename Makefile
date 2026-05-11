.PHONY: test docs clean pre-commit

test:
	pytest tests/ -v

docs:
	@echo "Gerando documentação com MkDocs..."
	.venv/Scripts/mkdocs build
	@echo "Documentação gerada na pasta site/."

docs-serve:
	@echo "Iniciando servidor de documentação local..."
	.venv/Scripts/mkdocs serve

clean:
	rm -rf docs/src
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache

pre-commit:
	pre-commit run --all-files
