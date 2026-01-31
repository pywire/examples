from pywire.runtime.page import BasePage
from pywire.core.wire import wire
from starlette.responses import Response
import json
from pywire.runtime.validation import form_validator, FieldRules, FormValidationSchema
from pywire.runtime.pydantic_integration import validate_with_model
from pywire.runtime.loader import load_component
from pywire.runtime.helpers import unwrap_wire, set_render_context, reset_render_context
import asyncio
from pywire.runtime.loader import load_layout
_LayoutBase = load_layout('/Users/rholmdahl/projects/pywire-workspace/examples/demo-routing/src/pages/__layout__.wire', '/Users/rholmdahl/projects/pywire-workspace/examples/demo-routing/src/pages/__error__.wire')

class ErrorPage(_LayoutBase):
    __spa_enabled__ = False
    __sibling_paths__ = []
    __file_path__ = '/Users/rholmdahl/projects/pywire-workspace/examples/demo-routing/src/pages/__error__.wire'

    def __init__(self, request, params, query, path=None, url=None, **kwargs):
        super().__init__(request, params, query, path, url, **kwargs)
        self._init_slots()
        self.__top_level_init__()

    def __top_level_init__(self):
        match self.error_code:
            case 404:
                self.title = 'Page Not Found'
                self.message = "Oops! The page you're looking for doesn't exist."
                self.color = '#6366f1'
            case 500:
                self.title = 'Server Error'
                self.message = 'Something went wrong.'
                self.color = '#ef4444'
            case _:
                self.title = f'Error {self.error_code}'
                self.message = 'An unknown error occurred.'
                self.color = '#ef4444'

    async def _render_slot_fill_default_94c35b64(self):
        parts = []
        import json
        from pywire.runtime.helpers import ensure_async_iterator
        parts.append(await self._render_region_r1())
        return ''.join(parts)

    async def _render_region_r1(self):
        parts = []
        import json
        from pywire.runtime.helpers import ensure_async_iterator
        _render_token = set_render_context(self, 'r1')
        try:
            self._begin_region_render('r1')
            attrs = {}
            attrs['style'] = 'text-align: center; margin-top: 50px; font-family: system-ui, sans-serif;'
            attrs['data-pw-region'] = 'r1'
            from pywire.runtime.helpers import render_attrs
            parts.append('<div')
            parts.append(render_attrs(attrs, None))
            parts.append('>')
            parts.append('\n    ')
            attrs = {}
            attrs['style'] = 'font-size: 3rem; color: ' + str(self.color) + ';'
            from pywire.runtime.helpers import render_attrs
            parts.append('<h1')
            parts.append(render_attrs(attrs, None))
            parts.append('>')
            parts.append(str(unwrap_wire(self.error_code)))
            parts.append('</h1>')
            parts.append('\n    ')
            attrs = {}
            from pywire.runtime.helpers import render_attrs
            parts.append('<h2')
            parts.append(render_attrs(attrs, None))
            parts.append('>')
            parts.append(str(unwrap_wire(self.title)))
            parts.append('</h2>')
            parts.append('\n    ')
            attrs = {}
            from pywire.runtime.helpers import render_attrs
            parts.append('<p')
            parts.append(render_attrs(attrs, None))
            parts.append('>')
            parts.append(str(unwrap_wire(self.message)))
            parts.append('</p>')
            parts.append('\n    ')
            attrs = {}
            attrs['href'] = '/'
            attrs['style'] = 'color: #6366f1; text-decoration: none;'
            from pywire.runtime.helpers import render_attrs
            parts.append('<a')
            parts.append(render_attrs(attrs, None))
            parts.append('>')
            parts.append('← Go Home')
            parts.append('</a>')
            parts.append('\n')
            parts.append('</div>')
            return ''.join(parts)
        finally:
            reset_render_context(_render_token)

    def _init_slots(self):
        if hasattr(super(), '_init_slots'):
            super()._init_slots()
        self.register_slot('e410ff403da6504f406cea34551f715f', 'default', self._render_slot_fill_default_94c35b64)
    __region_renderers__ = {'r1': '_render_region_r1'}
    INIT_HOOKS = []
__page_class__ = ErrorPage