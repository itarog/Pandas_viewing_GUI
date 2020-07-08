import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.pyplot import hist
from tkinter import *
from tkinter import ttk

from Settings import GridProperties, BuildingInstructions, SectionLayout
import inspect

class ActionsConstructor():

    def _activate_init_buttons(self):
        self.set_index_button_.config(state=NORMAL)
        self.select_column_button_.config(state=NORMAL)
        self.set_column_type_button_.config(state=NORMAL)
        self.data_observation_selection_button_.config(state=NORMAL)
        self.data_actions_selection_button_.config(state=NORMAL)
        self.data_masking_selection_button_.config(state=NORMAL)
        self.one_variable_graph_selection_button_.config(state=NORMAL)
        self.two_variable_graph_selection_button_.config(state=NORMAL)
        
    def _create_temp_copy(self):
        if self.change_idc == False:
            self.change_idc = True
            self.original_column_ = self.chosen_column_

    def _update_labels(self):
        pass

    def _interpert_false_true(self, string):
        if string == 'False':
            return False
        if string == 'True':
            return True
        

    # Menu options
    def _load_file_action(self):
        self.filepath = filedialog.askopenfilename(filetypes = self.filetypes)
        if self.filepath:
            self.df_ = pd.read_csv(self.filepath)
            self._activate_init_buttons()
            self.select_column_combobox_['values'] = list(self.df_.columns)
            self.set_index_combobox_['values'] = list(self.df_.columns)

    def _save_file_action(self):
        self.df_.to_csv(self.filepath, line_terminator='\n')

    def _save_file_as_action(self):
        save_file_path = None
        save_file_path = filedialog.asksaveasfile(filetypes = self.filetypes, defaultextension = self.filetypes)
        if save_file_path:
            self.filepath = save_file_path
            self._save_file_action()
          
    def _save_column_action(self):
        self.df_[self.select_column_combobox_results_['text']] = self.chosen_column_
        self.original_column_ = None
        self.change_idc = False

    def _save_column_as_action(self):
        new_name =  simpledialog.askstring('Save column as..', 'What name would you to give the new column?',
                                parent=self.window)
        self.df_[new_name] = self.chosen_column_.values
        self.chosen_column_ = self.df_[new_name]

    # Column selection
    def _select_column_action(self):
        self.chosen_column_name_ = self.select_column_combobox_results_['text']
        self.chosen_column_ = self.df_[self.select_column_combobox_results_['text']]
        self._update_labels()

    def _select_column_callback(self, event):
        self.select_column_combobox_results_.config(text = event.widget.get())

    def _set_index_action(self):
        self.df_ = self.df_.set_index(self.set_index_combobox_results_['text'])

    def _set_index_callback(self, event):
        self.set_index_combobox_results_.config(text = event.widget.get())

    def _set_column_type_action(self):
        self.dtype_mapper = {'int64' : np.int64,
                             'float64' : np.float64,
                             }
        self.chosen_column_ = self.chosen_column_.astype(self.dtype_mapper.get(self.set_column_type_combobox_results_['text']))

    def _set_column_type_callback(self, event):
        self.set_column_type_combobox_results_.config(text = event.widget.get())

    # Data observation
    def _data_observation_selection_action(self):
        self._build_object(section_layout = getattr(SectionLayout, self.data_observation_selection_combobox_results_['text']+'_section').value.get('layout'),
                           grid_location = getattr(GridProperties, 'data_observation_section').value.get('grid_location'),
                           columnspan = getattr(GridProperties, 'data_observation_section').value.get('columnspan', 1),
                           rowspan = getattr(GridProperties, 'data_observation_section').value.get('rowspan', 1)
                                   )
        self.data_observation_selection_button_.config(state=DISABLED)

    def _data_observation_selection_callback(self, event):
        self.data_observation_selection_combobox_results_.config(text = event.widget.get())

    def _data_observation_action(self):
        self.data_observation_selection_button_.config(state=NORMAL)
        self.data_observation_frame_.grid_forget()
        
    
    def _head_view_action(self):
        self.head_view_label_.config(text=self.chosen_column_.head(int(getattr(self, 'head_view_item_number_entry_').get())))

    def _tail_view_action(self):
        self.tail_view_label_.config(text=self.chosen_column_.tail(int(getattr(self, 'tail_view_item_number_entry_').get())))

    def _value_counts_action(self):
        if not self.value_counts_normalize_combobox_results_ in [True, False]:
            self.value_counts_normalize_combobox_results_ = False
        if not self.value_counts_ascending_combobox_results_ in [True, False]:
            self.value_counts_ascending_combobox_results_ = False
        self.value_counts_label_.config(text=self.chosen_column_.value_counts(normalize=self.value_counts_normalize_combobox_results_,
                                                                              ascending=self.value_counts_ascending_combobox_results_))

    def _value_counts_normalize_callback(self, event):
        self.value_counts_normalize_combobox_results_ = self._interpert_false_true(event.widget.get())

    def _value_counts_ascending_callback(self, event):
        self.value_counts_ascending_combobox_results_ = self._interpert_false_true(event.widget.get())

    def _describe_action(self):
        self.describe_label_.config(text=self.chosen_column_.describe())

    # Actions
    def _data_actions_selection_action(self):
        self._build_object(section_layout = getattr(SectionLayout, self.data_actions_selection_combobox_results_['text']+'_section').value.get('layout'),
                           grid_location = getattr(GridProperties, 'data_actions_section').value.get('grid_location'),
                           columnspan = getattr(GridProperties, 'data_actions_section').value.get('columnspan', 1),
                           rowspan = getattr(GridProperties, 'data_actions_section').value.get('rowspan', 1)
                                   )
        if self.data_actions_selection_combobox_results_['text'] == 'missing_data':
            self.missing_data_info_label_.config(text = 'You have '+str(self.chosen_column_.isnull().sum())+' values missing')
        self.data_actions_selection_button_.config(state=DISABLED)

    def _data_actions_selection_callback(self, event):
        self.data_actions_selection_combobox_results_.config(text = event.widget.get())

    def _data_actions_action(self):
        self.data_actions_selection_button_.config(state=NORMAL)
        self.data_actions_frame_.grid_forget()

    def _mean_replacement_action(self):
        self.replacement_value_ = self.chosen_column_.mean()
        self.replacement_value_entry_.delete(0, END)
        self.replacement_value_entry_.insert(0, self.replacement_value_)

    def _median_replacement_action(self):
        self.replacement_value_ = self.chosen_column_.median()
        self.replacement_value_entry_.delete(0, END)
        self.replacement_value_entry_.insert(0, self.replacement_value_)

    def _freq_replacement_action(self):
        pass
        # self.chosen_column_.mode().iloc[0]

    def _excute_replacement_action(self):
        self._create_temp_copy()
        self.replacement_value_ = float(self.replacement_value_entry_.get())
        self.chosen_column_ = self.chosen_column_.fillna(self.replacement_value_)

    def _symmetrical_binning_action(self):
        self._create_temp_copy()
        self.chosen_column_ = pd.cut(self.chosen_column_, bins=int(self.symmetrical_binning_entry_.get()))

    def _quantile_binning_action(self):
        self._create_temp_copy()
        self.chosen_column_ = pd.qcut(self.chosen_column_, q=int(self.quantile_binning_entry_.get()))

    def _auto_categorical_mapping_action(self):
        self.mapping_dict_ = dict(zip(set(self.chosen_column_.values), range(len(set(self.chosen_column_.values)))))
        self.categorical_mapping_entry_.delete(0, END)
        self.categorical_mapping_entry_.insert(0, self.mapping_dict_)

    def _excute_mapping_action(self):
        self.mapping_items_ = self.categorical_mapping_entry_.get()[1:-1].split(', ')
        self.mapping_keys_ = [value.split(':')[0].replace('\'','') for value in self.mapping_items_]
        self.mapping_values_ = [value.split(':')[1] for value in self.mapping_items_]
        self.mapping_dict_ = dict(zip(self.mapping_keys_,self.mapping_values_))
        self._create_temp_copy()
        self.chosen_column_ = self.chosen_column_.map(self.mapping_dict_)
    
    # Masking
    def _data_masking_selection_action(self):
        self._build_object(section_layout = getattr(SectionLayout, self.data_masking_selection_combobox_results_['text']).value.get('layout'),
                           grid_location = getattr(GridProperties, 'data_masking_section').value.get('grid_location'),
                           columnspan = getattr(GridProperties, 'data_masking_section').value.get('columnspan', 1),
                           rowspan = getattr(GridProperties, 'data_masking_section').value.get('rowspan', 1)
                           )
        self.data_masking_selection_button_.config(state=DISABLED)
        self.data_masking_select_column_combobox_['values'] = list(self.df_.columns)

    def _data_masking_selection_callback(self, event):
        self.data_masking_selection_combobox_results_.config(text = event.widget.get())

    def _data_masking_action(self):
        self.data_masking_selection_button_.config(state=NORMAL)
        self.data_masking_frame_.grid_forget()
        
    def _data_masking_select_column_action(self):
        self.data_masking_chosen_column_name_ = self.data_masking_select_column_combobox_results_['text']
        self.data_masking_chosen_column_ = self.df_[self.data_masking_select_column_combobox_results_['text']]

    def _data_masking_select_column_callback(self, event):
        self.data_masking_select_column_combobox_results_.config(text = event.widget.get())

    def _data_masking_select_operator_action(self):
        self.data_masking_chosen_operator_ = self.data_masking_select_operator_combobox_results_['text']

    def _data_masking_select_operator_callback(self, event):
        self.data_masking_select_operator_combobox_results_.config(text = event.widget.get())

    def _data_masking_select_target_action(self):
        self.data_masking_execution_entry_.delete(0, END)
        self.data_masking_execution_entry_.insert(0, self.chosen_column_name_+
                                                  '='+self.chosen_column_name_+
                                                  '['+self.data_masking_chosen_column_name_+
                                                  self.data_masking_chosen_operator_+
                                                  self.data_masking_select_target_entry_.get()+']'
                                                  )

    def _data_masking_execution_action(self):
        exec('self.chosen_column_=self.chosen_column_'+'["'+self.data_masking_chosen_column_name_+'"'+
                                                           self.data_masking_chosen_operator_+
                                                           self.data_masking_select_target_entry_.get()+']')
    
    # One variable Graphs
    def _one_variable_graph_selection_action(self):
        self._build_object(section_layout = getattr(SectionLayout, 'one_variable_graph_column_selection').value.get('layout'),
                           grid_location = getattr(GridProperties, 'one_variable_graph_column_selection').value.get('grid_location'),
                           columnspan = getattr(GridProperties, 'one_variable_graph_column_selection').value.get('columnspan', 1),
                           rowspan = getattr(GridProperties, 'one_variable_graph_column_selection').value.get('rowspan', 1)
                           )
        self.one_variable_select_column_combobox_['values'] = list(self.df_.columns)
        self.one_variable_graph_selection_button_.config(state=DISABLED)

    def _one_variable_graph_selection_callback(self, event):
        self.one_variable_graph_selection_combobox_results_.config(text = event.widget.get())

    def _one_variable_graph_column_selection_action(self):
        self.one_variable_graph_selection_button_.config(state=NORMAL)
        self.one_variable_graph_column_selection_frame_.grid_forget()

    def _one_variable_select_column_action(self):
        self.one_variable_chosen_column_ = self.df_[self.one_variable_select_column_combobox_results_['text']]

        self._build_object(section_layout = getattr(SectionLayout, self.one_variable_graph_selection_combobox_results_['text']+'_section').value.get('layout'),
                           grid_location = getattr(GridProperties, 'one_variable_graph_plot_setting').value.get('grid_location'),
                           columnspan = getattr(GridProperties, 'one_variable_graph_plot_setting').value.get('columnspan', 1),
                           rowspan = getattr(GridProperties, 'one_variable_graph_plot_setting').value.get('rowspan', 1)
                           )
        self.one_variable_select_column_button_.config(state=DISABLED)
        self.one_variable_graph_column_selection_button_.config(state=DISABLED)

    def _one_variable_select_column_callback(self, event):
        self.one_variable_select_column_combobox_results_.config(text = event.widget.get())

    def _one_variable_plot_section_action(self):
        self.one_variable_graph_column_selection_button_.config(state=NORMAL)
        self.one_variable_select_column_button_.config(state=NORMAL)
        self.one_variable_plot_section_frame_.grid_forget()

    def _get_hist_bins_num(self):
        if not self.histogram_plot_bins_num_entry_.get():
            return 50
        return int(self.histogram_plot_bins_num_entry_.get())

    def _get_hist_range(self):
        if self.histogram_plot_range_entry_.get() == '0':
            return (self.one_variable_chosen_column_.min() , self.one_variable_chosen_column_.max()) 
        x_min = float(self.histogram_plot_range_entry_.get().split(' ')[0])
        x_max = float(self.histogram_plot_range_entry_.get().split(' ')[-1])
        return (x_min, x_max)
    
    def _histogram_plot_excution_action (self):
        fig = Figure(figsize=(3.8,3.8))
        a = fig.add_subplot(111)
        self.histogram_bins_num_ = self._get_hist_bins_num()
        self.histogram_range_ = self._get_hist_range()
        a.hist(x=self.one_variable_chosen_column_, bins=self.histogram_bins_num_, range=self.histogram_range_)

