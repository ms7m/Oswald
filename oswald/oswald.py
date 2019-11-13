import falcon
from loguru import logger
import traceback

from oswald.tools import moduleFolder as tool_moduleFolder


class Oswald(object):
    def __init__(self, moduleFolder_prov):
        # Generate Object from path.
        try:
            self.modulePathObject = tool_moduleFolder.ProvidedModulePath(moduleFolder_prov)

            if self.modulePathObject.verify["status"] == False or not True:
                print(f"Warning: {self.modulePathObject.verify['status']}")
                raise Exception(self.modulePathObject.verify["message"])

            if self.modulePathObject.verify['status'] == True:
                # Generate ModuleFolderDetection object from this.
                self.ModuleFolderDetection_obj = tool_moduleFolder.ModuleFolderDetection(
                    self.modulePathObject
                ).result

                # Generate a Falcon API

                self._prov_falconAPI = falcon.API()
            else:
                logger.debug(self.modulePathObject.verify['status'])
                logger.info(self.modulePathObject.verify)
                logger.debug(traceback.print_exc())
                raise Exception("Folder does not exist.")

            if self.ModuleFolderDetection_obj:
                if self.ModuleFolderDetection_obj["status"] == 0:
                    addition_count = 0
                    for objs in self.ModuleFolderDetection_obj["obj"]:
                        for inner_obj_prov in objs.Endpoint.API_ENDS:
                            logger.info(
                                f"Attempting addition for {inner_obj_prov['endpoint']}"
                            )
                            try:
                                self._prov_falconAPI.add_route(
                                    inner_obj_prov["endpoint"],
                                    inner_obj_prov["endpointObj"],
                                )
                                addition_count += 1
                            except Exception as error:
                                logger.error(
                                    f"Addition failed for {inner_obj_prov['endpoint']}"
                                )
                                continue
                    logger.info(f"{addition_count} resource(s) added.")
                    self.api = self._prov_falconAPI
        except Exception as error:
            logger.error(f"Error on the whole block: {error}")
            logger.error(traceback.print_exc())
            raise Exception(error)
