import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score,roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV, cross_validate
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import warnings
warnings.simplefilter(action="ignore")

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 170)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

################################################################################
# 1.ADIM: VERİ SETİ SECİMİ : Airline_Passenger_Satisfaction
################################################################################

#veri setini yükleme

df = pd.read_csv("train.csv")

#veri setine kısa bir bakış ve bilgi alma
df.head()
df.info()

#veri setine genel bir bakış
def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Tail #####################")
    print(dataframe.tail(head))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())


check_df(df)
################################################################################
# 2.ADIM: İSTATİSTİKSEL ÖZET
################################################################################
# istatiklerle veri setimiz

sayisal_df = df.select_dtypes(include=["float64", "int64"])

# Temel istatistikleri getir
temel_istatistikler = sayisal_df.describe().T  # .T satır-sütun çevirir, okunabilirlik için

# Medyan sütunu da ekle
temel_istatistikler["medyan"] = sayisal_df.median()

# IQR (Q3 - Q1) ekle
temel_istatistikler["IQR"] = temel_istatistikler["75%"] - temel_istatistikler["25%"]

# Raporu göster
print(temel_istatistikler)

################################################################################
# 3.ADIM: EKSİK DEĞER ANALİZİ
################################################################################


#eksik değer sayımız
df.isnull().sum()
#eksik değer detay
def missing_values_table(dataframe, na_name=False):
    na_columns = [col for col in dataframe.columns if dataframe[col].isnull().sum() > 0]
    n_miss = dataframe[na_columns].isnull().sum().sort_values(ascending=False)
    ratio = (dataframe[na_columns].isnull().sum() / dataframe.shape[0] * 100).sort_values(ascending=False)
    missing_df = pd.concat([n_miss, np.round(ratio, 2)], axis=1, keys=['n_miss', 'ratio'])
    print(missing_df, end="\n")
    if na_name:
        return na_columns

na_columns = missing_values_table(df, na_name=True)

#eksik değerleri olan sutunumuzun veri setindeki durumu
df["Arrival Delay in Minutes"].hist()

#medyan ile doldurma
df["Arrival Delay in Minutes"].fillna(df["Arrival Delay in Minutes"].median(), inplace=True)

#eksik deger ikinci kontrol
df.isnull().sum()

################################################################################
# 4.ADIM: AYKIRI DEGER(OUTLİER) ANALİZİ
################################################################################

def aykiri_degerleri_bul_iqr(veri, grafik_goster=False):
    aykiri_ozet = {}

    for sutun in veri.select_dtypes(include=['float64', 'int64']).columns:
        q1 = veri[sutun].quantile(0.25)
        q3 = veri[sutun].quantile(0.75)
        iqr = q3 - q1
        alt_sinir = q1 - 1.5 * iqr
        ust_sinir = q3 + 1.5 * iqr

        aykirilar = veri[(veri[sutun] < alt_sinir) | (veri[sutun] > ust_sinir)]
        aykiri_ozet[sutun] = aykirilar.shape[0]

        if grafik_goster:
            import seaborn as sns
            import matplotlib.pyplot as plt
            sns.boxplot(x=veri[sutun])
            plt.title(f"{sutun} - Kutu Grafiği (Boxplot)")
            plt.show()

    return pd.DataFrame.from_dict(aykiri_ozet, orient='index', columns=["aykiri_sayisi"]).sort_values(
        by="aykiri_sayisi", ascending=False)

aykiri_rapor = aykiri_degerleri_bul_iqr(df, grafik_goster=False)
print(aykiri_rapor)

# Aykırı değer içeren sütunlar
aykiri_sutunlar = [
    "Departure Delay in Minutes",
    "Arrival Delay in Minutes",
    "Checkin service",
    "Flight Distance"
]

# Her sütun için ayrı kutu grafiği çiz
for sutun in aykiri_sutunlar:
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df[sutun])
    plt.title(f"{sutun} - Aykırı Değerler Kutu Grafiği")
    plt.xlabel(sutun)
    plt.grid(True)
    plt.show()


################################################################################
# 5.ADIM: GORSELLESTİRME
################################################################################

# Sayısal degiskenlerin görsellestirilmesi

sayisal_sutunlar = [
    "Age", "Flight Distance",
    "Departure Delay in Minutes",
    "Arrival Delay in Minutes"
]

for sutun in sayisal_sutunlar:
    plt.figure(figsize=(7, 4))
    df[sutun].hist(bins=40)
    plt.title(f"{sutun} - Histogram")
    plt.xlabel(sutun)
    plt.ylabel("Frekans")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

#Kategorik degiskenlerin gorsellestirilmesi

kategorik_sutunlar = []

for sutun in df.columns:
    if df[sutun].dtype == "O":
        kategorik_sutunlar.append(sutun)
    elif df[sutun].nunique() < 10:
        kategorik_sutunlar.append(sutun)

print("Kategorik değişkenler:")
print(kategorik_sutunlar)

kategorik_sutunlarr = ["Gender", "Customer Type", "Type of Travel", "Class", "satisfaction"]

for sutun in kategorik_sutunlarr:
    plt.figure(figsize=(6, 4))
    sns.countplot(x=df[sutun])
    plt.title(f"{sutun} - Sayım Grafiği")
    plt.xticks(rotation=30)
    plt.grid(True)
    plt.tight_layout()
    plt.show()



