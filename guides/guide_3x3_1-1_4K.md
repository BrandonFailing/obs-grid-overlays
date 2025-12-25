# 3x3 Grid - 1:1 Cells - 4K

## Specifications
- **Canvas Resolution:** 3840×2160
- **Grid Layout:** 3 columns × 3 rows (9 cells)
- **Cell Aspect Ratio:** 1:1
- **Bar Thickness:** 20px

## Cell Positions

| Cell | Position (X, Y) | Size (W × H) |
|------|-----------------|--------------|
| Cell 1 | 280, 0 | 707 × 707 |
| Cell 2 | 1567, 0 | 707 × 707 |
| Cell 3 | 2853, 0 | 707 × 707 |
| Cell 4 | 280, 727 | 707 × 707 |
| Cell 5 | 1567, 727 | 707 × 707 |
| Cell 6 | 2853, 727 | 707 × 707 |
| Cell 7 | 280, 1453 | 707 × 707 |
| Cell 8 | 1567, 1453 | 707 × 707 |
| Cell 9 | 2853, 1453 | 707 × 707 |

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
   - Add `grid_3x3_1-1_4K.png` as Image source
   - Place at the very top of source list

4. **(Optional) Remove Green Background**
   - Once positioned, you can delete the green layer
   - Or replace with a different color/image
