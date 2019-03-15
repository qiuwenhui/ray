import os


for i in range(100):
  os.system("python -m pytest -v python/ray/tests/test_failure.py")
