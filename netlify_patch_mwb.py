# netlify_patch_mwb.py
# 让 mwb 在 Netlify 上不要开 multiprocessing.Pool（避免 SemLock 报错）

import multiprocessing.pool as mpp

class DummyPool:
    def __enter__(self): return self
    def __exit__(self, *a): return False
    def map(self, func, it): return list(map(func, it))
    def imap_unordered(self, func, it): return iter(map(func, it))
    def close(self): pass
    def join(self): pass
    def terminate(self): pass

# 把 Pool 替换成单进程版本
mpp.Pool = lambda *a, **k: DummyPool()
