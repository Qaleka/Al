from behave import given, when, then, step
from lab_python_fp.unique import Unique

@given('We have list of string [{data}]')
def step_impl(context,data):
    context.data = data.split(', ')

@given('We have generator of integers [{data}]')
def step_impl(context,data):
    context.data = (int(elem) for elem in data.split(', '))

@given('We have list of integers [{data}]')
def step_impl(context,data):
    context.data = [int(elem) for elem in data.split(', ')]

@when('We run Unique()')
def step_impl(context):
    context.result = list(Unique(context.data))

@when('We run Unique() with ignore_case')
def step_impl(context):
    context.result = list(Unique(context.data,ignore_case = True))

@then('We must have string [{correct}]')
def step_impl(context,correct):
    context.correct = correct.split(', ')
    assert sorted(context.result) == sorted(context.correct)

@then('We must have [{correct}]')
def step_impl(context,correct):
    context.correct = []
    for i in correct.split(', '):
        context.correct.append(int(i))
    assert context.result == context.correct
