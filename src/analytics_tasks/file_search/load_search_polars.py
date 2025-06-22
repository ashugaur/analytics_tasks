import os
import polars as pl


def load_search_polars(scan_dir):
    """loads search index into a polars datafame"""

    print("\nLoading search index...")

    # change working directory
    os.chdir((scan_dir).replace("\\", "/"))

    # import scan
    scan0 = pl.read_parquet("scan0.parquet")
    searchx_final = pl.read_parquet("searchx_final.parquet")

    # scan0 = pd.read_pickle('scan0.pickle')
    # searchx_final = pd.read_pickle('searchx.pickle')

    # scan0 = pl.read_csv(r'scan0.csv')
    # searchx_final = pl.read_csv(r'searchx.csv')

    # import edupunk multimeda
    # em = pd.read_pickle('df_zip_edupunk_multimedia.pickle')
    # em['ext'] = em["unc"].apply(lambda row: os.path.splitext(os.path.basename(row))[1])

    # searchx = pd.merge(scan0, searchx_final, how='left', on='uf_id')
    try:
        searchx = scan0.join(
            searchx_final, left_on="uf_id", right_on="uf_id", how="left"
        )
    except:
        scan0 = scan0.with_columns(scan0["uf_id"].cast(pl.Int64))
        searchx_final = searchx_final.with_columns(
            searchx_final["uf_id"].cast(pl.Int64)
        )
        searchx = scan0.join(
            searchx_final, left_on="uf_id", right_on="uf_id", how="left"
        )
        print("ERROR       : The format for uf_id field may be inconsistent.")

    # searchx = pd.concat([searchx, em])
    # searchx = searchx.sort_values(by=['lastwritetime', 'creationtime'], ascending=False) #sort
    searchx = searchx.sort("lastwritetimeutc").reverse()
    print("Estimated size:", searchx.estimated_size(unit="mb"), "MB")

    return searchx

    del [scan0, searchx_final]

    print("\nsearchx loaded...")
