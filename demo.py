"""Comprehensive demo showcasing all shadcn-nicegui components."""
from nicegui import ui
from shadcn_nicegui import (
    button,
    input,
    select,
    heading,
    card,
    expandable,
    accordion,
    table,
    dialog,
    badge,
    avatar,
    separator,
    calendar,
    barchart,
    timeseries,
    set_global_font,
)


def main():
    """Main demo page."""

    # Set a nice font
    set_global_font('Inter, system-ui, -apple-system, sans-serif')

    @ui.page('/')
    def index():
        # Navigation Bar
        with ui.row().classes('w-full border-b border-slate-200 bg-white px-8 py-4 items-center justify-between sticky top-0 z-50'):
            with ui.row().classes('items-center gap-2'):
                ui.label('shadcn/nicegui').classes('text-lg font-semibold')

            with ui.row().classes('gap-6 items-center'):
                ui.link('Components', '#components').classes('text-sm text-slate-600 hover:text-slate-900 no-underline')
                ui.link('Examples', '#examples').classes('text-sm text-slate-600 hover:text-slate-900 no-underline')
                ui.link('GitHub', 'https://github.com/Spellytics/shadcn_nicegui', new_tab=True).classes('text-sm text-slate-600 hover:text-slate-900 no-underline')

        # Hero Section
        with ui.column().classes('w-full max-w-5xl mx-auto px-8 py-24 items-center text-center gap-6'):
            badge('v0.2.0', variant='outline')

            ui.label('Build your component library.').classes('text-5xl font-bold tracking-tight')

            ui.label('Beautifully designed components built with NiceGUI and Tailwind CSS. Copy, paste, and customize.').classes('text-xl text-slate-600 max-w-2xl')

            with ui.row().classes('gap-4 mt-4'):
                button('Get Started', variant='default', size='lg', on_click=lambda: ui.notify('Ready to build! 🚀'))
                ui.link('GitHub', 'https://github.com/Spellytics/shadcn_nicegui', new_tab=True).classes('inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors h-11 px-8 border border-slate-300 bg-white hover:bg-slate-100 hover:text-slate-900 text-black no-underline')

        # Features Section
        with ui.column().classes('w-full bg-slate-50 border-y border-slate-200'):
            with ui.column().classes('w-full max-w-5xl mx-auto px-8 py-16 gap-12'):
                with ui.row().classes('w-full gap-8 justify-between flex-wrap'):
                    with ui.column().classes('flex-1 min-w-[250px] gap-2'):
                        ui.label('Accessible').classes('text-lg font-semibold')
                        ui.label('Built with accessibility in mind. Keyboard navigation and screen reader support.').classes('text-sm text-slate-600')

                    with ui.column().classes('flex-1 min-w-[250px] gap-2'):
                        ui.label('Customizable').classes('text-lg font-semibold')
                        ui.label('Easily customize components with Tailwind CSS utility classes.').classes('text-sm text-slate-600')

                    with ui.column().classes('flex-1 min-w-[250px] gap-2'):
                        ui.label('Open Source').classes('text-lg font-semibold')
                        ui.label('Free and open source. Use it however you like.').classes('text-sm text-slate-600')

        # Main content
        with ui.column().classes('w-full max-w-5xl mx-auto px-8 py-16 gap-24'):
            with card(width='w-full', padding='p-8'):
                heading('Buttons', level=2)
                ui.label('Different button variants and sizes').classes('text-slate-600 mt-2')

                separator(additional_classes='my-4')

                ui.label('Variants').classes('font-semibold text-sm text-slate-900 mt-4')
                with ui.row().classes('gap-2 mt-2 flex-wrap'):
                    button('Default', variant='default', on_click=lambda: ui.notify('Default clicked!'))
                    button('Destructive', variant='destructive', on_click=lambda: ui.notify('Destructive clicked!', type='negative'))
                    button('Outline', variant='outline', on_click=lambda: ui.notify('Outline clicked!'))
                    button('Secondary', variant='secondary', on_click=lambda: ui.notify('Secondary clicked!'))
                    button('Ghost', variant='ghost', on_click=lambda: ui.notify('Ghost clicked!'))

                ui.label('Sizes').classes('font-semibold text-sm text-slate-900 mt-6')
                with ui.row().classes('gap-2 mt-2 items-center flex-wrap'):
                    button('Small', variant='default', size='sm')
                    button('Default', variant='default', size='default')
                    button('Large', variant='default', size='lg')

