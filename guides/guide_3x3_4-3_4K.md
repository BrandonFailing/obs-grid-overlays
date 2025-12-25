# 3x3 Grid - 4:3 Cells - 4K

## Specifications
- **Canvas Resolution:** 3840×2160
- **Grid Layout:** 3 columns × 3 rows (9 cells)
- **Cell Aspect Ratio:** 4:3
- **Bar Thickness:** 20px

## Cell Positions

| Cell | Position (X, Y) | Size (W × H) |
|------|-----------------|--------------|
| Cell 1 | 162, 0 | 942 × 707 |
| Cell 2 | 1449, 0 | 942 × 707 |
| Cell 3 | 2736, 0 | 942 × 707 |
| Cell 4 | 162, 727 | 942 × 707 |
| Cell 5 | 1449, 727 | 942 × 707 |
| Cell 6 | 2736, 727 | 942 × 707 |
| Cell 7 | 162, 1453 | 942 × 707 |
| Cell 8 | 1449, 1453 | 942 × 707 |
| Cell 9 | 2736, 1453 | 942 × 707 |

## OBS Setup Instructions

1. **Add Background Layer (Bottom)**
   - Add `background_green_4K.png` as Image source
   - This helps you see positioning during setup

2. **Add Your 9 Video Sources (Middle)**
   - For each source, right-click → Transform → Edit Transform
   - Use the positions from the table above
   - Set Bounding Box Type: "Scale to inner bounds"
   - Set Alignment: Center

3. **Add Grid Overlay (Top)**
   - Add `grid_3x3_4-3_4K.png` as Image source
   - Place at the very top of source list

4. **(Optional) Remove Green Background**
   - Once positioned, you can delete the green layer
   - Or replace with a different color/image
