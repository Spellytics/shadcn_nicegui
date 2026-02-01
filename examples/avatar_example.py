"""Example showing avatar components in shadcn-nicegui."""
from nicegui import ui
from shadcn_nicegui import (
    shadcn_avatar,
    shadcn_card,
    shadcn_heading,
    shadcn_badge,
)


@ui.page('/')
def index():
    with shadcn_card(width='w-full max-w-4xl', margin='mx-auto mt-8'):
        shadcn_heading('Avatar Component Demo', level=1)

        ui.separator().classes('my-6')

        # Avatar with fallback text - different sizes
        shadcn_heading('Different Sizes', level=2)
        with ui.row().classes('gap-4 items-center mt-4'):
            shadcn_avatar(fallback_text='SM', size='sm')
            shadcn_avatar(fallback_text='MD', size='md')
            shadcn_avatar(fallback_text='LG', size='lg')
            shadcn_avatar(fallback_text='XL', size='xl')

        ui.separator().classes('my-6')

        # Avatar with initials
        shadcn_heading('User Initials', level=2)
        with ui.row().classes('gap-4 mt-4'):
            shadcn_avatar(fallback_text='JD', size='lg')
            shadcn_avatar(fallback_text='AB', size='lg')
            shadcn_avatar(fallback_text='MK', size='lg')
            shadcn_avatar(fallback_text='SP', size='lg')

        ui.separator().classes('my-6')

        # Avatar shapes
        shadcn_heading('Shapes', level=2)
        with ui.row().classes('gap-4 items-center mt-4'):
            with ui.column().classes('gap-2 items-center'):
                shadcn_avatar(fallback_text='JD', size='lg', variant='circle')
                shadcn_badge('Circle', variant='secondary')

            with ui.column().classes('gap-2 items-center'):
                shadcn_avatar(fallback_text='JD', size='lg', variant='square')
                shadcn_badge('Square', variant='secondary')

        ui.separator().classes('my-6')

        # Avatar with images
        shadcn_heading('With Images', level=2)
        ui.label('Using placeholder images from picsum.photos').classes('text-sm text-slate-600 mt-2')
        with ui.row().classes('gap-4 mt-4'):
            shadcn_avatar(
                image_url='https://picsum.photos/seed/user1/200',
                size='sm'
            )
            shadcn_avatar(
                image_url='https://picsum.photos/seed/user2/200',
                size='md'
            )
            shadcn_avatar(
                image_url='https://picsum.photos/seed/user3/200',
                size='lg'
            )
            shadcn_avatar(
                image_url='https://picsum.photos/seed/user4/200',
                size='xl'
            )

        ui.separator().classes('my-6')

        # User profile example
        shadcn_heading('Profile Example', level=2)
        with ui.row().classes('gap-4 items-center mt-4'):
            shadcn_avatar(fallback_text='JD', size='xl')
            with ui.column().classes('gap-1'):
                ui.label('John Doe').classes('text-xl font-semibold text-slate-900')
                ui.label('john.doe@example.com').classes('text-sm text-slate-600')
                shadcn_badge('Premium User', variant='success')


if __name__ in {"__main__", "__mp_main__"}:
    ui.run()
