.PHONY: all clean_all

all: clean_data refine_data plot

clean_data:
	python3 clean_data.py

refine_data: ./data/clean_data.json
	python3 refine_data.py

plot: ./data/refined_data.json
	python3 graphics_parse.py

clean:
	rm -rf __pycache__
	rm -rf .ipynb_checkpoints

clean_all: clean
	rm ./data/clean_data.json
	rm ./data/refined_data.json

