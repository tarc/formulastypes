#include <iostream>

#include "fac-tmp.hpp"
#include "fibo-tmp.hpp"

#ifndef NOVARIADIC
#include "list-tmp.hpp"
#endif

using namespace std;

int main()
{
	cout << fact<10>::val << endl;
	cout << fibo<10>::val << endl;

#ifndef NOVARIADIC
	cout << count<int, char, long>::val << endl;
#endif

	return 0;
}
