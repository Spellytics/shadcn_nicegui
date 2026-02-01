"""Shadcn-style UI components for NiceGUI."""
from nicegui import ui
import plotly.graph_objects as go
from typing import List, Dict, Optional


# Global font configuration
class FontConfig:
    """Global font configuration for shadcn components."""
    _font_family: str = 'Inter, system-ui, -apple-system, sans-serif'

    @classmethod
    def set_font(cls, font_family: str):
        """Set the global font family for all components.

        Args:
            font_family: CSS font-family string (e.g., 'Roboto, sans-serif')
        """
        cls._font_family = font_family

    @classmethod
    def get_font(cls) -> str:
        """Get the current global font family."""
        return cls._font_family


def set_global_font(font_family: str):
    """Set the global font family for all shadcn components.

    Args:
        font_family: CSS font-family string (e.g., 'Roboto, sans-serif', 'Poppins, sans-serif')

    Example:
        set_global_font('Roboto, sans-serif')
        # or use Google Fonts
        set_global_font('"Poppins", sans-serif')
    """
    FontConfig.set_font(font_family)


def button(text: str, on_click=None, variant='default', size='default', icon=None, font_family: Optional[str] = None, additional_classes: str = ''):
    """Create a shadcn-style button

    Args:
        text: Button text
        on_click: Click handler
        variant: 'default', 'destructive', 'outline', 'ghost', 'secondary'
        size: 'default', 'sm', 'lg', 'icon'
        icon: Optional icon name
        font_family: Optional custom font family (overrides global font)
        additional_classes: Additional Tailwind classes
    """

    # Base classes for all buttons
    base_classes = 'inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50'

    # Variant-specific classes
    variant_classes = {
        'default': 'bg-slate-900 text-slate-50 hover:bg-slate-800 shadow text-white',
        'destructive': 'bg-red-500 text-slate-50 hover:bg-red-600 shadow-sm text-white',
        'outline': 'border border-slate-300 bg-white hover:bg-slate-100 hover:text-slate-900 text-black',
        'secondary': 'bg-slate-100 text-slate-900 hover:bg-slate-200 shadow-sm',
        'ghost': 'hover:bg-slate-100 hover:text-slate-900',
    }

    # Size-specific classes
    size_classes = {
        'default': 'h-10 px-4 py-2',
        'sm': 'h-9 rounded-md px-3',
        'lg': 'h-11 rounded-md px-8',
        'icon': 'h-10 w-10',
    }

    classes = f'{base_classes} {variant_classes.get(variant, variant_classes["default"])} {size_classes.get(size, size_classes["default"])} {additional_classes}'.strip()

    btn = ui.button(text, on_click=on_click).classes(classes)
    btn.props('flat no-caps')

    # Apply font family
    font = font_family or FontConfig.get_font()
    btn.style(f'font-family: {font}')

    return btn


def input(label: str = '', placeholder: str = '', value: str = '', font_family: Optional[str] = None, additional_classes: str = ''):
    """Create a shadcn-style input field

    Args:
        label: Input label
        placeholder: Placeholder text
        value: Initial value
        font_family: Optional custom font family (overrides global font)
        additional_classes: Additional Tailwind classes
    """
    font = font_family or FontConfig.get_font()

    with ui.column().classes('w-full gap-1'):
        if label:
            label_elem = ui.label(label).classes('text-sm font-medium text-black')
            label_elem.style(f'font-family: {font}')
        input_field = ui.input(placeholder=placeholder, value=value)
        input_field.classes(f'w-full {additional_classes}'.strip())
        input_field.props('outlined dense borderless')
        input_field.props('bg-color="white" color="slate-900"')
        input_field.style(f'font-family: {font}')

    return input_field


def select(options: list, label: str = '', value=None, font_family: Optional[str] = None, additional_classes: str = ''):
    """Create a shadcn-style select field

    Args:
        options: List of options
        label: Select label
        value: Initial value
        font_family: Optional custom font family (overrides global font)
        additional_classes: Additional Tailwind classes
    """
    font = font_family or FontConfig.get_font()

    with ui.column().classes('w-full gap-1'):
        if label:
            label_elem = ui.label(label).classes('text-sm font-medium text-black')
            label_elem.style(f'font-family: {font}')
        select_field = ui.select(options, value=value)
        select_field.classes(f'w-full {additional_classes}'.strip())
        select_field.props('outlined dense borderless')
        select_field.props('bg-color="white" color="slate-900"')
        select_field.style(f'font-family: {font}')

    return select_field


