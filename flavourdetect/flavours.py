# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Flavour:

    DESKTOP = 'DESKTOP'
    MOBILE = 'MOBILE'
    IOS = 'IOS'
    IPAD = 'IPAD'
    IPOD = 'IPOD'
    IPHONE = 'IPHONE'
    ANDROID = 'ANDROID'
    BLACKBERRY = 'BLACKBERRY'


"""
Provides a heirarchy of flavours in a dict
as child => parent pairs
"""
flavour_parents = {
    Flavour.IPAD: Flavour.IOS,
    Flavour.IPHONE: Flavour.IOS,
    Flavour.IPOD: Flavour.IOS,
    Flavour.IOS: Flavour.MOBILE,
    Flavour.ANDROID: Flavour.MOBILE,
    Flavour.BLACKBERRY: Flavour.MOBILE
}
