model_dependences = {
    'frame': [
        'fork',
        'shock',
        'crankset',
        'frontderailleur',
        'rearderailleur',
        'brake',
        'brakelever',
        'rotor',
        'stem',
        'seatpost',
        'wheels',
    ],
    'fork': [
        'frame',
        'brake',
        'brakelever',
        'stem',
        'wheels',
    ],
    'crankset': [
        'frame',
        'cassette',
        'rearderailleur',
        'frontderailleur',
        'derailleurlever',
    ],
    'cassette': [
        'crankset',
        'rearderailleur',
        'frontderailleur',
        'derailleurlever',
    ],
    'frontderailleur': [
        'frame',
        'crankset',
        'cassette',
        'rearderailleur',
        'derailleurlever',
    ],
    'rearderailleur': [
        'frame',
        'crankset',
        'cassette',
        'frontderailleur',
        'derailleurlever',
    ],
    'brake': [
        'frame',
        'fork',
        'brakelever',
        'wheels',
    ],
    'brakelever': [
        'frame',
        'fork',
        'brake',
        'wheels',
    ],
    'derailleurlever': [
        'crankset',
        'cassette',
        'frontderailleur',
        'rearderailleur',
    ],
    'rotor': [
        'frame',
        'wheels',
    ],
    'stem': [
        'frame',
        'fork',
        'handlebar'
    ],
    'handlebar': [
        'stem',
    ],
    'seatpost': [
        'frame',
    ],
    'wheels': [
        'frame',
        'fork',
        'brake',
        'brakelever',
        'rotor',
    ],
    'shock': [
        'frame',
    ],
}
