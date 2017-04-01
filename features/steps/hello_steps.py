from behave import *

@given(u'Hello is set up')
def step_impl(context):
    assert context.client

@when(u'we connect to "/"')
def step_impl(context):
    context.page = context.client.get('/')
    assert context.page

@then(u'we should see a message saying "Hello World"')
def step_impl(context):
    assert "Hello World" in context.page.data

@when(u'we connect to "/hello/{name}"')
def step_impl(context, name):
    path = "/hello/" + name
    context.page = context.client.get(path)
    assert context.client

@then(u'we should see a message saying "{greeting}"')
def step_impl(context, greeting):
    assert greeting in context.page.data
