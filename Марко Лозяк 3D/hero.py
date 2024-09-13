class Hero():
    def __init__(self,pos,land):
        self.land = land
        self.mode = True
        self.hero = loader.loadModel("buff_steve.glb")
        self.hero.setScale(2)
        self.hero.setPos(pos)
        self.hero.setHpr(0,90,0)

        self.hero.reparentTo(render)
        self.cameraBind()

    def cameraBind(self):
        base.disableMouse()
        base.camera.setHpr(0,90,90)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(5,8,5)
