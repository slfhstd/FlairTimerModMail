"""
Robust shim for project configuration.

This file attempts to locate a real configuration module named either
- a package module at `config/config.py` (importable as `config.config`), or
- a standalone `config.py` file elsewhere on `sys.path`.

It then imports that module and re-exports its public names so existing
`import config` usages continue to work regardless of whether the
configuration was moved into a `config/` directory or left as a file.
"""

import sys
import os
import importlib
import importlib.util


def _find_real_config():
	# Try the straightforward import first (works when `config` is a package)
	try:
		return importlib.import_module('config.config')
	except Exception:
		pass

	# Search sys.path for a candidate `config/config.py` or another `config.py` (not this file)
	this_path = os.path.abspath(__file__)
	for p in sys.path:
		if not p:
			p = os.getcwd()
		# candidate package file
		cand = os.path.join(p, 'config', 'config.py')
		if os.path.isfile(cand):
			spec = importlib.util.spec_from_file_location('config_real', cand)
			mod = importlib.util.module_from_spec(spec)
			spec.loader.exec_module(mod)
			return mod

		# candidate standalone config.py (avoid loading this shim file)
		cand2 = os.path.join(p, 'config.py')
		if os.path.isfile(cand2) and os.path.abspath(cand2) != this_path:
			spec = importlib.util.spec_from_file_location('config_real', cand2)
			mod = importlib.util.module_from_spec(spec)
			spec.loader.exec_module(mod)
			return mod

	return None


_real = _find_real_config()
if _real is None:
	raise ImportError('Could not locate real configuration (config/config.py or another config.py)')

# Re-export public names from the real config module
for _k, _v in _real.__dict__.items():
	if not _k.startswith('_'):
		globals()[_k] = _v

