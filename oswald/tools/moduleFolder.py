import importlib
import pathlib

from loguru import logger


def check_if_endpoint(obj):
    try:
        obj.Endpoint
        return True
    except AttributeError:
        return False


class ProvidedModulePath(object):
    def __init__(self, modulePath):
        self.modulePath = modulePath

        # Generate Path Object

        try:
            self.pathLib_obj = pathlib.Path(self.modulePath)
            if self.pathLib_obj.exists() == True:
                if len(self.pathLib_obj.parents) > 1:
                    self._verifiedPath = {
                        "status": False,
                        "message": "Please make modules in the same workspace as the program.",
                    }
                else:
                    self._verifiedPath = {"status": True, "message": None}
            else:
                self._verifiedPath = {
                    "status": False,
                    "message": "Directory does not exist.",
                }
        except Exception as error:
            logger.error(f"Error on verifying path: {error}")

    @property
    def prov_object(self):
        return self.pathLib_obj

    @property
    def verify(self):
        try:
            return self._verifiedPath
        except Exception as error:
            logger.error(f"VerifiedPath did not return a dict!: {error}")
            return {"status": None, "message": "Returned a unknown value."}


class ModuleFolderDetection(object):
    def __init__(self, provided_module_folder):
        self.provided_module_folder = provided_module_folder

        if isinstance(self.provided_module_folder, ProvidedModulePath) == True:
            if self.provided_module_folder.verify["status"] == True:
                current_endpoints = []

                for file_prov in self.provided_module_folder.prov_object.glob("*.py"):
                    ignore_files = ["__init__.py"]

                    if file_prov.name in ignore_files:
                        continue

                    if file_prov.name not in ignore_files:
                        if file_prov.is_dir() == True:
                            # Ignore directories.
                            continue
                        else:
                            pass

                    try:
                        parent_dir = file_prov.parent
                        file_name = file_prov.name
                        module_name = str(parent_dir) + "." + file_name.strip(".py")
                        logger.info(f"Importing {module_name}")
                        provided_api = importlib.import_module(f"{module_name}")

                        if check_if_endpoint(provided_api) == True:
                            current_endpoints.append(provided_api)
                        else:
                            logger.info(f"Improper Design for {module_name}")
                            continue
                    except Exception as error:
                        logger.error(f"Error on checking imports: {error}")

                    self.result = {
                        "status": 0,
                        "message": f"{len(current_endpoints)} were added.",
                        "obj": current_endpoints,
                    }
            else:
                self.result = {
                    "status": 1,
                    "message": f"Specified Path {self.provided_module_folder.path} does not exist.",
                }
        else:
            self.result = {
                "status": 1,
                "message": "Provided object was not valid and is not accepted.",
            }

    @property
    def get_res(self):
        return self.result
