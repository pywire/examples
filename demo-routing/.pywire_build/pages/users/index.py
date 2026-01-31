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
_LayoutBase = load_layout('/Users/rholmdahl/projects/pywire-workspace/examples/demo-routing/src/pages/users/__layout__.wire', '/Users/rholmdahl/projects/pywire-workspace/examples/demo-routing/src/pages/users/index.wire')

class IndexPage(_LayoutBase):
    __spa_enabled__ = False
    __sibling_paths__ = []
    __file_path__ = '/Users/rholmdahl/projects/pywire-workspace/examples/demo-routing/src/pages/users/index.wire'

    def __init__(self, request, params, query, path=None, url=None, **kwargs):
        super().__init__(request, params, query, path, url, **kwargs)
        self._init_slots()

    async def _render_slot_fill_default_0ef6f917(self):
        parts = []
        import json
        from pywire.runtime.helpers import ensure_async_iterator
        attrs = {}
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
        parts.append('User List')
        parts.append('</h3>')
        parts.append('\n    ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<p')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('This page is located at ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<code')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('/users')
        parts.append('</code>')
        parts.append(' (handled by ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<code')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('users/index.wire')
        parts.append('</code>')
        parts.append(').')
        parts.append('</p>')
        parts.append('\n    ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<p')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('Select a user from the sidebar to see dynamic parameter routing in action.')
        parts.append('</p>')
        parts.append('\n')
        parts.append('</article>')
        parts.append('\n')
        return ''.join(parts)

    def _init_slots(self):
        if hasattr(super(), '_init_slots'):
            super()._init_slots()
        self.register_slot('0de2a51949e7118ca950edcc982a7756', 'default', self._render_slot_fill_default_0ef6f917)
    INIT_HOOKS = []
__page_class__ = IndexPage