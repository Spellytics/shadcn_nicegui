"""Example showing font configuration in shadcn-nicegui."""
from nicegui import ui
from shadcn_nicegui import (
    shadcn_button,
    shadcn_card,
    shadcn_input,
    shadcn_heading,
    shadcn_badge,
    set_global_font,
)


@ui.page('/')
def index():
    # Set global font for all components
    set_global_font('Roboto, sans-serif')

    with shadcn_card(width='w-full max-w-4xl', margin='mx-auto mt-8'):
        shadcn_heading('Font Configuration Demo', level=1)

        ui.separator().classes('my-6')

        # Components using global font (Roboto)
        shadcn_heading('Using Global Font (Roboto)', level=2)
        shadcn_badge('Global Font', variant='default')
        shadcn_input(label='Name', placeholder='This uses Roboto font')
        shadcn_button('Button with Roboto', variant='default')

        ui.separator().classes('my-6')

        # Components with custom font override
        shadcn_heading('Custom Font Override', level=2)
        shadcn_heading('This uses Courier', level=3, font_family='Courier New, monospace')
        shadcn_badge('Monospace', variant='secondary', font_family='Courier New, monospace')
        shadcn_input(label='Code', placeholder='Monospace input', font_family='Courier New, monospace')
        shadcn_button('Monospace Button', variant='outline', font_family='Courier New, monospace')

        ui.separator().classes('my-6')

        # Change global font dynamically
        shadcn_heading('Change Font Dynamically', level=2)

        def change_to_serif():
            set_global_font('Georgia, serif')
            ui.notify('Font changed to Georgia (serif)')

        def change_to_sans():
            set_global_font('Arial, sans-serif')
            ui.notify('Font changed to Arial (sans-serif)')

        def change_to_mono():
            set_global_font('Courier New, monospace')
            ui.notify('Font changed to Courier New (monospace)')

        with ui.row().classes('gap-2'):
            shadcn_button('Serif Font', on_click=change_to_serif, variant='default')
            shadcn_button('Sans-Serif Font', on_click=change_to_sans, variant='secondary')
            shadcn_button('Monospace Font', on_click=change_to_mono, variant='outline')


if __name__ in {"__main__", "__mp_main__"}:
    ui.run()
