# Baby name explorer
My wife and I are expecting twin girls in the fall and could not find a tool that would let us view the combined popularity of spelling varients of names. For example, would Sarah + Sara push the name into the top 5 in popularity in a given year? 

Being the data nerds we are, we built this little utility.

## Setting up your search
You can add names to the list name_to_plot to plot them

Specify if you want to include male, female, or both names

Set show_sum to True if you want to add the name frequencies together. Set to false if not

If you like, you set the top n names to add to the plot (so top 10 or 20 in a given year). Set this to zero to not plot top names.

You can also limit the years that show the top names (note that in the mid century the top names were VERY frequent)

Finally, if you like you can see names that were similar in popularity to your query.

## Data source
The data used here is compiled from [this dataset from the Social Security Administration](https://www.ssa.gov/oact/babynames/limits.html)

## Other info
This uses pandas and plotly to munge and plot the data. Enjoy!