# Input Examples
            with ui.column().classes('w-full gap-6 mt-16'):
                with ui.row().classes('w-full items-center justify-between'):
                    with ui.column().classes('gap-1'):
                        ui.label('Input').classes('text-2xl font-semibold')
                        ui.label('A form input field for text entry.').classes('text-sm text-slate-600')

                with card(width='w-full', padding='p-8', additional_classes='border border-slate-200'):
                    with ui.column().classes('gap-4 max-w-sm'):
                        input(label='Email', placeholder='Email')
                        input(label='Password', placeholder='Password')

            # Card Variants Section
            with ui.column().classes('w-full gap-6 mt-16'):
                with ui.row().classes('w-full items-center justify-between'):
                    with ui.column().classes('gap-1'):
                        ui.label('Card').classes('text-2xl font-semibold')
                        ui.label('Displays content in a contained box with optional variants.').classes('text-sm text-slate-600')

                with ui.row().classes('w-full gap-4 flex-wrap'):
                    with card(width='w-64', padding='p-6', variant='default'):
                        ui.label('Default').classes('text-lg font-semibold')
                        ui.label('Subtle shadow with white background').classes('text-sm text-slate-600 mt-2')

                    with card(width='w-64', padding='p-6', variant='outlined'):
                        ui.label('Outlined').classes('text-lg font-semibold')
                        ui.label('Border with no shadow').classes('text-sm text-slate-600 mt-2')

                    with card(width='w-64', padding='p-6', variant='elevated'):
                        ui.label('Elevated').classes('text-lg font-semibold')
                        ui.label('Prominent shadow for emphasis').classes('text-sm text-slate-600 mt-2')

                    with card(width='w-64', padding='p-6', variant='ghost'):
                        ui.label('Ghost').classes('text-lg font-semibold')
                        ui.label('Minimal styling, no shadow').classes('text-sm text-slate-600 mt-2')

            # Badges & Avatars Section
            with card(width='w-full', padding='p-8'):
                heading('Badges & Avatars', level=2)
                ui.label('Status indicators and user avatars').classes('text-slate-600 mt-2')
# Badge Examples
            with ui.column().classes('w-full gap-6 mt-16'):
                with ui.row().classes('w-full items-center justify-between'):
                    with ui.column().classes('gap-1'):
                        ui.label('Badge').classes('text-2xl font-semibold')
                        ui.label('Displays a badge or a component that looks like a badge.').classes('text-sm text-slate-600')

                with card(width='w-full', padding='p-8', additional_classes='border border-slate-200'):
                    with ui.row().classes('gap-2 flex-wrap'):
                        badge('Default', variant='default')
                        badge('Secondary', variant='secondary')
                        badge('Outline', variant='outline')
                        badge('Destructive', variant='destructive')

            # Avatar Examples
            with ui.column().classes('w-full gap-6 mt-16'):
                with ui.row().classes('w-full items-center justify-between'):
                    with ui.column().classes('gap-1'):
                        ui.label('Avatar').classes('text-2xl font-semibold')
                        ui.label('An image element with a fallback for representing the user.').classes('text-sm text-slate-600')

                with card(width='w-full', padding='p-8', additional_classes='border border-slate-200'):
                    with ui.row().classes('gap-4 items-center flex-wrap'):
                        avatar(image_url='https://picsum.photos/seed/demo1/200', size='lg')
                        avatar(fallback_text='AB', size='lg')
                        avatar(fallback_text='CD', size='lg', variant='square')
                ui.label('Modal dialogs for confirmations and forms').classes('text-slate-600 mt-2')

                separator(additional_classes='my-4')
# Accordion Examples
            with ui.column().classes('w-full gap-6 mt-16'):
                with ui.row().classes('w-full items-center justify-between'):
                    with ui.column().classes('gap-1'):
                        ui.label('Accordion').classes('text-2xl font-semibold')
                        ui.label('A vertically stacked set of interactive headings that reveal content.').classes('text-sm text-slate-600')

                with card(width='w-full', padding='p-8', additional_classes='border border-slate-200'):
                    accordion([
                        {
                            'title': 'Is it accessible?',
                            'content': 'Yes. It adheres to the WAI-ARIA design pattern.'
                        },
                        {
                            'title': 'Is it styled?',
                            'content': 'Yes. It comes with default styles that match the shadcn design system.'
                        },
                        {
                            'title': 'Is it animated?',
                            'content': 'Yes. It\'s animated by default, but you can disable it if you prefer.'
                        },
                    ], variant='default')

