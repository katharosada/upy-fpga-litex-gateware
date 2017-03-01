"""
Module which allows control of the seven segment displays.
"""

from litex.build.generic_platform import ConstraintError

from litex.soc.interconnect.csr import AutoCSR
from litex.soc.interconnect.csr_eventmanager import *
from litex.gen.genlib.misc import WaitTimer

from litex.soc.cores.gpio import GPIOIn, GPIOOut

class SevenSegments(Module, AutoCSR):
    def __init__(self, platform, clk_freq):
        sevenseg = platform.request("sevenseg", 0);
        segvalue0 = Signal(8)
        segvalue1 = Signal(8)
        segvalue2 = Signal(8)
        mycounter = Signal(max=int(clk_freq/10000))
        selector = Signal(2)
        segvalue = Array((segvalue0, segvalue1, segvalue2, segvalue0))

        self.sync += [
          mycounter.eq(mycounter + 1)
        ]

        #   0
        # 5   1
        #   6
        # 4   2
        #   3   7

        self.comb += [
          # platform.request("user_led", 7).eq(platform.request("user_sw", 5)), # LED 1, SW 1
          selector.eq(mycounter[-2:]),
          segvalue0.eq(0b10010001), # H
          segvalue1.eq(0b01100001), # E
          segvalue2.eq(0b10001001), # Y
          sevenseg.segment0.eq(segvalue[selector][0]),
          sevenseg.segment1.eq(segvalue[selector][1]),
          sevenseg.segment2.eq(segvalue[selector][2]),
          sevenseg.segment3.eq(segvalue[selector][3]),
          sevenseg.segment4.eq(segvalue[selector][4]),
          sevenseg.segment5.eq(segvalue[selector][5]),
          sevenseg.segment6.eq(segvalue[selector][6]),
          sevenseg.segment7.eq(segvalue[selector][7]),
          If(selector == 2,
              sevenseg.enable0.eq(1),
              sevenseg.enable1.eq(1),
              sevenseg.enable2.eq(0),
          ).Elif(selector == 1,
              sevenseg.enable0.eq(1),
              sevenseg.enable1.eq(0),
              sevenseg.enable2.eq(1),
          ).Elif(selector == 0,
              sevenseg.enable0.eq(0),
              sevenseg.enable1.eq(1),
              sevenseg.enable2.eq(1),
          ).Else(
              sevenseg.enable0.eq(1),
              sevenseg.enable1.eq(1),
              sevenseg.enable2.eq(1),
          ),
          # platform.request("sevenseg", 0).eq(platform.request("user_sw", 4)), # SW 2
        ]

