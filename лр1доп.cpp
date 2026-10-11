#include <iostream>
#include <string>
#include <cmath>


bool isNumber(const std::string& s, double& result) {
    if (s.empty()) return false;

    size_t start = 0;
    bool negative = false;
    if (s[0] == '-' || s[0] == '+') {
        if (s[0] == '-') {
            negative = true;
        }
        start = 1;
    }

    bool hasDigit = false;
    bool hasDot = false;
    double value = 0.0;
    double fraction = 0.1;

    for (size_t i = start; i < s.size(); i++) {
        char c = s[i];
        if (c >= '0' && c <= '9') {
            hasDigit = true;
            int digit = c - '0';
            if (hasDot == false) {
                value = value * 10 + digit;
            } else {
                value = value + digit * fraction;
                fraction = fraction / 10;
            }
        } else if (c == '.' && hasDot == false) {
            hasDot = true;
        } else {
            return false;
        }
    }

    if (hasDigit == false) {
        return false;
    }

    if (negative == true) {
        result = -value;
    } else {
        result = value;
    }
    return true;
}



double getCoef(const std::string& name) {
    while (true) {
        std::cout << "Введите " << name << ": ";
        std::string s;
        std::getline(std::cin, s);
        double value;
        if (isNumber(s, value)) {
            return value;
        }
        std::cout << "Некорректное значение, повторите ввод." << std::endl;
    }
}


class Bisquare {
private:
    double a, b, c;
    double roots[4];
    int count;

public:
    Bisquare(double a1, double b1, double c1) {
        a = a1;
        b = b1;
        c = c1;
        count = 0;
    }

    void solve() {
        count = 0;

        if (a == 0) {
            if (b == 0) {
                return;
            }
            double t = -c / b;
            if (t > 0) {
                roots[count++] = std::sqrt(t);
                roots[count++] = -std::sqrt(t);
            } else if (t == 0) {
                roots[count++] = 0;
            }
            return;
        }

        double D = b*b - 4*a*c;

        if (D > 0) {
            double t1 = (-b + std::sqrt(D)) / (2*a);
            double t2 = (-b - std::sqrt(D)) / (2*a);
            double arr[2];
            arr[0] = t1;
            arr[1] = t2;
            for (int i = 0; i < 2; i++) {
                double t = arr[i];
                if (t > 0) {
                    roots[count++] = std::sqrt(t);
                    roots[count++] = -std::sqrt(t);
                } else if (t == 0) {
                    roots[count++] = 0;
                }
            }
        } else if (D == 0) {
            double t = -b / (2*a);
            if (t > 0) {
                roots[count++] = std::sqrt(t);
                roots[count++] = -std::sqrt(t);
            } else if (t == 0) {
                roots[count++] = 0;
            }
        }
    }

    void printRoots() {
    if (count == 0) {
        std::cout << "Действительных корней нет" << std::endl;
    } else {
        std::cout << "Найдено действительных корней: " << count << std::endl;
        if (count >= 1) {
            std::cout << "  x1 = " << roots[0] << std::endl;
        }
        if (count >= 2) {
            std::cout << "  x2 = " << roots[1] << std::endl;
        }
        if (count >= 3) {
            std::cout << "  x3 = " << roots[2] << std::endl;
        }
        if (count >= 4) {
            std::cout << "  x4 = " << roots[3] << std::endl;
        }
    }
}
};


int main(int argc, char* arg[]) {
    double coefs[3];
    bool haveCoef[3] = {false, false, false};
    std::string names[3] = {"A", "B", "C"};

    for (int i = 1; i < argc && i <= 3; i++) {
        double value;
        if (isNumber(arg[i], value)) {
            coefs[i - 1] = value;
            haveCoef[i - 1] = true;
        } else {
            std::cout << "Некорректный аргумент " << names[i - 1] << ": " << arg[i] << ". Значение будет введено с клавиатуры." << std::endl;
        }
    }

    for (int i = 0; i < 3; i++) {
        if (haveCoef[i] == false) {
            coefs[i] = getCoef(names[i]);
        }
    }

    Bisquare eq(coefs[0], coefs[1], coefs[2]);
    eq.solve();
    eq.printRoots();

    return 0;
}