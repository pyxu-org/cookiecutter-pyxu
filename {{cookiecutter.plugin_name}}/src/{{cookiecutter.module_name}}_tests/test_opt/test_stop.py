import datetime as dt

import numpy as np
from pyxu.operator import SquaredL2Norm

from pyxu.opt.solver import GradientDescent
from pyxu.opt.stop import Deadline


def test_stop():
    # Test that the solver runs only for 1 second
    # Get the current time
    init_time = dt.datetime.now()
    # Calculate the time 10 seconds in the future
    future_time = init_time + dt.timedelta(seconds=1.0)

    deadline = Deadline(t=future_time)
    N = 10
    y = np.arange(N)
    sl2 = SquaredL2Norm(dim_shape=N).argshift(-y)
    gd = GradientDescent(f=sl2)
    gd.fit(x0=np.random.randn(N), stop_crit=deadline)
    end_time = dt.datetime.now()
    assert end_time - init_time < dt.timedelta(seconds=1.1)
