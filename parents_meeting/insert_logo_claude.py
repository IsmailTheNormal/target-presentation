#!/usr/bin/env python3
"""
Insert the official Target International School logo into
presentations/claude/Target_Parents_Meeting_2026-27_Main_Presentation.pptx

- Cleans placeholder text shapes ('T', 'TARGET', 'International School') from slide layouts.
- Adds official Target Dark-Mode logo (crisp white text + vibrant red 'A') to Slide 1 (Cover, dark navy background).
- Adds official Target Color logo (navy text + vibrant red 'A') to Slides 2-18 (Content, light background) at top-right header.
- Adds official Target Dark-Mode logo to Slide 19 (Dark closing) at top-right header.
"""

import os
import pptx
from pptx.util import Inches
from pptx.enum.shapes import MSO_SHAPE_TYPE

def insert_logos():
    deck_path = 'presentations/claude/Target_Parents_Meeting_2026-27_Main_Presentation.pptx'
    logo_darkmode = 'presentations/target-logo-darkmode.png'
    logo_color = 'presentations/target-logo-transparent.png'

    if not os.path.exists(deck_path):
        raise FileNotFoundError(f"File not found: {deck_path}")

    prs = pptx.Presentation(deck_path)
    print(f"Loaded presentation: {deck_path} with {len(prs.slides)} slides")

    # 1. Clean placeholder shapes from layouts
    removed_count = 0
    for layout in prs.slide_layouts:
        to_remove = []
        for shp in layout.shapes:
            txt = shp.text_frame.text.strip() if shp.has_text_frame else ''
            if txt in ['T', 'TARGET', 'International School'] or shp.name in ['Shape 0', 'Text 1', 'Text 2', 'Text 3']:
                to_remove.append(shp._element)
        for elm in to_remove:
            elm.getparent().remove(elm)
            removed_count += 1
    print(f"Removed {removed_count} placeholder shapes from slide layouts.")

    # 2. Add dark-mode logo to Slide 1 (Cover, dark navy background) - top-left
    s1 = prs.slides[0]
    to_remove_s1 = [shp._element for shp in s1.shapes if shp.shape_type == MSO_SHAPE_TYPE.PICTURE and shp.left.inches < 1.0]
    for elm in to_remove_s1:
        elm.getparent().remove(elm)

    s1.shapes.add_picture(
        logo_darkmode,
        Inches(0.60),
        Inches(0.52),
        width=Inches(2.40),
        height=Inches(0.575)
    )
    print("Added official dark-mode logo (white text + red 'A') to Slide 1 (Cover, top-left).")

    # 3. Add color logo to Slides 2-18 (Content, light background) - top-right
    for idx in range(1, len(prs.slides) - 1):
        s = prs.slides[idx]
        to_remove_s = [shp._element for shp in s.shapes if shp.shape_type == MSO_SHAPE_TYPE.PICTURE and shp.left.inches > 7.0]
        for elm in to_remove_s:
            elm.getparent().remove(elm)
        s.shapes.add_picture(
            logo_color,
            Inches(7.95),
            Inches(0.35),
            width=Inches(1.65),
            height=Inches(0.395)
        )
    print(f"Added official color logo to Slides 2–{len(prs.slides)-1} (Content, top-right).")

    # 4. Add dark-mode logo to Slide 19 (Dark closing slide) - top-right
    s_last = prs.slides[-1]
    to_remove_last = [shp._element for shp in s_last.shapes if shp.shape_type == MSO_SHAPE_TYPE.PICTURE and shp.left.inches > 7.0]
    for elm in to_remove_last:
        elm.getparent().remove(elm)
    s_last.shapes.add_picture(
        logo_darkmode,
        Inches(7.95),
        Inches(0.35),
        width=Inches(1.65),
        height=Inches(0.395)
    )
    print(f"Added official dark-mode logo to Slide {len(prs.slides)} (Dark closing, top-right).")

    prs.save(deck_path)
    print(f"Successfully saved updated presentation to {deck_path}!")

if __name__ == '__main__':
    insert_logos()
