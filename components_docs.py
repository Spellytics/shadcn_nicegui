"""Components documentation page - showcasing all shadcn-nicegui components with examples and code."""
from nicegui import ui
from shadcn_nicegui import (
    button, input, select, heading, card, expandable, accordion,
    table, dialog, badge, avatar, separator, calendar,
    barchart, timeseries, set_global_font
)


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def create_code_block(code: str):
    """Create a styled code block."""
    with ui.card().classes('w-full bg-slate-950 text-slate-50 p-4 rounded-lg'):
        ui.html(f'<pre><code class="text-sm">{code}</code></pre>', sanitize=False).classes('overflow-x-auto')


def section_heading(text: str, level: int = 2):
    """Create a section heading with consistent styling."""
    size_class = 'text-2xl' if level == 2 else 'text-xl'
    ui.label(text).classes(f'{size_class} font-semibold mt-8 mb-4')


def subsection_heading(text: str):
    """Create a subsection heading."""
    section_heading(text, level=3)


def show_installation_section():
    """Show standard installation section."""
    section_heading('Installation')
    create_code_block('pip install shadcn-nicegui')


def show_api_param(name: str, description: str):
    """Show a single API parameter."""
    return f'''
        <div>
            <code class="text-sm bg-slate-100 px-2 py-1 rounded">{name}</code>
            <p class="text-sm text-slate-600 mt-1">{description}</p>
        </div>'''


def show_api_reference(params: list):
    """Show API reference section with parameters."""
    section_heading('API Reference')
    with card(width='w-full', padding='p-6', variant='outlined'):
        params_html = ''.join([show_api_param(name, desc) for name, desc in params])
        ui.html(f'<div class="space-y-4">{params_html}</div>', sanitize=False)


def show_preview_section(preview_fn):
    """Show a preview section with a component example."""
    with card(width='w-full', padding='p-6', variant='outlined'):
        ui.label('Preview').classes('text-sm font-semibold text-slate-700 mb-4')
        preview_fn()


def show_example_with_code(example_fn, code: str):
    """Show an example with its code."""
    with card(width='w-full', padding='p-6', variant='outlined'):
        example_fn()
    create_code_block(code)


# ============================================================================
# COMPONENT DOCUMENTATION FUNCTIONS
# ============================================================================

def show_accordion_docs():
    """Accordion component documentation."""
    heading('Accordion', level=1)
    ui.label('A vertically stacked set of interactive headings that reveal content.').classes(
        'text-lg text-slate-600 mt-2 mb-8'
    )

    # Preview
    show_preview_section(lambda: accordion([
        {'title': 'Is it accessible?', 'content': 'Yes. It adheres to the WAI-ARIA design pattern.'},
        {'title': 'Is it styled?', 'content': 'Yes. It comes with default styles that you can customize.'},
        {'title': 'Is it animated?', 'content': 'Yes. The expansion is animated by default.'},
    ], variant='default', width='w-full max-w-xl'))

    # Installation
    show_installation_section()

    # Usage
    section_heading('Usage')
    create_code_block('''from shadcn_nicegui import accordion

accordion([
    {'title': 'Item 1', 'content': 'Content 1'},
    {'title': 'Item 2', 'content': 'Content 2'},
], variant='default')''')

    # Examples
    section_heading('Examples')

    subsection_heading('Default')
    show_example_with_code(
        lambda: accordion([
            {'title': 'What is NiceGUI?', 'content': 'NiceGUI is a Python web framework for building browser-based UIs.'},
            {'title': 'What is Shadcn?', 'content': 'Shadcn UI is a collection of re-usable components.'},
        ], variant='default', width='w-full max-w-xl'),
        '''accordion([
    {'title': 'Item 1', 'content': 'Content 1'},
    {'title': 'Item 2', 'content': 'Content 2'},
], variant='default')'''
    )

    subsection_heading('Bordered')
    show_example_with_code(
        lambda: accordion([
            {'title': 'Getting Started', 'content': 'Install with pip install shadcn-nicegui'},
            {'title': 'Documentation', 'content': 'Check the README for detailed docs.'},
        ], variant='bordered', width='w-full max-w-xl'),
        '''accordion([
    {'title': 'Item 1', 'content': 'Content 1'},
    {'title': 'Item 2', 'content': 'Content 2'},
], variant='bordered')'''
    )

    # API Reference
    show_api_reference([
        ('items', "List of dictionaries with 'title' and 'content' keys. Required."),
        ('variant', "'default' | 'bordered' | 'separated'. Default: 'default'"),
        ('width', "Tailwind width classes. Default: 'w-full'"),
        ('font_family', 'Optional custom font family. Default: global font'),
    ])


