-- basic types
type Args = [Integer]

newtype Prog t = PR (Args -> t)

run :: Prog t -> Args ->t
run (PR act) args = act args

-- monadic functions
getArg :: Int -> Prog Integer
getArg n = PR (\args -> args !! n)

doubleIt :: Integer -> Prog Integer
doubleIt n = PR (\args -> 2*n)

sumToIt :: (Prog Integer) -> Integer -> Prog Integer
sumToIt (PR act) n = PR (\args -> (act args) + n)

mulToIt :: (Prog Integer) -> Integer -> Prog Integer
mulToIt (PR act) n = PR (\args -> (act args) * n)

-- monadic bind
bind :: (Prog a) -> (a -> Prog b) -> (Prog b)
bind (PR act) cont =
	PR ( \args ->
		let v = act args;
			(PR act') = cont v
		in
			act' args)

-- expression tree, represent programs
data Exp = Const Integer
		| Plus Exp Exp
		| Times Exp Exp
		-- Arg, being an Int, is platform dependente, as it's expected from a
		-- program, even though the states, being Integer's, are not limited
		-- this way
		| Arg Int


-- compilation: it takes an expression and return an action
compile :: Exp -> Prog Integer
compile (Const c) = PR(\args -> c)
compile (Arg n) = getArg n
compile (Plus e e') = bind (compile e) (\n -> (sumToIt (compile e') n))
compile (Times e e') = bind (compile e) (\n -> (mulToIt (compile e') n))

-- testing
testExp = 
	let exp = (Plus (Times (Arg 0) (Arg 1)) (Const 13))
	in compile exp
