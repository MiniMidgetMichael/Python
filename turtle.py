#! C:UsersMichaelLFarwellAppDataLocalProgramsPythonPython35-32python.exe
C:UsersMichaelLFarwellAppDataLocalProgramsPythonPython35-32python.exe
#! C:UsersMichaelLFarwellAppDataLocalProgramsPythonPython35-32python.exe
#! C:UsersMichaelLFarwellAppDataLocalProgramsPythonPython35-32python.exe
#
# turtle.py: a Tkinter based turtle graphics module for Python
# Version 1.1b - 4. 5. 2009
#
# Copyright (C) 2006 - 2010  Gregor Lingl
# email: glingl@aon.at
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the authors be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.


"""
Turtle graphics is a popular way for introducing programming to
kids. It was part of the original Logo programming language developed
by Wally Feurzig and Seymour Papert in 1966.

Imagine a robotic turtle starting at (0, 0) in the x-y plane. After an ``import turtle``, give it
the command turtle.forward(15), and it moves (on-screen!) 15 pixels in
the direction it is facing, drawing a line as it moves. Give it the
command turtle.right(25), and it rotates in-place 25 degrees clockwise.

By combining together these and similar commands, intricate shapes and
pictures can easily be drawn.

----- turtle.py

This module is an extended reimplementation of turtle.py from the
Python standard distribution up to Python 2.5. (See: http://www.python.org)

It tries to keep the merits of turtle.py and to be (nearly) 100%
compatible with it. This means in the first place to enable the
learning programmer to use all the commands, classes and methods
interactively when using the module from within IDLE run with
the -n switch.

Roughly it has the following features added:

- Better animation of the turtle movements, especially of turning the
  turtle. So the turtles can more easily be used as a visual feedback
  instrument by the (beginning) programmer.

- Different turtle shapes, gif-images as turtle shapes, user defined
  and user controllable turtle shapes, among them compound
  (multicolored) shapes. Turtle shapes can be stretched and tilted, which
  makes turtles very versatile geometrical objects.

- Fine control over turtle movement and screen updates via delay(),
  and enhanced tracer() and speed() methods.

- Aliases for the most commonly used commands, like fd for forward etc.,
  following the early Logo traditions. This reduces the boring work of
  typing long sequences of commands, which often occur in a natural way
  when kids try to program fancy pictures on their first encounter with
  turtle graphics.

- Turtles now have an undo()-method with configurable undo-buffer.

- Some simple commands/methods for creating event driven programs
  (mouse-, key-, timer-events). Especially useful for programming games.

- A scrollable Canvas class. The default scrollable Canvas can be
  extended interactively as needed while playing around with the turtle(s).

- A TurtleScreen class with methods controlling background color or
  background image, window and canvas size and other properties of the
  TurtleScreen.

- There is a method, setworldcoordinates(), to install a user defined
  coordinate-system for the TurtleScreen.

- The implementation uses a 2-vector class named Vec2D, derived from tuple.
  This class is public, so it can be imported by the application programmer,
  which makes certain types of computations very natural and compact.

- Appearance of the TurtleScreen and the Turtles at startup/import can be
  configured by means of a turtle.cfg configuration file.
  The default configuration mimics the appearance of the old turtle module.

- If configured appropriately the module reads in docstrings from a docstring
  dictionary in some different language, supplied separately  and replaces
  the English ones by those read in. There is a utility function
  write_docstringdict() to write a dictionary with the original (English)
  docstrings to disc, so it can serve as a template for translations.

Behind the scenes there are some features included with possible
extensions in mind. These will be commented and documented elsewhere.

"""

_ver = "turtle 1.1b- - for Python 3.1   -  4. 5. 2009"

# print(_ver)

import tkinter as TK
import types
import math
import time
import inspect
import sys

from os.path import isfile, split, join
from copy import deepcopy
from tkinter import simpledialog

_tg_classes = ['ScrolledCanvas', 'TurtleScreen', 'Screen',
               'RawTurtle', 'Turtle', 'RawPen', 'Pen', 'Shape', 'Vec2D']
_tg_screen_functions = ['addshape', 'bgcolor', 'bgpic', 'bye',
        'clearscreen', 'colormode', 'delay', 'exitonclick', 'getcanvas',
        'getshapes', 'listen', 'mainloop', 'mode', 'numinput',
        'onkey', 'onkeypress', 'onkeyrelease', 'onscreenclick', 'ontimer',
        'register_shape', 'resetscreen', 'screensize', 'setup',
        'setworldcoordinates', 'textinput', 'title', 'tracer', 'turtles', 'update',
        'window_height', 'window_width']
