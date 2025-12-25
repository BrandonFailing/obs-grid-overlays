# 2x2 Grid - 1:1 Cells - 4K

## Specifications
- **Canvas Resolution:** 3840×2160
- **Grid Layout:** 2 columns × 2 rows (4 cells)
- **Cell Aspect Ratio:** 1:1
- **Bar Thickness:** 20px

## Cell Positions

| Cell | Position (X, Y) | Size (W × H) |
|------|-----------------|--------------|
| Cell 1 | 420, 0 | 1070 × 1070 |
| Cell 2 | 2350, 0 | 1070 × 1070 |
| Cell 3 | 420, 1090 | 1070 × 1070 |
| Cell 4 | 2350, 1090 | 1070 × 1070 |

## OBS Setup Instructions

1. **Add Background Layer (Bottom)**
   - Add `background_green_4K.png` as Image source
   - This helps you see positioning during setup

2. **Add Your 4 Video Sources (Middle)**
   - For each source, right-click → Transform → Edit Transform
   - Use the positions from the table above
   - Set Bounding Box Type: "Scale to inner bounds"
   - Set Alignment: Center

3. **Add Grid Overlay (Top)**
   - Add `grid_2x2_1-1_4K.png` as Image source
   - Place at the very top of source list

4. **(Optional) Remove Green Background**
   - Once positioned, you can delete the green layer
   - Or replace with a different color/image
