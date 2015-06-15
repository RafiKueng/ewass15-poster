#!/usr/bin/env python

import qrcode
import qrcode.image.svg

factory = qrcode.image.svg.SvgPathImage

codes = {
    "coll_model_letter": "http://letters.zooniverse.org/letters/86-collaborative_gravitational_lens_modelling_using_spaghettilens_a_spacewarps_project",
    "spaghetti" : "http://labs.spacewarps.org/spaghetti/"
}


for k, v in codes.items():
    img = qrcode.make(v, image_factory=factory)
    img.save(k+'.svg')
    