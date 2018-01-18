#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""HMC5883L: Surface-mount, multi-chip module designed for low-field magnetic sensing with a digital interface for applications such as lowcost compassing and magnetometry"""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["Honeywell"]
__license__    = "TBD"
__version__    = "Version 0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

#
#   THIS FILE IS AUTOMATICALLY CREATED
#    D O     N O T     M O D I F Y  !
#

class REG:
	ConfigA = 0
	ConfigB = 1
	Mode = 2
	DataOutputX = 3
	DataOutputZ = 5
	DataOutputY = 7
	Status = 9
	Identification = 16
