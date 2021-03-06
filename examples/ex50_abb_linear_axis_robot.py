"""
Creates a `Robot` representing an ABB on a linear axis from a urdf model and the
semantics from a srdf file.
"""
import os

import compas
from compas.robots import RobotModel
from compas.robots import LocalPackageMeshLoader
from compas.robots import Joint
from compas.datastructures import Mesh

from compas_fab.robots import Robot
from compas_fab.robots import RobotSemantics
from compas_fab.artists import BaseRobotArtist
from compas_fab.backends import RosClient
from compas_fab.backends import RosError

compas.PRECISION = '12f'

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, '../data')
PATH = os.path.join(DATA, 'robot_description')

# packages = ['abb_irb4600_40_255', 'abb_linear_axis', 'abb_end_effectors']
# loaders = [LocalPackageMeshLoader(PATH, package) for package in packages]

urdf_filename = "abb_linear_axis_brick_suction_tool.urdf"
srdf_filename = "abb_linear_axis_suction_tool.srdf"
package = "abb_linear_axis"
urdf_filename = os.path.join(PATH, package, "urdf", urdf_filename)
srdf_filename = os.path.join(PATH, package, srdf_filename)

model = RobotModel.from_urdf_file(urdf_filename)
# model.load_geometry(loader)
artist = BaseRobotArtist(model)
# artist = RobotArtist(model)
semantics = RobotSemantics.from_srdf_file(srdf_filename, model)

robot = Robot(model, artist, semantics)

if __name__ == '__main__':
    robot.info()
