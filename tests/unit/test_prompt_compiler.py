import pytest
from backend.app.promptops.compiler import prompt_compiler


def test_prompt_compiler_interpolation():
    template = "Hello {{ name }}, your account balance is {{ balance }}."
    vars = {"name": "Alice", "balance": "$500"}
    res = prompt_compiler.compile(template, vars)
    assert res == "Hello Alice, your account balance is $500."


def test_prompt_compiler_variable_extraction():
    template = "Analyze {{ topic }} with tone {{ tone }}."
    extracted = prompt_compiler.extract_variables(template)
    assert set(extracted) == {"topic", "tone"}
