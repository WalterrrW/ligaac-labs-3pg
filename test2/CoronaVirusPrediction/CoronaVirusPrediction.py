import numpy
import numpy as np
import matplotlib.pyplot as plt


def get_first_pos(periods, coef):
    for elem in range(0, len(periods)):
        if round(coef[0] * pow(periods[elem], 2) + coef[1] * periods[elem] + coef[2], 1) >= 0:
            return periods[elem]


def get_second_neg_if_exists(periods, coef):
    decide = False
    for elem in range(0, len(periods)):
        if round(coef[0] * pow(periods[elem], 2) + coef[1] * periods[elem] + coef[2], 1) <= 0:
            decide = True
        elif round(coef[0] * pow(periods[elem], 2) + coef[1] * periods[elem] + coef[2], 1) >= 0 and decide:
            return periods[elem]
    return 0


def get_starting_day(periods, coef):
    count = 0
    if round(coef[0] * pow(periods[count], 2) + coef[1] * periods[count] + coef[2], 1) < 0:
        return get_first_pos(periods, coef)
    else:
        return get_second_neg_if_exists(periods, coef)


def predict_cases(periods, cases, coef, country):
    count = 0
    startingDate = get_starting_day(periods, coef)
    try:
        while True:
            day = int(input(f"\nEnter values greater than {startingDate} (or '0' to stop): "))
            if day == 0:
                break;
            elif day < startingDate:
                print(f"Please, enter values greater than {startingDate}!")
            else:
                future_cases_for_day = int(coef[0] * pow(day, 2) + coef[1] * day + coef[2])
                print(f"{future_cases_for_day} cases predicted in {country} on {day} day.")
    except:
        print("Unexpected error, try again!")
        predict_cases(periods, cases, coef, country)


def past_plot(periods, cases):
    coefficients = np.polyfit(periods, cases, 2)
    poly = np.poly1d(coefficients)
    new_x = np.linspace(periods[0], periods[-1])
    new_y = poly(new_x)
    plt.plot(periods, cases, "o", new_x, new_y)
    plt.xlim([periods[0] - 1, periods[-1] + 1])
    plt.show()


def create_plot(periods, cases, coef, country):
    prediction = [x for x in range(periods[-1] + 5, 2 * periods[-1], 5)]
    # print(prediction)

    count = 0
    while count < len(prediction):
        periods.append(prediction[count])
        cases.append(round(coef[0] * pow(prediction[count], 2) + coef[1] * prediction[count] + coef[2], 1))
        count += 1
    # print(periods)
    # print(cases)

    coefficients = np.polyfit(periods, cases, 3)

    poly = np.poly1d(coefficients)

    new_x = np.linspace(periods[0], periods[-1])

    new_y = poly(new_x)

    plt.plot(periods, cases, "o", new_x, new_y)

    plt.xlim([periods[0] - 1, periods[-1] + 1])

    plt.xlabel('Days')
    plt.ylabel('Cases')

    plt.show()

    # plt.savefig("C:/Users/sipos/OneDrive/Desktop/CoronaVirusProj/"+country+".png")


def calculate_coefficients(matrix1, finalMatrix):
    detOfMatrix1 = np.linalg.det(matrix1)

    buffermatrix = matrix1.copy()
    buffermatrix[:, 0] = finalMatrix
    detA = round(np.linalg.det(buffermatrix) / detOfMatrix1)

    buffermatrix = matrix1.copy()
    buffermatrix[:, 1] = finalMatrix
    detB = round(np.linalg.det(buffermatrix) / detOfMatrix1)

    buffermatrix = matrix1.copy()
    buffermatrix[:, 2] = finalMatrix
    detC = round(np.linalg.det(buffermatrix) / detOfMatrix1, 4)

    return [detC, detB, detA]


def calculate_values(mylist, power):
    mylist = [x ** power for x in mylist]
    return sum(mylist)


def calculate_final_values(periods, cases, power):
    periods = [x ** power for x in periods]
    for x in range(0, len(cases)):
        cases[x] = cases[x] * periods[x]
    return sum(cases)


def get_coef(periods, casesSpain):
    matrix = numpy.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]], dtype=float)

    matrix[0][0] = len(periods)
    matrix[0][1] = calculate_values(periods, 1)
    matrix[1][0] = calculate_values(periods, 1)
    matrix[1][1] = matrix[0][2] = matrix[2][0] = calculate_values(periods, 2)
    matrix[1][2] = matrix[2][1] = calculate_values(periods, 3)
    matrix[2][2] = calculate_values(periods, 4)

    matrix2 = numpy.array([sum(casesSpain),
                           calculate_final_values(periods, casesSpain.copy(), 1),
                           calculate_final_values(periods, casesSpain.copy(), 2)], dtype=float)

    return calculate_coefficients(matrix, matrix2)


def func(x, A, c, d):
    return A * np.exp(c * x) + d


def read_from_file(path):
    f = open(path, "r")
    periods = []
    cases = []
    for elem in f.readlines():
        s = elem.split(" ")
        periods.append(int(s[0]))
        cases.append(int(s[1]))
    return periods, cases


if __name__ == "__main__":

    # I use PyCharm to write this code and the plots (graphs) will be displayed in the IDE,
    # I also attach them to be seen if plot will not working
    # I cannot figure out how to save automatically the plots(graphs) locally when running this script
    # All of my graph are put in a HTML page and send to you in pack, please set the path's for each graph in the HTML page to see them

    # this program is set to plot and calculate cases in Romania, change it to Spain if you want the other country
    country = "Romania"

    periods = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
    casesRomania = [0, 0, 0, 0, 3, 4, 15, 123, 260, 762, 1760, 3183, 4761, 6633, 8418, 10096, 11616, 13163]
    casesSpain = [1, 2, 2, 2, 32, 198, 1024, 5753, 17147, 39673, 78797, 117710, 146690, 169496, 191726, 213024, 210773,
                  217466]


    # to read from files please uncomment these lines and set the path
    # periods, casesRomania = read_from_file("C:/Users/sipos/OneDrive/Desktop/CoronaVirusProj/casesRomania.dat")
    # print(periods)
    # print(casesRomania)
    #
    # periods, casesSpain = read_from_file("C:/Users/sipos/OneDrive/Desktop/CoronaVirusProj/casesSpain.dat")
    # print(periods)
    # print(casesSpain)

    if country.__eq__("Romania"):
        cases = casesRomania
    else:
        cases = casesSpain

    # calculate the coefficients
    coef = get_coef(periods, cases)

    # plot the graph for past-present cases
    past_plot(periods, cases)

    print(f"My coefficents: {coef}")

    # plot the graph for past-future cases
    create_plot(periods, cases, coef, country)

    # predict the cases base on days given, this value can be track on the future plot graph as well
    predict_cases(periods, cases, coef, country)
