import WeatherAnalyzer
from matplotlib import pyplot as plt

def main():
    data=WeatherAnalyzer.data_processing("105嬰兒出生數按生母原屬國籍.json")
    data.create_newdata("台北市")
    data.create_newdata("新北市")
    data.create_newdata("台南市")
    data.create_newdata("台中市")
    data.create_newdata("高雄市")
    plt.bar(data.newdata.keys(),data.newdata.values())
    plt.title('105年新生兒')
    plt.xlabel('城市')
    plt.ylabel('嬰兒數')
    
    plt.show()

    print("")



if __name__ == "__main__":
    main()