def heading(text: str, level: int = 3, color: str = 'text-black', font_family: Optional[str] = None, additional_classes: str = ''):
    """Create a shadcn-style heading

    Args:
        text: Heading text
        level: Heading level 1-6 (default: 3)
        color: Tailwind color class (default: 'text-black')
        font_family: Optional custom font family (overrides global font)
        additional_classes: Additional Tailwind classes
    """
    size_classes = {
        1: 'text-4xl font-bold',
        2: 'text-3xl font-bold',
        3: 'text-2xl font-semibold',
        4: 'text-xl font-semibold',
        5: 'text-lg font-medium',
        6: 'text-base font-medium'
    }

    classes = f'{size_classes.get(level, size_classes[3])} {color} {additional_classes}'.strip()
    font = font_family or FontConfig.get_font()
    heading = ui.label(text).classes(classes)
    heading.style(f'font-family: {font}')


def card(width: str = 'w-full max-w-4xl', margin: str = 'mx-auto', padding: str = 'p-8', additional_classes: str = '', variant: str = 'default'):
    """Create a shadcn-style card container

    Args:
        width: Width classes (default: 'w-full max-w-4xl')
        margin: Margin classes (default: 'mx-auto')
        padding: Padding classes (default: 'p-8')
        additional_classes: Additional Tailwind classes
        variant: 'default', 'outlined', 'elevated', 'ghost' (default: 'default')
    """
    # Base card classes
    base_classes = 'rounded-lg bg-white'

    # Variant-specific classes
    variant_classes = {
        'default': 'border border-slate-200 shadow-none',
        'outlined': 'border border-slate-200 shadow-none',
        'elevated': 'shadow-lg',
        'ghost': 'shadow-none',
    }

    variant_class = variant_classes.get(variant, variant_classes['default'])
    classes = f'{base_classes} {variant_class} {width} {margin} {padding} {additional_classes}'.strip()
    return ui.card().classes(classes)


def expandable(text: str, width: str = 'w-full', additional_classes: str = ''):
    """Create a shadcn-style expandable/accordion component

    Args:
        text: Expansion header text
        width: Width classes (default: 'w-full')
        additional_classes: Additional Tailwind classes
    """
    classes = f'{width} {additional_classes}'.strip()
    return ui.expansion(text).classes(classes)


def table(columns: List[Dict], rows: List[Dict], additional_classes: str = ''):
    """Create a shadcn-style table

    Args:
        columns: List of column definitions [{'name': 'id', 'label': 'ID', 'field': 'id', 'align': 'left'}, ...]
        rows: List of row data dictionaries
        additional_classes: Additional Tailwind classes
    """
    classes = f'w-full {additional_classes}'.strip()

    table = ui.table(columns=columns, rows=rows, row_key='id')
    table.classes(classes)

    # Apply shadcn styling via props
    table.props('flat bordered separator="none"')

    # Add darker bottom border for headers
    table.style('thead { border-bottom: 2px solid rgb(15 23 42) !important; }')

    return table


def dialog(title: str = '', additional_classes: str = ''):
    """Create a shadcn-style dialog/modal

    Args:
        title: Dialog title (optional)
        additional_classes: Additional Tailwind classes

    Returns:
        ui.dialog object that can be used with context manager

    Example:
        with dialog('Confirm Action') as dialog:
            ui.label('Are you sure?')
            with ui.row():
                button('Cancel', on_click=dialog.close, variant='outline')
                button('Confirm', on_click=lambda: (do_action(), dialog.close()))
    """
    dialog = ui.dialog()

    with dialog, ui.card().classes(f'p-6 min-w-96 max-w-2xl {additional_classes}'.strip()):
        if title:
            heading(title, level=3, color='text-slate-900')
            ui.separator().classes('my-4')

        # Content will be added by the context manager
        content_container = ui.column().classes('w-full gap-4')

    return dialog


def badge(text: str, variant: str = 'default', additional_classes: str = '', font_family: Optional[str] = None):
    """Create a shadcn-style badge

    Args:
        text: Badge text
        variant: 'default', 'secondary', 'destructive', 'outline', 'success'
        additional_classes: Additional Tailwind classes
        font_family: Optional custom font family (overrides global font)
    """
    # Base classes for all badges
    base_classes = 'inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-semibold transition-colors'

    # Variant-specific classes
    variant_classes = {
        'default': 'bg-slate-900 text-slate-50 hover:bg-slate-800',
        'secondary': 'bg-slate-100 text-slate-900 hover:bg-slate-200',
        'destructive': 'bg-red-500 text-slate-50 hover:bg-red-600',
        'outline': 'border border-slate-300 text-slate-900 bg-white',
        'success': 'bg-green-500 text-white hover:bg-green-600',
    }

    classes = f'{base_classes} {variant_classes.get(variant, variant_classes["default"])} {additional_classes}'.strip()

    font = font_family or FontConfig.get_font()
    badge = ui.label(text).classes(classes)
    badge.style(f'font-family: {font}')
    return badge


