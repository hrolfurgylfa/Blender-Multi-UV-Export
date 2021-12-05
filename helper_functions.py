"""
Multi UV Export, a simple blender addon to export UV layouts of multiple
objects at the same time. 
Copyright (C) 2021 Hrólfur Gylfason

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""


def combine_folder_and_file(folder_path: str, filename: str) -> str:
    if folder_path.endswith("/") or folder_path.endswith("\\"):
        return folder_path + filename
    else:
        return folder_path + "/" + filename
