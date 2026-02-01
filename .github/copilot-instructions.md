# Copilot Instructions for shadcn-nicegui

## Project Overview

This is a Python package providing Shadcn-style UI components for NiceGUI. The package enables developers to create beautiful, modern web interfaces using NiceGUI with Shadcn's design system.

## Development Workflow

Follow these steps **every time** when developing features or making changes:

### 1. Understanding the Request
- Read the user's request carefully
- Ask clarifying questions if the request is ambiguous
- Identify which components or files need to be modified

### 2. Code Implementation
- Make changes to `/shadcn_nicegui/components.py` for component logic
- Update `/shadcn_nicegui/__init__.py` if adding new exports
- Follow the existing code style and patterns
- Add type hints using `Optional`, `List`, `Dict` from `typing`
- Include comprehensive docstrings with Args sections

### 3. Testing Changes
- Create or update example files in `/examples/` directory
- Test imports: `python -c "from shadcn_nicegui import <component>"`
- Run example files to verify functionality
- Ensure the main guard uses: `if __name__ in {"__main__", "__mp_main__"}:`

### 4. Update Documentation
- Update `README.md` if adding new features or components
- Add usage examples for new components
- Update the "Available Components" list if adding new components

### 5. Package Building
- After significant changes, rebuild the package:
  ```bash
  python -m build
  ```
- Verify the build completes without errors (warnings are acceptable)

### 6. Version Management
- For breaking changes: increment major version (1.0.0)
- For new features: increment minor version (0.2.0)
- For bug fixes: increment patch version (0.1.1)
- Update version in both:
  - `/shadcn_nicegui/__init__.py`
  - `/pyproject.toml`

## Code Style Guidelines

### Component Structure
Every component should follow this pattern:

```python
def shadcn_component(
    required_param: str,
    optional_param: str = 'default',
    font_family: Optional[str] = None,
    additional_classes: Optional[List[str]] = None,
):
    """Brief description of the component.

    Args:
        required_param: Description of required parameter
        optional_param: Description with default value
        font_family: Optional custom font family (overrides global font)
        additional_classes: Optional list of additional Tailwind CSS classes

    Returns:
        The NiceGUI element created

    Example:
        component = shadcn_component('value')
    """
    # Get font configuration
    font = font_family or FontConfig.get_font()

    # Component implementation
    element = ui.element()
    element.style(f'font-family: {font}')

    return element
```

### Font Configuration
- All text-based components MUST support `font_family` parameter
- Always use: `font = font_family or FontConfig.get_font()`
- Apply font with: `element.style(f'font-family: {font}')`

### Tailwind CSS Classes
- Use Tailwind utility classes for styling
- Follow Shadcn's design tokens:
  - Colors: `slate-900`, `slate-50`, `red-500`, etc.
  - Spacing: `p-4`, `m-2`, `gap-4`, etc.
  - Typography: `text-sm`, `font-medium`, `text-xl`, etc.

### Type Safety
- Import types: `from typing import List, Dict, Optional`
- Use type hints for all parameters
- Use `Optional[type]` for parameters that can be `None`

## File Organization

```
shadcn_nicegui/
├── shadcn_nicegui/          # Main package
│   ├── __init__.py          # Package exports and version
│   └── components.py        # All component implementations
├── examples/                # Example usage files
│   ├── example.py          # Basic component showcase
│   ├── font_example.py     # Font configuration demo
│   └── test_import.py      # Import testing
├── dist/                    # Built distributions (created by build)
├── pyproject.toml          # Package configuration
├── README.md               # User documentation
├── LICENSE                 # MIT License
└── .github/
    └── copilot-instructions.md  # This file
```

## Component Checklist

When adding a new component, ensure:

- [ ] Component function is defined in `components.py`
- [ ] Component is exported in `__init__.py`
- [ ] Component is added to `__all__` list in `__init__.py`
- [ ] Component has comprehensive docstring with Args section
- [ ] Component supports `font_family` parameter (if text-based)
- [ ] Component follows Shadcn design patterns
- [ ] Example usage is added to `README.md`
- [ ] Example file demonstrates the component
- [ ] Component is tested and working

## Common Tasks

### Adding a New Component

1. Add function to `/shadcn_nicegui/components.py`
2. Export in `/shadcn_nicegui/__init__.py`:
   ```python
   from .components import (
       # ... existing imports
       new_component,
   )

   __all__ = [
       # ... existing exports
       "new_component",
   ]
   ```
3. Add to README.md component list
4. Create usage example
5. Test thoroughly

### Modifying Existing Components

1. Update function in `components.py`
2. Test with existing examples
3. Update documentation if behavior changed
4. Increment patch version

### Font Configuration Updates

1. Modify `FontConfig` class if needed
2. Update `set_global_font()` function
3. Ensure all components respect font settings
4. Update font examples

## Testing Strategy

### Manual Testing
```bash
# Test imports
python -c "from shadcn_nicegui import shadcn_button, set_global_font; print('✓ Imports work')"

# Run basic example
python examples/example.py

# Run font example
python examples/font_example.py
```

### Building Package
```bash
# Clean previous builds
rm -rf dist/ build/ *.egg-info

# Build new distributions
python -m build

# Verify build output
ls dist/
```

## Package Publication Workflow

### Before Publishing

1. Update version numbers
2. Update CHANGELOG (if exists)
3. Test all examples
4. Rebuild package: `python -m build`
5. Update `pyproject.toml` with correct author info

### Publishing to PyPI

```bash
# Test on TestPyPI first (optional)
twine upload --repository testpypi dist/*

# Publish to PyPI
twine upload dist/*
```

### After Publishing

1. Tag release in git: `git tag v0.1.0`
2. Push tags: `git push --tags`
3. Create GitHub release with changelog
4. Announce on relevant forums/communities

## Common Issues & Solutions

### Issue: Components not importing
**Solution**: Ensure component is in `__all__` list in `__init__.py`

### Issue: Font not applying
**Solution**: Check that `FontConfig.get_font()` is called and style is applied

### Issue: Build warnings about license
**Solution**: These are deprecation warnings and don't affect functionality. They can be ignored for now.

### Issue: NiceGUI multiprocessing error
**Solution**: Use `if __name__ in {"__main__", "__mp_main__"}:` instead of `if __name__ == "__main__":`

### Issue: Tailwind classes not working
**Solution**: Ensure NiceGUI is configured to use Tailwind (it is by default)

## Design Principles

1. **Consistency**: Follow Shadcn's design patterns and naming
2. **Flexibility**: Allow customization through parameters
3. **Simplicity**: Keep component APIs simple and intuitive
4. **Documentation**: Always include clear docstrings and examples
5. **Type Safety**: Use type hints for better IDE support
6. **Font Control**: All text components support font configuration

## Communication Style

- Be concise and direct
- Provide working code, not just suggestions
- Show examples for complex features
- Explain *why* when making architectural decisions
- Use markdown formatting for clarity
- Link to files using relative paths

## Remember

- **Always test after making changes**
- **Update documentation when adding features**
- **Follow the workflow steps in order**
- **Ask questions before making assumptions**
- **Keep code DRY (Don't Repeat Yourself)**
- **Maintain backward compatibility when possible**