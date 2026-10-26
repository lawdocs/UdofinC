import sys, io, re
class Doc:
    def __init__(self, path):
        self.path = path
        with io.open(path, 'r', encoding='utf-8') as f:
            self.s = f.read()
        self.log = []
    def _find_once(self, marker):
        n = self.s.count(marker)
        if n != 1:
            raise SystemExit(f"MARKER COUNT {n} (expected 1) in {self.path}: {marker[:90]!r}")
        return self.s.index(marker)
    def insert_after_line(self, marker, text):
        i = self._find_once(marker); j = self.s.index('\n', i)
        self.s = self.s[:j+1] + text + ('' if text.endswith('\n') else '\n') + self.s[j+1:]
        self.log.append(f"insert_after_line {marker[:60]!r}")
    def insert_before_line(self, marker, text):
        i = self._find_once(marker); j = self.s.rfind('\n', 0, i) + 1
        self.s = self.s[:j] + text + ('' if text.endswith('\n') else '\n') + self.s[j:]
        self.log.append(f"insert_before_line {marker[:60]!r}")
    def replace_once(self, old, new):
        self._find_once(old); self.s = self.s.replace(old, new, 1)
        self.log.append(f"replace_once {old[:60]!r}")
    def replace_all(self, old, new):
        n = self.s.count(old); self.s = self.s.replace(old, new)
        self.log.append(f"replace_all x{n} {old[:60]!r}")
    def append(self, text):
        if not self.s.endswith('\n'): self.s += '\n'
        self.s += text; self.log.append("append")
    def save(self):
        with io.open(self.path, 'w', encoding='utf-8') as f: f.write(self.s)
        print(f"SAVED {self.path} ({len(self.s.split())} words)")
        for l in self.log: print("  -", l)