def show_button_docs():
    """Button component documentation."""
    heading('Button', level=1)
    ui.label('Displays a button or a component that looks like a button.').classes(
        'text-lg text-slate-600 mt-2 mb-8'
    )

    # Preview
    show_preview_section(lambda: button('Button', variant='default'))

    # Installation
    show_installation_section()

    # Usage
    section_heading('Usage')
    create_code_block('''from shadcn_nicegui import button

button('Click me', variant='default')''')

    # Examples
    section_heading('Examples')

    subsection_heading('Variants')
    with card(width='w-full', padding='p-6', variant='outlined'):
        with ui.row().classes('gap-3 flex-wrap'):
            button('Default', variant='default')
            button('Secondary', variant='secondary')
            button('Outline', variant='outline')
            button('Ghost', variant='ghost')
            button('Destructive', variant='destructive')
    create_code_block('''button('Default', variant='default')
button('Secondary', variant='secondary')
button('Outline', variant='outline')
button('Ghost', variant='ghost')
button('Destructive', variant='destructive')''')

    subsection_heading('Sizes')
    with card(width='w-full', padding='p-6', variant='outlined'):
        with ui.row().classes('gap-3 items-center flex-wrap'):
            button('Small', size='sm')
            button('Default', size='default')
            button('Large', size='lg')
    create_code_block('''button('Small', size='sm')
button('Default', size='default')
button('Large', size='lg')''')

    # API Reference
    show_api_reference([
        ('text', 'Button text. Required.'),
        ('variant', "'default' | 'destructive' | 'outline' | 'ghost' | 'secondary'. Default: 'default'"),
        ('size', "'default' | 'sm' | 'lg' | 'icon'. Default: 'default'"),
        ('on_click', 'Click handler function. Optional.'),
    ])


def show_card_docs():
    """Card component documentation."""
    heading('Card', level=1)
    ui.label('Displays content in a contained, elevated surface.').classes(
        'text-lg text-slate-600 mt-2 mb-8'
    )

    # Preview
    show_preview_section(lambda: (
        card(width='w-80', padding='p-6', variant='default').__enter__(),
        heading('Card Title', level=3),
        ui.label('Card content goes here').classes('text-slate-600 mt-2'),
        card(width='w-80', padding='p-6', variant='default').__exit__(None, None, None)
    ))

    # Installation  
    show_installation_section()

    # Usage
    section_heading('Usage')
    create_code_block('''from shadcn_nicegui import card, heading

with card(width='w-80', padding='p-6'):
    heading('Card Title', level=3)
    ui.label('Card content')''')

    # Examples
    section_heading('Examples')
    
    subsection_heading('Variants')
    with card(width='w-full', padding='p-6', variant='outlined'):
        with ui.row().classes('gap-4 flex-wrap'):
            with card(width='w-60', padding='p-4', variant='default'):
                ui.label('Default').classes('font-semibold')
                ui.label('Subtle shadow').classes('text-sm text-slate-600 mt-1')
            
            with card(width='w-60', padding='p-4', variant='outlined'):
                ui.label('Outlined').classes('font-semibold')
                ui.label('Border, no shadow').classes('text-sm text-slate-600 mt-1')
            
            with card(width='w-60', padding='p-4', variant='elevated'):
                ui.label('Elevated').classes('font-semibold')
                ui.label('Prominent shadow').classes('text-sm text-slate-600 mt-1')
    
    create_code_block('''card(variant='default')
card(variant='outlined')
card(variant='elevated')
card(variant='ghost')''')

    # API Reference
    show_api_reference([
        ('width', "Tailwind width classes. Default: 'w-full max-w-4xl'"),
        ('margin', "Margin classes. Default: 'mx-auto'"),
        ('padding', "Padding classes. Default: 'p-8'"),
        ('variant', "'default' | 'outlined' | 'elevated' | 'ghost'. Default: 'default'"),
        ('additional_classes', 'Additional Tailwind classes. Optional.'),
    ])


