template <class... list> struct
count;

template <> struct
count<>
{
	static const int val = 0;
};

template <class head, class... tail> struct
count<head, tail...>
{
	static const int val = count<tail...>::val + 1;
};
