# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################


def index():
   
    """example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simple replace the two lines below with:
    return auth.wiki()"""
    
    session.counter = (session.counter or 0)+1
    return dict(message ="Hello World from myapp!!! ",counter = session.counter)

#simple form creation using HTML see default/first.html
def first():
    if request.vars.visitor_name:
        session.visitor_name = request.vars.visitor_name
        redirect(URL('second'))
    return dict()
#ad-hoc mechanism for authorization
def second():
        name = request.vars.visitor_name or redirect(URL('fifth'))
        return dict(name=name)
    #else:not request.function =='third' and not session.visitor_name:
        #redirect(URL('third'))
    #return dict()
#Form is created using FORM property in default controller but IS_NOT_EMPTY() isn't working.
def third():
    form = FORM(INPUT(_name='visitor_name',requiers=IS_NOT_EMPTY()),INPUT(_type='submit'))
    if form.process().accepted:
        session.visitor_name = form.vars.visitor_name
        redirect(URL('second'))
    return dict(form=form)
#Form is created using SQLFORM property in default controller but IS_NOT_EMPTY() is working.
def fourth():
    form=SQLFORM.factory(Field('visitor_name',label='What is your name?',requires=IS_NOT_EMPTY()))
    if form.process().accepted:
        session.visitor_name = form.vars.visitor_name
        redirect(URL('second'))
    return dict(form=form)
#Passing argument to callee function i.e second function
def fifth():
    form=SQLFORM.factory(Field('visitor_name',label='What is your name?',requires=IS_NOT_EMPTY()))
    if form.process().accepted:
        name = form.vars.visitor_name
        redirect(URL('second',vars=dict(name=name)))
    return dict(form=form)

