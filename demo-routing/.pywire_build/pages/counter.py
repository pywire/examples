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
_LayoutBase = load_layout('/Users/rholmdahl/projects/pywire-workspace/examples/demo-routing/src/pages/__layout__.wire', '/Users/rholmdahl/projects/pywire-workspace/examples/demo-routing/src/pages/counter.wire')

class CounterPage(_LayoutBase):
    __spa_enabled__ = False
    __sibling_paths__ = []
    __file_path__ = '/Users/rholmdahl/projects/pywire-workspace/examples/demo-routing/src/pages/counter.wire'

    def __init__(self, request, params, query, path=None, url=None, **kwargs):
        super().__init__(request, params, query, path, url, **kwargs)
        self._init_slots()
        self.__top_level_init__()

    def increment(self):
        """Increment the counter"""
        self.count.value += 1

    def __top_level_init__(self):
        self.count = wire(0)

    async def _render_slot_fill_default_12f28b86(self):
        parts = []
        import json
        from pywire.runtime.helpers import ensure_async_iterator
        parts.append(await self._render_region_r1())
        parts.append('\n')
        return ''.join(parts)

    async def _render_region_r1(self):
        parts = []
        import json
        from pywire.runtime.helpers import ensure_async_iterator
        _render_token = set_render_context(self, 'r1')
        try:
            self._begin_region_render('r1')
            attrs = {}
            attrs['data-pw-region'] = 'r1'
            from pywire.runtime.helpers import render_attrs
            parts.append('<article')
            parts.append(render_attrs(attrs, None))
            parts.append('>')
            parts.append('\n    ')
            attrs = {}
            from pywire.runtime.helpers import render_attrs
            parts.append('<h2')
            parts.append(render_attrs(attrs, None))
            parts.append('>')
            parts.append('Counter')
            parts.append('</h2>')
            parts.append('\n    ')
            attrs = {}
            from pywire.runtime.helpers import render_attrs
            parts.append('<p')
            parts.append(render_attrs(attrs, None))
            parts.append('>')
            parts.append('A simple counter component.')
            parts.append('</p>')
            parts.append('\n    ')
            attrs = {}
            attrs['data-on-click'] = 'increment'
            from pywire.runtime.helpers import render_attrs
            parts.append('<button')
            parts.append(render_attrs(attrs, None))
            parts.append('>')
            parts.append('Increment')
            parts.append('</button>')
            parts.append('\n    ')
            attrs = {}
            from pywire.runtime.helpers import render_attrs
            parts.append('<p')
            parts.append(render_attrs(attrs, None))
            parts.append('>')
            parts.append('Count: ')
            parts.append(str(unwrap_wire(self.count.value)))
            parts.append('</p>')
            parts.append('\n    ')
            attrs = {}
            from pywire.runtime.helpers import render_attrs
            parts.append('<p')
            parts.append(render_attrs(attrs, None))
            parts.append('>')
            parts.append('Count: ')
            parts.append(str(unwrap_wire(self.count.value)))
            parts.append('</p>')
            parts.append('\n')
            parts.append('</article>')
            return ''.join(parts)
        finally:
            reset_render_context(_render_token)

    def _init_slots(self):
        if hasattr(super(), '_init_slots'):
            super()._init_slots()
        self.register_slot('e410ff403da6504f406cea34551f715f', 'default', self._render_slot_fill_default_12f28b86)
    __region_renderers__ = {'r1': '_render_region_r1'}
    INIT_HOOKS = []
__page_class__ = CounterPage