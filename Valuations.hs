-- basic types
type BaseValuation = [Bool]

newtype Valuation t = VAL (BaseValuation -> t)

-- formulas
data Formula = P Integer
			| Or Formula
			| And Formula
			| Imp Formula
			| Not Formula

-- satisfy :: Formula -> Valuation Bool
