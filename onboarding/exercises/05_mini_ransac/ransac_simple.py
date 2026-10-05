"""Minimal RANSAC plane fit (no Numba, no warm-start).

Phase A warm-up for ``pipeline/cone_detection/cone_detection/ransac.py``.
Uses ``plane_from_points`` from exercise 02 — copy or import from there.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np


from plane import plane_from_points  # noqa: E402


def ransac_plane(points: np.ndarray,threshold: float = 0.05,max_iter: int = 100,rng: np.random.Generator | None = None,) -> tuple[np.ndarray, float, np.ndarray]:
    """Fit a plane with RANSAC.

    Args:
        points: (N, 3) XYZ cloud.
        threshold: absolute residual |n·x + d| for an inlier.
        max_iter: number of random hypotheses.
        rng: optional numpy Generator for reproducibility.

    Returns:
        ``n``, ``d`` for the best plane (``n · x + d = 0``), and a
        boolean inlier mask of shape (N,).
    """
    if points.ndim != 2 or points.shape[1] != 3:
        raise ValueError("points must be (N, 3)")
    if points.shape[0] < 3:
        raise ValueError("need at least 3 points")

    rng = rng or np.random.default_rng()

    best_plane = (None,None,np.ndarray(0))

    for i in range(max_iter):

        point = rng.choice(points,size = 3,replace=False)
        try:
            n,d = plane_from_points(point[0],point[1],point[2])

        except ValueError:
            continue
        
        margen = np.dot(points,n) + d


        valid = np.abs(margen) < threshold

        if valid.sum() > best_plane[2].sum():
            best_plane = (n,d,valid) 
    if best_plane[0] is None:
        raise RuntimeError
    
    return best_plane
    # === STUDENT TODO ===
    # For each iteration:
    #   1. Sample 3 distinct indices.
    #   2. Try plane_from_points (skip on ValueError).
    #   3. Count inliers with |n·x + d| < threshold.
    #   4. Keep the (n, d) with the most inliers.
    # After the loop, recompute the inlier mask for the best plane.
    # If no valid hypothesis was found, raise RuntimeError.
    # === END TODO ===