_tg_turtle_functions = ['back', 'backward', 'begin_fill', 'begin_poly', 'bk',
        'circle', 'clear', 'clearstamp', 'clearstamps', 'clone', 'color',
        'degrees', 'distance', 'dot', 'down', 'end_fill', 'end_poly', 'fd',
        'fillcolor', 'filling', 'forward', 'get_poly', 'getpen', 'getscreen', 'get_shapepoly',
        'getturtle', 'goto', 'heading', 'hideturtle', 'home', 'ht', 'isdown',
        'isvisible', 'left', 'lt', 'onclick', 'ondrag', 'onrelease', 'pd',
        'pen', 'pencolor', 'pendown', 'pensize', 'penup', 'pos', 'position',
        'pu', 'radians', 'right', 'reset', 'resizemode', 'rt',
        'seth', 'setheading', 'setpos', 'setposition', 'settiltangle',
        'setundobuffer', 'setx', 'sety', 'shape', 'shapesize', 'shapetransform', 'shearfactor', 'showturtle',
        'speed', 'st', 'stamp', 'tilt', 'tiltangle', 'towards',
        'turtlesize', 'undo', 'undobufferentries', 'up', 'width',
        'write', 'xcor', 'ycor']
_tg_utilities = ['write_docstringdict', 'done']

__all__ = (_tg_classes + _tg_screen_functions + _tg_turtle_functions +
           _tg_utilities + ['Terminator']) # + _math_functions)

_alias_list = ['addshape', 'backward', 'bk', 'fd', 'ht', 'lt', 'pd', 'pos',
               'pu', 'rt', 'seth', 'setpos', 'setposition', 'st',
               'turtlesize', 'up', 'width']

_CFG = {"width" : 0.5,               # Screen
        "height" : 0.75,
        "canvwidth" : 400,
        "canvheight": 300,
        "leftright": None,
        "topbottom": None,
        "mode": "standard",          # TurtleScreen
        "colormode": 1.0,
        "delay": 10,
        "undobuffersize": 1000,      # RawTurtle
        "shape": "classic",
        "pencolor" : "black",
        "fillcolor" : "black",
        "resizemode" : "noresize",
        "visible" : True,
        "language": "english",        # docstrings
        "exampleturtle": "turtle",
        "examplescreen": "screen",
        "title": "Python Turtle Graphics",
        "using_IDLE": False
       }

def config_dict(filename):
    """Convert content of config-file into dictionary."""
    with open(filename, "r") as f:
        cfglines = f.readlines()
    cfgdict = {}
    for line in cfglines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            key, value = line.split("=")
        except:
            print("Bad line in config-file %s:\n%s" % (filename,line))
            continue
        key = key.strip()
        value = value.strip()
        if value in ["True", "False", "None", "''", '""']:
            value = eval(value)
        else:
            try:
                if "." in value:
                    value = float(value)
                else:
                    value = int(value)
            except:
                pass # value need not be converted
        cfgdict[key] = value
    return cfgdict

def readconfig(cfgdict):
    """Read config-files, change configuration-dict accordingly.

    If there is a turtle.cfg file in the current working directory,
    read it from there. If this contains an importconfig-value,
    say 'myway', construct filename turtle_mayway.cfg else use
    turtle.cfg and read it from the import-directory, where
    turtle.py is located.
    Update configuration dictionary first according to config-file,
    in the import directory, then according to config-file in the
    current working directory.
    If no config-file is found, the default configuration is used.
    """
    default_cfg = "turtle.cfg"
    cfgdict1 = {}
    cfgdict2 = {}
    if isfile(default_cfg):
        cfgdict1 = config_dict(default_cfg)
    if "importconfig" in cfgdict1:
        default_cfg = "turtle_%s.cfg" % cfgdict1["importconfig"]
    try:
        head, tail = split(__file__)
        cfg_file2 = join(head, default_cfg)
    except:
        cfg_file2 = ""
    if isfile(cfg_file2):
        cfgdict2 = config_dict(cfg_file2)
    _CFG.update(cfgdict2)
    _CFG.update(cfgdict1)

try:
    readconfig(_CFG)
except:
    print ("No configfile read, reason unknown")


