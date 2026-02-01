"""Example usage of shadcn-nicegui components."""
from nicegui import ui
from shadcn_nicegui import (
    shadcn_button,
    shadcn_card,
    shadcn_input,
    shadcn_select,
    shadcn_heading,
    shadcn_badge,
    shadcn_barchart,
)


def main():
    """Run the example app."""

    @ui.page('/')
    def index():
        with shadcn_card(width='w-full max-w-4xl', margin='mx-auto mt-8'):
            shadcn_heading('Shadcn NiceGUI Components', level=1)

            with ui.row().classes('gap-4 mt-6'):
                shadcn_badge('Example', variant='default')
                shadcn_badge('v0.1.0', variant='secondary')

            ui.separator().classes('my-6')

            # Buttons section
            shadcn_heading('Buttons', level=2)
            with ui.row().classes('gap-2 mt-4'):
                shadcn_button('Default', variant='default')
                shadcn_button('Destructive', variant='destructive')
                shadcn_button('Outline', variant='outline')
                shadcn_button('Ghost', variant='ghost')
                shadcn_button('Secondary', variant='secondary')

            ui.separator().classes('my-6')

            # Form section
            shadcn_heading('Form Inputs', level=2)
            with ui.column().classes('gap-4 mt-4 w-full'):
                shadcn_input(label='Name', placeholder='Enter your name')
                shadcn_select(['Option 1', 'Option 2', 'Option 3'], label='Select an option')

            ui.separator().classes('my-6')

            # Chart section
            shadcn_heading('Charts', level=2)
            data = {'Mon': 10, 'Tue': 25, 'Wed': 15, 'Thu': 30, 'Fri': 20}
            shadcn_barchart(data, title='Weekly Activity', height=300)

    ui.run()


if __name__ in {"__main__", "__mp_main__"}:
    main()
