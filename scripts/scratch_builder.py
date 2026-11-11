#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/scratch_builder.py — Autonomous Scratch 3.0 Project (.sb3) Compiler

Generates 100% valid, native Scratch 3.0 (.sb3) ZIP archives with project.json
and official vector assets, ready for import into scratch.mit.edu or Scratch Desktop.
"""

import os
import json
import zipfile
import uuid

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ASSETS_DIR = os.path.join(REPO_ROOT, "assets", "scratch")

# Canonical Asset Definitions
CAT_COSTUME1 = {
    "assetId": "b7853f557e4426412e64bb3da6531a99",
    "name": "costume1",
    "bitmapResolution": 1,
    "md5ext": "b7853f557e4426412e64bb3da6531a99.svg",
    "dataFormat": "svg",
    "rotationCenterX": 48,
    "rotationCenterY": 50
}

CAT_COSTUME2 = {
    "assetId": "e6ddc55a6ddd9cc9d84fe0b4c21e016f",
    "name": "costume2",
    "bitmapResolution": 1,
    "md5ext": "e6ddc55a6ddd9cc9d84fe0b4c21e016f.svg",
    "dataFormat": "svg",
    "rotationCenterX": 46,
    "rotationCenterY": 53
}

STAGE_BACKDROP = {
    "assetId": "cd21514d0531fdffb22204e0ec5ed84a",
    "name": "backdrop1",
    "md5ext": "cd21514d0531fdffb22204e0ec5ed84a.svg",
    "dataFormat": "svg",
    "rotationCenterX": 240,
    "rotationCenterY": 180
}

MEOW_SOUND = {
    "assetId": "83c36d806dc92327b9e7049a565c6bff",
    "name": "Meow",
    "dataFormat": "wav",
    "format": "",
    "rate": 22050,
    "sampleCount": 18688,
    "md5ext": "83c36d806dc92327b9e7049a565c6bff.wav"
}

POP_SOUND = {
    "assetId": "83a9787d4cb6f3b7632b4ddfebf74367",
    "name": "pop",
    "dataFormat": "wav",
    "format": "",
    "rate": 11025,
    "sampleCount": 258,
    "md5ext": "83a9787d4cb6f3b7632b4ddfebf74367.wav"
}

class ScratchBlockBuilder:
    def __init__(self):
        self.blocks = {}

    def add(self, block_id, opcode, next_id=None, parent_id=None, inputs=None, fields=None, top_level=False, x=0, y=0):
        block = {
            "opcode": opcode,
            "next": next_id,
            "parent": parent_id,
            "inputs": inputs or {},
            "fields": fields or {},
            "topLevel": top_level
        }
        if top_level:
            block["x"] = x
            block["y"] = y
        self.blocks[block_id] = block
        return block_id

    def build(self):
        return self.blocks


def build_sb3(output_path, targets, required_asset_files=None):
    """Packages project.json and assets into a valid .sb3 file."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    project_json = {
        "targets": targets,
        "monitors": [],
        "extensions": [],
        "meta": {
            "semver": "3.0.0",
            "vm": "0.2.0",
            "agent": "Target School Scratch Compiler"
        }
    }

    if required_asset_files is None:
        required_asset_files = [
            "b7853f557e4426412e64bb3da6531a99.svg",
            "e6ddc55a6ddd9cc9d84fe0b4c21e016f.svg",
            "cd21514d0531fdffb22204e0ec5ed84a.svg",
            "83c36d806dc92327b9e7049a565c6bff.wav",
            "83a9787d4cb6f3b7632b4ddfebf74367.wav"
        ]

    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr("project.json", json.dumps(project_json, indent=2))
        for filename in required_asset_files:
            asset_src = os.path.join(ASSETS_DIR, filename)
            if os.path.exists(asset_src):
                z.write(asset_src, filename)
            else:
                print(f"Warning: Asset not found: {asset_src}")

    print(f"  ✓ Built Scratch Project: {output_path} ({os.path.getsize(output_path)} bytes)")
    return output_path


