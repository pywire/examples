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
_LayoutBase = load_layout('/Users/rholmdahl/projects/pywire-workspace/examples/demo-routing/src/pages/__layout__.wire', '/Users/rholmdahl/projects/pywire-workspace/examples/demo-routing/src/pages/users/__layout__.wire')

class LayoutPage(_LayoutBase):
    __spa_enabled__ = False
    __sibling_paths__ = []
    __file_path__ = '/Users/rholmdahl/projects/pywire-workspace/examples/demo-routing/src/pages/users/__layout__.wire'

    def __init__(self, request, params, query, path=None, url=None, **kwargs):
        super().__init__(request, params, query, path, url, **kwargs)
        self._init_slots()

    async def _render_slot_fill_default_0de2a519(self):
        parts = []
        import json
        from pywire.runtime.helpers import ensure_async_iterator
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<section')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('\n    ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<hgroup')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('\n        ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<h2')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('User Management')
        parts.append('</h2>')
        parts.append('\n        ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<p')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('Dynamic profiles and list view')
        parts.append('</p>')
        parts.append('\n    ')
        parts.append('</hgroup>')
        parts.append('\n    \n    ')
        attrs = {}
        attrs['class'] = 'grid'
        from pywire.runtime.helpers import render_attrs
        parts.append('<div')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('\n        ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<aside')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('\n            ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<nav')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('\n                ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<ul')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('\n                    ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<li')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        attrs = {}
        attrs['href'] = '/users'
        from pywire.runtime.helpers import render_attrs
        parts.append('<a')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('All Users')
        parts.append('</a>')
        parts.append('</li>')
        parts.append('\n                    ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<li')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        attrs = {}
        attrs['href'] = '/users/1'
        from pywire.runtime.helpers import render_attrs
        parts.append('<a')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('User #1')
        parts.append('</a>')
        parts.append('</li>')
        parts.append('\n                    ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<li')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        attrs = {}
        attrs['href'] = '/users/2'
        from pywire.runtime.helpers import render_attrs
        parts.append('<a')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('User #2')
        parts.append('</a>')
        parts.append('</li>')
        parts.append('\n                    ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<li')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        attrs = {}
        attrs['href'] = '/users/42'
        from pywire.runtime.helpers import render_attrs
        parts.append('<a')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('User #42')
        parts.append('</a>')
        parts.append('</li>')
        parts.append('\n                ')
        parts.append('</ul>')
        parts.append('\n            ')
        parts.append('</nav>')
        parts.append('\n        ')
        parts.append('</aside>')
        parts.append('\n        \n        ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<div')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('\n            ')
        parts.append(await self.render_slot('default', default_renderer=None, layout_id='0de2a51949e7118ca950edcc982a7756'))
        parts.append('\n        ')
        parts.append('</div>')
        parts.append('\n    ')
        parts.append('</div>')
        parts.append('\n')
        parts.append('</section>')
        parts.append('\n')
        return ''.join(parts)

    def _init_slots(self):
        if hasattr(super(), '_init_slots'):
            super()._init_slots()
        self.register_slot('e410ff403da6504f406cea34551f715f', 'default', self._render_slot_fill_default_0de2a519)
    LAYOUT_ID = '0de2a51949e7118ca950edcc982a7756'
    INIT_HOOKS = []
__page_class__ = LayoutPage