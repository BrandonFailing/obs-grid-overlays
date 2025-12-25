# 3x2 Grid - 4:3 Cells - 4K

## Specifications
- **Canvas Resolution:** 3840×2160
- **Grid Layout:** 3 columns × 2 rows (6 cells)
- **Cell Aspect Ratio:** 4:3
- **Bar Thickness:** 20px

## Cell Positions

| Cell | Position (X, Y) | Size (W × H) |
|------|-----------------|--------------|
| Cell 1 | 0, 60 | 1267 × 950 |
| Cell 2 | 1287, 60 | 1267 × 950 |
| Cell 3 | 2573, 60 | 1267 × 950 |
| Cell 4 | 0, 1150 | 1267 × 950 |
| Cell 5 | 1287, 1150 | 1267 × 950 |
| Cell 6 | 2573, 1150 | 1267 × 950 |

## OBS Setup Instructions

1. **Add Background Layer (Bottom)**
   - Add `background_green_4K.png` as Image source
   - This helps you see positioning during setup

2. **Add Your 6 Video Sources (Middle)**
   - For each source, right-click → Transform → Edit Transform
   - Use the positions from the table above
   - Set Bounding Box Type: "Scale to inner bounds"
   - Set Alignment: Center

3. **Add Grid Overlay (Top)**
   - Add `grid_3x2_4-3_4K.png` as Image source
   - Place at the very top of source list

4. **(Optional) Remove Green Background**
   - Once positioned, you can delete the green layer
   - Or replace with a different color/image