# Dialog Examples
            with ui.column().classes('w-full gap-6 mt-16'):
                with ui.row().classes('w-full items-center justify-between'):
                    with ui.column().classes('gap-1'):
                        ui.label('Dialog').classes('text-2xl font-semibold')
                        ui.label('A window overlaid on either the primary window or another dialog.').classes('text-sm text-slate-600')

                with card(width='w-full', padding='p-8', additional_classes='border border-slate-200'):
                    def show_dialog():
                        with dialog(title='Are you absolutely sure?') as d:
                            ui.label('This action cannot be undone. This will permanently delete your account and remove your data from our servers.').classes('text-sm text-slate-600')
                            with ui.row().classes('gap-2 mt-6 justify-end'):
                                button('Cancel', on_click=d.close, variant='outline')
                                button('Continue', on_click=lambda: (ui.notify('Action confirmed', type='positive'), d.close()), variant='default')
                            d.open()

                    button('Open Dialog', variant='outline', on_click=show_dialog)
# Table Examples
            with ui.column().classes('w-full gap-6 mt-16'):
                with ui.row().classes('w-full items-center justify-between'):
                    with ui.column().classes('gap-1'):
                        ui.label('Table').classes('text-2xl font-semibold')
                        ui.label('A responsive table component.').classes('text-sm text-slate-600')

                with card(width='w-full', padding='p-8', additional_classes='border border-slate-200'):
                    columns = [
                        {'name': 'name', 'label': 'Name', 'field': 'name', 'align': 'left'},
                        {'name': 'email', 'label': 'Email', 'field': 'email', 'align': 'left'},
                        {'name': 'role', 'label': 'Role', 'field': 'role', 'align': 'left'},
                    ]

                    rows = [
                        {'id': 1, 'name': 'John Doe', 'email': 'john@example.com', 'role': 'Admin'},
                        {'id': 2, 'name': 'Jane Smith', 'email': 'jane@example.com', 'role': 'User'},
                        {'id': 3, 'name': 'Bob Johnson', 'email': 'bob@example.com', 'role': 'User'},
                    ]

                    table(columns=columns, rows=rows)

        # Footer
        with ui.column().classes('w-full border-t border-slate-200 bg-slate-50 mt-24'):
            with ui.column().classes('w-full max-w-5xl mx-auto px-8 py-16 gap-8'):
                with ui.row().classes('w-full justify-between flex-wrap gap-8'):
                    with ui.column().classes('gap-4 flex-1 min-w-[200px]'):
                        ui.label('shadcn/nicegui').classes('font-semibold text-lg')
                        ui.label('Beautiful components for NiceGUI.').classes('text-sm text-slate-600')

                    with ui.column().classes('gap-3 min-w-[150px]'):
                        ui.label('Resources').classes('font-semibold text-sm')
                        ui.link('Documentation', '#docs').classes('text-sm text-slate-600 hover:text-slate-900 no-underline')
                        ui.link('Components', '#components').classes('text-sm text-slate-600 hover:text-slate-900 no-underline')
                        ui.link('Examples', '#examples').classes('text-sm text-slate-600 hover:text-slate-900 no-underline')

                    with ui.column().classes('gap-3 min-w-[150px]'):
                        ui.label('Community').classes('font-semibold text-sm')
                        ui.link('GitHub', 'https://github.com/Spellytics/shadcn_nicegui', new_tab=True).classes('text-sm text-slate-600 hover:text-slate-900 no-underline')
                        ui.link('Issues', 'https://github.com/Spellytics/shadcn_nicegui/issues', new_tab=True).classes('text-sm text-slate-600 hover:text-slate-900 no-underline')

                separator()

                with ui.row().classes('w-full justify-between items-center'):
                    ui.label('© 2026 shadcn/nicegui. MIT License.').classes('text-sm text-slate-600')
                    with ui.row().classes('gap-2 items-center'):
                        ui.label('Built with').classes('text-sm text-slate-600')
                        badge('NiceGUI', variant='outline')
                        ui.label('and').classes('text-sm text-slate-600')
                        badge('Tailwind', variant='outline')

    ui.run(
        title='Shadcn NiceGUI Demo',
        favicon='⚡',
        dark=False,
        reload=False,
        port=8081
    )


if __name__ in {"__main__", "__mp_main__"}:
    main()