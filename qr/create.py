#!/usr/bin/env python

import qrcode
import qrcode.image.svg

factory = qrcode.image.svg.SvgPathImage

codes = {
    "coll_model_letter": "http://letters.zooniverse.org/letters/86-collaborative_gravitational_lens_modelling_using_spaghettilens_a_spacewarps_project",
    "letter_simple": "http://letters.zooniverse.org",
    "spaghetti" : "http://labs.spacewarps.org/spaghetti/",
    'arxiv_marshall' : 'http://arxiv.org/abs/1504.06148',
    'arxiv_more'     : 'http://arxiv.org/abs/1504.05587',
    'arxiv_kueng'    : 'http://arxiv.org/abs/1502.00008',
    'sw_talk'        : 'http://talk.spacewarps.org/#/boards/BSW0000006'
}


for k, v in codes.items():
    img = qrcode.make(v)#, image_factory=factory)
    img.save(k+'.png')
    