# 4x4 Grid - 1:1 Cells - 4K

## Specifications
- **Canvas Resolution:** 3840×2160
- **Grid Layout:** 4 columns × 4 rows (16 cells)
- **Cell Aspect Ratio:** 1:1
- **Bar Thickness:** 20px

## Cell Positions

| Cell | Position (X, Y) | Size (W × H) |
|------|-----------------|--------------|
| Cell 1 | 210, 0 | 525 × 525 |
| Cell 2 | 1175, 0 | 525 × 525 |
| Cell 3 | 2140, 0 | 525 × 525 |
| Cell 4 | 3105, 0 | 525 × 525 |
| Cell 5 | 210, 545 | 525 × 525 |
| Cell 6 | 1175, 545 | 525 × 525 |
| Cell 7 | 2140, 545 | 525 × 525 |
| Cell 8 | 3105, 545 | 525 × 525 |
| Cell 9 | 210, 1090 | 525 × 525 |
| Cell 10 | 1175, 1090 | 525 × 525 |
| Cell 11 | 2140, 1090 | 525 × 525 |
| Cell 12 | 3105, 1090 | 525 × 525 |
| Cell 13 | 210, 1635 | 525 × 525 |
| Cell 14 | 1175, 1635 | 525 × 525 |
| Cell 15 | 2140, 1635 | 525 × 525 |
| Cell 16 | 3105, 1635 | 525 × 525 |

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
   - Add `grid_4x4_1-1_4K.png` as Image source
   - Place at the very top of source list

4. **(Optional) Remove Green Background**
   - Once positioned, you can delete the green layer
   - Or replace with a different color/image
