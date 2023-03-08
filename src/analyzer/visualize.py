import matplotlib.pyplot as plt

def drawplot(prepared_data, linreg):
    prices, volumes = prepared_data

    plt.scatter(prices, volumes)
    ax = plt.gca()
    ax.set_xlabel('Price')
    ax.set_ylabel('Volume')
    plt.plot(prices, linreg.intercept_ + linreg.coef_*prices, color='r')

    return linreg.coef_[0]
