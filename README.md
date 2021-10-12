# Rectangle-Square-problem

This is a demonstration of a rectangle-square problem. Rectangle and Square classes are in **figures.py**. To see the LSP violation run the **lsp_payload.py**.

The LSP violates because the same methods work differently for base class and the inheritor.


The way to solve this problem is to use different methods to set sizes if figures. This is made in True_Square class in **figures.py**.

**lsp_without_violation** - is a file which shows that everything is OK when yoe use the second Square implementation (True_Square).