source name_of_the_virtualenv/bin/activate.fish
(name_of_the_virtualenv) ⋊> ~/Desktop pip install pydantic
(name_of_the_virtualenv) ⋊> ~/Desktop python -c 'import pydantic; print(pydantic)'
<module 'pydantic' from '/Users/spb/Desktop/name_of_the_virtualenv/lib/python3.14/site-packages/pydantic/__init__.py'>

(name_of_the_virtualenv) ⋊> ~/Desktop deactivate
⋊> ~/Desktop python3.14 -c 'import pydantic'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pydantic
ModuleNotFoundError: No module named 'pydantic'
