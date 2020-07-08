from enum import Enum

class InitScreenSetup(Enum):
    layout = ('file_options', 'data_observation_selection_section', 'data_actions_selection_section', 'one_variable_graph_selection_section', 'data_masking_selection_section', 'two_variable_graph_selection_section')

class GridProperties(Enum):
    file_options = {'grid_location': (0,0),
                    'columnspan': 10,
                    }
    data_observation_selection_section = {'grid_location': (10,0),
                                          'columnspan': 10,
                                          }
    data_observation_section = {'grid_location': (20,0),
                                'columnspan': 10,
                                }
    data_actions_selection_section = {'grid_location': (10,10),
                                     'columnspan': 10,
                                     }
    data_actions_section = {'grid_location': (20,10),
                            'columnspan': 10,
                           }
    data_masking_selection_section = {'grid_location': (10,20),
                                     'columnspan': 10,
                                     }
    data_masking_section = {'grid_location': (20,20),
                            'columnspan': 10,
                           }
    one_variable_graph_selection_section = {'grid_location': (0,30),
                                            'columnspan': 20,
                                           }
    one_variable_graph_column_selection = {'grid_location': (10,30),
                                           'columnspan': 20,
                                           }
    one_variable_graph_plot_setting = {'grid_location': (20,30),
                                       'columnspan': 10,
                                      }
    one_variable_graph_plot_area = {'grid_location': (20,40),
                                    'columnspan': 10,
                                    'rowspan' : 20,
                                   }
    two_variable_graph_selection_section = {'grid_location': (0,50),
                                            'columnspan': 20,
                                           }
    two_variable_graph_column_selection = {'grid_location': (10,50),
                                           'columnspan': 20,
                                           }
    two_variable_graph_plot_setting = {'grid_location': (20,50),
                                       'columnspan': 10,
                                      }
    two_variable_graph_plot_area = {'grid_location': (20,60),
                                    'columnspan': 10,
                                    'rowspan' : 20,
                                    }

