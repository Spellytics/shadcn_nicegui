"""Example usage of the shadcn accordion component."""
from nicegui import ui
from shadcn_nicegui import accordion, heading, card

def main():
    with ui.column().classes('w-full max-w-2xl mx-auto p-8 gap-8'):
        heading('Accordion Component', level=1)

        # Default accordion
        with card(width='w-full', padding='p-6'):
            heading('Default Variant', level=3)
            ui.label('Items with bottom borders').classes('text-sm text-slate-600 mb-4')

            accordion([
                {
                    'title': 'Is it accessible?',
                    'content': 'Yes. It adheres to the WAI-ARIA design pattern and is keyboard navigable.'
                },
                {
                    'title': 'Is it styled?',
                    'content': 'Yes. It comes with default styles that you can customize with Tailwind CSS.'
                },
                {
                    'title': 'Is it animated?',
                    'content': 'Yes. The expansion and collapse is smoothly animated by NiceGUI.'
                },
            ], variant='default')

        # Bordered accordion
        with card(width='w-full', padding='p-6'):
            heading('Bordered Variant', level=3)
            ui.label('Each item has a border').classes('text-sm text-slate-600 mb-4')

            accordion([
                {
                    'title': 'What is NiceGUI?',
                    'content': 'NiceGUI is a Python web framework that lets you build browser-based UIs with Python.'
                },
                {
                    'title': 'What is Shadcn?',
                    'content': 'Shadcn UI is a collection of re-usable components built using Radix UI and Tailwind CSS.'
                },
                {
                    'title': 'Can I use it in production?',
                    'content': 'Yes! This component library is production-ready and follows best practices.'
                },
            ], variant='bordered')

        # Separated accordion
        with card(width='w-full', padding='p-6'):
            heading('Separated Variant', level=3)
            ui.label('Items are separated with spacing and shadows').classes('text-sm text-slate-600 mb-4')

            accordion([
                {
                    'title': 'Getting Started',
                    'content': 'Install the package with pip install shadcn-nicegui and import the components you need.'
                },
                {
                    'title': 'Customization',
                    'content': 'All components support additional Tailwind CSS classes for full customization.'
                },
                {
                    'title': 'Documentation',
                    'content': 'Check the README.md file for detailed documentation and examples.'
                },
            ], variant='separated')

        # FAQ Example
        with card(width='w-full', padding='p-6'):
            heading('FAQ Example', level=3)
            ui.label('A real-world use case').classes('text-sm text-slate-600 mb-4')

            accordion([
                {
                    'title': 'How do I install this package?',
                    'content': 'Run pip install shadcn-nicegui in your terminal. Make sure you have Python 3.8 or higher installed.'
                },
                {
                    'title': 'Can I customize the colors?',
                    'content': 'Yes! You can add additional Tailwind CSS classes or override styles. The components are built with customization in mind.'
                },
                {
                    'title': 'Does it work with FastAPI?',
                    'content': 'Yes! NiceGUI can be integrated with FastAPI, and these components work seamlessly in that setup.'
                },
                {
                    'title': 'Is there TypeScript support?',
                    'content': 'This is a Python library, but NiceGUI generates JavaScript/TypeScript compatible web applications.'
                },
                {
                    'title': 'How do I report bugs?',
                    'content': 'Please open an issue on the GitHub repository with a detailed description and reproduction steps.'
                },
            ], variant='default')

if __name__ in {"__main__", "__mp_main__"}:
    main()
    ui.run(port=8082, reload=False)
