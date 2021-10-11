from Buscador.util.consultaAmadeus import *

a=buscador.consultarAmadeus('BOG','CTG','2021-12-15','2021-12-16',1)
print(a['data'][1]['id'])