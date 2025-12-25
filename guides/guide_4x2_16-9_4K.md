# 4x2 Grid - 16:9 Cells - 4K

## Specifications
- **Canvas Resolution:** 3840×2160
- **Grid Layout:** 4 columns × 2 rows (8 cells)
- **Cell Aspect Ratio:** 16:9
- **Bar Thickness:** 20px

## Cell Positions

| Cell | Position (X, Y) | Size (W × H) |
|------|-----------------|--------------|
| Cell 1 | 0, 269 | 945 × 532 |
| Cell 2 | 965, 269 | 945 × 532 |
| Cell 3 | 1930, 269 | 945 × 532 |
| Cell 4 | 2895, 269 | 945 × 532 |
| Cell 5 | 0, 1359 | 945 × 532 |
| Cell 6 | 965, 1359 | 945 × 532 |
| Cell 7 | 1930, 1359 | 945 × 532 |
| Cell 8 | 2895, 1359 | 945 × 532 |

## OBS Setup Instructions

1. **Add Background Layer (Bottom)**
   - Add `background_green_4K.png` as Image source
   - This helps you see positioning during setup

2. **Add Your 8 Video Sources (Middle)**
   - For each source, right-click → Transform → Edit Transform
   - Use the positions from the table above
   - Set Bounding Box Type: "Scale to inner bounds"
   - Set Alignment: Center

3. **Add Grid Overlay (Top)**
   - Add `grid_4x2_16-9_4K.png` as Image source
   - Place at the very top of source list

4. **(Optional) Remove Green Background**
   - Once positioned, you can delete the green layer
   - Or replace with a different color/image
