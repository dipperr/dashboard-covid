import pandas as pd


def casos_novos_regiao(dframe, col):
    df = pd.DataFrame([])

    for r in dframe.regiao.unique().tolist():
        for e in dframe[dframe.regiao == r].estado.unique().tolist():
            df = pd.concat(
                [
                    df,
                    (
                        dframe[(dframe.regiao == r) & (dframe.estado == e)][['data', col]]
                        .set_index(keys='data').resample('M').sum().assign(estado=e, regiao=r)
                    )
                ]
            )
    df.reset_index(inplace=True)
    return df