# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 16:37:30 2023

@author: Maxine Lelasseux
"""

import pandas as pd

# Load your data from a CSV file (replace 'your_data.csv' with your actual file path)
df = pd.read_csv('homicide_contain_p.csv')

# Define the columns to combine and the new column names
columns_to_combine = {
    'Orientation': ['100','101', '102', '103', '104', '105'],
    'Bibliography': ['112', '113', '114', '115', '116', '117'],
    'Methodology': ['121', '123', '124', '125', '126', '127', '128'],
    'Geography': ['131', '132', '133', '135', '136', '137'],
    'Human biology': ['142', '144', '146', '147'],
    'Behaviour/personality': ['151', '152', '153', '154', '155', '156', 
                              '157', '158'],
    'Demography': ['160', '161', '162', '163', '164', '165', '166', 
                   '167', '168'],
    'History': ['170', '171', '172', '173', '174', '175', '179', '159'],
    'Total culture': ['181', '182', '183', '184', '185', '186'],
    'Language/communication': ['191', '192', '193', '195', '196', '197', '201', 
                               '202', '203', '204', '205', '207', '208'],
    'Records': ['211', '212', '214', '215', '217'],
    'Food quest': ['221', '222', '223', '224', '226', '227'],
    'Animal husbandry': ['231', '232', '233', '234', '237'],
    'Agriculture': ['241', '244', '245', '247', '249'],
    'Food processing': ['251', '252', '256'],
    'Food consumption': ['260', '261', '262', '263', '264', '266', '272'],
    'Drugs/alcohol': ['273', '275', '276', '277'],
    'Fabrics/clothing': ['281', '283', '285', '286', '291', '292', '293', 
                         '294', '296'],
    'Adornment': ['301', '302', '303', '304'],
    'Exploitative activities': ['311', '312', '313', '314', '316', 
                                '317', '318'],
    'Basic materials/chemical industries': ['322', '323', '326', '386'],
    'Building/construction': ['331', '333'],
    'Structures': ['341', '342', '343', '344', '346'],
    'Equipment/maintenance': ['352', '353', '354', '357'],
    'Settlements': ['361', '362', '363', '364', '366', '368', '369'],
    'Energy/power': ['372', '374', '377'],
    'Capital goods industries': ['396'], 
    'Machines/tools': ['407', '411', '412', '413', '415', '416', '417'],
    'Property': ['421', '422', '423', '424', '425', '426', '427', 
                 '428', '429'],
    'Exchange': ['431', '432', '433', '434', '435', '436', '437', 
                 '438', '439'],
    'Marketing': ['441', '443', '444'],
    'Finance': ['451', '452', '456', '458'],
    'Labor': ['461', '463', '464', '465', '466', '467', '468'],
    'Business/industrial organisation' : ['471', '472', '473', '474', 
                                          '476', '477'],
    'Transportation' : ['481', '482', '483', '484', '485', '486', '487', '489', 
                               '491', '492', '493', '494', '496', '497', 
                               '499', '501', '502', '505'],
    'Living standards/routines': ['511', '512', '513', '514', '515', 
                                  '516', '517'],
    'Recreation/entertainment': ['521', '522', '524', '525', 
                                  '526', '527', '541', '543', '544', '548'],
    'Arts': ['531', '532', '533', '534', '535', '536', '537', '538', 
             '539', '5310', '5311'],
    'Naming': ['550', '551', '552', '553'],
    'Mobility': ['554', '555', '556', '557', '558'],
    'Social stratifaction': ['563', '564', '565', '566', '567'], 
    'Non-kin social relationship': ['570', '571', '572', '573', '574', '575', 
                                '576', '577', '609'],
    'Ingroup antagonisms/brawls': ['578', '579'],
    'Mariage': ['580','581','582','583','584','585','586','587','588','589'],
    'Family': ['590', '591', '592', '593', '594', '595', '596', '597'],
    'Kinship': ['601', '602', '603', '604', '605', '606', '607', '608'],
    'Kin groups': ['610', '611', '612', '613', '614', '615', '616', '618'],
    'Local officials/community structure': ['621', '622', '623', '624', '625'],
    'Informal sanctions/ mechanisms of control': ['626', '627'],
    'Intergroup relations': ['628', '629'],
    'Territorial organisation/state': ['631', '632', '633', '634', '635', 
                                       '636', '640', '641', '642', '643', 
                                       '644', '645', '646', '647', '648', 
                                       '619'],
    'Government activities': ['651', '652', '653', '654', '656', '657', '659'],
    'Political behaviour': ['660', '661', '662', '663', '664', '665', '666', 
                            '667', '668', '669'],
    'Law': ['671', '672', '673', '674', '675', '676', '677'],
    'Justice': ['690', '691', '692', '693', '694', '695', '696', '697', '698'],
    'Military/armed forces': ['701', '702', '703', '704', '706', '707', '712', 
                              '714', '716'],
    'War/peacemaking': ['721', '722', '723', '724', '725', '726', '727', 
                        '728', '729'], 
    'Social problems/welfare': ['730', '731', '732', '733', '734', '735',
    '736', '737', '738', '743', '744', '745', '746', '747', '278'],
    'Sickness': ['750', '751', '752', '753', '755', '756', '757', '758', 
                 '759', '278'],
    'Death': ['760', '761', '763', '764', '765', '766', '767', '768', '769'],
    'Religous beliefs': ['770', '771', '772', '773', '774', '775', '776', 
                         '777', '778', '779'],
    'Religious practices': ['780', '781', '782', '783', '784', '785', '786', 
                            '787', '788', '789'],
    'Ecclesiastical organisation': ['791', '792', '793', '794', '795', '796', 
                                    '797', '798'],
    'Numbers/measures': ['801', '802', '804', '805'], 
    'Sciences/humanities': ['811', '812', '814', '815'],
    'Ideas about nature and people': ['820', '821', '822', '823', '824', 
                                      '825', '826', '827', '828', '829'],
    'Sex': ['831', '832', '833', '834', '835', '836', '837', '838', '839'],
    'Menstruation/contraception/birth': ['841', '842', '843', '844', '845', 
                                         '846', '847', '848'],
    'Infancy/childhood': ['851', '852', '853', '854', '855', '856', 
                          '857', '858'],
    'Socialisation': ['861', '862', '864', '865', '866', '867', '868', '869'],
    'Education': ['871', '872', '873', '874', '875', '876', '877'],
    'Adolescence': ['881', '882', '883', '884'],
    'Old age': ['885', '886', '888'],
    'Division of labor by gender': ['462', '890'], 
    'Texts': ['900', '901', '902'],
    'Archeological analyses': ['911']
}

# Combine the specified columns and set '1' if any column contains '1', otherwise '0'
for new_column, source_columns in columns_to_combine.items():
    df[new_column] = (df[source_columns].any(axis=1)).astype(int)

# Drop the columns used for combination
columns_to_drop = [col for cols in columns_to_combine.values() for col in cols]
df.drop(columns=columns_to_drop, inplace=True)

# Save the updated DataFrame to a new CSV file
df.to_csv('combined_homicide_data.csv', index=False)
