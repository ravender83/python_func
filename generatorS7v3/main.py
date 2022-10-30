#-------------------------------------------
#	Date:			2022.10.30
#	Author:			Piotr Ślęzak
#	
#	ToDo:
#		-
#-------------------------------------------
import pandas as pd
columns = ['PREFIX', 'NAME', 'NAMEPL', 'ADRES', 'GROUP', 'ID', 'MSG_PL_HP', 'MSG_PL_WP', 'MSG_EN_HP', 'MSG_EN_WP']

def main(args):
	df = pd.read_excel(args, sheet_name=None)
	print(df['Mechanizmy'])
	print('===== Koniec =====')
	return 0


if __name__ == '__main__':
    main('LK03.xlsx')
    # main(sys.argv)
