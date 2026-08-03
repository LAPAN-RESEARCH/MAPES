.PHONY: books clean figures verify

figures:
	python3 scripts/generate_figures.py

books: figures
	python3 scripts/build_books.py

verify:
	python3 scripts/verify_content.py

clean:
	python3 scripts/clean_build.py