def avatar(
    image_url: Optional[str] = None,
    fallback_text: str = '',
    size: str = 'md',
    variant: str = 'circle',
    font_family: Optional[str] = None,
    additional_classes: str = ''
):
    """Create a shadcn-style avatar

    Args:
        image_url: URL of the avatar image (if None, shows fallback text)
        fallback_text: Text to show when image is not available (usually initials)
        size: 'sm', 'md', 'lg', 'xl' (default: 'md')
        variant: 'circle' or 'square' (default: 'circle')
        font_family: Optional custom font family (overrides global font)
        additional_classes: Additional Tailwind classes

    Returns:
        The NiceGUI element containing the avatar

    Example:
        # With image
        avatar(image_url='https://example.com/avatar.jpg')

        # With fallback text
        avatar(fallback_text='JD', size='lg')
    """
    # Size classes
    size_classes = {
        'sm': 'h-8 w-8 text-xs',
        'md': 'h-10 w-10 text-sm',
        'lg': 'h-12 w-12 text-base',
        'xl': 'h-16 w-16 text-lg',
    }

    # Shape classes
    shape_class = 'rounded-full' if variant == 'circle' else 'rounded-md'

    # Base classes
    base_classes = f'inline-flex items-center justify-center overflow-hidden bg-slate-100 {shape_class} {size_classes.get(size, size_classes["md"])} {additional_classes}'.strip()

    font = font_family or FontConfig.get_font()

    if image_url:
        # Create avatar with image
        with ui.element('div').classes(base_classes) as avatar_container:
            ui.image(image_url).classes('h-full w-full object-cover')
        return avatar_container
    else:
        # Create avatar with fallback text
        avatar_label = ui.label(fallback_text).classes(f'{base_classes} font-medium text-slate-600')
        avatar_label.style(f'font-family: {font}')
        return avatar_label


def separator(orientation: str = 'horizontal', additional_classes: str = ''):
    """Create a shadcn-style separator/divider

    Args:
        orientation: 'horizontal' or 'vertical'
        additional_classes: Additional Tailwind classes
    """
    if orientation == 'vertical':
        classes = f'h-full w-px bg-slate-200 {additional_classes}'.strip()
    else:
        classes = f'w-full h-px bg-slate-200 {additional_classes}'.strip()

    return ui.separator().classes(classes)


def calendar(on_change=None, value=None, additional_classes: str = ''):
    """Create a shadcn-style date picker/calendar

    Args:
        on_change: Callback function when date is selected
        value: Initial date value (string in format 'YYYY-MM-DD' or None)
        additional_classes: Additional Tailwind classes

    Returns:
        ui.date object

    Example:
        calendar = calendar(on_change=lambda e: print(e.value))
    """
    classes = f'w-full {additional_classes}'.strip()

    date_picker = ui.date(value=value, on_change=on_change)
    date_picker.classes(classes)
    date_picker.props('outlined flat')

    return date_picker


def barchart(data: Dict[str, int], title: str = '', height: int = 400, label: str = 'Count', additional_classes: str = ''):
    """Create a shadcn-style bar chart

    Args:
        data: Dictionary with categories as keys and values as counts
        title: Chart title
        height: Chart height in pixels
        label: Label for the value in tooltip (default: 'Count')
        additional_classes: Additional Tailwind classes
    """
    categories = list(data.keys())
    values = list(data.values())

    # Create bar chart with shadcn-inspired styling
    fig = go.Figure(data=[
        go.Bar(
            x=categories,
            y=values,
            marker=dict(
                color='#0f172a',  # slate-900
                line=dict(color='#e5e7eb', width=0)
            ),
            text=values,
            textposition='outside',
            textfont=dict(
                size=12,
                color='#0f172a',
                family='Inter'
            ),
            hovertemplate=f'<br><b>  %{{x}}  </b><br>  {label}: %{{y}}  <br><extra></extra>',
        )
    ])

    # Shadcn-inspired layout
    fig.update_layout(
        title=dict(
            text=title,
            font=dict(family='Inter', size=16, color='#0f172a', weight=600),
            x=0,
            xanchor='left'
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family='Inter', size=12, color='#64748b'),
        margin=dict(l=40, r=20, t=60, b=60),
        height=height,
        xaxis=dict(
            showgrid=False,
            showline=True,
            linewidth=1,
            linecolor='#e5e7eb',
            tickfont=dict(size=11, color='#64748b'),
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='#f3f4f6',
            showline=False,
            tickfont=dict(size=11, color='#64748b'),
            range=[0, max(values) * 1.15] if values else [0, 1],
        ),
        hoverlabel=dict(
            bgcolor='#000000',
            font_size=12,
            font_family='Inter',
            font_color='white',
            bordercolor='#000000',
            namelength=-1
        )
    )

    # Create chart in a card with shadcn styling
    with ui.card().classes(f'w-full p-6 {additional_classes}'.strip()):
        ui.plotly(fig).classes('w-full')


