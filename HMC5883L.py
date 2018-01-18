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

from HMC5883L_constants import *

# name:        HMC5883L
# description: Surface-mount, multi-chip module designed for low-field magnetic sensing with a digital interface for applications such as lowcost compassing and magnetometry
# manuf:       Honeywell
# version:     Version 0.1
# url:         https://aerocontent.honeywell.com/aero/common/documents/myaerospacecatalog-documents/Defense_Brochures-documents/HMC5883L_3-Axis_Digital_Compass_IC.pdf
# date:        2016-08-01


# Derive from this class and implement read and write
class HMC5883L_Base:
	"""Surface-mount, multi-chip module designed for low-field magnetic sensing with a digital interface for applications such as lowcost compassing and magnetometry"""
	# Register ConfigA
	# Configure the device for setting the data output rate and measurement configuration. 
	
	def setConfigA(self, val):
		"""Set register ConfigA"""
		self.write(REG.ConfigA, val, 8)
	
	def getConfigA(self):
		"""Get register ConfigA"""
		return self.read(REG.ConfigA, 8)
	
	# Bits CRA7
	# Reserved for future function. Set to 0 when configuring CRA. 
	# Bits MA
	# Select number of samples averaged (1 to 8) per measurement output. 
	# Bits DO
	# All selectable data output rates in continuous measurement mode. All three channels shall be measured
	#           within a given output rate. Other output rates with maximum rate of 160 Hz can be achieved by
	#           monitoring DRDY interrupt pin in single measurement mode. 
	
	# Bits MS
	# The Measurement Configuration Bits define the measurement flow of the device,
	#           specifically whether or not to incorporate an applied bias into the measurement. 
	# 'b11 reserved. 
	
	# Register ConfigB
	# Set the device gain. 
	
	def setConfigB(self, val):
		"""Set register ConfigB"""
		self.write(REG.ConfigB, val, 8)
	
	def getConfigB(self):
		"""Get register ConfigB"""
		return self.read(REG.ConfigB, 8)
	
	# Bits GN
	# The Gain Configuration Bits configure the gain for the device.
	#           The gain configuration is common for all channels.
	#           <br>Sensor field range / Gain (LSb/G) / digital resolution (mG/LSb) / Output range 
	
	# Bits reserved_0
	# Register Mode
	# Select operating mode of the device 
	
	def setMode(self, val):
		"""Set register Mode"""
		self.write(REG.Mode, val, 8)
	
	def getMode(self):
		"""Get register Mode"""
		return self.read(REG.Mode, 8)
	
	# Bits HS
	# enable High Speed I2C, 3400kHz 
	# Bits unused_0
	# Bits MD
	# Register DataOutputX
	# These registers store the measurement result from channel X.
	#       The value stored in these two registers is a 16-bit value in 2's complement form, whose range is
	#       0xF800 to 0x07FF. 
	
	
	def setDataOutputX(self, val):
		"""Set register DataOutputX"""
		self.write(REG.DataOutputX, val, 16)
	
	def getDataOutputX(self):
		"""Get register DataOutputX"""
		return self.read(REG.DataOutputX, 16)
	
	# Bits DataOutputX
	# Register DataOutputZ
	# These registers store the measurement result from channel Z. 
	
	def setDataOutputZ(self, val):
		"""Set register DataOutputZ"""
		self.write(REG.DataOutputZ, val, 16)
	
	def getDataOutputZ(self):
		"""Get register DataOutputZ"""
		return self.read(REG.DataOutputZ, 16)
	
	# Bits DataOutputZ
	# Register DataOutputY
	# These registers store the measurement result from channel Y. 
	
	def setDataOutputY(self, val):
		"""Set register DataOutputY"""
		self.write(REG.DataOutputY, val, 16)
	
	def getDataOutputY(self):
		"""Get register DataOutputY"""
		return self.read(REG.DataOutputY, 16)
	
	# Bits DataOutputY
	# Register Status
	# Indicate the device status. 
	
	def setStatus(self, val):
		"""Set register Status"""
		self.write(REG.Status, val, 8)
	
	def getStatus(self):
		"""Get register Status"""
		return self.read(REG.Status, 8)
	
	# Bits reserved_0
	# Bits LOCK
	# Data output register lock. This bit is set when:
	#           1. some but not all for of the six data output registers have been read,
	#           2. Mode register has been read.
	#           When this bit is set, the six data output registers are locked and any new data will not be placed in these register until one of these conditions are met:
	#           1. all six bytes have been read,
	#           2. the mode register is changed,
	#           3. the measurement configuration (CRA) is changed,
	#           4. power is reset. 
	
	# Bits RDY
	# Ready Bit. Set when data is written to all six data registers. Cleared when device initiates a write to the data output registers and after one or more of the data output registers are written to. When RDY bit is clear it shall remain cleared for a 250 μs.
	#           DRDY pin can be used as an alternative to the status register for monitoring the device for measurement data. 
	
	# Register Identification
	# The identification value for this device is stored in this register. 
	
	def setIdentification(self, val):
		"""Set register Identification"""
		self.write(REG.Identification, val, 24)
	
	def getIdentification(self):
		"""Get register Identification"""
		return self.read(REG.Identification, 24)
	
	# Bits Identification
