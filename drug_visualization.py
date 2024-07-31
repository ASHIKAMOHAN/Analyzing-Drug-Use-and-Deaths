import pandas as pd
import matplotlib.pyplot as plt

# specifiying the column names and reading the csv file
drug_frequency = ['age', 'alcohol-frequency', 'marijuana-frequency', 'cocaine-frequency',
                  'crack-frequency', 'oxycontin-frequency', 'tranquilizer-frequency', 'stimulant-frequency',
                  'meth-frequency', 'sedative-frequency']
drugs = pd.read_csv(
    "drug/drug-use-by-age.csv", usecols=drug_frequency)
# setting 'age' as the index
drugs.set_index('age', inplace=True)
print(drugs)


def PlotLineGraph(data, x_col, y_col, title, legend):
    """
    Plotting a line graph using the given data.
    Arguments:
    data:pandas DataFrame-contains data to be plotted
    x_col:str-column name for the x axis
    y_col:str-column name for the y axis
    title:str-title for the line plot
    legend:str-legend for the line plot

    Returns:
    None
    """
    # Extracting x data for the x-axis
    x_data = data.index
    # Plotting data using plt.plot
    plt.figure(figsize=(10, 6))
    plt.plot(x_data, data['alcohol-frequency'], label="Alcohol Frequency")
    plt.plot(x_data, data['marijuana-frequency'], label="Marijuana Frequency")
    plt.plot(x_data, data['tranquilizer-frequency'],
             label="Tranquilizer Frequency")
    plt.plot(x_data, data['stimulant-frequency'], label="Stimulant Frequency")
    plt.plot(x_data, data['sedative-frequency'], label="Sedative Frequency")

    # Labelling x and y axes,adding title to the graph,and displaying the graph legend
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(title, size=18)
    plt.legend()
    plt.show()


# calling the PlotLineGraph with the data and column name
PlotLineGraph(drugs, 'age', 'Frequency',
              'Drug use by age', 'Frequency')

# specifiying the column names and reading the csv file
drug_use = ['age', 'alcohol-use', 'marijuana-use', 'cocaine-use', 'crack-use',
            'oxycontin-use', 'tranquilizer-use', 'stimulant-use', 'meth-use', 'sedative-use']
drugs = pd.read_csv(
    "drug/drug-use-by-age.csv", usecols=drug_use)
# setting 'age' as the index
drugs.set_index('age', inplace=True)
# computing sum of values of each column
total_usage = drugs.sum()
# Extracting the top five values
top_five = total_usage.nlargest(5)
# calculating the cumulative total of drug usage taht falls outside the top five values
top_five['others'] = total_usage.sum()-top_five.sum()


def plotpie(drug_use):
    """Plotting a piechart showing usage of drugs by age using specified columns
    Arguments:
    drug_use:list-list of column names indicating the drug usage

    Returns:
    None
    """
    # Plotting the data
    plt.figure()
    plt.pie(top_five, labels=top_five.index, autopct='%1.1f%%')
    plt.title('Drug Usage distribution by drug category')
    plt.show()


# calling the Plotpie with the data
plotpie(drug_use)

drug_deaths = pd.read_csv(
    "drug/drug_deaths.csv")


def PlotBarGraph(data):
    """plotting bar graph using the given data and column names.
    Arguments:
    data:pandas DataFrame-contains the data to be plotted

    Returns:
    None
    """
    age_counts = drug_deaths['Age'].value_counts().sort_index()
    # Plotting bar graph for the 'Age' column
    plt.figure(figsize=(10, 6))
    plt.bar(age_counts.index, age_counts.values)
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.title('Drug Deaths over Ages')

    plt.tight_layout()
    plt.show()


# calling the PlotBaarGraph with the data
PlotBarGraph(drug_deaths)
