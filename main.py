# The GPS Swears It Was a Shortcut — one line, the GPS's own excuse.
# Pure stdlib, deterministic: the same line every run, no network, no input.
# Writes the line alone (no trailing newline) to /output/entry.txt.
import os

# The line: the GPS blames the satellites and the driver, never itself.
# Fresh detail against a saturated field (cul-de-sac / lake / wedding):
# a cornfield, and satellites that cannot smell corn. Smug, defensive,
# caught red-handed — with the turn landing on who it trusts.
LINE = "I routed you through the cornfield because satellites can't smell corn, and I trust satellites more than I trust you."

# Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1 to 200
# characters, not only white space.
if not 1 <= len(LINE) <= 200:
    raise SystemExit(f"entry must be 1-200 characters, got {len(LINE)}")
if not LINE.strip():
    raise SystemExit("entry must not be only white space")
if "\n" in LINE or "\r" in LINE:
    raise SystemExit("entry must be a single line")
LINE.encode("utf-8").decode("utf-8")  # UTF-8 round-trip

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
print(LINE)
