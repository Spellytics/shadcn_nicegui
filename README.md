# Shadcn NiceGUI

Beautiful Shadcn-style UI components for [NiceGUI](https://nicegui.io/).

## Installation

```bash
pip install shadcn-nicegui
```

Or install from source:

```bash
git clone https://github.com/yourusername/shadcn-nicegui.git
cd shadcn-nicegui
pip install -e .
```

## Usage

```python
from nicegui import ui
from shadcn_nicegui import button, card, input, heading

with ui.page('/'):
    with card():
        heading('Welcome', level=1)
        input(label='Name', placeholder='Enter your name')
        button('Submit', variant='default')

ui.run()
```

## Available Components

- `button` - Styled buttons with variants (default, destructive, outline, ghost, secondary)
- `input` - Input fields
- `select` - Select/dropdown fields
- `heading` - Headings (h1-h6)
- `card` - Card containers with variants (default, outlined, elevated, ghost)
- `expandable` - Simple expandable sections
- `accordion` - Multi-item accordion with variants (default, bordered, separated)
- `table` - Data tables
- `dialog` - Modal dialogs
- `badge` - Badges
- `avatar` - User avatars with image or fallback text
- `separator` - Dividers
- `calendar` - Date picker
- `barchart` - Bar charts (using Plotly)
- `timeseries` - Time series charts (using Plotly)
- `set_global_font` - Configure font family globally

## Examples

### Accordion

```python
from shadcn_nicegui import accordion

accordion([
    {'title': 'Is it accessible?', 'content': 'Yes. It adheres to the WAI-ARIA design pattern.'},
    {'title': 'Is it styled?', 'content': 'Yes. It comes with default styles.'},
    {'title': 'Is it animated?', 'content': 'Yes. The expansion is smoothly animated.'},
], variant='default')
```

### Button Variants

```python
from shadcn_nicegui import shadcn_button

shadcn_button('Default', variant='default')
shadcn_button('Destructive', variant='destructive')
shadcn_button('Outline', variant='outline')
shadcn_button('Ghost', variant='ghost')
shadcn_button('Secondary', variant='secondary')
```

### Card with Content

```python
from shadcn_nicegui import shadcn_card, shadcn_heading

with shadcn_card(width='w-full max-w-md'):
    shadcn_heading('Card Title', level=3)
    ui.label('This is card content')
```
### Charts

```python
from shadcn_nicegui import shadcn_barchart, shadcn_timeseries

# Bar chart
data = {'Jan': 10, 'Feb': 20, 'Mar': 15}
shadcn_barchart(data, title='Monthly Sales')

# Time series
dates = ['2024-01-01', '2024-01-02', '2024-01-03']
values = [100, 150, 120]
shadcn_timeseries(dates, values, title='Daily Traffic')
```

### Avatars

```python
from shadcn_nicegui import shadcn_avatar

# Avatar with image
shadcn_avatar(image_url='https://example.com/avatar.jpg', size='lg')

# Avatar with fallback text (initials)
shadcn_avatar(fallback_text='JD', size='md')

# Different sizes: 'sm', 'md', 'lg', 'xl'
shadcn_avatar(fallback_text='AB', size='xl')

# Different shapes: 'circle' (default) or 'square'
shadcn_avatar(fallback_text='MK', size='lg', variant='square')
```

### Font Configuration

```python
from shadcn_nicegui import set_global_font, shadcn_button

# Set global font for all components
set_global_font('Roboto, sans-serif')

# Override font for specific component
shadcn_button('Click me', font_family='Arial, sans-serif')
```

## Development

```bash
# Install in development mode with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black .

# Lint
ruff check .
```

### Automatic Version Incrementing

The repository includes an automatic version incrementing system using git hooks:

- **`increment_version.py`**: Python script that increments the patch version (e.g., 0.2.0 → 0.2.1)
- **`.git/hooks/pre-commit`**: Git hook that runs before each commit

The pre-commit hook automatically:
1. Increments the patch version in `__init__.py` and `pyproject.toml`
2. Adds the modified files to the commit

To manually increment the version:
```bash
python3 increment_version.py
```

To disable automatic version incrementing, remove or rename the pre-commit hook:
```bash
mv .git/hooks/pre-commit .git/hooks/pre-commit.disabled
```

## License

MIT License

## Credits

Inspired by [shadcn/ui](https://ui.shadcn.com/) and built for [NiceGUI](https://nicegui.io/).
