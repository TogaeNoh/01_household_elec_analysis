import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def main():
    # Build Data Set
    df_e = df_electiricity()
    gdf_w = df_geometry()
    df_pop = df_population()

    # Display rows, columns and width in full
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)

    #Merge data
    gdf_join_e_pop=merge(df_pop, df_e, gdf_w)[0]
    gdf_join_e_pop_20=merge(df_pop, df_e, gdf_w)[1]

    #Plotting
    plotting(gdf_join_e_pop, gdf_join_e_pop_20)

def df_electiricity():
    ### dataframe of electiricity of households 2018 ###
    filename1 = 'data/UNdata_Export_Consumption_by_households.csv'

    # Call only columns that are necessary
    df_e = pd.read_csv(filename1)[['Country or Area', 'Year', 'Quantity']]  # Unit : Kilowatt-hours, million
    df_e = df_e[df_e.Year.eq(2018)]

    # Drop off unnecessary columns
    df_e = df_e.drop(columns=['Year'])

    # Rename Columns
    df_e.columns = ['country', 'quantity']

    df_e["country"] = df_e["country"].str.replace("Rep.", "Republic", case=False, regex=False)
    df_e["country"] = df_e["country"].str.replace("Is.", "Islands", case=False,regex=False)
    df_e["country"] = df_e["country"].str.replace("Dem.", "Democratic", case=False, regex=False)
    df_e["country"] = df_e["country"].str.replace("St.", "Saint", case=False, regex=False)
    df_e["country"] = df_e["country"].str.replace("Ppl's", "People's", case=False, regex=False)
    df_e["country"] = df_e["country"].str.replace("Fed.", "Federal", case=False, regex=False)

    df_e.replace(to_replace='Bolivia (Plur. State of)', value='Bolivia', inplace=True)
    df_e.replace(to_replace='Cabo Verde', value='Cape Verde', inplace=True)
    df_e.replace(to_replace='Czechia', value='Czech Republic', inplace=True)
    df_e.replace(to_replace='Micronesia (Fed. States of)', value='Micronesia, Federated States of', inplace=True)
    df_e.replace(to_replace="C??te d'Ivoire", value="Cote d'Ivoire", inplace=True)
    df_e.replace(to_replace="China, Hong Kong SAR", value="Hong Kong", inplace=True)
    df_e.replace(to_replace="Faeroe Islands", value="Faroe Islands", inplace=True)
    df_e.replace(to_replace="China, Macao SAR", value="Macau", inplace=True)
    df_e.replace(to_replace="Korea, DemocraticPeople's.Republic", value="Korea, Democratic People's Republic of", inplace=True)
    df_e.replace(to_replace="Russian Federation", value="Russia", inplace=True)
    df_e.replace(to_replace='Saint Kitts-Nevis', value='Saint Kitts and Nevis', inplace=True)
    df_e.replace(to_replace='State of Palestine', value='Palestine', inplace=True)
    df_e.replace(to_replace='Tanzania', value='United Republic of Tanzania', inplace=True)
    df_e.replace(to_replace='Venezuela (Bolivar. Republic)', value='Venezuela', inplace=True)
    df_e.replace(to_replace='Micronesia (Federal States of)', value='Micronesia, Federated States of', inplace=True)

    return df_e


def df_geometry():
    ### geopanda dataframe ###
    shapefile = 'data\TM_WORLD_BORDERS-0.3/TM_WORLD_BORDERS-0.3.shp'

    # Read shapefile using Geopandas
    gdf = gpd.read_file(shapefile)[['NAME', 'ISO3', 'geometry']]

    # Rename columns.
    gdf.columns = ['country', 'country_code', 'geometry']

    gdf.replace(to_replace='Burma', value='Myanmar', inplace=True)
    gdf.replace(to_replace='The former Yugoslav Republic of Macedonia', value='North Macedonia', inplace=True)
    gdf.replace(to_replace='Libyan Arab Jamahiriya', value='Libya', inplace=True)
    gdf.replace(to_replace='Swaziland', value='Eswatini', inplace=True)

    drop_index = [108,169,212,216,218,219,225,226,229,232,233,234]
    for i in range(140,151):
        drop_index.append(int(i))
    for i in range(239,246):
        drop_index.append(int(i))
    drop_index.sort()

    gdf.drop(gdf.index[gdf['country'] == 'Tokelau'], inplace=True)
    gdf = gdf.drop(drop_index)

    # These countries are dropped due to non-existing data (elec consumpsion or population)
    #                       Martinique
    #                           Mayotte
    #                    Åland Islands
    #                   Norfolk Island
    #          Cocos (Keeling) Islands
    #                       Antarctica
    #                    Bouvet Island
    # French Southern and Antarctic Lands
    # Heard Island and McDonald Islands
    #   British Indian Ocean Territory
    #                 Christmas Island
    # United States Minor Outlying Islands
    # Reunion
    #  Tokelau
    #  Saint Vincent and the Grenadines
    #  United States Virgin Islands
    # Wallis and Futuna Islands, Samoa
    #                            Svalbard
    #                        Saint Martin
    #                    Saint Barthelemy
    #                            Guernsey
    #                              Jersey
    # South Georgia South Sandwich Islands
    #                              Taiwan'''
    return gdf