def show_badge_docs():
    """Badge component documentation."""
    heading('Badge', level=1)
    ui.label('Displays a badge or a component that looks like a badge.').classes(
        'text-lg text-slate-600 mt-2 mb-8'
    )

    # Preview
    show_preview_section(lambda: badge('Badge', variant='default'))

    # Installation
    show_installation_section()

    # Usage
    section_heading('Usage')
    create_code_block('''from shadcn_nicegui import badge

badge('New', variant='default')''')

    # Examples
    section_heading('Examples')
    with card(width='w-full', padding='p-6', variant='outlined'):
        with ui.row().classes('gap-2 flex-wrap'):
            badge('Default', variant='default')
            badge('Secondary', variant='secondary')
            badge('Outline', variant='outline')
            badge('Destructive', variant='destructive')

    create_code_block('''badge('Default', variant='default')
badge('Secondary', variant='secondary')
badge('Outline', variant='outline')
badge('Destructive', variant='destructive')''')

    # API Reference
    show_api_reference([
        ('text', 'Badge text. Required.'),
        ('variant', "'default' | 'secondary' | 'outline' | 'destructive'. Default: 'default'"),
    ])


def show_input_docs():
    """Input component documentation."""
    heading('Input', level=1)
    ui.label('Displays a form input field.').classes('text-lg text-slate-600 mt-2 mb-8')

    # Preview
    show_preview_section(lambda: input(label='Email', placeholder='Enter your email', value=''))

    # Installation
    show_installation_section()

    # Usage
    section_heading('Usage')
    create_code_block('''from shadcn_nicegui import input

input(label='Email', placeholder='Enter email')''')

    # API Reference
    show_api_reference([
        ('label', "Input label. Default: ''"),
        ('placeholder', "Placeholder text. Default: ''"),
        ('value', "Initial value. Default: ''"),
        ('font_family', 'Optional custom font family. Default: global font'),
    ])


# ============================================================================
# MAIN APPLICATION
# ============================================================================

def create_header():
    """Create the page header."""
    with ui.header().classes('bg-white border-b border-slate-200'):
        with ui.row().classes('w-full max-w-7xl mx-auto px-6 py-4 items-center justify-between'):
            with ui.row().classes('items-center gap-2'):
                ui.label('⚡').classes('text-2xl')
                ui.label('shadcn-nicegui').classes('text-xl font-bold')
            ui.link(
                'GitHub',
                'https://github.com/yourusername/shadcn-nicegui',
                new_tab=True
            ).classes('text-sm text-slate-600 hover:text-slate-900')


def create_sidebar():
    """Create the sidebar navigation."""
    with ui.column().classes('w-64 min-h-screen border-r border-slate-200 p-6 gap-1 fixed'):
        ui.label('Getting Started').classes(
            'text-xs font-semibold text-slate-500 uppercase tracking-wide mb-2'
        )
        ui.link('Introduction', '#').classes('text-sm text-slate-600 hover:text-slate-900 py-1')
        ui.link('Installation', '#').classes('text-sm text-slate-600 hover:text-slate-900 py-1')

        ui.label('Components').classes(
            'text-xs font-semibold text-slate-500 uppercase tracking-wide mb-2 mt-6'
        )

        components = [
            ('Accordion', 'accordion'),
            ('Avatar', 'avatar'),
            ('Badge', 'badge'),
            ('Button', 'button'),
            ('Calendar', 'calendar'),
            ('Card', 'card'),
            ('Dialog', 'dialog'),
            ('Input', 'input'),
            ('Select', 'select'),
            ('Separator', 'separator'),
            ('Table', 'table'),
        ]

        for name, component_id in components:
            ui.link(name, f'#{component_id}').classes('text-sm text-slate-600 hover:text-slate-900 py-1')


def create_component_tabs():
    """Create tabs for different components."""
    with ui.tabs().classes('w-full') as tabs:
        accordion_tab = ui.tab('Accordion')
        button_tab = ui.tab('Button')
        card_tab = ui.tab('Card')
        badge_tab = ui.tab('Badge')
        input_tab = ui.tab('Input')

    with ui.tab_panels(tabs, value=accordion_tab).classes('w-full'):
        with ui.tab_panel(accordion_tab):
            show_accordion_docs()

        with ui.tab_panel(button_tab):
            show_button_docs()

        with ui.tab_panel(card_tab):
            show_card_docs()

        with ui.tab_panel(badge_tab):
            show_badge_docs()

        with ui.tab_panel(input_tab):
            show_input_docs()


def main():
    """Main documentation page."""
    create_header()

    with ui.row().classes('w-full max-w-7xl mx-auto'):
        create_sidebar()

        # Main content area
        with ui.column().classes('flex-1 ml-64 p-8 gap-0'):
            create_component_tabs()


if __name__ in {"__main__", "__mp_main__"}:
    main()
    ui.run(
        title='shadcn-nicegui Components',
        favicon='⚡',
        dark=False,
        reload=False,
        port=8083
    )