class Vec2D(tuple):
    """A 2 dimensional vector class, used as a helper class
    for implementing turtle graphics.
    May be useful for turtle graphics programs also.
    Derived from tuple, so a vector is a tuple!

    Provides (for a, b vectors, k number):
       a+b vector addition
       a-b vector subtraction
       a*b inner product
       k*a and a*k multiplication with scalar
       |a| absolute value of a
       a.rotate(angle) rotation
    """
    def __new__(cls, x, y):
        return tuple.__new__(cls, (x, y))
    def __add__(self, other):
        return Vec2D(self[0]+other[0], self[1]+other[1])
    def __mul__(self, other):
        if isinstance(other, Vec2D):
            return self[0]*other[0]+self[1]*other[1]
        return Vec2D(self[0]*other, self[1]*other)
    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vec2D(self[0]*other, self[1]*other)
    def __sub__(self, other):
        return Vec2D(self[0]-other[0], self[1]-other[1])
    def __neg__(self):
        return Vec2D(-self[0], -self[1])
    def __abs__(self):
        return (self[0]**2 + self[1]**2)**0.5
    def rotate(self, angle):
        """rotate self counterclockwise by angle
        """
        perp = Vec2D(-self[1], self[0])
        angle = angle * math.pi / 180.0
        c, s = math.cos(angle), math.sin(angle)
        return Vec2D(self[0]*c+perp[0]*s, self[1]*c+perp[1]*s)
    def __getnewargs__(self):
        return (self[0], self[1])
    def __repr__(self):
        return "(%.2f,%.2f)" % self


##############################################################################
### From here up to line    : Tkinter - Interface for turtle.py            ###
### May be replaced by an interface to some different graphics toolkit     ###
##############################################################################

## helper functions for Scrolled Canvas, to forward Canvas-methods
## to ScrolledCanvas class

def __methodDict(cls, _dict):
    """helper function for Scrolled Canvas"""
    baseList = list(cls.__bases__)
    baseList.reverse()
    for _super in baseList:
        __methodDict(_super, _dict)
    for key, value in cls.__dict__.items():
        if type(value) == types.FunctionType:
            _dict[key] = value

def __methods(cls):
    """helper function for Scrolled Canvas"""
    _dict = {}
    __methodDict(cls, _dict)
    return _dict.keys()

__stringBody = (
    'def %(method)s(self, *args, **kw): return ' +
    'self.%(attribute)s.%(method)s(*args, **kw)')

def __forwardmethods(fromClass, toClass, toPart, exclude = ()):
    ### MANY CHANGES ###
    _dict_1 = {}
    __methodDict(toClass, _dict_1)
    _dict = {}
    mfc = __methods(fromClass)
    for ex in _dict_1.keys():
        if ex[:1] == '_' or ex[-1:] == '_' or ex in exclude or ex in mfc:
            pass
        else:
            _dict[ex] = _dict_1[ex]

    for method, func in _dict.items():
        d = {'method': method, 'func': func}
        if isinstance(toPart, str):
            execString = \
                __stringBody % {'method' : method, 'attribute' : toPart}
        exec(execString, d)
        setattr(fromClass, method, d[method])   ### NEWU!


