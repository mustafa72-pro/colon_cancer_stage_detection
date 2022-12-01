import pandas as pd
import numpy as np

colon = pd.read_csv("dataset.csv")
colon = colon[pd.notnull(colon['STAGE'])]

colon['SEX'] = colon['SEX'].replace('M', '1')
colon['SEX'] = colon['SEX'].replace('F', '2')
colon['SEX']= pd.to_numeric(colon['SEX'])

colon['TOPOGRAPHY'] = colon['TOPOGRAPHY'].replace('colon_sigm', '1')
colon['TOPOGRAPHY'] = colon['TOPOGRAPHY'].replace('ungh_splen', '2')
colon['TOPOGRAPHY'] = colon['TOPOGRAPHY'].replace('colon_desc', '3')
colon['TOPOGRAPHY'] = colon['TOPOGRAPHY'].replace('cec', '4')
colon['TOPOGRAPHY'] = colon['TOPOGRAPHY'].replace('jonc_rect_sigm', '5')
colon['TOPOGRAPHY'] = colon['TOPOGRAPHY'].replace('rect', '6')
colon['TOPOGRAPHY'] = colon['TOPOGRAPHY'].replace('colon_trans', '7')
colon['TOPOGRAPHY'] = colon['TOPOGRAPHY'].replace('colon_asc', '8')
colon['TOPOGRAPHY'] = colon['TOPOGRAPHY'].replace('ungh_hep', '9')
colon['TOPOGRAPHY']= pd.to_numeric(colon['TOPOGRAPHY'])

colon['T'] = colon['T'].replace('T1', '1')
colon['T'] = colon['T'].replace('T2', '2')
colon['T'] = colon['T'].replace('T3', '3')
colon['T'] = colon['T'].replace('T4', '4')
colon['T'] = colon['T'].replace('Tx', '5')
colon['T']= pd.to_numeric(colon['T'])

colon['N'] = colon['N'].replace('N0', '0')
colon['N'] = colon['N'].replace('N1', '1')
colon['N'] = colon['N'].replace('N2', '2')
colon['N'] = colon['N'].replace('Nx', '3')
colon['N']= pd.to_numeric(colon['N'])

colon['M'] = colon['M'].replace('M0', '0')
colon['M'] = colon['M'].replace('M1', '1')
colon['M'] = colon['M'].replace('Mx', '2')
colon['M'] = colon['M'].replace('M1_hep', '3')
colon['M']= pd.to_numeric(colon['M'])


colon['SURGERY'] = colon['SURGERY'].replace('one', '1')
colon['SURGERY'] = colon['SURGERY'].replace('two', '2')
colon['SURGERY'] = colon['SURGERY'].replace('three', '3')
colon['SURGERY'] = colon['SURGERY'].replace('four', '4')
colon['SURGERY'] = colon['SURGERY'].replace('five', '5')
colon['SURGERY'] = colon['SURGERY'].replace('six', '6')
colon['SURGERY'] = colon['SURGERY'].replace('seven', '7')
colon['SURGERY'] = colon['SURGERY'].replace('eight', '8')
colon['SURGERY'] = colon['SURGERY'].replace('nine', '9')
colon['SURGERY'] = colon['SURGERY'].replace('ten', '10')
colon['SURGERY']= pd.to_numeric(colon['SURGERY'])


colon['STAGE'] = colon['STAGE'].replace('one', '1')
colon['STAGE'] = colon['STAGE'].replace('two', '2')
colon['STAGE'] = colon['STAGE'].replace('three', '3')
colon['STAGE'] = colon['STAGE'].replace('four', '4')
colon['STAGE']= pd.to_numeric(colon['STAGE'])


colon.drop(['PERIOD'],axis=1,inplace=True)
colon.to_csv('newdataset_classification1.csv', index=False)
