import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.pyplot import hist
from tkinter import *
from tkinter import ttk
from tkinter.font import Font

from Settings import InitScreenSetup, GridProperties, BuildingInstructions, SectionLayout
from Actions import ActionsConstructor 

import inspect

class GraphicsConstructor(ActionsConstructor):
    def __init__(self,
                 window = 'window',
                 filepath = None,
                 filetypes = [('CSV Files', '*.csv')],
                 change_idc = False,
                 ):

        args, _, _, values = inspect.getargvalues(inspect.currentframe())
        values.pop("self")

        for arg, val in values.items():
          setattr(self, arg, val)

        _, _, self.methods_, *_ = inspect.getmembers(GraphicsConstructor)
        
        self.object_constructor = {name.split('_')[-1] : method for name, method in dict(self.methods_[1]).items() if '_create_and_place' in name}
        self.constructor_shapes_ = {name.split('_')[-1] : method for name, method in dict(self.methods_[1]).items() if '_construct_geometry' in name}
        
        self._set_fonts()
        self._set_init_screen()
        
    def _set_fonts(self):
        self.code_font = Font(family='Verdana', size=8)
        self.syntex_font = Font(family='Verdana', size=8)
        self.frame_font = Font(family='Verdana', size=10)
        self.label_font = Font(family='Verdana', size=10)
        self.button_font = Font(family='Verdana', size=10)
        self.info_font = Font(family='Verdana', size=12)

                      