def generate_lesson_26_projects(dest_dir):
    """
    Generates Starter and Solution .sb3 projects for Lesson 26:
    'Scratchda Jonli Animatsiyalar: Kostyumlar, Qadam Tashlash va Gapiruvchi Pufakchalar'
    """
    # 1. SOLUTION PROJECT: Complete Walk Cycle + Left-Right Rotation + Edge Bounce + Spacebar Speech
    sol_builder = ScratchBlockBuilder()
    
    # Script 1: Walk Cycle Loop
    sol_builder.add("b_flag", "event_whenflagclicked", next_id="b_rot", top_level=True, x=80, y=80)
    sol_builder.add("b_rot", "motion_setrotationstyle", next_id="b_forever", parent_id="b_flag", fields={"STYLE": ["left-right", None]})
    sol_builder.add("b_forever", "control_forever", next_id=None, parent_id="b_rot", inputs={"SUBSTACK": [2, "b_nextcostume"]})
    sol_builder.add("b_nextcostume", "looks_nextcostume", next_id="b_move", parent_id="b_forever")
    sol_builder.add("b_move", "motion_movesteps", next_id="b_wait", parent_id="b_nextcostume", inputs={"STEPS": [1, [4, "10"]]})
    sol_builder.add("b_wait", "control_wait", next_id="b_bounce", parent_id="b_move", inputs={"DURATION": [1, [4, "0.15"]]})
    sol_builder.add("b_bounce", "motion_ifonedgebounce", next_id=None, parent_id="b_wait")

    # Script 2: Speech Bubble on Spacebar
    sol_builder.add("b_space", "event_whenkeypressed", next_id="b_say", top_level=True, x=80, y=360, fields={"KEY_OPTION": ["space", None]})
    sol_builder.add("b_say", "looks_sayforsecs", next_id=None, parent_id="b_space", inputs={
        "MESSAGE": [1, [10, "Salom! Men jonli qadam tashlayapman!"]],
        "SECS": [1, [4, "2"]]
    })

    targets_solution = [
        {
            "isStage": True,
            "name": "Stage",
            "variables": {},
            "lists": {},
            "broadcasts": {},
            "blocks": {},
            "currentCostume": 0,
            "costumes": [STAGE_BACKDROP],
            "sounds": [POP_SOUND],
            "volume": 100,
            "layerOrder": 0
        },
        {
            "isStage": False,
            "name": "ScratchCat",
            "variables": {},
            "lists": {},
            "broadcasts": {},
            "blocks": sol_builder.build(),
            "currentCostume": 0,
            "costumes": [CAT_COSTUME1, CAT_COSTUME2],
            "sounds": [MEOW_SOUND],
            "volume": 100,
            "visible": True,
            "x": -100,
            "y": -30,
            "size": 100,
            "direction": 90,
            "draggable": False,
            "rotationStyle": "left-right"
        }
    ]

    sol_path = os.path.join(dest_dir, "yechim_jonli_animatsiya.sb3")
    build_sb3(sol_path, targets_solution)

    # 2. STARTER PROJECT: Cat is set up with both costumes, ready for student to attach blocks
    start_builder = ScratchBlockBuilder()
    start_builder.add("s_flag", "event_whenflagclicked", next_id=None, top_level=True, x=80, y=80)
    # Give a hint comment or standalone blocks on workspace for student to connect
    start_builder.add("s_hint_move", "motion_movesteps", next_id=None, top_level=True, x=280, y=80, inputs={"STEPS": [1, [4, "10"]]})
    start_builder.add("s_hint_costume", "looks_nextcostume", next_id=None, top_level=True, x=280, y=140)
    start_builder.add("s_hint_wait", "control_wait", next_id=None, top_level=True, x=280, y=200, inputs={"DURATION": [1, [4, "0.15"]]})

    targets_starter = [
        {
            "isStage": True,
            "name": "Stage",
            "variables": {},
            "lists": {},
            "broadcasts": {},
            "blocks": {},
            "currentCostume": 0,
            "costumes": [STAGE_BACKDROP],
            "sounds": [POP_SOUND],
            "volume": 100,
            "layerOrder": 0
        },
        {
            "isStage": False,
            "name": "ScratchCat",
            "variables": {},
            "lists": {},
            "broadcasts": {},
            "blocks": start_builder.build(),
            "currentCostume": 0,
            "costumes": [CAT_COSTUME1, CAT_COSTUME2],
            "sounds": [MEOW_SOUND],
            "volume": 100,
            "visible": True,
            "x": 0,
            "y": 0,
            "size": 100,
            "direction": 90,
            "draggable": False,
            "rotationStyle": "left-right"
        }
    ]

    start_path = os.path.join(dest_dir, "starter_jonli_animatsiya.sb3")
    build_sb3(start_path, targets_starter)

    return start_path, sol_path


