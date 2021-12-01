import pulp as pl
solver_list = pl.listSolvers()
print(solver_list)


path_to_clp = r'C:\Users\fhdeng3\Desktop\Clp-1.17.6-win32-msvc15\bin\clp.exe'
model = pl.LpProblem("Example", pl.LpMinimize)
solver = pl.COIN_CMD(path=path_to_clp)
_var = pl.LpVariable('a')
_var2 = pl.LpVariable('a2')
model += _var + _var2 == 1
result = model.solve(solver)
