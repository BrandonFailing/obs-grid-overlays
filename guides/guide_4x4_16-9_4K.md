# 4x4 Grid - 16:9 Cells - 4K

## Specifications
- **Canvas Resolution:** 3840×2160
- **Grid Layout:** 4 columns × 4 rows (16 cells)
- **Cell Aspect Ratio:** 16:9
- **Bar Thickness:** 20px

## Cell Positions

| Cell | Position (X, Y) | Size (W × H) |
|------|-----------------|--------------|
| Cell 1 | 6, 0 | 933 × 525 |
| Cell 2 | 971, 0 | 933 × 525 |
| Cell 3 | 1936, 0 | 933 × 525 |
| Cell 4 | 2901, 0 | 933 × 525 |
| Cell 5 | 6, 545 | 933 × 525 |
| Cell 6 | 971, 545 | 933 × 525 |
| Cell 7 | 1936, 545 | 933 × 525 |
| Cell 8 | 2901, 545 | 933 × 525 |
| Cell 9 | 6, 1090 | 933 × 525 |
| Cell 10 | 971, 1090 | 933 × 525 |
| Cell 11 | 1936, 1090 | 933 × 525 |
| Cell 12 | 2901, 1090 | 933 × 525 |
| Cell 13 | 6, 1635 | 933 × 525 |
| Cell 14 | 971, 1635 | 933 × 525 |
| Cell 15 | 1936, 1635 | 933 × 525 |
| Cell 16 | 2901, 1635 | 933 × 525 |

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
   - Add `grid_4x4_16-9_4K.png` as Image source
   - Place at the very top of source list

4. **(Optional) Remove Green Background**
   - Once positioned, you can delete the green layer
   - Or replace with a different color/image
