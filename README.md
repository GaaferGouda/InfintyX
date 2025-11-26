# Infinity X Animation

A beautiful animated lemniscate (infinity symbol) with gradient colors and arrow head, inspired by the Infinity X brand logo.

![Infinity X Animation](https://img.shields.io/badge/Python-3.7+-blue.svg)
![PyGame](https://img.shields.io/badge/PyGame-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎨 Features

- **Smooth infinity symbol animation** using mathematical lemniscate curve
- **Gradient color effect** (dark blue → light blue) matching Infinity X branding
- **Animated arrow head** following the curve
- **Clean white background** with professional logo text
- **60 FPS smooth rendering**
- **Mathematically accurate** parametric curve implementation

## 📸 Preview

The animation displays:
- An infinity symbol (lemniscate) that continuously loops
- Color gradient from dark navy blue to light grayish blue
- Arrow head pointing in the direction of motion
- "INFINITY X" text at the bottom

## 🔧 Requirements

- Python 3.7 or higher
- PyGame 2.0 or higher

## 📦 Installation

### 1. Clone or Download
```bash
git clone <your-repository-url>
cd infinity-x-animation
```

### 2. Install Dependencies
```bash
pip install pygame
```

Or if you have Python 3:
```bash
pip3 install pygame
```

### 3. Verify Installation
```bash
python -c "import pygame; print(pygame.version.ver)"
```

## 🚀 Usage

### Run the Animation

**Option 1: Command Line**
```bash
python infinity_animation.py
```

**Option 2: Python 3**
```bash
python3 infinity_animation.py
```

**Option 3: In VSCode**
1. Open `infinity_animation.py`
2. Press `F5` or click "Run Python File"

### Controls
- **Close Window**: Click the X button or press `Alt+F4` (Windows) / `Cmd+Q` (Mac)

## 📁 Project Structure

```
infinity-x-animation/
│
├── infinity_animation.py    # Main animation script
├── README.md                # This file
└── requirements.txt         # Python dependencies (optional)
```

## 🎓 How It Works

### Mathematical Foundation
The animation uses the **lemniscate of Bernoulli** curve, defined by the parametric equations:

```
x = (a * cos(t)) / (1 + sin²(t))
y = (a * sin(t) * cos(t)) / (1 + sin²(t))
```

Where:
- `t` is the parameter (angle in radians)
- `a` is the size of the curve

### Key Components

1. **`lem_curve(t, u, c)`** - Generates points on the lemniscate curve
2. **`PointHistory` class** - Maintains a queue of recent points for the trail effect
3. **`rotate_pt(p, c, theta)`** - Rotates points to create arrow head
4. **`scale_segment(p0, p1, u)`** - Scales line segments for arrow geometry
5. **`interpolate_color()`** - Creates smooth color gradients

## 🎨 Customization

### Change Colors
Edit these values in the code:
```python
dark_blue = (0, 52, 89)      # Starting color
mid_blue = (25, 85, 140)     # Middle color
light_blue = (120, 150, 180) # Ending color
```

### Adjust Animation Speed
```python
t += 1 / 20  # Increase denominator for slower, decrease for faster
```

### Modify Trail Length
```python
line_pts = PointHistory(50)  # Change 50 to desired length
```

### Change Window Size
```python
width, height = 1200, 800  # Adjust dimensions
```

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'pygame'"
**Solution:**
```bash
pip install pygame
```

### Issue: "python is not recognized"
**Solution:**
- Try `python3` instead
- Or use `py infinity_animation.py` on Windows

### Issue: Animation is too fast/slow
**Solution:** Adjust the frame rate
```python
game_clock.tick(60)  # Change 60 to desired FPS
```

### Issue: Window doesn't close properly
**Solution:** The script now includes proper event handling. Make sure you're using the latest version.

## 📚 Technical Details

- **Language**: Python 3.7+
- **Graphics Library**: PyGame 2.0+
- **Window Size**: 1200x800 pixels
- **Frame Rate**: 60 FPS
- **Color Mode**: RGB
- **Curve Type**: Lemniscate of Bernoulli

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👏 Acknowledgments

- Mathematical curve equations from [Wolfram MathWorld](https://mathworld.wolfram.com/Lemniscate.html)
- Inspired by the Infinity X brand logo
- Built with PyGame community support

## 📧 Contact

For questions or suggestions, please open an issue in the repository.

---

**Made with ❤️ and Python**

*Enjoy the infinity! ∞*
