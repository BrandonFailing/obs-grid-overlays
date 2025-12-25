# OBS Grid Overlays

**Simple, drag-and-drop grid overlays for OBS Studio** - No scripts, no plugins, just clean PNG overlays.

Perfect for multi-camera setups, podcasts, security camera views, gaming streams, and any scenario where you need to display multiple video sources in a clean grid layout.

## 🎯 What's Included

- **54 Grid Overlays** across 6 different layouts, 3 aspect ratios, and 3 resolutions
- **9 Setup Backgrounds** (green, blue, magenta) to make positioning easier
- **54 Position Guides** with exact coordinates for every grid configuration
- **Metadata JSON** for programmatic access to all configurations

## 📐 Grid Layouts

| Layout | Cells | Best For |
|--------|-------|----------|
| 2×2 | 4 | Small panels, interviews, quad-cam |
| 3×2 | 6 | Standard multi-cam, security feeds |
| 4×2 | 8 | Wide panels, podcast setups |
| 3×3 | 9 | Classic grid, multiple participants |
| 4×3 | 12 | Large multi-cam setups |
| 4×4 | 16 | Maximum grid, control rooms |

## 🎨 Aspect Ratios

- **4:3** - Classic TV format, perfect for traditional cameras
- **16:9** - Modern widescreen, matches most webcams and capture cards
- **1:1** - Square cells, great for social media vertical content

## 📺 Resolutions

- **1080p** (1920×1080) - Standard HD streaming
- **1440p** (2560×1440) - High-quality streaming
- **4K** (3840×2160) - Professional production

## 🚀 Quick Start

### 1. Download Your Grid

Choose the overlay that matches your setup:
- `grid_{LAYOUT}_{ASPECT}_{RESOLUTION}.png`

**Example:** `grid_3x2_4-3_1080p.png` = 3×2 grid with 4:3 cells at 1080p

### 2. Download Setup Background (Optional but Recommended)

- `background_green_{RESOLUTION}.png` - Makes black gridlines visible during setup

### 3. Setup in OBS

**Layer order (bottom to top):**
```
┌──────────────────────────┐
│  Grid Overlay            │  ← TOP
├──────────────────────────┤
│  Camera 6                │
│  Camera 5                │
│  ...                     │  ← MIDDLE
│  Camera 2                │
│  Camera 1                │
├──────────────────────────┤
│  Setup Background        │  ← BOTTOM
└──────────────────────────┘
```

### 4. Position Your Sources

See the corresponding guide in `/guides/` for exact positions:
- `guide_{LAYOUT}_{ASPECT}_{RESOLUTION}.md`

Each guide includes a table with X, Y coordinates and bounding box sizes for every cell.

### 5. (Optional) Remove Setup Background

Once positioned, you can delete or hide the green background layer.

## 📋 Detailed Setup Example

**Scenario:** 6 webcams in 1080p with 4:3 aspect ratio

1. In OBS, create a new scene called "Multi-Cam Grid"

2. Add the green background:
   - Add Image → `background_green_1080p.png`
   - This goes at the bottom of your source list

3. Add your 6 webcam sources
   - They'll show clearly against the green background

4. Position each camera using the guide:
   - Open `guide_3x2_4-3_1080p.md`
   - For each camera, right-click → Transform → Edit Transform
   - Enter the position and bounding box from the guide
   - Set Alignment to "Center"

5. Add the grid overlay:
   - Add Image → `grid_3x2_4-3_1080p.png`
   - This goes at the TOP of your source list

6. Done! Your grid is perfectly aligned.

## 🎭 Use Cases

### Live Streaming
- **Gaming:** Show multiple players, face cams, and gameplay
- **Podcasts:** Display all participants in a clean grid
- **Interviews:** Multi-angle shots with professional separation

### Video Production
- **Security Monitoring:** Display multiple camera feeds
- **Events:** Show different angles simultaneously
- **Sports:** Multi-cam sports coverage

### Content Creation
- **Reactions:** Show reactor + content in organized layout
- **Tutorials:** Display different steps/angles
- **Comparisons:** Side-by-side comparisons of products/processes

## 🎨 Customization Tips

### Different Bar Colors
Want white bars instead of black? You can:
1. Use the generator script to create custom colors
2. Edit the PNG in any image editor
3. Request a specific color in the issues

### Different Bar Thickness
The default is 20px bars. To change:
1. Use the generator script with custom `BAR_THICKNESS`
2. Regenerate with your preferred thickness

### Mixed Aspect Ratios
Need different aspect ratios in the same grid? This is advanced, but you can:
1. Layer multiple overlays
2. Manually create custom overlays in an image editor
3. Request it as a feature

## 📁 File Structure

```
obs-grid-overlays/
├── overlays/           # All grid overlay PNGs
├── backgrounds/        # Setup background PNGs
├── guides/            # Position guides (Markdown)
├── metadata.json      # Machine-readable configuration data
├── generator.py       # Python script to generate custom grids
└── README.md          # This file
```

## 🔧 Generator Script

Want a custom configuration? Use the included Python script:

```bash
python generator.py
```

Customize by editing these variables:
- `RESOLUTIONS` - Add your custom resolution
- `GRIDS` - Add custom grid layouts
- `ASPECT_RATIOS` - Add custom aspect ratios
- `BAR_THICKNESS` - Change bar width
- `BACKGROUND_COLORS` - Add custom background colors

## 🤝 Contributing

Contributions welcome! Here are some ideas:
- Additional grid layouts
- Different bar styles (rounded, gradients, etc.)
- Custom themed overlays
- Video tutorials
- Translations
- OBS scene collection templates

## 📝 License

MIT License - Free to use for personal and commercial projects.

## 🙏 Credits

Created to solve a common OBS problem: clean multi-camera layouts without complex scripts.

## 💡 Why This Works Better Than Scripts

**Simplicity:**
- No Lua/Python knowledge required
- No debugging script errors
- No plugin dependencies
- Works across all OBS versions

**Flexibility:**
- Full manual control over each source
- Easy to adjust on the fly
- Mix different source types freely
- No performance overhead

**Reliability:**
- PNGs never break
- No updates needed
- Works offline
- Compatible with all OBS features

## 🐛 Troubleshooting

**Sources don't fit perfectly:**
- Use "Scale to inner bounds" in Transform settings
- Check that you're using the correct aspect ratio overlay
- Verify position coordinates from the guide

**Can't see the gridlines:**
- Add the green/blue background layer underneath
- Make sure the overlay is on TOP of source list
- Check that overlay matches your canvas resolution

**Need different settings:**
- Use the generator script to create custom overlays
- Or open an issue requesting specific configurations

## 📬 Support

- **Issues:** Report bugs or request features
- **Discussions:** Share your setups and ask questions
- **Pull Requests:** Contribute improvements

---

**Made with ❤️ for the OBS community**
