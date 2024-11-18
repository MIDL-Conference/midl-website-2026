DEBUG = #--no-minify
TARGET = output/

.phony: FORCE

all: $(TARGET)

$(TARGET): FORCE
# 	PYTHONPATH=/home/hoel/code/midl-website-builder python -m mwb . $@ $(DEBUG)
# 	PYTHONPATH="/home/hoel/code/midl-website/builder" python -m mwb . $@ $(DEBUG)
	python -m mwb . $@ $(DEBUG)

FORCE: