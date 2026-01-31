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
_LayoutBase = load_layout('/Users/rholmdahl/projects/pywire-workspace/examples/demo-routing/src/pages/users/__layout__.wire', '/Users/rholmdahl/projects/pywire-workspace/examples/demo-routing/src/pages/users/[uid].wire')

class [uid]Page(_LayoutBase):
    __spa_enabled__ = False
    __sibling_paths__ = []
    __file_path__ = '/Users/rholmdahl/projects/pywire-workspace/examples/demo-routing/src/pages/users/[uid].wire'

    def __init__(self, request, params, query, path=None, url=None, **kwargs):
        super().__init__(request, params, query, path, url, **kwargs)
        self._init_slots()
        self.__top_level_init__()

    def __top_level_init__(self):
        print(f'users/{self.uid}.wire')
        print('hello world')

    async def _render_slot_fill_default_a36eaacb(self):
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
            parts.append('<h3')
            parts.append(render_attrs(attrs, None))
            parts.append('>')
            parts.append('User Profile')
            parts.append('</h3>')
            parts.append('\n    ')
            attrs = {}
            from pywire.runtime.helpers import render_attrs
            parts.append('<p')
            parts.append(render_attrs(attrs, None))
            parts.append('>')
            parts.append('Profile ID: ')
            attrs = {}
            from pywire.runtime.helpers import render_attrs
            parts.append('<mark')
            parts.append(render_attrs(attrs, None))
            parts.append('>')
            parts.append(str(unwrap_wire(self.uid)))
            parts.append('</mark>')
            parts.append('</p>')
            parts.append('\n    ')
            attrs = {}
            from pywire.runtime.helpers import render_attrs
            parts.append('<p')
            parts.append(render_attrs(attrs, None))
            parts.append('>')
            parts.append('This route is handled by ')
            attrs = {}
            from pywire.runtime.helpers import render_attrs
            parts.append('<code')
            parts.append(render_attrs(attrs, None))
            parts.append('>')
            parts.append('users/[uid].wire')
            parts.append('</code>')
            parts.append('.')
            parts.append('</p>')
            parts.append('\n')
            parts.append('</article>')
            return ''.join(parts)
        finally:
            reset_render_context(_render_token)

    def _init_slots(self):
        if hasattr(super(), '_init_slots'):
            super()._init_slots()
        self.register_slot('0de2a51949e7118ca950edcc982a7756', 'default', self._render_slot_fill_default_a36eaacb)
    __region_renderers__ = {'r1': '_render_region_r1'}
    INIT_HOOKS = []
__page_class__ = [uid]Page