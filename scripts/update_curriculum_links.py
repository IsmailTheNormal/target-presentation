#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

with open("scripts/annual_curriculum_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

NEW_LINKS = {
  "26-dars-mvc-backend-va-relyatsion-baza": {
    "hw_url": "classes/9-sinf/6-hafta/26-dars-mvc-backend-va-relyatsion-baza/vazifa.html",
    "test_url": "classes/9-sinf/6-hafta/26-dars-mvc-backend-va-relyatsion-baza/test.html"
  },
  "29-dars-gps-navigatsiya-va-eng-qisqa-yol": {
    "hw_url": "classes/7-8-sinf/7-hafta/29-dars-gps-navigatsiya-va-eng-qisqa-yol/vazifa.html",
    "test_url": "classes/7-8-sinf/7-hafta/29-dars-gps-navigatsiya-va-eng-qisqa-yol/test.html"
  },
  "21-dars-raqamli-iz-va-maxfiylik": {
    "hw_url": "classes/5-6-sinf/7-hafta/21-dars-raqamli-iz-va-maxfiylik/vazifa.html",
    "test_url": "classes/5-6-sinf/7-hafta/21-dars-raqamli-iz-va-maxfiylik/test.html"
  }
}

updated = 0
for c in data["cohorts"]:
    for w in c["weeks"]:
        for l in w.get("lessons", []):
            lid = l.get("id")
            if lid in NEW_LINKS:
                l["has_hw"] = True
                l["hw_url"] = NEW_LINKS[lid]["hw_url"]
                l["has_test"] = True
                l["test_url"] = NEW_LINKS[lid]["test_url"]
                updated += 1
                print(f"✓ Updated {lid}")

with open("scripts/annual_curriculum_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nSuccessfully updated {updated} lessons in scripts/annual_curriculum_data.json!")