class BuildingInstructions(Enum):
#'DF=pd.read_csv(FILE_PATH)',

    set_index = {'action_name' : 'set_index',
                 'action_code' : 'DF=DF.set_index()',
                 'frame_text' : 'Set index section',
                 'button_text' : 'Excute code',
                 'father_frame_name' : 'window',
                 'required_building_blocks' : ('frame', 'code', 'combobox', 'button'),
                 }
    
    select_column = {'action_name' : 'select_column',
                     'action_code' : 'SERIES=DF[COLUMN]',
                     'frame_text' : 'Column selection section',
                     'button_text' : 'Excute code',
                     'father_frame_name' : 'window',
                     'required_building_blocks' : ('frame', 'code', 'combobox', 'button'),
                     }

    set_column_type = {'action_name' : 'set_column_type',
                       'action_code' : 'SERIES=SERIES.astype(TYPE)',
                       'frame_text' : 'Column type casting section',
                       'default_combobox_options' : ['int64', 'float64', 'object', 'bool'],
                       'button_text' : 'Excute code',
                       'father_frame_name' : 'window',
                       'required_building_blocks' : ('frame', 'code', 'combobox', 'button'),
                       }

    
    data_observation_selection_section = {'action_name' : 'data_observation_selection',
                                          'label_text' : 'choose a data observation option:',
                                          'frame_text' : 'Data observation selection',
                                          'button_text' : 'Present',
                                          'father_frame_name' : 'window',
                                          'default_combobox_options' : ['head_view', 'tail_view', 'value_counts', 'describe'],
                                          'required_building_blocks' : ('frame', 'label', 'combobox', 'button'),
                                          }

    data_observation_section = {'action_name' : 'data_observation',
                                'frame_text' : 'Data observation',
                                'button_text' : 'Collapse section',
                                'father_frame_name' : 'window',
                                'required_building_blocks' : ('frame','button',),
                                }
    
    head_view = {'action_name' : 'head_view',
                 'action_code' : 'SERIES.head()',
                 'frame_text' : 'Head view',
                 'button_text' : 'Present',
                 'father_frame_name' : 'data_observation_frame_',
                 'required_building_blocks' : ('frame', 'label', 'code', 'button'),
                 }

    head_view_item_number = {'action_name' : 'head_view_item_number',
                             'action_code' : 'SERIES.head(NUMBER)',
                             'frame_text' : 'Set item number',
                             'entry_default_value' : 5,
                             'father_frame_name' : 'data_observation_frame_',
                             'required_building_blocks' : ('frame', 'code', 'entry',),
                             }

    tail_view = {'action_name' : 'tail_view',
                 'action_code' : 'SERIES.tail()',
                 'frame_text' : 'Tail view',
                 'button_text' : 'Present',
                 'father_frame_name' : 'data_observation_frame_',
                 'required_building_blocks' : ('frame', 'label', 'code', 'button'),
                 }

    tail_view_item_number = {'action_name' : 'tail_view_item_number',
                             'action_code' : 'SERIES.tail(NUMBER)',
                             'frame_text' : 'Set item number',
                             'entry_default_value' : 5,
                             'father_frame_name' : 'data_observation_frame_',
                             'required_building_blocks' : ('frame', 'code', 'entry',),
                             }

    value_counts = {'action_name' : 'value_counts',
                    'action_code' : 'SERIES.value_counts()',
                    'frame_text' : 'Value counts',
                    'button_text' : 'Present',
                    'father_frame_name' : 'data_observation_frame_',
                    'required_building_blocks' : ('frame', 'label', 'code', 'button'),
                   }
    
    value_counts_normalize = {'action_name' : 'value_counts_normalize',
                              'action_code' : 'SERIES.value_counts(normalize=NORMALIZE)',
                              'frame_text' : 'Normalize',
                              'default_combobox_options' : ['False', 'True'],
                              'button_text' : 'Set value',
                              'father_frame_name' : 'data_observation_frame_',
                              'required_building_blocks' : ('frame', 'code', 'combobox',),
                              }

    value_counts_ascending = {'action_name' : 'value_counts_ascending',
                              'action_code' : 'SERIES.value_counts(ascending=ASCENDING)',
                              'frame_text' : 'Ascending',
                              'default_combobox_options' : ['False', 'True'],
                              'button_text' : 'Set value',
                              'father_frame_name' : 'data_observation_frame_',
                              'required_building_blocks' : ('frame', 'code', 'combobox',),
                              }
