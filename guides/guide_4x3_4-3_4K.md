# 4x3 Grid - 4:3 Cells - 4K

## Specifications
- **Canvas Resolution:** 3840×2160
- **Grid Layout:** 4 columns × 3 rows (12 cells)
- **Cell Aspect Ratio:** 4:3
- **Bar Thickness:** 20px

## Cell Positions

| Cell | Position (X, Y) | Size (W × H) |
|------|-----------------|--------------|
| Cell 1 | 1, 0 | 942 × 707 |
| Cell 2 | 966, 0 | 942 × 707 |
| Cell 3 | 1931, 0 | 942 × 707 |
| Cell 4 | 2896, 0 | 942 × 707 |
| Cell 5 | 1, 727 | 942 × 707 |
| Cell 6 | 966, 727 | 942 × 707 |
| Cell 7 | 1931, 727 | 942 × 707 |
| Cell 8 | 2896, 727 | 942 × 707 |
| Cell 9 | 1, 1453 | 942 × 707 |
| Cell 10 | 966, 1453 | 942 × 707 |
| Cell 11 | 1931, 1453 | 942 × 707 |
| Cell 12 | 2896, 1453 | 942 × 707 |

## OBS Setup Instructions

1. **Add Background Layer (Bottom)**
   - Add `background_green_4K.png` as Image source
   - This helps you see positioning during setup

2. **Add Your 12 Video Sources (Middle)**
   - For each source, right-click → Transform → Edit Transform
   - Use the positions from the table above
   - Set Bounding Box Type: "Scale to inner bounds"
   - Set Alignment: Center

3. **Add Grid Overlay (Top)**
   - Add `grid_4x3_4-3_4K.png` as Image source
   - Place at the very top of source list

4. **(Optional) Remove Green Background**
   - Once positioned, you can delete the green layer
   - Or replace with a different color/image
