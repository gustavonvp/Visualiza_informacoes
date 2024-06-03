# define an objective function
import hyperopt


def objective(args):
    case, val = args
    if case == 'case 1':
        return val
    else:
        return val ** 2

# define a search space
from hyperopt import hp
space = hp.choice('a',
    [
        ('case 1', 1 + hp.lognormal('c1', 0, 1)),
        ('case 2', hp.uniform('c2', -10, 10))
    ])

# minimize the objective over the space
from hyperopt import fmin, tpe, space_eval
best = fmin(objective, space, algo=tpe.suggest, max_evals=100)

print(best)
# -> {'a': 1, 'c2': 0.01420615366247227}
print(space_eval(space, best))
# -> ('case 2', 0.01420615366247227}


from hyperopt import hp
from hyperopt.pyll import scope

space = hp.choice('classifier_type', [
    {
        'type': 'naive_bayes',
    },
    {
        'type': 'svm',
        'C': hp.lognormal('svm_C', 0, 1),
        'kernel': hp.choice('svm_kernel', [
            {'ktype': 'linear'},
            {'ktype': 'RBF', 'width': hp.lognormal('svm_rbf_width', 0, 1)},
            ]),
    },
    {
        'type': 'dtree',
        'criterion': hp.choice('dtree_criterion', ['gini', 'entropy']),
        'max_depth': hp.choice('dtree_max_depth',
            [None, hp.qlognormal('dtree_max_depth_int', 2, 1, 1)]),
        'min_samples_split': hp.qlognormal('dtree_min_samples_split', 3, 1, 1),
    },
    ])


@scope.define
def foo(a, b=0):
     print('runing foo', a, b, '', 'palavra')
     return a + b / 2

# -- this will print 0, foo is called as usual.
print(foo(0))

# In describing search spaces you can use `foo` as you
# would in normal Python. These two calls will not actually call foo,
# they just record that foo should be called to evaluate the graph.

space1 = scope.foo(hp.uniform('a', 0, 10))
space2 = scope.foo(hp.uniform('a', 0, 10), hp.normal('b', 0, 1))
space3 = scope.foo(hp.uniform('a', 0, -10, 10,), hp.normal('b', 0, 1), hp.normal('', -10,10))
space4 = scope.foo(hp.uniform('a', 0, -10, 10,), hp.normal('b', 0, 1),
                   hp.normal('', -10,10), hp.normal('palavra', 1,2))
# -- this will print an pyll.Apply node
print(space1)

# -- this will draw a sample by running foo()
print(hyperopt.pyll.stochastic.sample(space1))

print(space3)
#print(hyperopt.pyll.base.scope.__new__(exit()))
print(hyperopt.pyll.stochastic.sample(space3))

print(space4)
print(hyperopt.pyll.stochastic.sample(space4))
print(hyperopt.pyll.base.scope.__sizeof__(space4))

#print(hp.qlognormal)
#print(space)