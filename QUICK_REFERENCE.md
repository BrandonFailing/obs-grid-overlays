# Quick Reference Guide

## File Naming Convention

### Grid Overlays
Format: `grid_{LAYOUT}_{ASPECT}_{RESOLUTION}.png`

**Examples:**
- `grid_3x2_4-3_1080p.png` - 3×2 grid, 4:3 cells, 1080p
- `grid_4x4_16-9_4K.png` - 4×4 grid, 16:9 cells, 4K
- `grid_2x2_1-1_1440p.png` - 2×2 grid, square cells, 1440p

### Setup Backgrounds
Format: `background_{COLOR}_{RESOLUTION}.png`

**Examples:**
- `background_green_1080p.png`
- `background_blue_1440p.png`
- `background_magenta_4K.png`

### Position Guides
Format: `guide_{LAYOUT}_{ASPECT}_{RESOLUTION}.md`

**Examples:**
- `guide_3x2_4-3_1080p.md`
- `guide_4x4_16-9_4K.md`

## Common Configurations

### Podcast (4 people)
**Use:** `grid_2x2_16-9_1080p.png`
- 4 cells in a 2×2 layout
- 16:9 for modern webcams
- 1080p for standard streaming

### Security Cameras (6 feeds)
**Use:** `grid_3x2_4-3_1080p.png`
- 6 cells in a 3×2 layout
- 4:3 for traditional security cameras
- 1080p for standard monitors

### Gaming Stream (Multiple players)
**Use:** `grid_4x2_16-9_1080p.png`
- 8 cells for multiple player cameras
- 16:9 for gaming webcams
- 1080p for Twitch/YouTube streaming

### Zoom-style Grid (9 people)
**Use:** `grid_3x3_16-9_1080p.png`
- Classic 3×3 grid
- 16:9 for webcams
- 1080p for video calls

### Instagram/TikTok Multi-cam
**Use:** `grid_3x3_1-1_1080p.png`
- Square cells for vertical video
- 1:1 aspect ratio
- 1080p for social media

## Layer Setup Checklist

- [ ] Add setup background (green/blue/magenta) to BOTTOM
- [ ] Add all camera/video sources in MIDDLE
- [ ] Position each source using guide coordinates
- [ ] Set "Scale to inner bounds" for each source
- [ ] Set "Center" alignment for each source
- [ ] Add grid overlay to TOP
- [ ] Test visibility and positioning
- [ ] (Optional) Remove or hide setup background

## OBS Transform Settings

For each camera source:

```
Right-click source → Transform → Edit Transform

Position:           [X, Y from guide]
Bounding Box Type:  Scale to inner bounds
Size:               [Width × Height from guide]
Alignment:          Center
```

## Resolution Cheat Sheet

| Resolution | Canvas Size | Common Name | Use Case |
|------------|-------------|-------------|----------|
| 1080p | 1920×1080 | Full HD | Standard streaming |
| 1440p | 2560×1440 | 2K / QHD | High-quality streams |
| 4K | 3840×2160 | Ultra HD | Professional production |

## Aspect Ratio Guide

| Ratio | Decimal | Description | Common Sources |
|-------|---------|-------------|----------------|
| 4:3 | 1.333 | Classic TV | Security cams, old webcams |
| 16:9 | 1.778 | Widescreen | Modern webcams, capture cards |
| 1:1 | 1.000 | Square | Social media, custom crops |

## Tips for Perfect Alignment

1. **Use the setup background** - Green/blue makes positioning visible
2. **Copy-paste sources** - Duplicate a positioned source, then change the input
3. **Use the guide tables** - Exact coordinates prevent guesswork
4. **Lock sources** - Right-click → Lock after positioning to prevent accidents
5. **Save as Scene Collection** - Reuse your layout across projects

## Performance Notes

Grid overlays have **zero performance impact** because:
- They're static PNG images
- No script processing
- No real-time calculations
- Just normal OBS layers

You can use the most complex grid (4×4, 16 cells) with no FPS loss.

## Common Issues

**Problem:** Sources overlap the gridlines
**Solution:** Make sure grid overlay is at the TOP of source list

**Problem:** Can't see gridlines during setup
**Solution:** Add green/blue background to bottom layer

**Problem:** Sources are stretched/squashed
**Solution:** Use "Scale to inner bounds" instead of "Stretch to bounds"

**Problem:** Sources don't fill their cells
**Solution:** Increase source size or use zoom/crop

**Problem:** Wrong grid size showing
**Solution:** Verify you're using correct resolution overlay for your canvas

## Workflow: From Zero to Grid in 5 Minutes

1. **Minute 1:** Download overlay + background for your resolution
2. **Minute 2:** Create OBS scene, add background and sources
3. **Minute 3:** Open position guide, start positioning sources
4. **Minute 4:** Add grid overlay on top, verify alignment
5. **Minute 5:** Fine-tune positions, remove background if desired

Done! Your professional multi-cam grid is ready.
