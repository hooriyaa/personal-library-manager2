import pandas as pd

# 📌 Convert MySQL Data to Pandas DataFrame
def convert_to_dataframe(data):
    df = pd.DataFrame(data, columns=["ID", "Title", "Author", "Publication Year", "Genre", "Status", "Rating", "Summary", "Added On"])
    return df

