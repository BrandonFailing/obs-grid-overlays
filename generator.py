from PIL import Image, ImageDraw
import os
import json

# Create output directory structure
output_dir = "/home/claude/obs-grid-overlays"
os.makedirs(output_dir, exist_ok=True)
os.makedirs(f"{output_dir}/overlays", exist_ok=True)
os.makedirs(f"{output_dir}/backgrounds", exist_ok=True)
os.makedirs(f"{output_dir}/guides", exist_ok=True)

# Configuration
RESOLUTIONS = [
    (1920, 1080, "1080p"),
    (2560, 1440, "1440p"),
    (3840, 2160, "4K")
]

GRIDS = [
    (2, 2, "2x2"),
    (3, 2, "3x2"),
    (4, 2, "4x2"),
    (3, 3, "3x3"),
    (4, 3, "4x3"),
    (4, 4, "4x4")
]

ASPECT_RATIOS = {
    "4:3": 4/3,
    "16:9": 16/9,
    "1:1": 1/1
}

BAR_THICKNESS = 20

BACKGROUND_COLORS = {
    "green": (0, 255, 0, 255),
    "blue": (0, 100, 255, 255),
    "magenta": (255, 0, 255, 255)
}

def calculate_cell_dimensions(canvas_width, canvas_height, cols, rows, aspect_ratio, bar_thickness):
    """Calculate optimal cell dimensions for given aspect ratio"""
    total_bar_width = (cols - 1) * bar_thickness
    total_bar_height = (rows - 1) * bar_thickness
    
    available_width = canvas_width - total_bar_width
    available_height = canvas_height - total_bar_height
    
    cell_width = available_width / cols
    cell_height = available_height / rows
    
    # Calculate content size based on aspect ratio
    max_width_from_height = cell_height * aspect_ratio
    max_height_from_width = cell_width / aspect_ratio
    
    if max_width_from_height <= cell_width:
        content_width = max_width_from_height
        content_height = cell_height
    else:
        content_width = cell_width
        content_height = max_height_from_width
    
    return cell_width, cell_height, content_width, content_height