class ScrolledCanvas(TK.Frame):
    """Modeled after the scrolled canvas class from Grayons's Tkinter book.

    Used as the default canvas, which pops up automatically when
    using turtle graphics functions or the Turtle class.
    """
    def __init__(self, master, width=500, height=350,
                                          canvwidth=600, canvheight=500):
        TK.Frame.__init__(self, master, width=width, height=height)
        self._rootwindow = self.winfo_toplevel()
        self.width, self.height = width, height
        self.canvwidth, self.canvheight = canvwidth, canvheight
        self.bg = "white"
        self._canvas = TK.Canvas(master, width=width, height=height,
                                 bg=self.bg, relief=TK.SUNKEN, borderwidth=2)
        self.hscroll = TK.Scrollbar(master, command=self._canvas.xview,
                                    orient=TK.HORIZONTAL)
        self.vscroll = TK.Scrollbar(master, command=self._canvas.yview)
        self._canvas.configure(xscrollcommand=self.hscroll.set,
                               yscrollcommand=self.vscroll.set)
        self.rowconfigure(0, weight=1, minsize=0)
        self.columnconfigure(0, weight=1, minsize=0)
        self._canvas.grid(padx=1, in_ = self, pady=1, row=0,
                column=0, rowspan=1, columnspan=1, sticky='news')
        self.vscroll.grid(padx=1, in_ = self, pady=1, row=0,
                column=1, rowspan=1, columnspan=1, sticky='news')
        self.hscroll.grid(padx=1, in_ = self, pady=1, row=1,
                column=0, rowspan=1, columnspan=1, sticky='news')
        self.reset()
        self._rootwindow.bind('<Configure>', self.onResize)

    def reset(self, canvwidth=None, canvheight=None, bg = None):
        """Adjust canvas and scrollbars according to given canvas size."""
        if canvwidth:
            self.canvwidth = canvwidth
        if canvheight:
            self.canvheight = canvheight
        if bg:
            self.bg = bg
        self._canvas.config(bg=bg,
                        scrollregion=(-self.canvwidth//2, -self.canvheight//2,
                                       self.canvwidth//2, self.canvheight//2))
        self._canvas.xview_moveto(0.5*(self.canvwidth - self.width + 30) /
                                                               self.canvwidth)
        self._canvas.yview_moveto(0.5*(self.canvheight- self.height + 30) /
                                                              self.canvheight)
        self.adjustScrolls()


    def adjustScrolls(self):
        """ Adjust scrollbars according to window- and canvas-size.
        """
        cwidth = self._canvas.winfo_width()
        cheight = self._canvas.winfo_height()
        self._canvas.xview_moveto(0.5*(self.canvwidth-cwidth)/self.canvwidth)
        self._canvas.yview_moveto(0.5*(self.canvheight-cheight)/self.canvheight)
        if cwidth < self.canvwidth or cheight < self.canvheight:
            self.hscroll.grid(padx=1, in_ = self, pady=1, row=1,
                              column=0, rowspan=1, columnspan=1, sticky='news')
            self.vscroll.grid(padx=1, in_ = self, pady=1, row=0,
                              column=1, rowspan=1, columnspan=1, sticky='news')
        else:
            self.hscroll.grid_forget()
            self.vscroll.grid_forget()

    def onResize(self, event):
        """self-explanatory"""
        self.adjustScrolls()

    def bbox(self, *args):
        """ 'forward' method, which canvas itself has inherited...
        """
        return self._canvas.bbox(*args)

    def cget(self, *args, **kwargs):
        """ 'forward' method, which canvas itself has inherited...
        """
        return self._canvas.cget(*args, **kwargs)

    def config(self, *args, **kwargs):
        """ 'forward' method, which canvas itself has inherited...
        """
        self._canvas.config(*args, **kwargs)

    def bind(self, *args, **kwargs):
        """ 'forward' method, which canvas itself has inherited...
        """
        self._canvas.bind(*args, **kwargs)

    def unbind(self, *args, **kwargs):
        """ 'forward' method, which canvas itself has inherited...
        """
        self._canvas.unbind(*args, **kwargs)

    def focus_force(self):
        """ 'forward' method, which canvas itself has inherited...
        """
        self._canvas.focus_force()

__forwardmethods(ScrolledCanvas, TK.Canvas, '_canvas')


class _Root(TK.Tk):
    """Root class for Screen based on Tkinter."""
    def __init__(self):
        TK.Tk.__init__(self)

    def setupcanvas(self, width, height, cwidth, cheight):
        self._canvas = ScrolledCanvas(self, width, height, cwidth, cheight)
        self._canvas.pack(expand=1, fill="both")

    def _getcanvas(self):
        return self._canvas

    def set_geometry(self, width, height, startx, starty):
        self.geometry("%dx%d%+d%+d"%(width, height, startx, starty))

    def ondestroy(self, destroy):
        self.wm_protocol("WM_DELETE_WINDOW", destroy)

    def win_width(self):
        return self.winfo_screenwidth()

    def win_height(self):
        return self.winfo_screenheight()

Canvas = TK.Canvas


class TurtleScreenBase(object):
    """Provide the basic graphics functionality.
       Interface between Tkinter and turtle.py.

       To port turtle.py to some different graphics toolkit
       a corresponding TurtleScreenBase class has to be implemented.
    """

    @staticmethod
    def _blankimage():
        """return a blank image object
        """
        img = TK.PhotoImage(width=1, height=1)
        img.blank()
        return img

    @staticmethod
    def _image(filename):
        """return an image object containing the
        imagedata from a gif-file named filename.
        """
        return TK.PhotoImage(file=filename)

    def __init__(self, cv):
        self.cv = cv
        if isinstance(cv, ScrolledCanvas):
            w = self.cv.canvwidth
            h = self.cv.canvheight
        else:  # expected: ordinary TK.Canvas
            w = int(self.cv.cget("width"))
            h = int(self.cv.cget("height"))
            self.cv.config(scrollregion = (-w//2, -h//2, w//2, h//2 ))
        self.canvwidth = w
        self.canvheight = h
        self.xscale = self.yscale = 1.0

    def _createpoly(self):
        """Create an invisible polygon item on canvas self.cv)
        """
        return self.cv.create_polygon((0, 0, 0, 0, 0, 0), fill="", outline="")

    def _drawpoly(self, polyitem, coordlist, fill=None,
                  outline=None, width=None, top=False):
        """Configure polygonitem polyitem according to provided
        arguments:
        coordlist is sequence of coordinates
        fill is filling color
        outline is outline color
        top is a boolean value, which specifies if polyitem
        will be put on top of the canvas' displaylist so it
        will not be covered by other items.
        """
        cl = []
        for x, y in coordlist:
            cl.append(x * self.xscale)
            cl.append(-y * self.yscale)
        self.cv.coords(polyitem, *cl)
        if fill is not None:
            self.cv.itemconfigure(polyitem, fill=fill)
        if outline is not None:
            self.cv.itemconfigure(polyitem, outline=outline)
        if width is not None:
            self.cv.itemconfigure(polyitem, width=width)
        if top:
            self.cv.tag_raise(polyitem)

    def _createline(self):
        """Create an invisible line item on canvas self.cv)
        """
        return self.cv.create_line(0, 0, 0, 0, fill="", width=2,
                                   capstyle = TK.ROUND)

    def _drawline(self, lineitem, coordlist=None,
                  fill=None, width=None, top=False):
        """Configure lineitem according to provided arguments:
        coordlist is sequence of coordinates
        fill is drawing color
        width is width of drawn line.
        top is a boolean value, which specifies if polyitem
        will be put on top of the canvas' displaylist so it
        will not be covered by other items.
        """
        if coordlist is not None:
            cl = []
            for x, y in coordlist:
                cl.append(x * self.xscale)
                cl.append(-y * self.yscale)
            self.cv.coords(lineitem, *cl)
        if fill is not None:
            self.cv.itemconfigure(lineitem, fill=fill)
        if width is not None:
            self.cv.itemconfigure(lineitem, width=width)
        if top:
            self.cv.tag_raise(lineitem)

    def _delete(self, item):
        """Delete graphics item from canvas.
        If item is"all" delete all graphics items.
        """
        self.cv.delete(item)

    def _update(self):
        """Redraw graphics items on canvas
        """
        self.cv.update()

    def _delay(self, delay):
        """Delay subsequent canvas actions for delay ms."""
        self.cv.after(delay)

    def _iscolorstring(self, color):
        """Check if the string color is a legal Tkinter color string.
        """
        try:
            rgb = self.cv.winfo_rgb(color)
            ok = True
        except TK.TclError:
            ok = False
        return ok

    def _bgcolor(self, color=None):
        """Set canvas' backgroundcolor if color is not None,
        else return backgroundcolor."""
        if color is not None:
            self.cv.config(bg = color)
            self._update()
        else:
            return self.cv.cget("bg")

    def _write(self, pos, txt, align, font, pencolor):
        """Write txt at pos in canvas with specified font
        and color.
        Return text item and x-coord of right bottom corner
        of text's bounding box."""
        x, y = pos
        x = x * self.xscale
        y = y * self.yscale
        anchor = {"left":"sw", "center":"s", "right":"se" }
        item = self.cv.create_text(x-1, -y, text = txt, anchor = anchor[align],
                                        fill = pencolor, font = font)
        x0, y0, x1, y1 = self.cv.bbox(item)
        self.cv.update()
        return item, x1-1

##    def _dot(self, pos, size, color):
##        """may be implemented for some other graphics toolkit"""

    def _onclick(self, item, fun, num=1, add=None):
        """Bind fun to mouse-click event on turtle.
        fun must be a function with two arguments, the coordinates
        of the clicked point on the canvas.
        num, the number of the mouse-button defaults to 1
        """
        if fun is None:
            self.cv.tag_unbind(item, "<Button-%s>" % num)
        else:
            def eventfun(event):
                x, y = (self.cv.canvasx(event.x)/self.xscale,
                        -self.cv.canvasy(event.y)/self.yscale)
                fun(x, y)
            self.cv.tag_bind(item, "<Button-%s>" % num, eventfun, add)

    def _onrelease(self, item, fun, num=1, add=None, args=None):
        """Bind fun to mouse-button-release event on turtle.
        fun must be a function with two arguments, the coordinates
        of the point on the canvas where mouse button is released.
        num, the number of the mouse-button defaults to 1

        If a turtle is clicked, first _onclick-event will be performed,
        then _onscreensclick-event.
        """
        if fun is None:
            self.cv.tag_unbind(item, "<Button%s-ButtonRelease>" % num)
        else:
            if not(args is None):
                def eventfun(event):
                    fun(args)
            else:
                def eventfun(event):
                    x, y = (self.cv.canvasx(event.x)/self.xscale,
                            -self.cv.canvasy(event.y)/self.yscale)
                    fun(x, y)
            self.cv.tag_bind(item, "<Button%s-ButtonRelease>" % num,
                             eventfun, add)

    def _ondrag(self, item, fun, num=1, add=None):
        """Bind fun to mouse-move-event (with pressed mouse button) on turtle.
        fun must be a function with two arguments, the coordinates of the
        actual mouse position on the canvas.
        num, the number of the mouse-button defaults to 1

        Every sequence of mouse-move-events on a turtle is preceded by a
        mouse-click event on that turtle.
        """
        if fun is None:
            self.cv.tag_unbind(item, "<Button%s-Motion>" % num)
        else:
            def eventfun(event):
                try:
                    x, y = (self.cv.canvasx(event.x)/self.xscale,
                           -self.cv.canvasy(event.y)/self.yscale)
                    fun(x, y)
                except:
                    pass
            self.cv.tag_bind(item, "<Button%s-Motion>" % num, eventfun, add)

    def _onscreenclick(self, fun, num=1, add=None, args=None):
        """Bind fun to mouse-click event on canvas.
        fun must be a function with two arguments, the coordinates
        of the clicked point on the canvas.
        num, the number of the mouse-button defaults to 1

        If a turtle is clicked, first _onclick-event will be performed,
        then _onscreensclick-event.
        """
        if fun is None:
            self.cv.unbind("<Button-%s>" % num)
        else:
            def eventfun(event):
                x, y = (self.cv.canvasx(event.x)/self.xscale,
                        -self.cv.canvasy(event.y)/self.yscale)
                fun(x, y)
            self.cv.bind("<Button-%s>" % num, eventfun, add)

    def _onkeyrelease(self, fun, key):
        """Bind fun to key-release event of key.
        Canvas must have focus. See method listen
        """
        if fun is None:
            self.cv.unbind("<KeyRelease-%s>" % key, None)
        else:
            def eventfun(event):
                fun()
            self.cv.bind("<KeyRelease-%s>" % key, eventfun)

    def _onkeypress(self, fun, key=None):
        """If key is given, bind fun to key-press event of key.
        Otherwise bind fun to any key-press.
        Canvas must have focus. See method listen.
        """
        if fun is None:
            if key is None:
                self.cv.unbind("<KeyPress>", None)
            else:
                self.cv.unbind("<KeyPress-%s>" % key, None)
        else:
            def eventfun(event):
                fun()
            if key is None:
                self.cv.bind("<KeyPress>", eventfun)
            else:
                self.cv.bind("<KeyPress-%s>" % key, eventfun)

    def _listen(self):
        """Set focus on canvas (in order to collect key-events)
        """
        self.cv.focus_force()

    def _ontimer(self, fun, t):
        """Install a timer, which calls fun after t milliseconds.
        """
        if t == 0:
            self.cv.after_idle(fun)
        else:
            self.cv.after(t, fun)

    def _createimage(self, image):
        """Create and return image item on canvas.
        """
        return self.cv.create_image(0, 0, image=image)

    def _drawimage(self, item, pos, image):
        """Configure image item as to draw image object
        at position (x,y) on canvas)
        """
        x, y = pos
        self.cv.coords(item, (x * self.xscale, -y * self.yscale))
        self.cv.itemconfig(item, image=image)

    def _setbgpic(self, item, image):
        """Configure image item as to draw image object
        at center of canvas. Set item to the first item
        in the displaylist, so it will be drawn below
        any other item ."""
        self.cv.itemconfig(item, image=image)
        self.cv.tag_lower(item)

    def _type(self, item):
        """Return 'line' or 'polygon' or 'image' depending on
        type of item.
        """
        return self.cv.type(item)

    def _pointlist(self, item):
        """returns list of coordinate-pairs of points of item
        Example (for insiders):
        >>> from turtle import *
        >>> getscreen()._pointlist(getturtle().turtle._item)
        [(0.0, 9.9999999999999982), (0.0, -9.9999999999999982),
        (9.9999999999999982, 0.0)]
        >>> """
        cl = self.cv.coords(item)
        pl = [(cl[i], -cl[i+1]) for i in range(0, len(cl), 2)]
        return  pl

    def _setscrollregion(self, srx1, sry1, srx2, sry2):
        self.cv.config(scrollregion=(srx1, sry1, srx2, sry2))

    def _rescale(self, xscalefactor, yscalefactor):
        items = self.cv.find_all()
        for item in items:
            coordinates = list(self.cv.coords(item))
            newcoordlist = []
            while coordinates:
                x, y = coordinates[:2]
                newcoordlist.append(x * xscalefactor)
                newcoordlist.append(y * yscalefactor)
                coordinates = coordinates[2:]
            self.cv.coords(item, *newcoordlist)

    def _resize(self, canvwidth=None, canvheight=None, bg=None):
        """Resize the canvas the turtles are drawing on. Does
        not alter the drawing window.
        """
        # needs amendment
        if not isinstance(self.cv, ScrolledCanvas):
            return self.canvwidth, self.canvheight
        if canvwidth is canvheight is bg is None:
            return self.cv.canvwidth, self.cv.canvheight
        if canvwidth is not None:
            self.canvwidth = canvwidth
        if canvheight is not None:
            self.canvheight = canvheight
        self.cv.reset(canvwidth, canvheight, bg)

    def _window_size(self):
        """ Return the width and height of the turtle window.
        """
        width = self.cv.winfo_width()
        if width <= 1:  # the window isn't managed by a geometry manager
            width = self.cv['width']
        height = self.cv.winfo_height()
        if height <= 1: # the window isn't managed by a geometry manager
            height = self.cv['height']
        return width, height

    def mainloop(self):
        """Starts event loop - calling Tkinter's mainloop function.

        No argument.

        Must be last statement in a turtle graphics program.
        Must NOT be used if a script is run from within IDLE in -n mode
        (No subprocess) - for interactive use of turtle graphics.

        Example (for a TurtleScreen instance named screen):
        >>> screen.mainloop()

        """
        TK.mainloop()

    def textinput(self, title, prompt):
        """Pop up a dialog window for input of a string.

        Arguments: title is the title of the dialog window,
        prompt is a text mostly describing what information to input.

        Return the string input
        If the dialog is canceled, return None.

        Example (for a TurtleScreen instance named screen):
        >>> screen.textinput("NIM", "Name of first player:")

        """
        return simpledialog.askstring(title, prompt)

    def numinput(self, title, prompt, default=None, minval=None, maxval=None):
        """Pop up a dialog window for input of a number.

        Arguments: title is the title of the dialog window,
        prompt is a text mostly describing what numerical information to input.
        default: default value
        minval: minimum value for imput
        maxval: maximum value for input

        The number input must be in the range minval .. maxval if these are
        given. If not, a hint is issued and the dialog remains open for
        correction. Return the number input.
        If the dialog is canceled,  return None.

        Example (for a TurtleScreen instance named screen):
        >>> screen.numinput("Poker", "Your stakes:", 1000, minval=10, maxval=10000)

        """
        return simpledialog.askfloat(title, prompt, initialvalue=default,
                                     minvalue=minval, maxvalue=maxval)


##############################################################################
###                  End of Tkinter - interface                            ###
##############################################################################


class Terminator (Exception):
    """Will be raised in TurtleScreen.update, if _RUNNING becomes False.

    This stops execution of a turtle graphics script.
    Main purpose: use in the Demo-Viewer turtle.Demo.py.
    """
    pass


class TurtleGraphicsError(Exception):
    """Some TurtleGraphics Error
    """


class Shape(object):
    """Data structure modeling shapes.

    attribute _type is one of "polygon", "image", "compound"
    attribute _data is - depending on _type a poygon-tuple,
    an image or a list constructed using the addcomponent method.
    """
    def __init__(self, type_, data=None):
        self._type = type_
        if type_ == "polygon":
            if isinstance(data, list):
                data = tuple(data)
        elif type_ == "image":
            if isinstance(data, str):
                if data.casefold().endswith(".gif") and isfile(data):
                    data = TurtleScreen._image(data)
                # else data assumed to be Photoimage
        elif type_ == "compound":
            data = []
        else:
            raise TurtleGraphicsError("There is no shape type %s" % type_)
        self._data = data

    def addcomponent(self, poly, fill, outline=None):
        """Add component to a shape of type compound.

        Arguments: poly is a polygon, i. e. a tuple of number pairs.
        fill is the fillcolor of the component,
        outline is the outline color of the component.

        call (for a Shapeobject namend s):
        --   s.addcomponent(((0,0), (10,10), (-10,10)), "red", "blue")

        Example:
        >>> poly = ((0,0),(10,-5),(0,10),(-10,-5))
        >>> s = Shape("compound")
        >>> s.addcomponent(poly, "red", "blue")
        >>> # .. add more components and then use register_shape()
        """
        if self._type != "compound":
            raise TurtleGraphicsError("Cannot add component to %s Shape"
                                                                % self._type)
        if outline is None:
            outline = fill
        self._data.append([poly, fill, outline])


class Tbuffer(object):
    """Ring buffer used as undobuffer for RawTurtle objects."""
    def __init__(self, bufsize=10):
        self.bufsize = bufsize
        self.buffer = [[None]] * bufsize
        self.ptr = -1
        self.cumulate = False
    def reset(self, bufsize=None):
        if bufsize is None:
            for i in range(self.bufsize):
                self.buffer[i] = [None]
        else:
            self.bufsize = bufsize
            self.buffer = [[None]] * bufsize
        self.ptr = -1
    def push(self, item):
        if self.bufsize > 0:
            if not self.cumulate:
                self.ptr = (self.ptr + 1) % self.bufsize
                self.buffer[self.ptr] = item
            else:
                self.buffer[self.ptr].append(item)
    def pop(self):
        if self.bufsize > 0:
            item = self.buffer[self.ptr]
            if item is None:
                return None
            else:
                self.buffer[self.ptr] = [None]
                self.ptr = (self.ptr - 1) % self.bufsize
                return (item)
    def nr_of_items(self):
        return self.bufsize - self.buffer.count([None])
    def __repr__(self):
        return str(self.buffer) + " " + str(self.ptr)



class TurtleScreen(TurtleScreenBase):
    """Provides screen oriented methods like setbg etc.

    Only relies upon the methods of TurtleScreenBase and NOT
    upon components of the underlying graphics toolkit -
    which is Tkinter in this case.
    """
    _RUNNING = True

    def __init__(self, cv, mode=_CFG["mode"],
                 colormode=_CFG["colormode"], delay=_CFG["delay"]):
        self._shapes = {
                   "arrow" : Shape("polygon", ((-10,0), (10,0), (0,10))),
                  "turtle" : Shape("polygon", ((0,16), (-2,14), (-1,10), (-4,7),
                              (-7,9), (-9,8), (-6,5), (-7,1), (-5,-3), (-8,-6),
                              (-6,-8), (-4,-5), (0,-7), (4,-5), (6,-8), (8,-6),
                              (5,-3), (7,1), (6,5), (9,8), (7,9), (4,7), (1,10),
                              (2,14))),
                  "circle" : Shape("polygon", ((10,0), (9.51,3.09), (8.09,5.88),
                              (5.88,8.09), (3.09,9.51), (0,10), (-3.09,9.51),
                              (-5.88,8.09), (-8.09,5.88), (-9.51,3.09), (-10,0),
                              (-9.51,-3.09), (-8.09,-5.88), (-5.88,-8.09),
                              (-3.09,-9.51), (-0.00,-10.00), (3.09,-9.51),
                              (5.88,-8.09), (8.09,-5.88), (9.51,-3.09))),
                  "square" : Shape("polygon", ((10,-10), (10,10), (-10,10),
                              (-10,-10))),
                "triangle" : Shape("polygon", ((10,-5.77), (0,11.55),
                              (-10,-5.77))),
                  "classic": Shape("polygon", ((0,0),(-5,-9),(0,-7),(5,-9))),
                   "blank" : Shape("image", self._blankimage())
                  }

        self._bgpics = {"nopic" : ""}

        TurtleScreenBase.__init__(self, cv)
        self._mode = mode
        self._delayvalue = delay
        self._colormode = _CFG["colormode"]
        self._keys = []
        self.clear()
        if sys.platform == 'darwin':
            # Force Turtle window to the front on OS X. This is needed because
            # the Turtle window will show behind the Terminal window when you
            # start the demo from the command line.
            rootwindow = cv.winfo_toplevel()
            rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
            rootwindow.call('wm', 'attributes', '.', '-topmost', '0')

    def clear(self):
        """Delete all drawings and all turtles from the TurtleScreen.

        No argument.

        Reset empty TurtleScreen to its initial state: white background,
        no backgroundimage, no eventbindings and tracing on.

        Example (for a TurtleScreen instance named screen):
        >>> screen.clear()

        Note: this method is not available as function.
        """
        self._delayvalue = _CFG["delay"]
        self._colormode = _CFG["colormode"]
        self._delete("all")
        self._bgpic = self._createimage("")
        self._bgpicname = "nopic"
        self._tracing = 1
        self._updatecounter = 0
        self._turtles = []
        self.bgcolor("white")
        for btn in 1, 2, 3:
            self.onclick(None, btn)
        self.onkeypress(None)
        for key in self._keys[:]:
            self.onkey(None, key)
            self.onkeypress(None, key)
        Turtle._pen = None

    def mode(self, mode=None):
        """Set turtle-mode ('standard', 'logo' or 'world') and perform reset.

        Optional argument:
        mode -- on of the strings 'standard', 'logo' or 'world'

        Mode 'standard' is compatible with turtle.py.
        Mode 'logo' is compatible with most Logo-Turtle-Graphics.
        Mode 'world' uses userdefined 'worldcoordinates'. *Attention*: in
        this mode angles appear distorted if x/y unit-ratio doesn't equal 1.
        If mode is not given, return the current mode.

             Mode      Initial turtle heading     positive angles
         ------------|-------------------------|-------------------
          'standard'    to the right (east)       counterclockwise
            'logo'        upward    (north)         clockwise

        Examples:
        >>> mode('logo')   # resets turtle heading to north
        >>> mode()
        'logo'
        """
        if mode is None:
            return self._mode
        mode = mode.casefold()
        if mode not in ["standard", "logo", "world"]:
            raise TurtleGraphicsError("No turtle-graphics-mode %s" % mode)
        self._mode = mode
        if mode in ["standard", "logo"]:
            self._setscrollregion(-self.canvwidth//2, -self.canvheight//2,
                                       self.canvwidth//2, self.canvheight//2)
            self.xscale = self.yscale = 1.0
        self.reset()

    def setworldcoordinates(self, llx, lly, urx, ury):
        """Set up a user defined coordinate-system.

        Arguments:
        llx -- a number, x-coordinate of lower left corner of canvas
