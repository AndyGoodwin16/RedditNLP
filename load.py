import pandas as pd
import json
counter = 1


#read the json file into multiple chunks of 10000 lines
chunks = pd.read_json('corpus-webis-tldr-17.json', lines=True, chunksize = 100000)


dfs_subredit = []
dfs_authors = []
dfs_authors_subreddit = []
chunk_size = 0

for chunk in chunks:
    #number of posts by author in each chunk
    df_authors = chunk.groupby(['author']).size().reset_index(name='counts')
    dfs_authors.append(df_authors)

    #number of posts by subreddit in each chunk
    df_subreddit = chunk.groupby(['subreddit']).size().reset_index(name='counts')
    dfs_subredit.append(df_subreddit)

    #number of category by author
    df_authors_subreddit = chunk.groupby(["author","subreddit"]).size().reset_index(name='counts')
    dfs_authors_subreddit.append(df_authors_subreddit)

    print(counter)
    counter+=1
    chunk_size= chunk_size+ chunk.shape[0]

#concatenat dataframes to get the Total of authors and subreddit 
resu_authors  = pd.concat(dfs_authors).groupby(['author']).sum().reset_index()
resu_subreddit  = pd.concat(dfs_subredit).groupby(['subreddit']).sum().reset_index()
resu_auth_subreddit  = pd.concat(dfs_authors_subreddit).groupby(["author","subreddit"]).sum().reset_index()
_resu_auth_subreddit  = pd.concat(dfs_authors_subreddit).groupby(["author"]).sum().reset_index()

d = {'Category': ["nb_posts","nb_authors","nb_subreddit"], 'count': [chunk_size,resu_authors.shape[0],resu_subreddit.shape[0]]}
df_stats = pd.DataFrame(data=d)

#Write the results into separate csv files 

resu_authors.to_csv("./posts_by_subreddit/posts_by_authors_concat.csv", index=None)
resu_subreddit.to_csv("./posts_by_subreddit/posts_by_subreddit_concat.csv", index=None)
resu_auth_subreddit.to_csv("./posts_by_subreddit/posts_by_authors_subreddit.csv", index=None)
df_stats.to_csv("./posts_by_subreddit/stats.csv", index=None)
_resu_auth_subreddit.to_csv("./posts_by_subreddit/_posts_by_authors_subreddit.csv", index=None)





