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
_LayoutBase = load_layout('/Users/rholmdahl/projects/pywire-workspace/examples/demo-routing/src/pages/__layout__.wire', '/Users/rholmdahl/projects/pywire-workspace/examples/demo-routing/src/pages/about.wire')

class AboutPage(_LayoutBase):
    __spa_enabled__ = False
    __sibling_paths__ = []
    __file_path__ = '/Users/rholmdahl/projects/pywire-workspace/examples/demo-routing/src/pages/about.wire'

    def __init__(self, request, params, query, path=None, url=None, **kwargs):
        super().__init__(request, params, query, path, url, **kwargs)
        self._init_slots()

    async def _render_slot_fill_default_10694576(self):
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
        parts.append('<h2')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('About pywire')
        parts.append('</h2>')
        parts.append('\n    ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<p')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('pywire is a modern, reactive Python web framework that brings the development experience of modern JavaScript frameworks to the Python ecosystem.')
        parts.append('</p>')
        parts.append('\n    ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<p')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('It supports:')
        parts.append('</p>')
        parts.append('\n    ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<ul')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('\n        ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<li')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('Hot Reloading')
        parts.append('</li>')
        parts.append('\n        ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<li')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('File-based Routing')
        parts.append('</li>')
        parts.append('\n        ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<li')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('Server-side Rendering')
        parts.append('</li>')
        parts.append('\n        ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<li')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('Zero JS (unless you want it)')
        parts.append('</li>')
        parts.append('\n    ')
        parts.append('</ul>')
        parts.append('\n')
        parts.append('</article>')
        parts.append('\n')
        return ''.join(parts)

    def _init_slots(self):
        if hasattr(super(), '_init_slots'):
            super()._init_slots()
        self.register_slot('e410ff403da6504f406cea34551f715f', 'default', self._render_slot_fill_default_10694576)
    INIT_HOOKS = []
__page_class__ = AboutPage