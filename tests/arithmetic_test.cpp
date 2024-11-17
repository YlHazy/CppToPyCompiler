#include <iostream>
#include <string>
#include <stack>
#include <cctype>
using namespace std;

bool isOperator(char op) {
    return op == '+' || op == '-' || op == '*' || op == '/';
}

int precedence(char op) {
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    return 0;
}

double applyOperation(double a, double b, char op, bool &error) {
    if (op == '+') {
        return a + b;
    } else if (op == '-') {
        return a - b;
    } else if (op == '*') {
        return a * b;
    } else if (op == '/') {
        if (b == 0) {
            cout << "Error: Division by zero" << endl;
            error = true;
            return 0;
        }
        return a / b;
    }
    cout << "Error: Invalid operator '" << op << "'" << endl;
    error = true;
    return 0;
}

double evaluate_expression(const string &expr, bool &error) {
    stack<double> values;
    stack<char> ops;
    size_t i = 0;

    while (i < expr.length()) {
        if (isspace(expr[i])) {
            i++;
            continue;
        }

        if (expr[i] == '(') {
            ops.push(expr[i]);
        } else if (isdigit(expr[i]) || ((expr[i] == '+' || expr[i] == '-') &&
                  (i == 0 || expr[i - 1] == '(' || isOperator(expr[i - 1])))) {
            // Parse number with optional unary '+' or '-'
            int sign = 1;
            if (expr[i] == '+') {
                i++;
            } else if (expr[i] == '-') {
                sign = -1;
                i++;
            }

            double val = 0;
            while (i < expr.length() && isdigit(expr[i])) {
                val = (val * 10) + (expr[i] - '0');
                i++;
            }
            if (i < expr.length() && expr[i] == '.') {
                // Parse fractional part
                i++;
                double frac = 0, base = 0.1;
                while (i < expr.length() && isdigit(expr[i])) {
                    frac += (expr[i] - '0') * base;
                    base *= 0.1;
                    i++;
                }
                val += frac;
            }
            values.push(sign * val);
            i--;
        } else if (expr[i] == ')') {
            bool found_parenthesis = false;
            while (!ops.empty()) {
                if (ops.top() == '(') {
                    ops.pop();
                    found_parenthesis = true;
                    break;
                }
                double val2 = values.top(); values.pop();
                if (values.empty()) {
                    cout << "Error: Invalid expression" << endl;
                    error = true;
                    return 0;
                }
                double val1 = values.top(); values.pop();
                char op = ops.top(); ops.pop();
                double result = applyOperation(val1, val2, op, error);
                if (error) return 0;
                values.push(result);
            }
            if (!found_parenthesis) {
                cout << "Error: Mismatched parentheses" << endl;
                error = true;
                return 0;
            }
        } else if (isOperator(expr[i])) {
            while (!ops.empty() && precedence(ops.top()) >= precedence(expr[i])) {
                char op = ops.top(); ops.pop();
                double val2 = values.top(); values.pop();
                if (values.empty()) {
                    cout << "Error: Invalid expression" << endl;
                    error = true;
                    return 0;
                }
                double val1 = values.top(); values.pop();
                double result = applyOperation(val1, val2, op, error);
                if (error) return 0;
                values.push(result);
            }
            ops.push(expr[i]);
        } else {
            cout << "Error: Invalid character '" << expr[i] << "' in expression" << endl;
            error = true;
            return 0;
        }
        i++;
    }

    while (!ops.empty()) {
        if (ops.top() == '(' || ops.top() == ')') {
            cout << "Error: Mismatched parentheses" << endl;
            error = true;
            return 0;
        }
        double val2 = values.top(); values.pop();
        if (values.empty()) {
            cout << "Error: Invalid expression" << endl;
            error = true;
            return 0;
        }
        double val1 = values.top(); values.pop();
        char op = ops.top(); ops.pop();
        double result = applyOperation(val1, val2, op, error);
        if (error) return 0;
        values.push(result);
    }

    if (values.size() != 1) {
        cout << "Error: Invalid expression" << endl;
        error = true;
        return 0;
    }
    return values.top();
}

int main() {
    string expr;
    cout << "Enter an expression: ";
    getline(cin, expr);
    bool error = false;
    double result = evaluate_expression(expr, error);
    if (!error) {
        cout << "Result: " << result << endl;
    }
    return 0;
}
