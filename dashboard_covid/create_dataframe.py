import pandas as pd
import glob
import warnings

warnings.filterwarnings('ignore')


class CreateDf:

    def get_names_files(self, regpath):
        return glob.glob(regpath)

    def read_csv(self, regpath):
        dframe = pd.DataFrame([])
        for a in self.get_names_files(regpath):
            dframe = pd.concat([dframe, pd.read_csv(a, sep=';')])
        return dframe


class DataFrame:
    def __init__(self):
        self.__dframe = CreateDf().read_csv('./datasets/*.csv')

    def format(self):
        self.__dframe.drop(
            labels=['municipio', 'codmun', 'codRegiaoSaude', 'nomeRegiaoSaude', 'semanaEpi', 'interior/metropolitana',
                    'populacaoTCU2019', 'coduf'],
            axis=1, inplace=True
        )
        brasil = self.__dframe.query("regiao == 'Brasil'").drop(labels=['estado'], axis=1) \
            .reset_index(drop=True).copy()

        regiao = self.__dframe.query("regiao != 'Brasil'").reset_index(drop=True) \
            .dropna(axis=1, how='all').copy()

        del self.__dframe

        for df in [brasil, regiao]:
            df.loc[:, 'data'] = pd.to_datetime(df.loc[:, 'data'])

        return brasil, regiao

