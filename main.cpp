#include <iostream>

#include "fac-tmp.hpp"
#include "fibo-tmp.hpp"
#include "list-tmp.hpp"

using namespace std;

int main()
{
	cout << fact<10>::val << endl;
	cout << fibo<900>::val << endl;
	cout << count<int, char, long>::val << endl;

	return 0;
}
