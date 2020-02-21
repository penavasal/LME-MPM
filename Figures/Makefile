PY = /opt/anaconda3/bin/python3

Python:
	$(PY) Dyka_Analytical.py
	$(PY) Shape_Fun_LME.py
	$(PY) Shape_Fun_MPM.py
	$(PY) Shape_Fun_GIMP.py

watch:  ## Recompile if any updates
	@while [ 1 ]; do; inotifywait $(ALL); sleep 0.01; make all; done
