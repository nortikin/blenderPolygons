# -*- coding:utf-8 -*-

# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110- 1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

# ----------------------------------------------------------
# Author: Stephen Leger (s-leger)
#
# ----------------------------------------------------------
import bpy


class MaterialUtils():

    @staticmethod
    def build_default_mat(name, color=(1.0, 1.0, 1.0)):
        midx = bpy.data.materials.find(name)
        if midx < 0:
            mat = bpy.data.materials.new(name)
            mat.diffuse_color = color
        else:
            mat = bpy.data.materials[midx]
        return mat

    @staticmethod
    def add_wall_materials(obj):
        int_mat = MaterialUtils.build_default_mat('inside', (0.5, 1.0, 1.0))
        out_mat = MaterialUtils.build_default_mat('outside', (0.5, 1.0, 0.5))
        oth_mat = MaterialUtils.build_default_mat('cuts', (1.0, 0.2, 0.2))
        obj.data.materials.append(out_mat)
        obj.data.materials.append(int_mat)
        obj.data.materials.append(oth_mat)

    @staticmethod
    def add_stair_materials(obj):
        cei_mat = MaterialUtils.build_default_mat('Stair_ceiling', (0.5, 1.0, 1.0))
        whi_mat = MaterialUtils.build_default_mat('Stair_white', (1.0, 1.0, 1.0))
        con_mat = MaterialUtils.build_default_mat('Stair_concrete', (0.5, 0.5, 0.5))
        wood_mat = MaterialUtils.build_default_mat('Stair_wood', (0.28, 0.2, 0.1))
        metal_mat = MaterialUtils.build_default_mat('Stair_metal', (0.4, 0.4, 0.4))
        glass_mat = MaterialUtils.build_default_mat('Stair_glass', (0.2, 0.2, 0.2))
        glass_mat.use_transparency = True
        glass_mat.alpha = 0.5
        glass_mat.game_settings.alpha_blend = 'ADD'
        obj.data.materials.append(cei_mat)
        obj.data.materials.append(whi_mat)
        obj.data.materials.append(con_mat)
        obj.data.materials.append(wood_mat)
        obj.data.materials.append(metal_mat)
        obj.data.materials.append(glass_mat)

    @staticmethod
    def add_handle_materials(obj):
        metal_mat = MaterialUtils.build_default_mat('metal', (0.4, 0.4, 0.4))
        obj.data.materials.append(metal_mat)

    @staticmethod
    def add_door_materials(obj):
        int_mat = MaterialUtils.build_default_mat('door_inside', (0.7, 0.2, 0.2))
        out_mat = MaterialUtils.build_default_mat('door_outside', (0.7, 0.2, 0.7))
        glass_mat = MaterialUtils.build_default_mat('glass', (0.2, 0.2, 0.2))
        metal_mat = MaterialUtils.build_default_mat('metal', (0.4, 0.4, 0.4))
        glass_mat.use_transparency = True
        glass_mat.alpha = 0.5
        glass_mat.game_settings.alpha_blend = 'ADD'
        obj.data.materials.append(out_mat)
        obj.data.materials.append(int_mat)
        obj.data.materials.append(glass_mat)
        obj.data.materials.append(metal_mat)

    @staticmethod
    def add_window_materials(obj):
        int_mat = MaterialUtils.build_default_mat('window_inside', (0.7, 0.2, 0.2))
        out_mat = MaterialUtils.build_default_mat('window_outside', (0.7, 0.2, 0.7))
        glass_mat = MaterialUtils.build_default_mat('glass', (0.2, 0.2, 0.2))
        metal_mat = MaterialUtils.build_default_mat('metal', (0.4, 0.4, 0.4))
        tablet_mat = MaterialUtils.build_default_mat('tablet', (0.2, 0.2, 0.2))
        store_mat = MaterialUtils.build_default_mat('store', (0.2, 0.0, 0.0))
        glass_mat.use_transparency = True
        glass_mat.alpha = 0.5
        glass_mat.game_settings.alpha_blend = 'ADD'
        obj.data.materials.append(out_mat)
        obj.data.materials.append(int_mat)
        obj.data.materials.append(glass_mat)
        obj.data.materials.append(metal_mat)
        obj.data.materials.append(tablet_mat)
        obj.data.materials.append(store_mat)
