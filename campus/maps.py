from flask import Flask, redirect, url_for, request, render_template


map1 = {
    'harvard': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d619.6106794143685!2d-71.1169532534133!3d42.37701424764919!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89e377427d7f0199%3A0x5937c65cee2427f0!2sHarvard%20University!5e0!3m2!1sen!2sin!4v1622385460056!5m2!1sen!2sin',
    'columbia': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d12384.172567597949!2d-123.0950382060631!3d49.26783884698765!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c2f63e709ae301%3A0x18520444473fa1c4!2sColumbia%20College!5e0!3m2!1sen!2sin!4v1622385545265!5m2!1sen!2sin',
    'oxford': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d299.9377677350572!2d-1.2546155114787036!3d51.75474469632338!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4876c6a9ef8c485b%3A0xd2ff1883a001afed!2sUniversity%20of%20Oxford!5e0!3m2!1sen!2sin!4v1622385581322!5m2!1sen!2sin',
    'yale': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d865.54063240435!2d-72.92276201632697!3d41.316455585847926!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89e7d9b6cd624945%3A0xae34a2c4b4d30427!2sYale%20University!5e0!3m2!1sen!2sin!4v1622385605092!5m2!1sen!2sin',
    'stanford': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1088.3104719653154!2d-122.17070322791544!3d37.427531877976875!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x808fbb2a67728bea9d%3A0x29cdf01a44fc687f!2sStanford%20University!5e0!3m2!1sen!2sin!4v1622385635725!5m2!1sen!2sin',
    'uc berkeley': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d936.356340510859!2d-122.2590190330818!3d37.87164280930274!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x808f7718c522d7c1%3A0xda8034ea3b6b3289!2sUniversity%20of%20California%2C%20Berkeley!5e0!3m2!1sen!2sin!4v1622385702420!5m2!1sen!2sin',
    'carnegie mellon': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3036.448614057127!2d-79.94503858429321!3d40.44320676195223!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8834f21f58679a9f%3A0x88716b461fc4daf4!2sCarnegie%20Mellon%20University!5e0!3m2!1sen!2sin!4v1622385732637!5m2!1sen!2sin',
    'mit': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d309.88867040488475!2d-71.09436406354229!3d42.360120407240586!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89e370aaf51a6a87%3A0xd0e08ea5b308203c!2sMassachusetts%20Institute%20of%20Technology!5e0!3m2!1sen!2sin!4v1622385759334!5m2!1sen!2sin',
    'princeton': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d537.5724989467335!2d-74.65560212551752!3d40.343027584506125!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c3e6d8cd98b6e9%3A0x2ba7ed6fa90024f!2sPrinceton%20University!5e0!3m2!1sen!2sin!4v1622385806232!5m2!1sen!2sin',
    'cornell': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d309.4278049092756!2d-76.47360199912775!3d42.45348454318713!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89d0821a6191da9d%3A0xf50ee64d821b9ff4!2sCornell%20University!5e0!3m2!1sen!2sin!4v1622385837914!5m2!1sen!2sin'
}

gyms = {
    'harvard': 'Hemenway Gymnasium, Malkin Athletic Center, and Radcliffe Gym',
    'columbia': 'F45 Training Panathur, Isha Place - Whitefield, and The Columbia Gym',
    'oxford': 'Buzz Gym Oxford Westgate, Nuffield Health The Oxfordshire Health and Racquets Club, and PureGym Oxford Central',
    'yale': 'CrossFit HCC, Payne Whitney Gymnasium, and mActivity Fitness Center',
    'stanford': 'Fitness 19, Oasis Health and Fitness Club, and Impulse Leisure - Corringham',
    'uc berkeley': 'The Green Yogi, Sausalito Fitness Club, and Recreational Sports Facility',
    'carnegie mellon': 'Pittsburgh Fitness Project, Altus, and X Shadyside',
    'mit': 'MIT D Block Gym, IRON ADDICTS GYM, and Six Pack multi-gym and fitness studio',
    'princeton': 'Forge Performance, Locomotion, and Princeton Fitness and Wellness',
    'cornell': 'Orangetheory Fitness, Appel Fitness Center, and Teagle Hall Fitness Center'
}

names = ['harvard', 'columbia', 'oxford', 'yale', 'stanford', 'uc berkeley', 'carnegie mellon', 'mit', 'princeton', 'cornell']

res = {

    'harvard': "Buckminster's Cafe, Pokeworks, and Russell House Tavern",
    'columbia': "Le Monde, Row House, and Calle Ocho",
    'oxford': "The Alternative Tuck Shop, No.1 Ship Street, and Vaults and Garden",
    'yale': "Koffee Katering, Choupette Crêperie and Cafè, and Union League Cafe",
    'stanford': "East Restaurant - Pan-Asian Rooftop, Dine Bell Restaurant, and GALITO'S",
    'uc berkeley': "King Pin Donut, Taste of Mediterranean, and Stuffed Inn",
    'carnegie mellon': "Union Grill Oakland, Lucca Ristorante and Schatz Dining Room",
    'mit': "Shawarma Shack, Sulmona, and Anna's Taqueria",
    'princeton': "Roots Ocean Prime, The Dinky Bar and Kitchen, and Prospect House and Garden",
    'cornell': "North Star Dining Room, Louie's Lunch, and Risley Dining Room"
}

lib = {
    'harvard': "Cabot Science Library, Loeb Music Library, and Houghton Library",
    'columbia': "Butler Library, Columbia University Music and Arts Library, and Morningside Heights Library",
    'oxford': "Bodleian Library, Christ Church Library, and Codrington Library",
    'yale': "Sterling Memorial Library, Marx Science and Social Science Library, and Divinity School Library",
    'stanford': "Cecil H Green Library, David Rumsey Map Center, and Lathrop Library",
    'uc berkeley': "The Bancroft Library, C. V. Starr East Asian Library, and Moffitt Library",
    'carnegie mellon': "Hunt Library, Mellon Institute Library, and Lippman Library",
    'mit': "MIT Libraries, Rotch Library, and Barker Engineering Library",
    'princeton': "Lewis Science Library, Marquand Art Library, and Stokes Library",
    'cornell': "Albert R. Mann Library, Uris Library, and John M. Olin Library"
}
app = Flask(__name__)
