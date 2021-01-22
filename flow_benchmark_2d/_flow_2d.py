""" Mesh generation for cases defined in Flemisch et al 2018.
"""
from pathlib import Path
from typing import Optional, Dict
import porepy as pp


def case3(mesh_args: Optional[Dict[str, float]] = None) -> pp.GridBucket:
    """Case 3 in 2d flow benchmark.

    Parameters:
        mesh_args (dict): Mesh arguments to be passed to PorePy. If not
            provided, the grid as defined in the benchmark, with about
            1500 2d cells, will be returned.

    Returns:
        pp.GridBucket: Mixed-dimensional grid of the domain.

    """
    abs_path = Path(__file__)
    directory = abs_path.parent / Path("case3")

    if mesh_args is None:
        return _from_file(directory, "mesh1500.geo")
    else:
        return _from_file(directory, "benchmark_2d_case_3.csv", mesh_args)


def case4(mesh_args: Optional[Dict[str, float]] = None) -> pp.GridBucket:
    """Case 4 in 2d flow benchmark.

    Parameters:
        mesh_args (dict): Mesh arguments to be passed to PorePy. If not
            provided, the grid as defined in the benchmark, with about
            11500 2d cells, will be returned.

    Returns:
        pp.GridBucket: Mixed-dimensional grid of the domain.

    """
    abs_path = Path(__file__)
    directory = abs_path.parent / Path("case4")

    if mesh_args is None:
        return _from_file(directory, "mesh11500.geo")
    else:
        return _from_file(directory, "benchmark_2d_case_4.csv", mesh_args)


def _from_file(directory, filename, mesh_args=None):
    if mesh_args is not None:
        # Import fracture network, generate .geo file, run gmsh, import again
        full_file_name = directory / Path(filename)
        network = pp.fracture_importer.network_2d_from_csv(str(full_file_name))
        return network.mesh(mesh_args)
    else:
        # Use the predefined mesh file
        full_file_name = directory / Path(filename)
        return pp.fracture_importer.dfm_from_gmsh(str(full_file_name), 2)