#        a.set_title (self.combobox_results_label['text'], fontsize=16)
        a.set_ylabel("Y", fontsize=14)
        a.set_xlabel("X", fontsize=14)

        canvas = FigureCanvasTkAgg(fig, master=getattr(self, getattr(BuildingInstructions, 'histogram_plot_excution').value.get('father_frame_name'))) 
        canvas.get_tk_widget().grid(row = getattr(GridProperties, 'one_variable_graph_plot_area').value.get('grid_location')[0],
                                    column= getattr(GridProperties, 'one_variable_graph_plot_area').value.get('grid_location')[1],
                                    rowspan= getattr(GridProperties, 'one_variable_graph_plot_area').value.get('rowspan',1),
                                    columnspan= getattr(GridProperties, 'one_variable_graph_plot_area').value.get('columnspan',1))
        canvas.draw()

    # Two variables Graphs
    def _two_variable_graph_selection_action(self):
        self._build_object(section_layout = getattr(SectionLayout, 'two_variable_graph_column_selection').value.get('layout'),
                           grid_location = getattr(GridProperties, 'two_variable_graph_column_selection').value.get('grid_location'),
                           columnspan = getattr(GridProperties, 'two_variable_graph_column_selection').value.get('columnspan', 1),
                           rowspan = getattr(GridProperties, 'two_variable_graph_column_selection').value.get('rowspan', 1)
                                   )
        self.two_variable_select_x_column_combobox_['values'] = list(self.df_.columns)
        self.two_variable_select_y_column_combobox_['values'] = list(self.df_.columns)
        self.two_variable_graph_selection_button_.config(state=DISABLED)

    def _two_variable_graph_selection_callback(self, event):
        self.two_variable_graph_selection_combobox_results_.config(text = event.widget.get())

    def _two_variable_graph_column_selection_action(self):
        self.two_variable_graph_selection_button_.config(state=NORMAL)
        self.two_variable_graph_column_selection_frame_.grid_forget()

    def _two_variable_select_x_column_action(self):
        self.two_variable_chosen_x_column_ = self.df_[self.two_variable_select_x_column_combobox_results_['text']]

    def _two_variable_select_x_column_callback(self, event):
        self.two_variable_select_x_column_combobox_results_.config(text = event.widget.get())

    def _two_variable_select_y_column_action(self):
        self.two_variable_chosen_y_column_ = self.df_[self.two_variable_select_y_column_combobox_results_['text']]

    def _two_variable_select_y_column_callback(self, event):
        self.two_variable_select_y_column_combobox_results_.config(text = event.widget.get())

    def _two_variable_select_column_action(self):
        self._build_object(section_layout = getattr(SectionLayout, self.two_variable_graph_selection_combobox_results_['text']+'_section').value.get('layout'),
                           grid_location = getattr(GridProperties, 'two_variable_graph_plot_setting').value.get('grid_location'),
                           columnspan = getattr(GridProperties, 'two_variable_graph_plot_setting').value.get('columnspan', 1),
                           rowspan = getattr(GridProperties, 'two_variable_graph_plot_setting').value.get('rowspan', 1)
                                   )
        self.two_variable_select_column_button_.config(state=DISABLED)
        self.two_variable_select_x_column_button_.config(state=DISABLED)
        self.two_variable_select_y_column_button_.config(state=DISABLED)
        self.two_variable_graph_column_selection_button_.config(state=DISABLED)
        
    def _two_variable_plot_section_action(self):
        self.two_variable_graph_column_selection_button_.config(state=NORMAL)
        self.two_variable_select_x_column_button_.config(state=NORMAL)
        self.two_variable_select_y_column_button_.config(state=NORMAL)
        self.two_variable_select_column_button_.config(state=NORMAL)
        self.two_variable_plot_section_frame_.grid_forget()
        pass

    def _scatter_plot_excution_action (self):
        fig = Figure(figsize=(3.8,3.8))
        a = fig.add_subplot(111)
        a.scatter(x=self.two_variable_chosen_x_column_,
                  y=self.two_variable_chosen_y_column_,
                  marker=self.scatter_plot_marker_entry_.get(),)

#        a.set_title (self.combobox_results_label['text'], fontsize=16)
        a.set_ylabel("Y", fontsize=14)
        a.set_xlabel("X", fontsize=14)

        canvas = FigureCanvasTkAgg(fig, master=getattr(self, getattr(BuildingInstructions, 'scatter_plot_excution').value.get('father_frame_name'))) 
        canvas.get_tk_widget().grid(row = getattr(GridProperties, 'two_variable_graph_plot_area').value.get('grid_location')[0],
                                    column= getattr(GridProperties, 'two_variable_graph_plot_area').value.get('grid_location')[1],
                                    rowspan= getattr(GridProperties, 'two_variable_graph_plot_area').value.get('rowspan',1),
                                    columnspan= getattr(GridProperties, 'two_variable_graph_plot_area').value.get('columnspan',1))
        canvas.draw()
