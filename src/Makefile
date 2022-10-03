all: database


clean_data:
	python3 clean_data.py

refine_data:
	clean_data
	python3 refine_data.py

database: 
	refine_data
	python3 database.py

install:
	sudo apt-get install -Y python3 python3-virtualenv sqlite3 gzip

setup: 
	install
	requirements.txt
	virtualenv .venv
	./.venv/bin/pip install -r requirements.txt

plot:
	python3 plot.py

clean:
	rm -rf __pycache__
	rm -f clean_*.csv refined_*.csv database.db

