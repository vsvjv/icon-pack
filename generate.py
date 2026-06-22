import os
import json

ICON_DIR = "./icons"

icons = []

for file in os.listdir(ICON_DIR):
    if file.lower().endswith(".png"):
        name = os.path.splitext(file)[0]

        icons.append({
            "name": name,
            "file": f"icons/{file}"
        })

icons.sort(key=lambda x: x["name"].lower())

output = {
    "version": "1.0",
    "total": len(icons),
    "icons": icons
}

with open("icons.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"✅ 完成！生成 icons.json，共 {len(icons)} 个图标")