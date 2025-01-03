#include <iostream>
#include <cmath>
#include <ctime>

using namespace std;

void greetUser(double balance);
void showAccount(double balance);
double addFunds();
double withdrawFunds(double balance);
double bills(double balance);

int main()
{
    double cash = 0;
    greetUser(cash);
    return 0;
}

void greetUser(double balance)
{
    int option;

    do
    {
        cout << "Welcome to Venstar Banking!\n";
        cout << "How may we help you?\n";
        cout << "1. View Account Balance\n";
        cout << "2. Add Funds \n";
        cout << "3. Withdraw Funds \n";
        cout << "4. View Bills \n";
        cout << "5. Exit\n";
        cin >> option;

        switch (option)
        {
        case 1:
            showAccount(balance);
            break;

        case 2:
            balance += addFunds();
            showAccount(balance);
            break;

        case 3:
            balance -= withdrawFunds(balance);
            showAccount(balance);
            break;

        case 4:
            cout << "Here are your bills: \n";
            balance -= bills(balance);
            break;

        case 5:
            cout << "Thank you for banking with us! ";
            break;

        default:
            cout << "Select a valid option \n";
        }
    } while (option != 5);
}
void showAccount(double balance)
{
    cout << "Here is your available balance: $" << balance << '\n';
}
double addFunds()
{

    double money;
    cout << "How much money would you like to add? ";
    cin >> money;

    if (money < 0)
    {
        cout << "That is not a valid amount of money! ";
    }

    else
    {
        return money;
    }
    
    return 0;
}
double withdrawFunds(double balance)
{

    double moneyWithdrawn;
    cout << "How much would you like to withdraw? ";
    cin >> moneyWithdrawn;

    if (moneyWithdrawn > balance)
    {
        cout << "Aw man, Insufficient Funds\n";
    }

    else
    {
        return moneyWithdrawn;
    }
    return 0;
}
double bills(double balance)
{

    char payBillOption;
    int bill;

    double water = 150;
    double electricity = 80;
    double wifi = 350; // Gotta have that good 0 ping
    double groceries = 100;
    double carNote = 1250;
    double rent = 2200;
    double total = water + electricity + wifi + groceries + carNote + rent;

    cout << "1.Water-$" << water << '\n';
    cout << "2.Electricity-$" << electricity << '\n';
    cout << "3.Wifi-$" << wifi << '\n';
    cout << "4.Groceries-$" << groceries << '\n';
    cout << "5.Car Note-$" << carNote << '\n';
    cout << "6.Rent-$" << rent << '\n';

    cout << "Would you like to pay your bills? \n";
    cout << "Y or N? (Yes or No) \n";
    cin >> payBillOption;

    if (payBillOption != 'Y' && payBillOption != 'y')
    {
        return 0;
    }

    else
    {
        cout << "Which bill would you like to pay? \n";
        cout << "1.Water \n";
        cout << "2.Electricity \n";
        cout << "3.Wifi \n";
        cout << "4.Groceries \n";
        cout << "5.Car Note \n";
        cout << "6.Rent \n";
        cout << "7.All Bills\n";
        cin >> bill;
    }

    switch (bill)
    {
    case 1:
        balance -= water;
        showAccount(balance);
        break;

    case 2:
        balance -= electricity;
        showAccount(balance);
        break;

    case 3:
        balance -= wifi;
        showAccount(balance);
        break;

    case 4:
        balance -= groceries;
        showAccount(balance);
        break;

    case 5:
        balance -= carNote;
        showAccount(balance);
        break;

    case 6:
        balance -= rent;
        showAccount(balance);
        break;

    case 7:
        balance -= total;
        showAccount(balance);
        break;

    default:
        cout << "That is not an available bill\n";
        break;
    }

    if (bill > balance)
    {
        cout << "Insufficient funds for bills \n\n";
    }

    else
    {
        return balance;
    }

    return 0;
}
