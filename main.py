import argparse
import json
import ssl
import plotext as plt
import urllib.request, urllib.error

# ignore SSL certificate error
cont = ssl.create_default_context()
cont.check_hostname = False
cont.verify_mode = ssl.CERT_NONE


class PlotGrowth(object):

    """
    This class is used to visualize the number of active users with respect to the date by plotting a graph.

    input parameters:
    url : This is the url endpoint that contains the data needed.
    start_date: used to filter the data to get the first date needed.
    end_date: used to filter the data to get the last date needed.
    """

    def __init__(self, url, start_date, end_date):
        self.url = url
        self.start_date = start_date
        self.end_date = end_date
        self.keys = None
        self.dates = []
        self.users = []

    def request_data(self):
        api = urllib.request.urlopen(self.url, context=cont)
        assert api.getcode() == 200, "status code is not 200, received status code is {}".format(api.getcode())
        data = api.read().decode()
        data = json.loads(data)
        return data

    def plot(self):
        plt.bar(self.dates, self.users)
        plt.title("Growth of Users")
        plt.clc()
        plt.plotsize(100, 20)
        plt.show()

    def extract_data(self, data):
        flag = False
        for date in self.keys:
            if flag:
                self.dates.append(date)
                self.users.append(data[date])

                if date == self.end_date:
                    flag = False
            else:
                if date == self.start_date:
                    self.dates.append(date)
                    self.users.append(data[date])
                    flag = True
        return

    def plot_growth(self):

        data = self.request_data()
        self.keys = list(data.keys())

        assert self.start_date in self.keys, 'Data for years before {} is not available'.format(self.keys[0])
        assert self.end_date in self.keys, 'Data for years after {} is not available'.format(self.keys[-1])

        self.extract_data(data)

        self.plot()


if __name__ == '__main__':
    # initializing parser
    parser = argparse.ArgumentParser(description='Userbase Growth .', epilog='Enjoy the view!')

    # adding optional arguments
    parser.add_argument('Start_date', type=str, help='the start date you would like to check from')
    parser.add_argument('End_date', type=str, help='the end date you would like to check to')

    # read arguments from the commandline
    args = parser.parse_args()

    # API endpoint
    url = ' http://sam-user-activity.eu-west-1.elasticbeanstalk.com/ '

    results = PlotGrowth(url, args.Start_date, args.End_date)
    results.plot_growth()
