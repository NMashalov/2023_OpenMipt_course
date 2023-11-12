from jinja2 import Template

a = {
    'name1': 'value',
    'name2' : 'value2'
}

print(Template('''
{%- for key, value in a.items()%}         
    -  key: {{key}}
       value: {{value}}
{% endfor %}'''
).render(a=a))