"""Example showing font configuration in shadcn-nicegui."""
from nicegui import ui
from shadcn_nicegui import (
    button,
    card,
    input,
    heading,
    badge,
    set_global_font,
)


@ui.page('/')
def index():
    # Set global font for all components
    set_global_font('Roboto, sans-serif')

    with card(width='w-full max-w-4xl', margin='mx-auto mt-8'):
        heading('Font Configuration Demo', level=1)

        ui.separator().classes('my-6')

        # Components using global font (Roboto)
        heading('Using Global Font (Roboto)', level=2)
        badge('Global Font', variant='default')
        input(label='Name', placeholder='This uses Roboto font')
        button('Button with Roboto', variant='default')

        ui.separator().classes('my-6')

        # Components with custom font override
        heading('Custom Font Override', level=2)
        heading('This uses Courier', level=3, font_family='Courier New, monospace')
        badge('Monospace', variant='secondary', font_family='Courier New, monospace')
        input(label='Code', placeholder='Monospace input', font_family='Courier New, monospace')
        button('Monospace Button', variant='outline', font_family='Courier New, monospace')

        ui.separator().classes('my-6')

        # Change global font dynamically
        heading('Change Font Dynamically', level=2)

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
            button('Serif Font', on_click=change_to_serif, variant='default')
            button('Sans-Serif Font', on_click=change_to_sans, variant='secondary')
            button('Monospace Font', on_click=change_to_mono, variant='outline')


if __name__ in {"__main__", "__mp_main__"}:
    ui.run()
