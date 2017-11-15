'''Printing module
'''
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

DATE_FORMAT = "%Y-%m-%d"

def print_popularity(candidates_list):
    '''Plots candidates popularity
    '''

    '''
    candidates_list = {
        "A":[("2017-10-01",10),("2017-10-02",12)],
        "B":[("2017-10-01",8),("2017-10-02",15)]
    }
    '''

    plt.clf()
    plt.xlabel("Days")
    plt.ylabel("Popularity")
    plt.title("Last 10 days")
    plt.grid(True)
    

    for candidate, items_list in candidates_list.items():
        y = []
        dates = []
        print(candidate)
        for date, value in items_list:
            dates.append(date)
            y.append(value)
        x = [dt.datetime.strptime(d, DATE_FORMAT).date() for d in dates]
        print(x)
        print(y)

        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter(DATE_FORMAT))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator())
        plt.plot(x,y, label = str(candidate))
        plt.gcf().autofmt_xdate()
        #plt.plot_date(x, y, fmt=DATE_FORMAT, xdate=True, label=str(candidate))

    plt.legend()
    plt.show()

def main():
    '''Main function
    '''
    #print_popularity(None)

if __name__ == '__main__':
    main()