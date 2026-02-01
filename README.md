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
- `card` - Card containers
- `expandable` - Accordion/expandable sections
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

## License

MIT License

## Credits

Inspired by [shadcn/ui](https://ui.shadcn.com/) and built for [NiceGUI](https://nicegui.io/).
