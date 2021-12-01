import pulp as pl
path_to_cplex = r'C:\Program Files\IBM\ILOG\CPLEX_Studio1210\cplex\bin\x64_win64\cplex.exe'
model = pl.LpProblem("Example", pl.LpMinimize)
solver = pl.CPLEX_CMD(path=path_to_cplex)
_var = pl.LpVariable('a')
_var2 = pl.LpVariable('a2')
model += _var + _var2 == 1
result = model.solve(solver)

