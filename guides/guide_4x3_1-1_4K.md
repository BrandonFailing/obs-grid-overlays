# 4x3 Grid - 1:1 Cells - 4K

## Specifications
- **Canvas Resolution:** 3840×2160
- **Grid Layout:** 4 columns × 3 rows (12 cells)
- **Cell Aspect Ratio:** 1:1
- **Bar Thickness:** 20px

## Cell Positions

| Cell | Position (X, Y) | Size (W × H) |
|------|-----------------|--------------|
| Cell 1 | 119, 0 | 707 × 707 |
| Cell 2 | 1084, 0 | 707 × 707 |
| Cell 3 | 2049, 0 | 707 × 707 |
| Cell 4 | 3014, 0 | 707 × 707 |
| Cell 5 | 119, 727 | 707 × 707 |
| Cell 6 | 1084, 727 | 707 × 707 |
| Cell 7 | 2049, 727 | 707 × 707 |
| Cell 8 | 3014, 727 | 707 × 707 |
| Cell 9 | 119, 1453 | 707 × 707 |
| Cell 10 | 1084, 1453 | 707 × 707 |
| Cell 11 | 2049, 1453 | 707 × 707 |
| Cell 12 | 3014, 1453 | 707 × 707 |

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
   - Add `grid_4x3_1-1_4K.png` as Image source
   - Place at the very top of source list

4. **(Optional) Remove Green Background**
   - Once positioned, you can delete the green layer
   - Or replace with a different color/image
