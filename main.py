import math
import random


# вычисляю реальный выход функции
def real_out_function(x):
    return math.exp(x - 2) - math.sin(x)


class function:
    begin_coordinate_x = -100
    end_coordinate_x = 200

    # инициализирую все координаты х с которыми буду работать
    def __init__(self):
        self.coordinates_x = []
        for it in range(self.begin_coordinate_x, self.end_coordinate_x, 15):
            self.coordinates_x.append(it / 100)

    # возвращаю все координаты х
    def get_all_coordinate_x(self):
        return self.coordinates_x

    # возвращаю координату x по ее индексу
    def get_coordinate_x(self, index):
        return self.coordinates_x[index]


# вычисляю ошибку прогноза
def predicted_error(real_coordinate, predicted_coordinate):
    return real_coordinate - predicted_coordinate


class neuron:
    def __init__(self):
        self.weights = [random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1),
                        0]

    # возвращаю веса нейрона
    def get_weights(self):
        return self.weights

    # корректирую веса для новой эпохи
    def update_weights(self, training_standard, error, vector_coordinate):
        for it in range(0, 4):
            self.weights[it] = self.weights[it] + training_standard * error * vector_coordinate[it]

    # вычисляю прогнозируемое значение (координату)
    def predicted_coordinate(self, coordinate):
        predicted_coordinate = 0
        for it in range(0, 4):
            predicted_coordinate += self.weights[it] * coordinate[it]
        predicted_coordinate += self.weights[4]
        return predicted_coordinate


# функция запуска нейронной сети
def start():
    my_neuron = neuron()
    my_function = function()
    neurons_count = 4
    training_standard = 1
    required_quadratic_error = 2
    epoch_number = 0
    while True:
        now_number_iteration = 0
        max_number_iteration = 20 - neurons_count
        quadratic_error = 0
        while now_number_iteration != max_number_iteration:
            vector_coordinate = []
            for it in range(4):
                vector_coordinate.append(my_function.get_coordinate_x(now_number_iteration + it))
            predicted_coordinate = my_neuron.predicted_coordinate(vector_coordinate)
            real_math_coordinate = real_out_function(
                my_function.get_coordinate_x(now_number_iteration + neurons_count))
            error = predicted_error(real_math_coordinate, predicted_coordinate)
            my_neuron.update_weights(training_standard, error, vector_coordinate)
            now_number_iteration += 1
            quadratic_error += (real_math_coordinate - predicted_coordinate) ** 2
        quadratic_error = math.sqrt(quadratic_error)
        if quadratic_error < required_quadratic_error:
            break
        print('Номер эпохи: ', epoch_number)
        print('Квадратическая ошибка: ', quadratic_error)
        epoch_number += 1


if __name__ == '__main__':
    start()