def create_grid_overlay(canvas_width, canvas_height, cols, rows, bar_thickness):
    """Create a grid overlay with transparent cells and black bars"""
    img = Image.new('RGBA', (canvas_width, canvas_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Calculate cell dimensions
    total_bar_width = (cols - 1) * bar_thickness
    total_bar_height = (rows - 1) * bar_thickness
    available_width = canvas_width - total_bar_width
    available_height = canvas_height - total_bar_height
    cell_width = available_width / cols
    cell_height = available_height / rows
    
    # Draw vertical bars
    for i in range(1, cols):
        x = i * cell_width + (i - 1) * bar_thickness
        draw.rectangle(
            [(x, 0), (x + bar_thickness, canvas_height)],
            fill=(0, 0, 0, 255)
        )
    
    # Draw horizontal bars
    for i in range(1, rows):
        y = i * cell_height + (i - 1) * bar_thickness
        draw.rectangle(
            [(0, y), (canvas_width, y + bar_thickness)],
            fill=(0, 0, 0, 255)
        )
    
    return img

def create_background(canvas_width, canvas_height, color):
    """Create a solid color background"""
    img = Image.new('RGBA', (canvas_width, canvas_height), color)
    return img

def generate_position_guide(canvas_width, canvas_height, cols, rows, aspect_ratio_name, aspect_ratio_value, res_name, grid_name):
    """Generate markdown guide with cell positions"""
    bar_thickness = BAR_THICKNESS
    
    total_bar_width = (cols - 1) * bar_thickness
    total_bar_height = (rows - 1) * bar_thickness
    available_width = canvas_width - total_bar_width
    available_height = canvas_height - total_bar_height
    cell_width = available_width / cols
    cell_height = available_height / rows
    
    # Calculate content dimensions
    max_width_from_height = cell_height * aspect_ratio_value
    max_height_from_width = cell_width / aspect_ratio_value
    
    if max_width_from_height <= cell_width:
        content_width = max_width_from_height
        content_height = cell_height
    else:
        content_width = cell_width
        content_height = max_height_from_width
    
    guide = f"""# {grid_name} Grid - {aspect_ratio_name} Cells - {res_name}

## Specifications
- **Canvas Resolution:** {canvas_width}×{canvas_height}
- **Grid Layout:** {cols} columns × {rows} rows ({cols * rows} cells)
- **Cell Aspect Ratio:** {aspect_ratio_name}
- **Bar Thickness:** {bar_thickness}px

## Cell Positions

| Cell | Position (X, Y) | Size (W × H) |
|------|-----------------|--------------|
"""
    
    positions = []
    for row in range(rows):
        for col in range(cols):
            x = col * (cell_width + bar_thickness)
            y = row * (cell_height + bar_thickness)
            
            # Center content within cell
            content_x = x + (cell_width - content_width) / 2
            content_y = y + (cell_height - content_height) / 2
            
            cell_num = row * cols + col + 1
            guide += f"| Cell {cell_num} | {content_x:.0f}, {content_y:.0f} | {content_width:.0f} × {content_height:.0f} |\n"
            
            positions.append({
                "cell": cell_num,
                "x": round(content_x),
                "y": round(content_y),
                "width": round(content_width),
                "height": round(content_height)
            })
    
    guide += f"""
## OBS Setup Instructions

1. **Add Background Layer (Bottom)**
   - Add `background_green_{res_name}.png` as Image source
   - This helps you see positioning during setup

2. **Add Your {cols * rows} Video Sources (Middle)**
   - For each source, right-click → Transform → Edit Transform
   - Use the positions from the table above
   - Set Bounding Box Type: "Scale to inner bounds"
   - Set Alignment: Center

3. **Add Grid Overlay (Top)**
   - Add `grid_{grid_name}_{aspect_ratio_name.replace(':', '-')}_{res_name}.png` as Image source
   - Place at the very top of source list

4. **(Optional) Remove Green Background**
   - Once positioned, you can delete the green layer
   - Or replace with a different color/image
"""
    
    return guide, positions

# Generate all combinations
print("Starting Grid Overlay Generator...")
print("=" * 60)

all_metadata = {}

for width, height, res_name in RESOLUTIONS:
    print(f"\n📐 Generating {res_name} ({width}×{height})...")
    
    # Create backgrounds for this resolution
    for bg_name, bg_color in BACKGROUND_COLORS.items():
        bg_img = create_background(width, height, bg_color)
        bg_filename = f"background_{bg_name}_{res_name}.png"
        bg_img.save(f"{output_dir}/backgrounds/{bg_filename}")
        print(f"  ✓ Background: {bg_filename}")
    
    for cols, rows, grid_name in GRIDS:
        print(f"  🔲 Grid: {grid_name} ({cols}×{rows})...")
        
        for aspect_name, aspect_value in ASPECT_RATIOS.items():
            # Create grid overlay
            overlay = create_grid_overlay(width, height, cols, rows, BAR_THICKNESS)
            overlay_filename = f"grid_{grid_name}_{aspect_name.replace(':', '-')}_{res_name}.png"
            overlay.save(f"{output_dir}/overlays/{overlay_filename}")
            
            # Generate guide
            guide_text, positions = generate_position_guide(
                width, height, cols, rows, aspect_name, aspect_value, res_name, grid_name
            )
            guide_filename = f"guide_{grid_name}_{aspect_name.replace(':', '-')}_{res_name}.md"
            with open(f"{output_dir}/guides/{guide_filename}", 'w') as f:
                f.write(guide_text)
            
            # Store metadata
            metadata_key = f"{grid_name}_{aspect_name}_{res_name}"
            all_metadata[metadata_key] = {
                "resolution": res_name,
                "width": width,
                "height": height,
                "grid": grid_name,
                "cols": cols,
                "rows": rows,
                "total_cells": cols * rows,
                "aspect_ratio": aspect_name,
                "bar_thickness": BAR_THICKNESS,
                "overlay_file": overlay_filename,
                "guide_file": guide_filename,
                "positions": positions
            }
            
            print(f"    ✓ {aspect_name}: {overlay_filename}")

# Save metadata JSON
with open(f"{output_dir}/metadata.json", 'w') as f:
    json.dump(all_metadata, f, indent=2)

print("\n" + "=" * 60)
print("✅ Generation Complete!")
print(f"📁 Output directory: {output_dir}")
print(f"📊 Total overlays: {len(RESOLUTIONS) * len(GRIDS) * len(ASPECT_RATIOS)}")
print(f"🎨 Total backgrounds: {len(RESOLUTIONS) * len(BACKGROUND_COLORS)}")
print(f"📄 Total guides: {len(RESOLUTIONS) * len(GRIDS) * len(ASPECT_RATIOS)}")

