from robosuite.models.robots import ManipulatorModel

class X5(ManipulatorModel):
    def __init__(self, **kwargs):
        super().__init__(
            fname="robots/X5/X5.xml",  # 指向你的 MJCF 文件
            idn=0,
            **kwargs
        )
