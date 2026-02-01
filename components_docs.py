"""Components documentation page - showcasing all shadcn-nicegui components with examples and code."""
from nicegui import ui
from shadcn_nicegui import (
    button, input, select, heading, card, expandable, accordion,
    table, dialog, badge, avatar, separator, calendar,
    barchart, timeseries, set_global_font
)


def create_code_block(code: str):
    """Create a styled code block."""
    with ui.card().classes('w-full bg-slate-950 text-slate-50 p-4 rounded-lg'):
        ui.html(f'<pre><code class="text-sm">{code}</code></pre>', sanitize=False).classes('overflow-x-auto')


def show_accordion_docs():
    """Accordion component documentation."""
    heading('Accordion', level=1)
    ui.label('A vertically stacked set of interactive headings that reveal content.').classes('text-lg text-slate-600 mt-2 mb-8')

    # Preview section
    with card(width='w-full', padding='p-6', variant='outlined'):
        ui.label('Preview').classes('text-sm font-semibold text-slate-700 mb-4')
        accordion([
            {'title': 'Is it accessible?', 'content': 'Yes. It adheres to the WAI-ARIA design pattern.'},
            {'title': 'Is it styled?', 'content': 'Yes. It comes with default styles that you can customize.'},
            {'title': 'Is it animated?', 'content': 'Yes. The expansion is animated by default.'},
        ], variant='default', width='w-full max-w-xl')

    # Installation
    ui.label('Installation').classes('text-2xl font-semibold mt-8 mb-4')
    create_code_block('pip install shadcn-nicegui')

    # Usage
    ui.label('Usage').classes('text-2xl font-semibold mt-8 mb-4')
    create_code_block('''from shadcn_nicegui import accordion

accordion([
    {'title': 'Item 1', 'content': 'Content 1'},
    {'title': 'Item 2', 'content': 'Content 2'},
], variant='default')''')

    # Examples
    ui.label('Examples').classes('text-2xl font-semibold mt-8 mb-4')

    # Default
    ui.label('Default').classes('text-xl font-semibold mt-6 mb-3')
    with card(width='w-full', padding='p-6', variant='outlined'):
        accordion([
            {'title': 'What is NiceGUI?', 'content': 'NiceGUI is a Python web framework for building browser-based UIs.'},
            {'title': 'What is Shadcn?', 'content': 'Shadcn UI is a collection of re-usable components.'},
        ], variant='default', width='w-full max-w-xl')
    create_code_block('''accordion([
    {'title': 'Item 1', 'content': 'Content 1'},
    {'title': 'Item 2', 'content': 'Content 2'},
], variant='default')''')

    # Bordered
    ui.label('Bordered').classes('text-xl font-semibold mt-6 mb-3')
    with card(width='w-full', padding='p-6', variant='outlined'):
        accordion([
            {'title': 'Getting Started', 'content': 'Install with pip install shadcn-nicegui'},
            {'title': 'Documentation', 'content': 'Check the README for detailed docs.'},
        ], variant='bordered', width='w-full max-w-xl')
    create_code_block('''accordion([
    {'title': 'Item 1', 'content': 'Content 1'},
    {'title': 'Item 2', 'content': 'Content 2'},
], variant='bordered')''')

    # API Reference
    ui.label('API Reference').classes('text-2xl font-semibold mt-8 mb-4')
    with card(width='w-full', padding='p-6', variant='outlined'):
        ui.html('''
            <div class="space-y-4">
                <div>
                    <code class="text-sm bg-slate-100 px-2 py-1 rounded">items</code>
                    <p class="text-sm text-slate-600 mt-1">List of dictionaries with 'title' and 'content' keys. Required.</p>
                </div>
                <div>
                    <code class="text-sm bg-slate-100 px-2 py-1 rounded">variant</code>
                    <p class="text-sm text-slate-600 mt-1">'default' | 'bordered' | 'separated'. Default: 'default'</p>
                </div>
                <div>
                    <code class="text-sm bg-slate-100 px-2 py-1 rounded">width</code>
                    <p class="text-sm text-slate-600 mt-1">Tailwind width classes. Default: 'w-full'</p>
                </div>
                <div>
                    <code class="text-sm bg-slate-100 px-2 py-1 rounded">font_family</code>
                    <p class="text-sm text-slate-600 mt-1">Optional custom font family. Default: global font</p>
                </div>
            </div>
        ''', sanitize=False)


