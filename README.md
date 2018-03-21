# django_rholang_editor

## Introduction

[Rholang](https://developer.rchain.coop/) is a new language for writing smart contracts that run on the RChain virtual machine.
You can find more in the [Rholang tutorial](https://developer.rchain.coop/tutorial) 

##Usage

```python
from django.forms import Form
from django_rholang_editor.fields import RholangTextFormField

class EditorForm(Form):
    rho = RholangTextFormField()
```


## Install

1.install using pip
```bash
pip install django-rholang-editor
```

2.Update `INSTALLED_APPS`:
```python
INSTALLED_APPS = (
    # ...
    'django_ace',
)
```
