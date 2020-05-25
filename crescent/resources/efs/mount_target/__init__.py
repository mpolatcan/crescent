from .mount_target import MountTarget


class MountTargetFactory:
    @staticmethod
    def Create(id: str): return MountTarget(id)


__all__ = ["MountTargetFactory"]
