import pandas as pd
from matplotlib import pyplot as plt


class MobileDataStatistics:

    def __init__(self):
        self.mobile = pd.read_csv("mobile-data-usage.csv", encoding='cp1252')

        YM = self.mobile["quarter"].str.split("-", n=1, expand=True)
        self.mobile = self.mobile.assign(Year=YM[0])
        self.mobile = self.mobile.assign(Quarter=YM[1])

        plt.style.use("dark_background")

    def viewData(self):
        print(self.mobile)

    def viewUsageByYear(self, year):
        yearStats = self.mobile[self.mobile["Year"] == str(year)]
        print(yearStats)

    def viewTotalUsageByYear(self, year):
        yearStats = self.mobile[self.mobile["Year"] == str(year)].groupby("Year").sum().reset_index()
        print(yearStats)

    def plotLineChartByYear(self, year):
        yearStats = self.mobile[self.mobile["Year"] == str(year)]

        plt.plot(yearStats["Quarter"], yearStats["volume_of_mobile_data"], label=year)
        plt.title("Mobile Usage in " + str(year))
        plt.xlabel("Year")
        plt.ylabel("Volume of Mobile Data")
        plt.legend()
        plt.show()
        #plt.savefig("linechart.png")

    def barChartByYear(self):
        yearStats = self.mobile.groupby("Year").sum().reset_index()

        plt.bar(yearStats["Year"], yearStats["volume_of_mobile_data"])
        plt.title("Mobile Usage by Year")
        plt.xlabel("Year")
        plt.ylabel("Volume of Mobile Data")
        plt.show()
        #plt.savefig("barchart.png")

    def pieChartByYear(self):
        yearStats = self.mobile.groupby("Year").sum().reset_index()

        plt.pie(yearStats["volume_of_mobile_data"], labels=yearStats["Year"])
        plt.show()
        #plt.savefig("piechart.png")

    def scatterChart(self):

        plt.scatter(self.mobile["Year"], self.mobile["volume_of_mobile_data"])
        plt.title("Mobile Usage by Year")
        plt.xlabel("Year")
        plt.ylabel("Volume of Mobile Data")
        plt.show()
        #plt.savefig("scatterchart.png")



# USE THE FOLLOWING CODE TO TEST YOUR SOLUTION OUT

mds = MobileDataStatistics()
mds.viewData()
mds.viewUsageByYear(2012)
mds.viewTotalUsageByYear(2012)
mds.plotLineChartByYear(2012)
mds.barChartByYear()
mds.pieChartByYear()
mds.scatterChart()


