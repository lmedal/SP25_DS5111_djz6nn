default:
	@cat Makefile

env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update: env
	. env/bin/activate && pip install -r requirements.txt

sample_data/ygainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > sample_data/ygainers.html

sample_data/ygainers.csv: sample_data/ygainers.html
	python -c "import pandas as pd; raw = pd.read_html('sample_data/ygainers.html'); raw[0].to_csv('sample_data/ygainers.csv')"

sample_data/wjsgainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=500 'https://www.wsj.com/market-data/stocks/us/movers' > sample_data/wjsgainers.html

sample_data/wjsgainers.csv:
	python scripts/test_wsj_selenium.py

lint:
	. env/bin/activate && pylint bin/normalize_csv.py

format:
	. env/bin/activate && black bin/normalize_csv.py

test:
	. env/bin/activate && make lint
	PYTHONPATH=. env/bin/python -m pytest -vv tests
gainers:
	env/bin/python get_gainer.py --src=$(SRC)
