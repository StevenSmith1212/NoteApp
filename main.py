import blip.BlipNode as b
import blipmap.BMap as bm


b1 = b.BlipNode("B1", [])
b2 = b.BlipNode('b2', [])

chart = bm.BMap([])


b.dC(b1, b2)

chart.addBlip(b1) 


chart.showMap()

