update:
	python3 -m venv env
	. env/bin/activate && pip install -r requirements.txt

ygainers.csv:
	google-chrome --headless --disable-gpu --dump-dom https://example.com > ygainers.csv

