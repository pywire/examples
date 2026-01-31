from pywire.runtime.page import BasePage
from pywire.core.wire import wire
from starlette.responses import Response
import json
from pywire.runtime.validation import form_validator, FieldRules, FormValidationSchema
from pywire.runtime.pydantic_integration import validate_with_model
from pywire.runtime.loader import load_component
from pywire.runtime.helpers import unwrap_wire, set_render_context, reset_render_context
import asyncio

class LayoutPage(BasePage):
    __spa_enabled__ = False
    __sibling_paths__ = []
    __file_path__ = '/Users/rholmdahl/projects/pywire-workspace/examples/demo-routing/src/pages/__layout__.wire'

    def __init__(self, request, params, query, path=None, url=None, **kwargs):
        super().__init__(request, params, query, path, url, **kwargs)
        self._init_slots()

    async def _render_template(self):
        parts = []
        import json
        from pywire.runtime.helpers import ensure_async_iterator
        attrs = {}
        attrs['lang'] = 'en'
        from pywire.runtime.helpers import render_attrs
        parts.append('<html')
        parts.append(render_attrs(attrs, self.attrs))
        parts.append('>')
        parts.append('\n')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<body')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<pywire-head')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('\n    ')
        attrs = {}
        attrs['charset'] = 'UTF-8'
        from pywire.runtime.helpers import render_attrs
        parts.append('<meta')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('\n    ')
        attrs = {}
        attrs['name'] = 'viewport'
        attrs['content'] = 'width=device-width, initial-scale=1'
        from pywire.runtime.helpers import render_attrs
        parts.append('<meta')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('\n    ')
        attrs = {}
        attrs['rel'] = 'stylesheet'
        attrs['href'] = 'https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css'
        from pywire.runtime.helpers import render_attrs
        parts.append('<link')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('\n    ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<title')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('pywire Routing Demo')
        parts.append('</title>')
        parts.append('\n')
        parts.append('</pywire-head>')
        parts.append('\n\n    ')
        attrs = {}
        attrs['class'] = 'container'
        from pywire.runtime.helpers import render_attrs
        parts.append('<header')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('\n        ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<nav')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('\n            ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<ul')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('\n                ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<li')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<strong')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('pywire Demo')
        parts.append('</strong>')
        parts.append('</li>')
        parts.append('\n            ')
        parts.append('</ul>')
        parts.append('\n            ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<ul')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('\n                ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<li')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        attrs = {}
        attrs['href'] = '/'
        from pywire.runtime.helpers import render_attrs
        parts.append('<a')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('Home')
        parts.append('</a>')
        parts.append('</li>')
        parts.append('\n                ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<li')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        attrs = {}
        attrs['href'] = '/about'
        from pywire.runtime.helpers import render_attrs
        parts.append('<a')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('About')
        parts.append('</a>')
        parts.append('</li>')
        parts.append('\n                ')
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
        parts.append('Users')
        parts.append('</a>')
        parts.append('</li>')
        parts.append('\n            ')
        parts.append('</ul>')
        parts.append('\n        ')
        parts.append('</nav>')
        parts.append('\n    ')
        parts.append('</header>')
        parts.append('\n    ')
        attrs = {}
        attrs['class'] = 'container'
        from pywire.runtime.helpers import render_attrs
        parts.append('<main')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('\n        ')
        parts.append(await self.render_slot('default', default_renderer=None, layout_id='e410ff403da6504f406cea34551f715f'))
        parts.append('\n    ')
        parts.append('</main>')
        parts.append('\n    ')
        attrs = {}
        attrs['class'] = 'container'
        from pywire.runtime.helpers import render_attrs
        parts.append('<footer')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('\n        ')
        attrs = {}
        from pywire.runtime.helpers import render_attrs
        parts.append('<small')
        parts.append(render_attrs(attrs, None))
        parts.append('>')
        parts.append('Built with pywire & Pico CSS')
        parts.append('</small>')
        parts.append('\n    ')
        parts.append('</footer>')
        parts.append('\n\n')
        parts.append('</body>')
        parts.append('</html>')
        if not getattr(self, '__no_spa__', False) and (not getattr(self, '__is_component__', False)) and (getattr(self, '__spa_enabled__', False) or getattr(self.request.app.state, 'enable_pjax', False)):
            sibling_paths = getattr(self, '__sibling_paths__', [])
            pjax_enabled = getattr(self.request.app.state, 'enable_pjax', False)
            debug = getattr(self.request.app.state, 'debug', False)
            parts.append('<script id="_pywire_spa_meta" type="application/json">')
            parts.append(json.dumps({'sibling_paths': sibling_paths, 'enable_pjax': pjax_enabled, 'debug': debug}))
            parts.append('</script>')
            parts.append(f'<script src="{self.request.app.state.pywire._get_client_script_url()}"></script>')
        return ''.join(parts)

    def _init_slots(self):
        pass
    LAYOUT_ID = 'e410ff403da6504f406cea34551f715f'
    INIT_HOOKS = []
__page_class__ = LayoutPage