def timeseries(dates: List[str], values: List[int], title: str = '', height: int = 400, line_color: str = '#0f172a', smooth: bool = True, label: str = 'Count', additional_classes: str = ''):
    """Create a shadcn-style timeseries chart

    Args:
        dates: List of date strings (e.g., ['2024-01-01', '2024-01-02', ...])
        values: List of corresponding values
        title: Chart title
        height: Chart height in pixels
        line_color: Line color (default: slate-900)
        smooth: Use smooth curves (True) or straight lines (False)
        label: Label for the value in tooltip (default: 'Count')
        additional_classes: Additional Tailwind classes
    """
    # Create line chart with shadcn-inspired styling
    fig = go.Figure(data=[
        go.Scatter(
            x=dates,
            y=values,
            mode='lines+markers+text',
            line=dict(
                color=line_color,
                width=2,
                shape='spline' if smooth else 'linear'
            ),
            marker=dict(
                color=line_color,
                size=6,
                line=dict(color='white', width=2)
            ),
            text=values,
            textposition='top center',
            textfont=dict(
                size=11,
                color='#0f172a',
                family='Inter'
            ),
            fill='tozeroy',
            fillcolor='rgba(15, 23, 42, 0.05)',  # Very subtle fill
            hovertemplate=f'<br><b>  %{{x}}  </b><br>  {label}: %{{y}}  <br><extra></extra>',
        )
    ])

    # Shadcn-inspired layout
    fig.update_layout(
        title=dict(
            text=title,
            font=dict(family='Inter', size=16, color='#0f172a', weight=600),
            x=0,
            xanchor='left'
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family='Inter', size=12, color='#64748b'),
        margin=dict(l=40, r=20, t=60, b=60),
        height=height,
        xaxis=dict(
            showgrid=False,
            showline=True,
            linewidth=1,
            linecolor='#e5e7eb',
            tickfont=dict(size=11, color='#64748b'),
            tickangle=-45,
            range=[-0.5, len(dates) - 0.5] if dates else [0, 1],
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='#f3f4f6',
            showline=False,
            tickfont=dict(size=11, color='#64748b'),
            range=[0, max(values) * 1.15] if values else [0, 1],
        ),
        hoverlabel=dict(
            bgcolor='#000000',
            font_size=12,
            font_family='Inter',
            font_color='white',
            bordercolor='#000000',
            namelength=-1
        )
    )

    # Create chart in a card with shadcn styling
    with ui.card().classes(f'w-full p-6 {additional_classes}'.strip()):
        ui.plotly(fig).classes('w-full')


def accordion(items: List[Dict[str, str]], width: str = 'w-full', variant: str = 'default', font_family: Optional[str] = None, additional_classes: str = ''):
    """Create a shadcn-style accordion component with multiple expandable items.

    Args:
        items: List of accordion items, each with 'title' and 'content' keys
               Example: [{'title': 'Item 1', 'content': 'Content 1'}, ...]
        width: Width classes (default: 'w-full')
        variant: 'default', 'bordered', 'separated' (default: 'default')
        font_family: Optional custom font family (overrides global font)
        additional_classes: Additional Tailwind classes

    Returns:
        The container element with all accordion items

    Example:
        accordion([
            {'title': 'Is it accessible?', 'content': 'Yes. It adheres to the WAI-ARIA design pattern.'},
            {'title': 'Is it styled?', 'content': 'Yes. It comes with default styles.'},
        ])
    """
    font = font_family or FontConfig.get_font()

    # Variant-specific classes
    variant_classes = {
        'default': 'border-b border-slate-200',
        'bordered': 'border border-slate-200 rounded-lg mb-2',
        'separated': 'mb-4 border border-slate-200 rounded-lg shadow-sm',
    }

    container_class = 'default' if variant == 'default' else ''

    with ui.column().classes(f'{width} {container_class} {additional_classes}'.strip()) as container:
        for item in items:
            title = item.get('title', '')
            content = item.get('content', '')

            item_classes = variant_classes.get(variant, variant_classes['default'])

            with ui.expansion(title, icon='').classes(item_classes) as exp:
                # Style the expansion header
                exp._props['header-class'] = 'text-sm font-medium hover:no-underline'

                # Add content
                with ui.column().classes('pb-4 pt-0'):
                    content_label = ui.label(content).classes('text-sm text-slate-600')
                    content_label.style(f'font-family: {font}')

                # Apply font to expansion header
                exp.style(f'font-family: {font}')

    return container
