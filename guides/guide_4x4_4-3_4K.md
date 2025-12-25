# 4x4 Grid - 4:3 Cells - 4K

## Specifications
- **Canvas Resolution:** 3840×2160
- **Grid Layout:** 4 columns × 4 rows (16 cells)
- **Cell Aspect Ratio:** 4:3
- **Bar Thickness:** 20px

## Cell Positions

| Cell | Position (X, Y) | Size (W × H) |
|------|-----------------|--------------|
| Cell 1 | 122, 0 | 700 × 525 |
| Cell 2 | 1088, 0 | 700 × 525 |
| Cell 3 | 2052, 0 | 700 × 525 |
| Cell 4 | 3018, 0 | 700 × 525 |
| Cell 5 | 122, 545 | 700 × 525 |
| Cell 6 | 1088, 545 | 700 × 525 |
| Cell 7 | 2052, 545 | 700 × 525 |
| Cell 8 | 3018, 545 | 700 × 525 |
| Cell 9 | 122, 1090 | 700 × 525 |
| Cell 10 | 1088, 1090 | 700 × 525 |
| Cell 11 | 2052, 1090 | 700 × 525 |
| Cell 12 | 3018, 1090 | 700 × 525 |
| Cell 13 | 122, 1635 | 700 × 525 |
| Cell 14 | 1088, 1635 | 700 × 525 |
| Cell 15 | 2052, 1635 | 700 × 525 |
| Cell 16 | 3018, 1635 | 700 × 525 |

## OBS Setup Instructions

1. **Add Background Layer (Bottom)**
   - Add `background_green_4K.png` as Image source
   - This helps you see positioning during setup

2. **Add Your 16 Video Sources (Middle)**
   - For each source, right-click → Transform → Edit Transform
   - Use the positions from the table above
   - Set Bounding Box Type: "Scale to inner bounds"
   - Set Alignment: Center

3. **Add Grid Overlay (Top)**
   - Add `grid_4x4_4-3_4K.png` as Image source
   - Place at the very top of source list

4. **(Optional) Remove Green Background**
   - Once positioned, you can delete the green layer
   - Or replace with a different color/image
