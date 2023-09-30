# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class List(Component):
    """A List component.
play ordered or unordered list

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    dmc.ListItem components only.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- aria-* (string; optional):
    Wild card aria attributes.

- bg (string; optional):
    background.

- bga (a value equal to: 'inherit', 'initial', 'scroll', 'fixed', 'local'; optional):
    backgroundAttachment.

- bgp (string | number; optional):
    backgroundPosition.

- bgr (a value equal to: 'inherit', 'initial', 'repeat', 'repeat-x', 'repeat-y', 'no-repeat'; optional):
    backgroundRepeat.

- bgsz (string | number; optional):
    backgroundSize.

- bottom (string | number; optional):
    bottom.

- c (string; optional):
    color.

- center (boolean; optional):
    Center items with icon.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    Adds class names to Mantine components.

- data-* (string; optional):
    Wild card data attributes.

- display (a value equal to: 'none', 'inherit', 'initial', 'inline', 'block', 'contents', 'flex', 'grid', 'inline-block', 'inline-flex', 'inline-grid', 'inline-table', 'list-item', 'run-in', 'table', 'table-caption', 'table-column-group', 'table-header-group', 'table-footer-group', 'table-row-group', 'table-cell', 'table-column', 'table-row'; optional):
    display.

- ff (string; optional):
    fontFamily.

- fs (a value equal to: 'inherit', 'initial', 'normal', 'italic', 'oblique'; optional):
    fontStyle.

- fw (number; optional):
    fontWeight.

- fz (string | number; optional):
    fontSize.

- h (string | number; optional):
    height.

- icon (a list of or a singular dash component, string or number; optional):
    Icon that should replace list item dot.

- inset (string | number; optional):
    inset.

- left (string | number; optional):
    left.

- lh (string | number; optional):
    lineHeight.

- listStyleType (a value equal to: 'disc', 'circle', 'square', 'decimal', 'lower-roman', 'upper-roman', 'lower-greek', 'lower-latin', 'upper-latin', 'lower-alpha', 'upper-alpha', 'none', 'inherit'; optional):
    List style.

- lts (string | number; optional):
    letterSpacing.

- m (string | number; optional):
    margin.

- mah (string | number; optional):
    minHeight.

- maw (string | number; optional):
    maxWidth.

- mb (string | number; optional):
    marginBottom.

- mih (string | number; optional):
    minHeight.

- miw (string | number; optional):
    minWidth.

- ml (string | number; optional):
    marginLeft.

- mr (string | number; optional):
    marginRight.

- mt (string | number; optional):
    marginTop.

- mx (string | number; optional):
    marginRight, marginLeft.

- my (string | number; optional):
    marginTop, marginBottom.

- opacity (number; optional):
    opacity.

- p (string | number; optional):
    padding.

- pb (string | number; optional):
    paddingBottom.

- pl (string | number; optional):
    paddingLeft.

- pos (a value equal to: 'inherit', 'initial', 'fixed', 'static', 'absolute', 'relative', 'sticky'; optional):
    position.

- pr (string | number; optional):
    paddingRight.

- pt (string | number; optional):
    paddingTop.

- px (string | number; optional):
    paddingRight, paddingLeft.

- py (string | number; optional):
    paddingTop, paddingBottom.

- right (string | number; optional):
    right.

- size (number; optional):
    Font size from theme or number to set value in px.

- spacing (number; optional):
    Spacing between items from theme or number to set value in px.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- ta (a value equal to: 'center', 'inherit', 'initial', 'left', 'right', 'justify'; optional):
    textAlign.

- td (a value equal to: 'none', 'inherit', 'initial', 'underline', 'overline', 'line-through'; optional):
    textDecoration.

- top (string | number; optional):
    top.

- tt (a value equal to: 'none', 'inherit', 'initial', 'capitalize', 'uppercase', 'lowercase'; optional):
    textTransform.

- type (a value equal to: 'ordered', 'unordered'; optional):
    List type: ol or ul.

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- w (string | number; optional):
    width.

- withPadding (boolean; optional):
    Include padding-left to offset list from main content."""
    _children_props = ['icon']
    _base_nodes = ['icon', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'List'
    @_explicitize_args
    def __init__(self, children=None, type=Component.UNDEFINED, withPadding=Component.UNDEFINED, size=Component.UNDEFINED, icon=Component.UNDEFINED, spacing=Component.UNDEFINED, center=Component.UNDEFINED, listStyleType=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, id=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, bga=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, classNames=Component.UNDEFINED, styles=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'aria-*', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'center', 'className', 'classNames', 'data-*', 'display', 'ff', 'fs', 'fw', 'fz', 'h', 'icon', 'inset', 'left', 'lh', 'listStyleType', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'right', 'size', 'spacing', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'tt', 'type', 'unstyled', 'w', 'withPadding']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['children', 'id', 'aria-*', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'center', 'className', 'classNames', 'data-*', 'display', 'ff', 'fs', 'fw', 'fz', 'h', 'icon', 'inset', 'left', 'lh', 'listStyleType', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'right', 'size', 'spacing', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'tt', 'type', 'unstyled', 'w', 'withPadding']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(List, self).__init__(children=children, **args)