#        self.object_constructor = {'frame': self._create_and_place_frame,
#                                   'code': self._create_and_place_code,
#                                   'label': self._create_and_place_label,
#                                   'button': self._create_and_place_button,
#                                   'combobox': self._create_and_place_combobox,
#                                   }

      
#        self.constructor_shapes_ = {'single_row': self._build_single_row,
#                                    'single_column': self._build_single_column,
#                                    'rectangular_row': self._build_rectangular_row,
#                                    'rectangular_column': self._build_rectangular_column,
#                                    }

    def _set_init_screen(self):
        for section in SectionLayout.__dict__.keys():
            if section in InitScreenSetup.layout.value:
                self._build_object(section_layout = getattr(SectionLayout, section).value.get('layout'),
                                   grid_location = getattr(GridProperties, section).value.get('grid_location'),
                                   columnspan = getattr(GridProperties, section).value.get('columnspan', 1),
                                   rowspan = getattr(GridProperties, section).value.get('rowspan', 1),
                                   shape_geometry = getattr(SectionLayout, section).value.get('shape_geometry', 'singlecolumn'),
                                   shape_limit = getattr(SectionLayout, section).value.get('shape_limit', None),
                                   )
        self._disable_init_buttons()

    def _disable_init_buttons(self):
        self.set_index_button_.config(state=DISABLED)
        self.select_column_button_.config(state=DISABLED)
        self.set_column_type_button_.config(state=DISABLED)
        self.data_observation_selection_button_.config(state=DISABLED)
        self.data_actions_selection_button_.config(state=DISABLED)
        self.data_masking_selection_button_.config(state=DISABLED)
        self.one_variable_graph_selection_button_.config(state=DISABLED)
        self.two_variable_graph_selection_button_.config(state=DISABLED)

    def _build_object(self, section_layout, grid_location, columnspan, rowspan, shape_geometry = 'singlecolumn', shape_limit = None):
        if shape_limit:
            self.constructor_shapes_.get(shape_geometry)(self, section_layout, grid_location[0], grid_location[1], columnspan, rowspan, shape_limit)
        else:
            self.constructor_shapes_.get(shape_geometry)(self, section_layout, grid_location[0], grid_location[1], columnspan, rowspan)

    def _construct_geometry_singlerow (self, section_layout, row_num, column_num, columnspan, rowspan):
        block_number = 0
        for building_instructions in section_layout: 
            building_blocks = building_instructions.get('required_building_blocks')
            for building_block in building_blocks:
                self.object_constructor.get(building_block)(self, building_instructions, row_num, column_num+block_number, columnspan, rowspan)
                block_number += 1

    def _construct_geometry_singlecolumn (self, section_layout, row_num, column_num, columnspan, rowspan):
        block_number = 0
        for building_instructions in section_layout: 
            building_blocks = building_instructions.get('required_building_blocks')
            for building_block in building_blocks:
                self.object_constructor.get(building_block)(self, building_instructions, row_num+block_number, column_num, columnspan, rowspan)
                block_number += 1
                
    def _construct_geometry_rectangularrow (self, section_layout, row_num, column_num, columnspan, rowspan, shape_limit):
        block_number = 0
        for building_instructions in section_layout: 
            building_blocks = building_instructions.get('required_building_blocks')
            for building_block in building_blocks:
                self.object_constructor.get(building_block)(self, building_instructions, row_num + (block_number//shape_limit)*rowspan, column_num + (block_number%shape_limit), columnspan, rowspan)
                block_number += 1
                
    def _construct_geometry_rectangularcolumn(self, section_layout, row_num, column_num, columnspan, rowspan, shape_limit):
        block_number = 0
        for building_instructions in section_layout: 
            building_blocks = building_instructions.get('required_building_blocks')
            for building_block in building_blocks:
                self.object_constructor.get(building_block)(self, building_instructions, row_num + (block_number%shape_limit), column_num + (block_number//shape_limit)*columnspan, columnspan, rowspan)
                block_number += 1

    def _create_and_place_frame (self, building_instructions, row_num, column_num, columnspan, rowspan):
        setattr(self,
                building_instructions.get('action_name')+'_frame_',
                LabelFrame(getattr(self, building_instructions.get('father_frame_name')), text = building_instructions.get('frame_text'), font=self.frame_font))
        getattr(self, building_instructions.get('action_name')+'_frame_').grid(row=row_num, column = column_num, columnspan = columnspan, rowspan = rowspan) #sticky=W+E+N+S

    def _create_and_place_code (self, building_instructions, row_num, column_num, columnspan, rowspan):
        setattr(self,
                building_instructions.get('action_name')+'_code_',
                Label(getattr(self, building_instructions.get('action_name')+'_frame_'), text = building_instructions.get('action_code'), font=self.code_font, fg='grey', bg='white'))
        getattr(self, building_instructions.get('action_name')+'_code_').grid(row=row_num, column = column_num, columnspan = columnspan, rowspan = rowspan)

    def _create_and_place_syntex (self, building_instructions, row_num, column_num, columnspan, rowspan):
        setattr(self,
                building_instructions.get('action_name')+'_syntex_',
                Label(getattr(self, building_instructions.get('action_name')+'_frame_'), text = building_instructions.get('action_syntex'), font=self.syntex_font, fg='white', bg='black'))
        getattr(self, building_instructions.get('action_name')+'_syntex_').grid(row=row_num, column = column_num, columnspan = columnspan, rowspan = rowspan)
        
    def _create_and_place_label (self, building_instructions, row_num, column_num, columnspan, rowspan):
        setattr(self,
                building_instructions.get('action_name')+'_label_',
                Label(getattr(self, building_instructions.get('action_name')+'_frame_'), text = building_instructions.get('label_text'), font=self.label_font))
        getattr(self, building_instructions.get('action_name')+'_label_').grid(row=row_num, column = column_num, columnspan = columnspan, rowspan = rowspan)

    def _create_and_place_button (self, building_instructions, row_num, column_num, columnspan, rowspan):
        setattr(self,
                building_instructions.get('action_name')+'_button_',
                Button(getattr(self, building_instructions.get('action_name')+'_frame_'), text = building_instructions.get('button_text'), command = getattr(self, '_'+building_instructions.get('action_name')+'_action'), font=self.button_font))
        getattr(self, building_instructions.get('action_name')+'_button_').grid(row=row_num, column = column_num, columnspan = columnspan, rowspan = rowspan)

    def _create_and_place_combobox (self, building_instructions, row_num, column_num, columnspan, rowspan):
        setattr(self,
                building_instructions.get('action_name')+'_combobox_',
                ttk.Combobox(getattr(self, building_instructions.get('action_name')+'_frame_')))
        getattr(self,
                building_instructions.get('action_name')+'_combobox_').grid(row=row_num, column = column_num, columnspan = columnspan, rowspan = rowspan)
        getattr(self,
                building_instructions.get('action_name')+'_combobox_').bind("<<ComboboxSelected>>", getattr(self, '_'+building_instructions.get('action_name')+'_callback'))
        getattr(self,
                building_instructions.get('action_name')+'_combobox_')['values']=building_instructions.get('default_combobox_options', [])
        setattr(self,
                building_instructions.get('action_name')+'_combobox_results_',
                Label(getattr(self, building_instructions.get('action_name')+'_frame_')))

    def _create_and_place_entry (self, building_instructions, row_num, column_num, columnspan, rowspan):
        setattr(self,
                building_instructions.get('action_name')+'_entry_',
                Entry(getattr(self, building_instructions.get('action_name')+'_frame_')))        
        getattr(self, building_instructions.get('action_name')+'_entry_').grid(row=row_num, column = column_num, columnspan = columnspan, rowspan = rowspan)
        getattr(self, building_instructions.get('action_name')+'_entry_').insert(0, building_instructions.get('entry_default_value', 0))

