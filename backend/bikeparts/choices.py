APPLICATION_CHOICES = [
    ('CITY', 'City'),
    ('ROAD', 'Road'),
    ('TREKKING', 'Trekking'),
    ('MTB', 'All Mountain'),
    ('XC', 'Cross Country'),
    ('DH', 'Downhill'),
    ('ENDURO', 'Enduro'),
]

WHEEL_SIZES = [
    (20, '20"'),
    (24, '24"'),
    (26, '26"'),
    (27.5, '27.5"'),
    (29, '29"'),
]

HEADTUBE_TYPES = [
    ('TP', 'Tapered'),
    ('ECT', 'Conventional Threaded'),
    ('EC', 'Conventional Threadless'),
    ('ZS', 'ZeroStack'),
    ('IS', 'Integrated'),
]

HEADTUBE_DIAMETRES = [
    ('1 1/8 - 1 1/2', '1 1/8 - 1 1/4"'),
    ('1 1/8 - 1 1/2', '1 1/8 - 1 1/2"'),
    ('1 1/8', '1 1/8"'),
    ('1 1/4', '1 1/4"'),
    ('1 1/3', '1 1/3"'),
    ('1 1/2', '1 1/2"'),
]

SEATCLAMP_SIZES = [
    (28.6, '28.6mm'),
    (30.0, '30.0mm'),
    (31.8, '31.8mm'),
    (34.9, '34.9mm'),
    (36.4, '36.4mm'),
]

BOTTOM_BRACKET_SIZES = [
    (68, '68mm'),
    (73, '73mm'),
]

BRAKE_MOUNT_TYPES = [
    ('IS', 'IS'),
    ('PM', 'PM'),
    ('P', 'Pivots'),
]

REAR_DERAILLEUR_MOUNT_TYPES = [
    ('H', 'Hanger'),
    ('B', 'Bolt-on'),
]

FRONT_DERAILLEUR_MOUNT_TYPES = [
    ('CL', 'Clamp'),
    ('DM', 'Direct Mount'),
]

BRAKE_ROTOR_SIZES = [
    (140, '140mm'),
    (160, '160mm'),
    (180, '180mm'),
    (200, '200mm'),
]

HUB_TYPES = [
    ('CASETTE', 'Casette'),
    ('FREEWHEEL', 'Freewheel'),
]

BRAKE_TYPES = [
    ('DISC', 'Disc'),
    ('RIM', 'Rim')
]

SUSPENSION_TYPES = [
    ('AIR', 'Air'),
    ('OIL', 'Oil Spring')
]

AXLE_TYPE = [
    ('9x100', '9x100'),
    ('15x100', '15x100'),
    ('15x110', '15x110'),
]

SPEED_COMPATIBILITY_CHOICES = [
    ('3x6', '3x6'),
    ('3x7', '3x7'),
    ('3x8', '3x8'),
    ('3x9', '3x9'),
    ('3x10', '3x10'),
    ('3x11', '3x11'),
    ('2x8', '2x8'),
    ('2x9', '2x9'),
    ('2x10', '2x10'),
    ('2x11', '2x11'),
    ('2x12', '2x12'),
    ('1x10', '1x10'),
    ('1x11', '1x11'),
    ('1x12', '1x12'),
]

HANDLEBAR_DIAMETERS = [
    (25.4, '25.4'),
    (31.8, '31.8'),
]