def show_button_docs():
    """Button component documentation."""
    heading('Button', level=1)
    ui.label('Displays a button or a component that looks like a button.').classes('text-lg text-slate-600 mt-2 mb-8')

    # Preview
    with card(width='w-full', padding='p-6', variant='outlined'):
        ui.label('Preview').classes('text-sm font-semibold text-slate-700 mb-4')
        button('Button', variant='default')

    # Installation
    ui.label('Installation').classes('text-2xl font-semibold mt-8 mb-4')
    create_code_block('pip install shadcn-nicegui')

    # Usage
    ui.label('Usage').classes('text-2xl font-semibold mt-8 mb-4')
    create_code_block('''from shadcn_nicegui import button

button('Click me', variant='default')''')

    # Examples
    ui.label('Examples').classes('text-2xl font-semibold mt-8 mb-4')

    ui.label('Variants').classes('text-xl font-semibold mt-6 mb-3')
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

    ui.label('Sizes').classes('text-xl font-semibold mt-6 mb-3')
    with card(width='w-full', padding='p-6', variant='outlined'):
        with ui.row().classes('gap-3 items-center flex-wrap'):
            button('Small', size='sm')
            button('Default', size='default')
            button('Large', size='lg')
    create_code_block('''button('Small', size='sm')
button('Default', size='default')
button('Large', size='lg')''')

    # API Reference
    ui.label('API Reference').classes('text-2xl font-semibold mt-8 mb-4')
    with card(width='w-full', padding='p-6', variant='outlined'):
        ui.html('''
            <div class="space-y-4">
                <div>
                    <code class="text-sm bg-slate-100 px-2 py-1 rounded">text</code>
                    <p class="text-sm text-slate-600 mt-1">Button text. Required.</p>
                </div>
                <div>
                    <code class="text-sm bg-slate-100 px-2 py-1 rounded">variant</code>
                    <p class="text-sm text-slate-600 mt-1">'default' | 'destructive' | 'outline' | 'ghost' | 'secondary'. Default: 'default'</p>
                </div>
                <div>
                    <code class="text-sm bg-slate-100 px-2 py-1 rounded">size</code>
                    <p class="text-sm text-slate-600 mt-1">'default' | 'sm' | 'lg' | 'icon'. Default: 'default'</p>
                </div>
                <div>
                    <code class="text-sm bg-slate-100 px-2 py-1 rounded">on_click</code>
                    <p class="text-sm text-slate-600 mt-1">Click handler function. Optional.</p>
                </div>
            </div>
        ''', sanitize=False)


def show_card_docs():
    """Card component documentation."""
    heading('Card', level=1)
    ui.label('Displays content in a contained, elevated surface.').classes('text-lg text-slate-600 mt-2 mb-8')

    # Preview
    with card(width='w-full', padding='p-6', variant='outlined'):
        ui.label('Preview').classes('text-sm font-semibold text-slate-700 mb-4')
        with card(width='w-80', padding='p-6', variant='default'):
            heading('Card Title', level=3)
            ui.label('Card content goes here').classes('text-slate-600 mt-2')

    # Usage
    ui.label('Usage').classes('text-2xl font-semibold mt-8 mb-4')
    create_code_block('''from shadcn_nicegui import card, heading

with card(width='w-80', padding='p-6'):
    heading('Card Title', level=3)
    ui.label('Card content')''')

    # Examples
    ui.label('Examples').classes('text-2xl font-semibold mt-8 mb-4')

    ui.label('Variants').classes('text-xl font-semibold mt-6 mb-3')
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


def show_badge_docs():
    """Badge component documentation."""
    heading('Badge', level=1)
    ui.label('Displays a badge or a component that looks like a badge.').classes('text-lg text-slate-600 mt-2 mb-8')

    # Preview
    with card(width='w-full', padding='p-6', variant='outlined'):
        ui.label('Preview').classes('text-sm font-semibold text-slate-700 mb-4')
        badge('Badge', variant='default')

    # Usage
    ui.label('Usage').classes('text-2xl font-semibold mt-8 mb-4')
    create_code_block('''from shadcn_nicegui import badge

badge('New', variant='default')''')

    # Examples
    ui.label('Examples').classes('text-2xl font-semibold mt-8 mb-4')
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


def show_input_docs():
    """Input component documentation."""
    heading('Input', level=1)
    ui.label('Displays a form input field.').classes('text-lg text-slate-600 mt-2 mb-8')

    # Preview
    with card(width='w-full', padding='p-6', variant='outlined'):
        ui.label('Preview').classes('text-sm font-semibold text-slate-700 mb-4')
        input(label='Email', placeholder='Enter your email', value='')

    # Usage
    ui.label('Usage').classes('text-2xl font-semibold mt-8 mb-4')
    create_code_block('''from shadcn_nicegui import input

input(label='Email', placeholder='Enter email')''')


def main():
    """Main documentation page."""

    # Header
    with ui.header().classes('bg-white border-b border-slate-200'):
        with ui.row().classes('w-full max-w-7xl mx-auto px-6 py-4 items-center justify-between'):
            with ui.row().classes('items-center gap-2'):
                ui.label('⚡').classes('text-2xl')
                ui.label('shadcn-nicegui').classes('text-xl font-bold')
            ui.link('GitHub', 'https://github.com/yourusername/shadcn-nicegui', new_tab=True).classes('text-sm text-slate-600 hover:text-slate-900')

    with ui.row().classes('w-full max-w-7xl mx-auto'):
        # Sidebar
        with ui.column().classes('w-64 min-h-screen border-r border-slate-200 p-6 gap-1 fixed'):
            ui.label('Getting Started').classes('text-xs font-semibold text-slate-500 uppercase tracking-wide mb-2')
            ui.link('Introduction', '#').classes('text-sm text-slate-600 hover:text-slate-900 py-1')
            ui.link('Installation', '#').classes('text-sm text-slate-600 hover:text-slate-900 py-1')

            ui.label('Components').classes('text-xs font-semibold text-slate-500 uppercase tracking-wide mb-2 mt-6')

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

        # Main content
        with ui.column().classes('flex-1 ml-64 p-8 gap-0'):
            # Tabs for different components
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


if __name__ in {"__main__", "__mp_main__"}:
    main()
    ui.run(
        title='shadcn-nicegui Components',
        favicon='⚡',
        dark=False,
        reload=False,
        port=8083
    )
