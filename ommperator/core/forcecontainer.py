class ForceContainer(list):
    """ A force container is a container that holds ForceOmmperators.
    It facilitaties mass-modifying properties"""
    def update(self, **kwargs):
        for force_ommp in self:
            force_ommp.set_params(**kwargs)

class CustomForceContainer(list):
    """ A force container is a container that holds CustomForceOmmperators.
    It facilitaties mass-modifying properties"""
    def update(self, *args):
        for force_ommp in self:
            force_ommp.set_params(*args)