def df_population():
    ### dataframe widipedia world population ###
    df_pop = pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)')[0]  # [0] : list -> dataframe

    # Drop off unnecessary columns
    df_pop = df_pop.drop(columns=['UN continentalregion[4]',
                                      'UN statisticalsubregion[4]',
                                      'Population(1 July 2019)',
                                      'Change'])
    # Rename the columns
    df_pop.columns = ['country', 'population']

    # delete remark such as [a]
    for index, row in df_pop.iterrows():
        if '[' and '(' in row['country']:
            int_index = row['country'].index('(')
            old_str = str(row['country'])
            new_str = str(row['country'][:(int_index-1)])
            df_pop.replace(to_replace=old_str, value=new_str, inplace=True)
        elif '[' in row['country']:
            old_str = str(row['country'])
            new_str = str(row['country'][:-3])
            df_pop.replace(to_replace=old_str, value=new_str, inplace=True)
        elif '(' in row['country']:
            int_index = row['country'].index('(')
            old_str = str(row['country'])
            new_str = str(row['country'][:(int_index-1)])
            df_pop.replace(to_replace=old_str, value=new_str, inplace=True)

    df_pop.replace(to_replace='Brunei', value='Brunei Darussalam', inplace=True)
    df_pop.replace(to_replace='DR Congo', value='Democratic Republic of the Congo', inplace=True)
    df_pop.replace(to_replace='Falkland Islands', value='Falkland Islands (Malvinas)', inplace=True)
    df_pop.replace(to_replace='F.S. Micronesia', value='Micronesia, Federated States of', inplace=True)
    df_pop.replace(to_replace='Iran', value='Iran (Islamic Republic of)', inplace=True)
    df_pop.replace(to_replace='Ivory Coast', value="Cote d'Ivoire", inplace=True)
    df_pop.replace(to_replace='North Korea', value="Korea, Democratic People's Republic of", inplace=True)
    df_pop.replace(to_replace='South Korea', value='Korea, Republic of', inplace=True)
    df_pop.replace(to_replace="Laos", value="Lao People's Democratic Republic", inplace=True)
    df_pop.replace(to_replace='State of Palestine', value='Palestine', inplace=True)
    df_pop.replace(to_replace='Moldova', value='Republic of Moldova', inplace=True)
    df_pop.replace(to_replace='Syria', value='Syrian Arab Republic', inplace=True)
    df_pop.replace(to_replace='São Tomé and Príncipe', value='Sao Tome and Principe', inplace=True)
    df_pop.replace(to_replace='East Timor', value='Timor-Leste', inplace=True)
    df_pop.replace(to_replace='Vietnam', value='Viet Nam', inplace=True)
    df_pop.replace(to_replace='Tanzania', value='United Republic of Tanzania', inplace=True)

    return df_pop

def merge(df_pop,df_e,gdf_w):

    gdf_join_pop = gdf_w.merge(df_pop,
                             on='country',
                             how='left')

    gdf_join_e_pop = gdf_join_pop.merge(df_e,
                           on='country',
                           how='left')

    # Insert Population data of Vatican City into gdf_join_e_pop
    gdf_join_e_pop.loc[gdf_join_e_pop.country == 'Holy See (Vatican City)', "population"] = 801

    gdf_join_e_pop['Q/P'] = gdf_join_e_pop.quantity/gdf_join_e_pop.population*1000000

    gdf_join_e_pop.sort_values(by=['Q/P'], inplace=True,ascending=False)
    gdf_join_e_pop_20 = gdf_join_e_pop.head(20)

    gdf_join_e_pop.sort_values(by=['quantity'], inplace=True,ascending=False)

    return gdf_join_e_pop, gdf_join_e_pop_20

def plotting(gdf_join_e_pop, gdf_join_e_pop_20):
    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()
    fig1.set_size_inches(8, 6)
    fig2.set_size_inches(8, 6)

    ax1.set_title('Electricity Consumption in Households per Capita', fontsize=14)
    gdf_join_e_pop.plot(column='Q/P',
                  ax=ax1,
                  legend=True,
                    cmap='gist_rainbow',
                  legend_kwds={'label': "Kilowatt-hours",
                               'orientation': "horizontal"})

    ax2.bar(gdf_join_e_pop_20['country'], gdf_join_e_pop_20['Q/P'], color='blue')
    ax2.set_xlabel('Country', fontsize=14)
    ax2.set_ylabel('Kilowatt-hours', fontsize=14)
    ax2.set_xticks(gdf_join_e_pop_20['country']) #This line of code prevents from error. 'set_xticks' has to come before set_'set_xticklabels'
    ax2.set_xticklabels(labels =gdf_join_e_pop_20['country'].tolist(), rotation = 80 ) #labels take list object
    ax2.set_title('Top 20 countries in Electiricity consumption in households per capita', fontsize=14)

    plt.tight_layout() #This line helps to show long names of countries(x axis)
    plt.show()
    
if __name__ == '__main__':
    main()