# configuration for logbook data analysis

# desired data columns for processing (will drop all other columns)
# desired_columns = ['VoyageFrom', 'VoyageTo', 'ShipType', 'Company',
#                    'ShipName', 'Nationality', 'WarsAndFights', 'Year']
desired_columns = ['VoyageFrom', 'VoyageTo', 'ShipType', 'Nationality',
                   'Year', 'slave_logs']

# columns containing logbook text (to search for mentions of slaves)
text_columns = ['CargoMemo', 'LifeOnBoardMemo', 'OtherRem', 'EncRem']

# slave synonyms to search logs for
slave_words = ['slave',  'slaves', 'slaaf', 'slaven', 'meisjesslaaf',
               'manslaaf', 'manslaven', 'slavenjong', 'jongensslaaf',
               'meidslaaf', 'servant', 'slavenmeid', 'vrouwslaaf',
               'vrouwslaven', 'slavenhandel', 'slaaf', 'esclavo', 'esclavos',
               'esclave', 'esclaves']

non_slave_ships = ['assurance', 'san carlos', 'san perpetua', 'severn',
                   'la atrevida', 'el cuervo', 'el carlos real', 'greyhound',
                   'jason', 'la perle', 'la leopard', 'scipio',
                   'princes louisa', 'pollux']

# add dict for slave voyage logs columns
slave_voyage_conversions = {'portdep': 'VoyageFrom', 'portret': 'VoyageTo',
                            'rig': 'ShipType', 'national': 'Nationality',
                            'yeardep': 'Year'}
