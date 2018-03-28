# django_rholang_editor

## Introduction

[Rholang](https://developer.rchain.coop/) is a new language for writing smart contracts that run on the RChain virtual machine.
You can find more in the [Rholang tutorial](https://developer.rchain.coop/tutorial) 

##Usage

If you want to use the django form way and post the text in the rholang-editor. You may use as below.
```python
from django.forms import Form
from django_rholang_editor.fields import RholangTextFormField

class EditorForm(Form):
    rho = RholangTextFormField()
```

There is multiple way to configure the attrs of the `RholangTextFormField`

```python
RholangTextFormField(
    default_text="",
    height="100px",
    width="100%",
    js_variable='editor'
)
```

`ARGS`


* default_text

implement the default text in the rholang text editor .
 
* height

the rholang editor widget height

* width

the rholang editor widget width

* js_variable

the js variable name of the rholang editor . You can call the `js_variable` after the editor in the 
html to figure others implement or other interactions with other components.




## Install

1. install using pip
```bash
pip install django-rholang-editor
```

2. Update `INSTALLED_APPS`:
```python
INSTALLED_APPS = (
    # ...
    'django_ace',
)
```
