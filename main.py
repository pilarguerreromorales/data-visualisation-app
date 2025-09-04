from graphics import GraphWin

from program import startButton, DisplayMenu, RegionMenu, inputTitle, population_piechart, education_graph, \
    life_expectancy, total_population, CountryMenu, country_population, End_or_Repeat, LoadData


def main():
    win = GraphWin("Regions Insights", 500, 500)
    win.setCoords(0.0, 0.0, 4.0, 4.5)
    win.setBackground('white')

    demographics_table, humancapital_table, country_data = LoadData()

    startButton(win)

    while True:
        selection = DisplayMenu(win)

        if selection == "region":
            plot, region = RegionMenu(win)

            if plot == 1:
                title = inputTitle(win)
                population_piechart(demographics_table, region, title)

            if plot == 2:
                title = inputTitle(win)
                education_graph(humancapital_table , region, title)

            if plot == 3:
                title= inputTitle(win)
                life_expectancy(demographics_table, title)

            if plot == 4:
                title = inputTitle(win)
                total_population(demographics_table, title)

        elif selection == "country":
            country = CountryMenu(win)
            title = inputTitle(win)
            country_population(country_data , country, title)



        value = End_or_Repeat(win)

        if value ==1:
            continue
        elif value == 2:
            break


if __name__ == "__main__":
    main()