# percentiles
    describe = {'action_name' : 'describe',
                'action_code' : 'SERIES.describe()',
                'frame_text' : 'Describe',
                'button_text' : 'Present',
                'father_frame_name' : 'data_observation_frame_',
                'required_building_blocks' : ('frame', 'label', 'code', 'button'),
                }
    
    data_actions_selection_section = {'action_name' : 'data_actions_selection',
                                      'label_text' : 'choose an action:',
                                      'frame_text' : 'Data actions selection',
                                      'button_text' : 'Present',
                                      'father_frame_name' : 'window',
                                      'default_combobox_options' : ['missing_data', 'binning_data', 'categorical_mapping'],
                                      'required_building_blocks' : ('frame', 'label', 'combobox', 'button'),
                                     }

    data_actions_section = {'action_name' : 'data_actions',
                            'frame_text' : 'Data actions',
                            'button_text' : 'Collapse section',
                            'father_frame_name' : 'window',
                            'required_building_blocks' : ('frame','button',),
                            }

    missing_data_info = {'action_name' : 'missing_data_info',
                         'label_text' : 'You have .. values missing',
                         'action_code' : 'SERIES.isnull().sum()',
                         'frame_text' : 'Info',
                         'father_frame_name' : 'data_actions_frame_',
                         'required_building_blocks' : ('frame', 'label', 'code'),
                        }

    mean_replacement = {'action_name' : 'mean_replacement',
                        'action_code' : 'REPLACE_VALUE=SERIES.mean()',
                        'frame_text' : 'Mean replacement',
                        'button_text' : 'Excute code',
                        'father_frame_name' : 'data_actions_frame_',
                        'required_building_blocks' : ('frame', 'code', 'button'),
                        }

    median_replacement = {'action_name' : 'median_replacement',
                          'action_code' : 'REPLACE_VALUE=SERIES.median()',
                          'frame_text' : 'Median replacement',
                          'button_text' : 'Excute code',
                          'father_frame_name' : 'data_actions_frame_',
                          'required_building_blocks' : ('frame', 'code', 'button'),
                          }

    freq_replacement = {'action_name' : 'freq_replacement',
                        'action_code' : 'REPLACE_VALUE=??',
                        'frame_text' : 'Most frequent value replacement',
                        'button_text' : 'Excute code',
                        'father_frame_name' : 'data_actions_frame_',
                        'required_building_blocks' : ('frame', 'code', 'button'),
                        }

    replacement_value = {'action_name' : 'replacement_value',
                         'frame_text' : 'Enter REPLACE_VALUE',
                         'action_syntex' : "Proper syntex: value",
                         'father_frame_name' : 'data_actions_frame_',
                         'required_building_blocks' : ('frame', 'syntex', 'entry'),
                         }

    excute_replacement = {'action_name' : 'excute_replacement',
                          'action_code' : 'SERIES=SERIES.fillna(REPLACE_VALUE)',
                          'frame_text' : 'Excute raplacement',
                          'button_text' : 'Excute code',
                          'father_frame_name' : 'data_actions_frame_',
                          'required_building_blocks' : ('frame', 'code', 'button'),
                          }

    symmetrical_binning = {'action_name' : 'symmetrical_binning',
                           'action_code' : 'SERIES=pd.cut(SERIES, bins=BINS_NUM)',
                           'label_text' : 'Enter BINS_NUM for symmetrical binning',
                           'frame_text' : 'Symmetrical binning',
                           'button_text' : 'Excute code',
                           'father_frame_name' : 'data_actions_frame_',
                           'required_building_blocks' : ('frame', 'label', 'code', 'entry', 'button'),
                           }

    quantile_binning = {'action_name' : 'quantile_binning',
                        'action_code' : 'SERIES=pd.qcut(SERIES, q=QUANTILE_NUM)',
                        'label_text' : ' Enter QUANTILE_NUM',
                        'frame_text' : 'Quantile binning',
                        'button_text' : 'Excute code',
                        'father_frame_name' : 'data_actions_frame_',
                        'required_building_blocks' : ('frame', 'label', 'code', 'entry', 'button'),
                        }
    
    auto_categorical_mapping = {'action_name' : 'auto_categorical_mapping',
                                'action_code' : 'MAPPING_DICT=dict(zip(set(SERIES.values), range(len(set(SERIES.values)))))',
                                'frame_text' : 'Auto categorical mapping',
                                'button_text' : 'Excute code',
                                'father_frame_name' : 'data_actions_frame_',
                                'required_building_blocks' : ('frame', 'code', 'button'),
                                }

    categorical_mapping = {'action_name' : 'categorical_mapping',
                           'action_syntex' : "Proper syntex: {'key1': value1, 'key2': value2, ...}",
                           'frame_text' : 'Categorical mapping',
                           'father_frame_name' : 'data_actions_frame_',
                           'required_building_blocks' : ('frame', 'syntex', 'entry'),
                           }

    excute_mapping = {'action_name' : 'excute_mapping',
                      'action_code' : 'SERIES.map(MAPPING_DICT)',
                      'frame_text' : 'Excute mapping',
                      'button_text' : 'Excute code',
                      'father_frame_name' : 'data_actions_frame_',
                      'required_building_blocks' : ('frame', 'code', 'button'),
                      }
    
    data_masking_selection_section = {'action_name' : 'data_masking_selection',
                                      'label_text' : 'choose a data masking option:',
                                      'frame_text' : 'Data masking selection',
                                      'button_text' : 'Present',
                                      'father_frame_name' : 'window',
                                      'default_combobox_options' : ['masking_by_column'],
                                      'required_building_blocks' : ('frame', 'label', 'combobox', 'button'),
                                      }
    
    data_masking_section = {'action_name' : 'data_masking',
                            'frame_text' : 'Selected masking option',
                            'button_text' : 'Collapse section',
                            'father_frame_name' : 'window',
                            'required_building_blocks' : ('frame','button',),
                            }

    data_masking_select_column = {'action_name' : 'data_masking_select_column',
                                  'action_code' : 'MASK_SERIES',
                                  'frame_text' : 'Column selection',
                                  'button_text' : 'Select column',
                                  'father_frame_name' : 'data_masking_frame_',
                                  'required_building_blocks' : ('frame', 'code', 'combobox', 'button'),
                                  }
    
    data_masking_select_operator = {'action_name' : 'data_masking_select_operator',
                                    'action_code' : 'OPERATOR',
                                    'frame_text' : 'Logic operator selection',
                                    'button_text' : 'Select operator',
                                    'father_frame_name' : 'data_masking_frame_',
                                    'default_combobox_options' : ['>', '=', '<', '==', '!='],
                                    'required_building_blocks' : ('frame', 'code', 'combobox', 'button'),
                                    }

    data_masking_select_target = {'action_name' : 'data_masking_select_target',
                                  'action_code' : 'TARGET',
                                  'frame_text' : 'Target selection',
                                  'father_frame_name' : 'data_masking_frame_',
                                  'button_text' : 'Show expression',
                                  'required_building_blocks' : ('frame', 'code', 'entry', 'button'),
                                  }

    data_masking_execution = {'action_name' : 'data_masking_execution',
                              'action_syntex' : 'SERIES=SERIES[MASK_SERIES OPERATOR TARGET]',
                              'frame_text' : 'Execution',
                              'button_text' : 'Apply mask',
                              'father_frame_name' : 'data_masking_frame_',
                              'required_building_blocks' : ('frame', 'syntex', 'entry', 'button'),
                              }

    one_variable_graph_selection_section = {'action_name' : 'one_variable_graph_selection',
                                            'label_text' : 'choose a graph:',
                                            'frame_text' : 'One variable graph selection',
                                            'button_text' : 'Move to column selection',
                                            'father_frame_name' : 'window',
                                            'default_combobox_options' : ['histogram'],
                                            'required_building_blocks' : ('frame', 'label', 'combobox', 'button'),
                                            }

    one_variable_graph_column_selection = {'action_name' : 'one_variable_graph_column_selection',
                                           'frame_text' : 'One variable column selection',
                                           'button_text' : 'Collapse section',
                                           'father_frame_name' : 'window',
                                           'required_building_blocks' : ('frame','button',),
                                           }

    one_variable_graph_select_column = {'action_name' : 'one_variable_select_column',
                                        'frame_text' : 'Column selection',
                                        'button_text' : 'Present Graph',
                                        'father_frame_name' : 'one_variable_graph_column_selection_frame_',
                                        'required_building_blocks' : ('frame', 'combobox', 'button'),
                                        }

    one_variable_plot_section = {'action_name' : 'one_variable_plot_section',
                                 'frame_text' : 'One variable plot',
                                 'button_text' : 'Collapse section',
                                 'father_frame_name' : 'window',
                                 'required_building_blocks' : ('frame','button',),
                                 }
    
    histogram_plot_bins_num = {'action_name' : 'histogram_plot_bins_num',
                               'action_code' : 'FIG.hist(bins=BINS_NUM)',
                               'entry_default_value' : 50,
                               'frame_text' : 'BINS_NUM',
                               'father_frame_name' : 'one_variable_plot_section_frame_',
                               'required_building_blocks' : ('frame', 'code', 'entry'),
                               }

    histogram_plot_range = {'action_name' : 'histogram_plot_range',
                            'action_code' : 'FIG.hist(range=RANGE)',
                            'action_syntex' : 'Proper syntex: X_MIN X_MAX',
                            'frame_text' : 'RANGE',
                            'father_frame_name' : 'one_variable_plot_section_frame_',
                            'required_building_blocks' : ('frame', 'code', 'syntex', 'entry'),
                            }

    histogram_plot_excution = {'action_name' : 'histogram_plot_excution',
                               'action_code' : 'FIG.hist(x=HIST_SERIES)',
                               'frame_text' : 'Excution',
                               'button_text' : 'Present',
                               'father_frame_name' : 'one_variable_plot_section_frame_',
                               'required_building_blocks' : ('frame', 'code', 'button'),
                               }

    two_variable_graph_selection_section = {'action_name' : 'two_variable_graph_selection',
                                            'label_text' : 'choose a graph:',
                                            'frame_text' : 'Two variable graph selection',
                                            'button_text' : 'Move to column selection',
                                            'father_frame_name' : 'window',
                                            'default_combobox_options' : ['scatter'],
                                            'required_building_blocks' : ('frame', 'label', 'combobox', 'button'),
                                            }

    two_variable_graph_column_selection = {'action_name' : 'two_variable_graph_column_selection',
                                           'frame_text' : 'Two variable column selection',
                                           'button_text' : 'Collapse section',
                                           'father_frame_name' : 'window',
                                           'required_building_blocks' : ('frame','button',),
                                           }

    two_variable_graph_select_x_column = {'action_name' : 'two_variable_select_x_column',
                                          'frame_text' : 'X Column selection',
                                          'button_text' : 'Select x column',
                                          'father_frame_name' : 'two_variable_graph_column_selection_frame_',
                                          'required_building_blocks' : ('frame', 'combobox', 'button'),
                                          }
    
    two_variable_graph_select_y_column = {'action_name' : 'two_variable_select_y_column',
                                          'frame_text' : 'Y Column selection',
                                          'button_text' : 'Select y column',
                                          'father_frame_name' : 'two_variable_graph_column_selection_frame_',
                                          'required_building_blocks' : ('frame', 'combobox', 'button'),
                                          }

    two_variable_graph_select_column = {'action_name' : 'two_variable_select_column',
                                          'frame_text' : 'Column selection',
                                          'button_text' : 'Present graph',
                                          'father_frame_name' : 'two_variable_graph_column_selection_frame_',
                                          'required_building_blocks' : ('frame', 'button'),
                                          }

    two_variable_plot_section = {'action_name' : 'two_variable_plot_section',
                                 'frame_text' : 'Two variable plot',
                                 'button_text' : 'Collapse section',
                                 'father_frame_name' : 'window',
                                 'required_building_blocks' : ('frame','button',),
                                 }

    scatter_plot_marker = {'action_name' : 'scatter_plot_marker',
                           'action_code' : 'FIG.scatter(marker=MARKER)',
                           'frame_text' : 'MARKER',
                           'entry_default_value' : 'o',
                           'father_frame_name' : 'two_variable_plot_section_frame_',
                           'required_building_blocks' : ('frame', 'code',  'entry'),
                           }
    
    scatter_plot_excution = {'action_name' : 'scatter_plot_excution',
                             'action_code' : 'FIG.scatter(x=X_SERIES, y=Y_SERIES)',
                             'frame_text' : 'Excution',
                             'button_text' : 'Present',
                             'father_frame_name' : 'two_variable_plot_section_frame_',
                             'required_building_blocks' : ('frame', 'code',  'button'),
                            }
