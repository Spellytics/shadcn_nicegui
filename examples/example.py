"""Example usage of shadcn-nicegui components."""
from nicegui import ui
from shadcn_nicegui import (
    button,
    card,
    input,
    select,
    heading,
    badge,
    barchart,
)


def main():
    """Run the example app."""

    @ui.page('/')
    def index():
        with card(width='w-full max-w-4xl', margin='mx-auto mt-8'):
            heading('Shadcn NiceGUI Components', level=1)

            with ui.row().classes('gap-4 mt-6'):
                badge('Example', variant='default')
                badge('v0.1.0', variant='secondary')

            ui.separator().classes('my-6')

            # Buttons section
            heading('Buttons', level=2)
            with ui.row().classes('gap-2 mt-4'):
                button('Default', variant='default')
                button('Destructive', variant='destructive')
                button('Outline', variant='outline')
                button('Ghost', variant='ghost')
                button('Secondary', variant='secondary')

            ui.separator().classes('my-6')

            # Form section
            heading('Form Inputs', level=2)
            with ui.column().classes('gap-4 mt-4 w-full'):
                input(label='Name', placeholder='Enter your name')
                select(['Option 1', 'Option 2', 'Option 3'], label='Select an option')

            ui.separator().classes('my-6')

            # Chart section
            heading('Charts', level=2)
            data = {'Mon': 10, 'Tue': 25, 'Wed': 15, 'Thu': 30, 'Fri': 20}
            barchart(data, title='Weekly Activity', height=300)

    ui.run()


if __name__ in {"__main__", "__mp_main__"}:
    main()
