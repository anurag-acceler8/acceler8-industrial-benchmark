#!/usr/bin/env python3
"""Regenerate recommended_org_structure.data.js from recommended_org_structure.json."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
json_path = HERE / "recommended_org_structure.json"
js_path = HERE / "recommended_org_structure.data.js"

data = json.loads(json_path.read_text())
js_path.write_text(
    "/* Auto-synced from recommended_org_structure.json */\n"
    "window.RECOMMENDED_ORG_STRUCTURE = "
    + json.dumps(data, indent=2)
    + ";\n"
)
print(f"Updated {js_path.name} from {json_path.name}")
