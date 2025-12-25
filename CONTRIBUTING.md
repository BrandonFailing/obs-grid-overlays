# Contributing to OBS Grid Overlays

Thanks for your interest in contributing! This project aims to provide simple, reliable grid overlays for OBS users.

## How to Contribute

### 1. Reporting Issues

Found a bug or have a feature request?

**Before submitting:**
- Search existing issues to avoid duplicates
- Check if your OBS canvas resolution matches the overlay resolution
- Verify you're following the setup guide

**When creating an issue:**
- Use a clear, descriptive title
- Include OBS version and operating system
- Describe expected vs actual behavior
- Include screenshots if relevant
- Mention which overlay file you're using

### 2. Suggesting Features

We love new ideas! Feature requests might include:
- New grid layouts (e.g., 5×3, asymmetric grids)
- Different visual styles (rounded corners, gradients, colors)
- Additional resolutions
- Specialized overlays (PIP layouts, corner grids, etc.)

**Please include:**
- Your use case (why you need this)
- Visual mockup or description
- Whether you'd be willing to help implement it

### 3. Submitting Code

#### Setting Up Development Environment

```bash
git clone https://github.com/yourusername/obs-grid-overlays.git
cd obs-grid-overlays

# Install Python dependencies (only PIL/Pillow needed)
pip install Pillow

# Generate overlays
python generator.py
```

#### Code Guidelines

**Python Code:**
- Follow PEP 8 style guidelines
- Add comments for complex calculations
- Keep functions focused and single-purpose
- Update metadata.json when adding configurations

**File Naming:**
- Overlays: `grid_{LAYOUT}_{ASPECT}_{RESOLUTION}.png`
- Backgrounds: `background_{COLOR}_{RESOLUTION}.png`
- Guides: `guide_{LAYOUT}_{ASPECT}_{RESOLUTION}.md`

**Documentation:**
- Update README.md for new features
- Add examples to QUICK_REFERENCE.md
- Include position guides for new layouts

#### Pull Request Process

1. **Fork the repository**
2. **Create a feature branch:** `git checkout -b feature/amazing-grid`
3. **Make your changes**
4. **Test thoroughly:** Verify overlays work in OBS
5. **Update documentation:** README, guides, etc.
6. **Commit with clear messages:** `git commit -m "Add 5x3 grid layout"`
7. **Push to your fork:** `git push origin feature/amazing-grid`
8. **Open a Pull Request**

**PR Checklist:**
- [ ] Code follows project style
- [ ] All generated files are included
- [ ] Documentation is updated
- [ ] Tested in OBS Studio
- [ ] No breaking changes (or clearly documented)

### 4. Creating New Grid Layouts

To add a new grid layout:

```python
# In generator.py, add to GRIDS list:
GRIDS = [
    # ... existing grids ...
    (5, 3, "5x3"),  # (columns, rows, name)
]
```

Then run `python generator.py` to generate all variations.

### 5. Adding New Aspect Ratios

```python
# In generator.py, add to ASPECT_RATIOS dict:
ASPECT_RATIOS = {
    # ... existing ratios ...
    "21:9": 21/9,  # Ultrawide
}
```

### 6. Supporting New Resolutions

```python
# In generator.py, add to RESOLUTIONS list:
RESOLUTIONS = [
    # ... existing resolutions ...
    (2048, 1080, "2K_ultrawide"),  # (width, height, name)
]
```

## Code of Conduct

### Our Standards

- **Be respectful** - Different skill levels and perspectives
- **Be constructive** - Criticism should be helpful
- **Be collaborative** - We're all here to help OBS users
- **Be patient** - Not everyone has the same availability

### Unacceptable Behavior

- Harassment, discrimination, or trolling
- Spam or off-topic content
- Publishing others' private information
- Unprofessional conduct

## Style Guidelines

### Python Code Style

```python
# Good: Clear variable names, documented logic
def calculate_cell_dimensions(canvas_width, canvas_height, cols, rows, aspect_ratio):
    """Calculate optimal cell dimensions for given aspect ratio"""
    # Account for bars between cells
    total_bar_width = (cols - 1) * BAR_THICKNESS
    available_width = canvas_width - total_bar_width
    
    # Distribute evenly
    cell_width = available_width / cols
    return cell_width

# Bad: Unclear names, no comments
def calc(w, h, c, r, a):
    x = (c - 1) * 20
    return (w - x) / c
```

### Documentation Style

- Use clear, concise language
- Include examples
- Assume reader is OBS user, not necessarily programmer
- Screenshots when helpful (but keep file sizes reasonable)

### Commit Messages

```
Good:
- "Add 5x3 grid layout for wide setups"
- "Fix positioning calculation for 1:1 aspect ratio"
- "Update README with troubleshooting section"

Bad:
- "updates"
- "fix"
- "asdfasdf"
```

## Testing Checklist

Before submitting PR, verify:

- [ ] Generated overlays are correct resolution
- [ ] Transparent areas are truly transparent
- [ ] Black bars are exactly 20px (or documented thickness)
- [ ] Position guides have accurate coordinates
- [ ] Overlays work in OBS Studio (actually test it!)
- [ ] No regression in existing layouts
- [ ] Documentation is clear and accurate

## Getting Help

- **Questions:** Open a discussion
- **Bugs:** Open an issue
- **Ideas:** Open an issue with "enhancement" label
- **General chat:** Discussions tab

## Recognition

Contributors will be:
- Listed in README (if substantial contribution)
- Credited in release notes
- Appreciated by the OBS community! 🎉

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for helping make OBS Grid Overlays better for everyone! 🙏