def generate_lesson_24_projects(dest_dir):
    """
    Generates Starter and Solution .sb3 projects for Lesson 24:
    'Scratch 3.0 Sehri: Spraytlar, Sahnalar va Birinchi Qadamlar'
    Arrow-key steering, coordinates, and reset on Green Flag.
    """
    sol_builder = ScratchBlockBuilder()
    # Green flag reset
    sol_builder.add("b_flag", "event_whenflagclicked", next_id="b_goto", top_level=True, x=60, y=60)
    sol_builder.add("b_goto", "motion_gotoxy", next_id="b_rot", parent_id="b_flag", inputs={
        "X": [1, [4, "0"]],
        "Y": [1, [4, "0"]]
    })
    sol_builder.add("b_rot", "motion_setrotationstyle", next_id=None, parent_id="b_goto", fields={"STYLE": ["left-right", None]})

    # Arrow keys
    # Right arrow
    sol_builder.add("k_right", "event_whenkeypressed", next_id="k_r_dir", top_level=True, x=60, y=200, fields={"KEY_OPTION": ["right arrow", None]})
    sol_builder.add("k_r_dir", "motion_pointindirection", next_id="k_r_move", parent_id="k_right", inputs={"DIRECTION": [1, [4, "90"]]})
    sol_builder.add("k_r_move", "motion_movesteps", next_id=None, parent_id="k_r_dir", inputs={"STEPS": [1, [4, "15"]]})

    # Left arrow
    sol_builder.add("k_left", "event_whenkeypressed", next_id="k_l_dir", top_level=True, x=260, y=200, fields={"KEY_OPTION": ["left arrow", None]})
    sol_builder.add("k_l_dir", "motion_pointindirection", next_id="k_l_move", parent_id="k_left", inputs={"DIRECTION": [1, [4, "-90"]]})
    sol_builder.add("k_l_move", "motion_movesteps", next_id=None, parent_id="k_l_dir", inputs={"STEPS": [1, [4, "15"]]})

    # Up arrow
    sol_builder.add("k_up", "event_whenkeypressed", next_id="k_u_change", top_level=True, x=60, y=360, fields={"KEY_OPTION": ["up arrow", None]})
    sol_builder.add("k_u_change", "motion_changeyby", next_id=None, parent_id="k_up", inputs={"DY": [1, [4, "15"]]})

    # Down arrow
    sol_builder.add("k_down", "event_whenkeypressed", next_id="k_d_change", top_level=True, x=260, y=360, fields={"KEY_OPTION": ["down arrow", None]})
    sol_builder.add("k_d_change", "motion_changeyby", next_id=None, parent_id="k_down", inputs={"DY": [1, [4, "-15"]]})

    targets_solution = [
        {
            "isStage": True,
            "name": "Stage",
            "variables": {},
            "lists": {},
            "broadcasts": {},
            "blocks": {},
            "currentCostume": 0,
            "costumes": [STAGE_BACKDROP],
            "sounds": [POP_SOUND],
            "volume": 100,
            "layerOrder": 0
        },
        {
            "isStage": False,
            "name": "ScratchCat",
            "variables": {},
            "lists": {},
            "broadcasts": {},
            "blocks": sol_builder.build(),
            "currentCostume": 0,
            "costumes": [CAT_COSTUME1, CAT_COSTUME2],
            "sounds": [MEOW_SOUND],
            "volume": 100,
            "visible": True,
            "x": 0,
            "y": 0,
            "size": 100,
            "direction": 90,
            "draggable": False,
            "rotationStyle": "left-right"
        }
    ]

    sol_path = os.path.join(dest_dir, "yechim_spraytlar_va_harakat.sb3")
    build_sb3(sol_path, targets_solution)

    # Starter project
    start_builder = ScratchBlockBuilder()
    start_builder.add("s_flag", "event_whenflagclicked", next_id=None, top_level=True, x=60, y=60)
    start_builder.add("s_goto", "motion_gotoxy", next_id=None, top_level=True, x=240, y=60, inputs={"X": [1, [4, "0"]], "Y": [1, [4, "0"]]})

    targets_starter = [
        {
            "isStage": True,
            "name": "Stage",
            "variables": {},
            "lists": {},
            "broadcasts": {},
            "blocks": {},
            "currentCostume": 0,
            "costumes": [STAGE_BACKDROP],
            "sounds": [POP_SOUND],
            "volume": 100,
            "layerOrder": 0
        },
        {
            "isStage": False,
            "name": "ScratchCat",
            "variables": {},
            "lists": {},
            "broadcasts": {},
            "blocks": start_builder.build(),
            "currentCostume": 0,
            "costumes": [CAT_COSTUME1, CAT_COSTUME2],
            "sounds": [MEOW_SOUND],
            "volume": 100,
            "visible": True,
            "x": 0,
            "y": 0,
            "size": 100,
            "direction": 90,
            "draggable": False,
            "rotationStyle": "all around"
        }
    ]

    start_path = os.path.join(dest_dir, "starter_spraytlar_va_harakat.sb3")
    build_sb3(start_path, targets_starter)
    return start_path, sol_path


if __name__ == "__main__":
    p26_dir = os.path.join(REPO_ROOT, "classes", "5-6-sinf", "10-hafta", "26-dars-scratch-jonli-animatsiyalar-va-kostyumlar", "projects")
    print(f"Building Scratch projects for Lesson 26 in {p26_dir}...")
    generate_lesson_26_projects(p26_dir)

    p24_dir = os.path.join(REPO_ROOT, "classes", "5-6-sinf", "10-hafta", "24-dars-scratch-spraytlar-va-sahnalar", "projects")
    print(f"Building Scratch projects for Lesson 24 in {p24_dir}...")
    generate_lesson_24_projects(p24_dir)

    print("🎉 All Scratch .sb3 projects generated successfully!")
