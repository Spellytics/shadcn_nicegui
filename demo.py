"""Comprehensive demo showcasing all shadcn-nicegui components."""
from nicegui import ui
from shadcn_nicegui import (
    button,
    input,
    select,
    heading,
    card,
    expandable,
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
        # Header
        with ui.row().classes('w-full bg-slate-900 p-6 items-center justify-between'):
            with ui.row().classes('items-center gap-4'):
                ui.label('⚡').classes('text-4xl')
                with ui.column().classes('gap-0'):
                    ui.label('Shadcn NiceGUI').classes('text-2xl font-bold text-white')
                    ui.label('Beautiful UI components for NiceGUI').classes('text-sm text-slate-300')
            
            with ui.row().classes('gap-2'):
                badge('v0.2.0', variant='secondary')
                badge('Open Source', variant='success')
        
        # Main content
        with ui.column().classes('w-full max-w-7xl mx-auto p-8 gap-8'):
            
            # Introduction
            with card(width='w-full', padding='p-8'):
                heading('Welcome to Shadcn NiceGUI', level=1)
                ui.label('A collection of beautiful Shadcn-style UI components built for NiceGUI. Clean, modern, and easy to use.').classes('text-lg text-slate-600 mt-2')
                
                separator(additional_classes='my-6')
                
                with ui.row().classes('gap-2'):
                    button('Get Started', variant='default', on_click=lambda: ui.notify('Ready to build! 🚀'))
                    ui.link('View on GitHub', 'https://github.com/Spellytics/shadcn_nicegui', new_tab=True).classes('inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 h-10 px-4 py-2 border border-slate-300 bg-white hover:bg-slate-100 hover:text-slate-900 text-black no-underline')
            
            # Buttons Section
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
            
            # Form Inputs Section
            with card(width='w-full', padding='p-8'):
                heading('Form Inputs', level=2)
                ui.label('Text inputs and selects with labels').classes('text-slate-600 mt-2')
                
                separator(additional_classes='my-4')
                
                with ui.column().classes('gap-4 max-w-md mt-4'):
                    input(label='Name', placeholder='Enter your name')
                    input(label='Email', placeholder='you@example.com')
                    select(['Option 1', 'Option 2', 'Option 3'], label='Select an option', value='Option 1')
                    
                    with ui.row().classes('gap-2'):
                        button('Submit', variant='default')
                        button('Cancel', variant='outline')
            
            # Badges & Avatars Section
            with card(width='w-full', padding='p-8'):
                heading('Badges & Avatars', level=2)
                ui.label('Status indicators and user avatars').classes('text-slate-600 mt-2')
                
                separator(additional_classes='my-4')
                
                ui.label('Badge Variants').classes('font-semibold text-sm text-slate-900 mt-4')
                with ui.row().classes('gap-2 mt-2 flex-wrap'):
                    badge('Default', variant='default')
                    badge('Secondary', variant='secondary')
                    badge('Success', variant='success')
                    badge('Destructive', variant='destructive')
                    badge('Outline', variant='outline')
                
                ui.label('Avatars').classes('font-semibold text-sm text-slate-900 mt-6')
                with ui.row().classes('gap-4 mt-2 items-center flex-wrap'):
                    avatar(fallback_text='JD', size='sm')
                    avatar(fallback_text='AB', size='md')
                    avatar(fallback_text='MK', size='lg')
                    avatar(fallback_text='SP', size='xl')
                
                ui.label('With Images').classes('font-semibold text-sm text-slate-900 mt-6')
                with ui.row().classes('gap-4 mt-2 flex-wrap'):
                    avatar(image_url='https://picsum.photos/seed/demo1/200', size='md')
                    avatar(image_url='https://picsum.photos/seed/demo2/200', size='md')
                    avatar(image_url='https://picsum.photos/seed/demo3/200', size='md')
                    avatar(fallback_text='JD', size='md', variant='square')
            
            # Dialog Section
            with card(width='w-full', padding='p-8'):
                heading('Dialogs', level=2)
                ui.label('Modal dialogs for confirmations and forms').classes('text-slate-600 mt-2')
                
                separator(additional_classes='my-4')
                
                def show_dialog():
                    with dialog(title='Confirm Action') as d:
                        ui.label('Are you sure you want to proceed with this action?').classes('text-slate-700')
                        with ui.row().classes('gap-2 mt-4 justify-end'):
                            button('Cancel', on_click=d.close, variant='outline')
                            button('Confirm', on_click=lambda: (ui.notify('Confirmed!', type='positive'), d.close()), variant='default')
                        d.open()
                
                button('Open Dialog', variant='default', on_click=show_dialog)
            
            # Table Section
            with card(width='w-full', padding='p-8'):
                heading('Data Table', level=2)
                ui.label('Display structured data in tables').classes('text-slate-600 mt-2')
                
                separator(additional_classes='my-4')
                
                columns = [
                    {'name': 'id', 'label': 'ID', 'field': 'id', 'align': 'left'},
                    {'name': 'name', 'label': 'Name', 'field': 'name', 'align': 'left'},
                    {'name': 'email', 'label': 'Email', 'field': 'email', 'align': 'left'},
                    {'name': 'role', 'label': 'Role', 'field': 'role', 'align': 'left'},
                ]
                
                rows = [
                    {'id': 1, 'name': 'John Doe', 'email': 'john@example.com', 'role': 'Admin'},
                    {'id': 2, 'name': 'Jane Smith', 'email': 'jane@example.com', 'role': 'User'},
                    {'id': 3, 'name': 'Bob Johnson', 'email': 'bob@example.com', 'role': 'User'},
                    {'id': 4, 'name': 'Alice Williams', 'email': 'alice@example.com', 'role': 'Manager'},
                ]
                
                table(columns=columns, rows=rows)
            
            # Expandable Section
            with card(width='w-full', padding='p-8'):
                heading('Expandable Sections', level=2)
                ui.label('Accordion-style collapsible content').classes('text-slate-600 mt-2')
                
                separator(additional_classes='my-4')
                
                with expandable('Getting Started', width='w-full'):
                    ui.label('Install the package with pip install shadcn-nicegui and start building beautiful UIs!')
                
                with expandable('Features', width='w-full'):
                    ui.label('• Beautiful Shadcn-style design\n• Easy to use API\n• Fully customizable\n• Font configuration support').classes('whitespace-pre-line')
                
                with expandable('Documentation', width='w-full'):
                    ui.label('Check out the README.md for full documentation and examples.')
            
            # Charts Section
            with card(width='w-full', padding='p-8'):
                heading('Charts', level=2)
                ui.label('Beautiful data visualizations with Plotly').classes('text-slate-600 mt-2')
                
                separator(additional_classes='my-4')
                
                # Bar chart
                heading('Bar Chart', level=3)
                data = {'Mon': 12, 'Tue': 19, 'Wed': 15, 'Thu': 25, 'Fri': 22, 'Sat': 18, 'Sun': 10}
                barchart(data, title='Weekly Activity', height=300, label='Users')
                
                # Time series
                heading('Time Series', level=3)
                ui.label('').classes('mt-8')
                dates = ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06', '2024-01-07']
                values = [100, 150, 120, 180, 160, 200, 170]
                timeseries(dates, values, title='Daily Traffic', height=300, label='Visitors')
            
            # Calendar Section
            with card(width='w-full', padding='p-8'):
                heading('Date Picker', level=2)
                ui.label('Select dates with a beautiful calendar').classes('text-slate-600 mt-2')
                
                separator(additional_classes='my-4')
                
                calendar(on_change=lambda e: ui.notify(f'Selected: {e.value}'))
            
            # Footer
            separator(additional_classes='my-8')
            
            with ui.row().classes('w-full justify-center items-center gap-2 pb-8'):
                ui.label('Built with').classes('text-slate-600')
                ui.label('❤️').classes('text-red-500')
                ui.label('using').classes('text-slate-600')
                badge('NiceGUI', variant='secondary')
                ui.label('and').classes('text-slate-600')
                badge('Shadcn', variant='secondary')
    
    ui.run(
        title='Shadcn NiceGUI Demo',
        favicon='⚡',
        dark=False,
        reload=False
    )


if __name__ in {"__main__", "__mp_main__"}:
    main()
