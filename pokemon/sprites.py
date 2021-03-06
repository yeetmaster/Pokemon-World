Sprites = {
  0x0: { 'sprite': 'white_area',
    'level': 0x0, #auf keinen fall passierbar, wenn doch: teleport zu alabastia
  },
  0x1: {'sprite': 'grass',
    'level': 0x1, #normal passierbar
  },
  0x2: {    'sprite': 'grass_flower_left',
    'level': 0x1,
  },
  0x3: {    'sprite': 'grass_flower_right',
    'level': 0x1,
  },
  0x4: {   'sprite': 'block_white',
    'level': 0x2, #nicht passierbar (blockade) - keine interaktion
  },
  0x5: {    'sprite': 'grass_wild',
    'level': 0x3, #normal passierbar & chance auf mob (definiert in maps)
  }, 
  0x6: {    'sprite': 'sign',
    'level': 0x4, #0x2 and on_action_key => read_text (defined in map_file)
  },
  0x7: {   'sprite': 'fence',
    'level': 0x2,
  },
  0x8: {    'sprite': 'water_middle',
    'level': 0x3, #normal passierbar & wasser_pokemon
  },
  0x9: {    'sprite': 'water_edge_left',
    'level': 0x5, #0x2 and on_surf => move to water, change_charakter_skin
  },
  0xa: {    'sprite': 'water_edge_right',
    'level': 0x5,
  },
  0xb: {    'sprite': 'water_edge_top',
    'level': 0x5,
  },
  0xc: {    'sprite': 'water_left',
    'level': 0x5,
  },
  0xd: {    'sprite': 'water_right',
    'level': 0x5,
  },
  0xe: {    'sprite': 'grass_step',
    'level': 0x1,
  },
  0xf: {    'sprite': 'grass_full',
    'level': 0x1,
  },
  0x10: {    'sprite': 'house_door',
    'level': 0x6, #movement_trigger => changemap.
  },
  0x11: {    'sprite': 'house_roof_left_top',
    'level': 0x2,
  },
  0x12: {    'sprite': 'house_roof_left_bottom',
    'level': 0x2,
  },
  0x13: {    'sprite': 'house_left_bottom',
    'level': 0x2,
  },
  0x14: {    'sprite': 'house_right_bottom',
    'level': 0x2,
  },
  0x15: {    'sprite': 'house_window',
    'level': 0x2,
  },
  0x16: {    'sprite': 'house_roof_right_bottom',
    'level': 0x2,
  },
  0x17: {    'sprite': 'house_roof_right_top',
    'level': 0x2,
  },
  0x18: {     'sprite': 'house_roof_top',
    'level': 0x2,
  },
  0x19: {    'sprite': 'house_window_left',
    'level': 0x2,
  },
 0x1a: {    'sprite': 'big_house_roof_left_bottom',
    'level': 0x2,
 },
0x1b: {	'sprite': 'big_house_roof_top',
	'level': 0x2,
},
0x1c: {	'sprite': 'big_house_roof_bottom',
	'level': 0x2,
},
0x1d: {	'sprite':'big_house_roof_left_top',
	'level': 0x2,
},
0x1f: {	'sprite': 'big_house_roof_right_top',
	'level': 0x2,
},
0x20: {	'sprite': 'big_house_roof_right_bottom',
	'level':0x2,
},
0x21: {	'sprite': 'big_house_windows',
	'level': 0x2},
0x22: {	'sprite': 'big_house_right_bottom',
	'level': 0x2,
},
0x23: {	'sprite': 'block_black',
	'level': 0x2,
},
0x24: {	'sprite': 'stock_stair',
	'level': 0x1,
},
0x25: {	'sprite': 'stock_1',
	'level': 0x7,#interact just with -Y (jump down)
},
0x26: {	'sprite': 'stock_2',
	'level': 0x7,
},
0x27: {	'sprite': 'stock_3',
	'level': 0x7,
},
0x28: {	'sprite': 'stock_4',
	'level': 0x7,
},
0x29: {	'sprite': 'stock_5',
	'level': 0x7,
},
0x2a: {	'sprite': 'stock_6',
	'level': 0x7,
},
0x3b: {	'sprite': 'stair_up',
	'level': 0x8,#same as door, but 'stair'-Trigger instead.
},
0x3c: {	'sprite': 'stair_down',
	'level': 0x8,
},
0x3d: {	'sprite': 'carpet_top_vert',
	'level': 0x1,#maybe new level (exit on move-on)
},
0x3e: {	'sprite': 'carpet_bottom_vert',
	'level': 0x1,
},
0x3f: {	'sprite': 'house_tile',
	'level': 0x1,
},
0x40: {	'sprite': 'flower_top',
	'level': 0x2,
},
0x41: {	'sprite': 'flower_bottom',
	'level': 0x2,
},
0x42: {	'sprite': 'bed_bottom',
	'level':0x2,
},
0x43: {	'sprite': 'bed_top',
	'level': 0x2,
},
0x44: {	'sprite': 'nes',
	'level': 0x2,
},
0x45: {	'sprite': 'house_tile_2',
	'level': 0x1,
},
0x46: {	'sprite': 'table_right_bottom',
	'level': 0x2,
},
0x47: {	'sprite': 'table_left_bottom',
	'level': 0x2,
},
0x48: {	'sprite': 'tv',
	'level': 0x2,
},
0x49: {	'sprite': 'bookshelf_black_bottom',
	'level': 0x2,#interact: read random line in "knowledges.txt"
},
0x4a: {	'sprite': 'bookshelf_black_top',
	'level': 0x2,
},
0x4b: {	'sprite': 'carpet_hort',
	'level': 0x1,
},
0x4c: {	'sprite': 'wall',
	'level': 0x2,
},
0x4d: {	'sprite': 'wall_poster',
	'level': 0x2,
},
0x4e: {	'sprite': 'wall_window_open',
	'level': 0x2,
},
0x4f: {	'sprite': 'wall_window_closed',
	'level': 0x2,
},
0x50: {	'sprite': 'house_chair',
	'level': 0x1,
},
0x51: {	'sprite': 'computer_bottom',

	'level': 0x2,#access.pc
},
0x52: {	'sprite': 'computer_top',
	'level': 0x2,#access.pc
},
0x53: {	'sprite': 'bookshelf_white_bottom',
	'level': 0x2,#interact: read random line in "knowledges.txt"
},
0x54: {	'sprite': 'bookshelf_white_top',
	'level': 0x2,
},
0x55: {	'sprite': 'table_right_top',
	'level': 0x2,
},
0x56: {	'sprite': 'table_left_top',
	'level': 0x2,
},
}