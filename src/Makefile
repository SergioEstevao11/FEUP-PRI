all: clean_data refine_data plot


clean_data:
	python3 clean_data.py

refine_data:
	python3 refine_data.py

install:
	sudo apt-get install -Y python3 python3-virtualenv sqlite3 gzip

setup: install
	requirements.txt
	virtualenv .venv
	./.venv/bin/pip install -r requirements.txt

plot:
	python3 plot.py

clean:
	rm -rf __pycache__
	rm -rf .ipynb_checkpoints

clean_all: clean
	rm -f ./data/clean_data.json ./data/refined_data.json
	rm -rf ./.venv/


