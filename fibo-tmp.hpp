template <unsigned int n> struct
fibo
{
	static const unsigned int pval = fibo<n-1>::val;
	static const unsigned int val = fibo<n-1>::val + fibo<n-1>::pval;
};

template <> struct
fibo<1>
{
	static const unsigned int val = 0;
};

template <> struct
fibo<2>
{
	static const unsigned int pval = 0;
	static const unsigned int val = 1;
};