class SectionLayout(Enum):
    file_options = {'layout': (BuildingInstructions.set_index.value,
                               BuildingInstructions.select_column.value,
                               BuildingInstructions.set_column_type.value,
                               ),
                    'shape_geometry' : 'rectangularcolumn',
                    'shape_limit' : 4,
                    }
    data_observation_selection_section = {'layout': (BuildingInstructions.data_observation_selection_section.value,
                                                     )
                                          }
    
    head_view_section = {'layout': (BuildingInstructions.data_observation_section.value,
                                    BuildingInstructions.head_view.value,
                                    BuildingInstructions.head_view_item_number.value,
                                    )
                         }
    
    tail_view_section = {'layout': (BuildingInstructions.data_observation_section.value,
                                    BuildingInstructions.tail_view.value,
                                    BuildingInstructions.tail_view_item_number.value,
                                    )
                         }
    
    value_counts_section = {'layout': (BuildingInstructions.data_observation_section.value,
                                       BuildingInstructions.value_counts.value,
                                       BuildingInstructions.value_counts_normalize.value,
                                       BuildingInstructions.value_counts_ascending.value,
                                       )
                            }
    
    describe_section = {'layout': (BuildingInstructions.data_observation_section.value,
                                   BuildingInstructions.describe.value,
                                   )
                        }

    
    data_actions_selection_section = {'layout': (BuildingInstructions.data_actions_selection_section.value,
                                            )
                                 }

    missing_data_section = {'layout': (BuildingInstructions.data_actions_section.value,
                                       BuildingInstructions.missing_data_info.value,
                                       BuildingInstructions.mean_replacement.value,
                                       BuildingInstructions.median_replacement.value,
                                       BuildingInstructions.freq_replacement.value,
                                       BuildingInstructions.replacement_value.value,
                                       BuildingInstructions.excute_replacement.value
                                       )
                           }

    binning_data_section = {'layout': (BuildingInstructions.data_actions_section.value,
                                       BuildingInstructions.symmetrical_binning.value,
                                       BuildingInstructions.quantile_binning.value,
                                       )
                           }
    categorical_mapping_section = {'layout': (BuildingInstructions.data_actions_section.value,
                                              BuildingInstructions.auto_categorical_mapping.value,
                                              BuildingInstructions.categorical_mapping.value,
                                              BuildingInstructions.excute_mapping.value,
                                       )
                           }

    data_masking_selection_section = {'layout': (BuildingInstructions.data_masking_selection_section.value,
                                                 )
                                     }
    
    masking_by_column = {'layout': (BuildingInstructions.data_masking_section.value,
                                    BuildingInstructions.data_masking_select_column.value,
                                    BuildingInstructions.data_masking_select_operator.value,
                                    BuildingInstructions.data_masking_select_target.value,
                                    BuildingInstructions.data_masking_execution.value,
                                    )
                        }
    
    one_variable_graph_selection_section = {'layout': (BuildingInstructions.one_variable_graph_selection_section.value,
                                                       )
                                            }

    one_variable_graph_column_selection = {'layout': (BuildingInstructions.one_variable_graph_column_selection.value,
                                                      BuildingInstructions.one_variable_graph_select_column.value,
                                                      )
                                           }
    
    histogram_section = {'layout': (BuildingInstructions.one_variable_plot_section.value,
                                    BuildingInstructions.histogram_plot_bins_num.value,
                                    BuildingInstructions.histogram_plot_range.value,
                                    BuildingInstructions.histogram_plot_excution.value,
                                    )
                        }

    two_variable_graph_selection_section = {'layout': (BuildingInstructions.two_variable_graph_selection_section.value,
                                                       )
                                            }

    two_variable_graph_column_selection = {'layout': (BuildingInstructions.two_variable_graph_column_selection.value,
                                                      BuildingInstructions.two_variable_graph_select_x_column.value,
                                                      BuildingInstructions.two_variable_graph_select_y_column.value,
                                                      BuildingInstructions.two_variable_graph_select_column.value,
                                                      )
                                           }
    
    scatter_section = {'layout': (BuildingInstructions.two_variable_plot_section.value,
                                  BuildingInstructions.scatter_plot_marker.value,
                                  BuildingInstructions.scatter_plot_excution.value,
                                  )
                      }
