"""Pure Pursuit steering formula (toy).

Phase A warm-up for
``pipeline/control/control/controllers/pure_pursuit.py``.
"""
from __future__ import annotations

import math
import numpy as np


def compute_steer(
    alpha: float,
    ld: float,
    wheelbase: float,
    max_steer: float,
) -> float:
    """Return normalized steering in ``[-1, 1]``.

    Pure Pursuit:
        κ = 2 · sin(α) / Ld
        δ = atan(L · κ)
        steer_norm = clamp(δ / max_steer, -1, 1)

    Args:
        alpha: angle from vehicle heading to chase target (rad).
        ld: lookahead distance (m), must be > 0.
        wheelbase: L (m).
        max_steer: maximum front-wheel angle (rad).
    """
    # === STUDENT TODO ===
    try:
        k=(2*math.sin(alpha))/ld
    except:
        raise ZeroDivisionError("ld must be higher than 0")
    delta = math.atan(wheelbase*k)
    return float(np.clip(delta/max_steer,-1,1))
    # === END TODO ===
