"""Example demonstrating dark mode theme support."""
from nicegui import ui
from shadcn_nicegui import (
    button,
    input,
    card,
    badge,
    heading,
    separator,
    accordion,
    set_theme,
    set_global_font,
)


def main():
    """Main demo page with theme switching."""

    # Set font
    set_global_font('Inter, system-ui, -apple-system, sans-serif')

    # Start with light theme (default)
    current_theme = {'mode': 'light'}

    @ui.page('/')
    def index():
        def toggle_theme():
            """Toggle between light and dark themes."""
            if current_theme['mode'] == 'light':
                current_theme['mode'] = 'dark'
                set_theme('dark')
            else:
                current_theme['mode'] = 'light'
                set_theme('light')

            # Reload the page to apply theme
            ui.navigate.reload()

        # Apply current theme
        set_theme(current_theme['mode'])

        with ui.column().classes('w-full max-w-4xl mx-auto p-8 gap-8'):
            # Header with theme toggle
            with ui.row().classes('w-full justify-between items-center'):
                heading('Dark Mode Theme Demo', level=1)
                button(
                    f'Switch to {"Dark" if current_theme["mode"] == "light" else "Light"} Mode',
                    on_click=toggle_theme,
                    variant='outline'
                )

            separator()

            # Cards showcase
            heading('Cards', level=2)
            with ui.row().classes('w-full gap-4 flex-wrap'):
                card(
                    width='w-64',
                    padding='p-6',
                    variant='default',
                    title='Default Card',
                    subtitle='Standard style',
                    card_content='This card uses the default variant with theme colors.'
                )
                card(
                    width='w-64',
                    padding='p-6',
                    variant='elevated',
                    title='Elevated Card',
                    subtitle='With shadow',
                    card_content='This card has a shadow for emphasis.'
                )

            separator(additional_classes='my-6')

            # Buttons showcase
            heading('Buttons', level=2)
            with ui.row().classes('gap-2 flex-wrap'):
                button('Default', variant='default')
                button('Secondary', variant='secondary')
                button('Outline', variant='outline')
                button('Ghost', variant='ghost')
                button('Destructive', variant='destructive')

            separator(additional_classes='my-6')

            # Badges showcase
            heading('Badges', level=2)
            with ui.row().classes('gap-2 flex-wrap'):
                badge('Default', variant='default')
                badge('Secondary', variant='secondary')
                badge('Outline', variant='outline')
                badge('Success', variant='success')
                badge('Destructive', variant='destructive')

            separator(additional_classes='my-6')

            # Form inputs
            heading('Form Inputs', level=2)
            with card(width='w-full', padding='p-6'):
                with ui.column().classes('gap-4 max-w-md'):
                    input(label='Email', placeholder='Enter your email')
                    input(label='Password', placeholder='Enter your password')
                    button('Submit', variant='default')

            separator(additional_classes='my-6')

            # Accordion
            heading('Accordion', level=2)
            with card(width='w-full', padding='p-6'):
                accordion([
                    {
                        'title': 'What is dark mode?',
                        'content': 'Dark mode is a color scheme that uses light text on a dark background.'
                    },
                    {
                        'title': 'How to toggle themes?',
                        'content': 'Use the button at the top of the page to switch between light and dark modes.'
                    },
                    {
                        'title': 'Are all components supported?',
                        'content': 'Yes! All shadcn-nicegui components support both light and dark themes.'
                    },
                ], variant='default')

    ui.run(
        title='Dark Mode Demo',
        favicon='🌓',
        dark=False,  # NiceGUI dark mode (keep false, we handle theming ourselves)
        reload=True,
        port=8085
    )


if __name__ in {"__main__", "__mp_main__"}:
    main()
