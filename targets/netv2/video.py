from litevideo.output import VideoOut

from targets.netv2.base import BaseSoC


class VideoSoC(BaseSoC):
    csr_map = {
        "hdmi_out0": 25,        
    }
    csr_map.update(BaseSoC.csr_map)

    def __init__(self, platform, *args, **kw):
        BaseSoC.__init__(self, platform, *args, **kw)

        mode = "ycbcr422"
        if mode == "ycbcr422":
            hdmi_out0_dram_port = self.sdram.crossbar.get_port(mode="read", dw=16, cd="pix", reverse=True)
            self.submodules.hdmi_out0 = VideoOut(platform.device,
                                                 platform.request("hdmi_out"),
                                                 hdmi_out0_dram_port,
                                                 "ycbcr422")
        elif mode == "rgb":
            hdmi_out0_dram_port = self.sdram.crossbar.get_port(mode="read", dw=32, cd="pix", reverse=True)
            self.submodules.hdmi_out0 = VideoOut(platform.device,
                                                 platform.request("hdmi_out"),
                                                 hdmi_out0_dram_port,
                                                 "rgb")

#        self.platform.add_false_path_constraints(
#            self.crg.cd_sys.clk,
#            self.hdmi_out0.driver.clocking.cd_pix.clk)


SoC = VideoSoC
