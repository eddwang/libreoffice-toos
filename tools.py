# -*- coding: utf-8 -*-


def console(*args, **kwargs):
    '''Start the"python interpreter" gui
    Allowed keyword arguments are:
    'loc' : for passing caller's locales and/or globals to the console context
    any constructor constant (BACKGROUND, FOREGROUND...) to tweak the console aspect
    Examples:
    - console()  # defaut constructor)
    - console(loc=locals())
    - console(BACKGROUND=0x0, FOREGROUND=0xFFFFFF)
    '''
    # we need to load apso before import statement
    ctx = XSCRIPTCONTEXT.getComponentContext()
    ctx.ServiceManager.createInstance("apso.python.script.organizer.impl")
    # now we can use apso_utils library
    from apso_utils import console
    from pathlib import Path
    from uno import fileUrlToSystemPath
    import os
    def execfile(python_file):
        desktop = XSCRIPTCONTEXT.getDesktop()
        doc = desktop.loadComponentFromURL(__file__, "_default", 0, ())
        doc.CurrentController.Frame.ContainerWindow.Visible = True
        doc.CurrentController.Frame.ContainerWindow.toFront()
        exec(open(python_file).read())
        return

    desktop = XSCRIPTCONTEXT.getDesktop()
    doc = desktop.getCurrentComponent()
    __file__ = os.path.join(str(Path.home()),".config") if doc.Location == "" else fileUrlToSystemPath(doc.Location)
    os.chdir(os.path.dirname(__file__))

    kwargs.setdefault('loc', {})
    kwargs['loc'].setdefault('XSCRIPTCONTEXT', XSCRIPTCONTEXT)
    kwargs['loc'].setdefault('execfile', execfile)
    kwargs['loc'].setdefault('__file__', __file__)
    kwargs['loc'].setdefault('os', os)
    kwargs.setdefault('BACKGROUND',0x0)
    kwargs.setdefault('FOREGROUND',0xFFFFFF)
    kwargs.setdefault('WIDTH',1000)
    console(**kwargs)
    
g_exportedScripts = console,

