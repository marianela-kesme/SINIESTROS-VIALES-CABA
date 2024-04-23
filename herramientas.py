import pandas as pd

df_hechos = pd.read_excel('homicidios.xlsx', sheet_name='HECHOS')

def mostrarColumnasConNulos(df, decimales=2):
    columnasConNulos = df.columns[df.isnull().any()].tolist()
    dfNulos = df[columnasConNulos]
    dfTotalNulos = pd.DataFrame({
        "columna": dfNulos.columns,
        "numeroDeNulos": dfNulos.isnull().sum(),
        "porcentajeDeNulos": (dfNulos.isnull().sum() / dfNulos.shape[0]) * 100.0
    }, index=None)
    dfTotalNulos["porcentajeDeNulos"] = dfTotalNulos["porcentajeDeNulos"].round(decimales).astype(str) + "%"
    return dfTotalNulos

mostrarColumnasConNulos(df_hechos) 

def imputarSD(df):
    
    for dato in range(len(df)):
        for col in df.columns:
            if df.loc[dato, col] == "SD":
                df.loc[dato, col] = pd.NaT
    return df





def imputarSDSD(df):
    for dato in range(len(df)):
        for col in df.columns:
            if df.loc[dato, col] == "SD-SD":
                df.loc[dato, col] = pd.NaT
    return df