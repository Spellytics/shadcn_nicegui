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
from shadcn_nicegui import shadcn_button, shadcn_card, shadcn_input

with ui.page('/'):
    with shadcn_card():
        shadcn_heading('Welcome', level=1)
        shadcn_input(label='Name', placeholder='Enter your name')
        shadcn_button('Submit', variant='default')

ui.run()
```

## Available Components

- `shadcn_button` - Styled buttons with variants (default, destructive, outline, ghost, secondary)
- `shadcn_input` - Input fields
- `shadcn_select` - Select/dropdown fields
- `shadcn_heading` - Headings (h1-h6)
- `shadcn_card` - Card containers
- `shadcn_expandable` - Accordion/expandable sections
- `shadcn_table` - Data tables
- `shadcn_dialog` - Modal dialogs
- `shadcn_badge` - Badges
- `shadcn_separator` - Dividers
- `shadcn_calendar` - Date picker
- `shadcn_barchart` - Bar charts (using Plotly)
- `shadcn_timeseries` - Time series charts (using Plotly)

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
