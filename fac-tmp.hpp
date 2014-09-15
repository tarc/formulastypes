template <int n> struct
fact
{
	static const int val = n * fact<n-1>::val;
};

template <> struct
fact<0>
{
	static const int val = 1;
};
